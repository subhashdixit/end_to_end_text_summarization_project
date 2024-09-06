from transformers import AutoModelForSeq2SeqLM, AutoTokenizer  # Import model and tokenizer classes from Hugging Face Transformers
from datasets import load_dataset, load_from_disk, load_metric  # Import dataset and metric loading functions
import torch  # Import PyTorch for handling tensors and device management
import pandas as pd  # Import pandas for data manipulation and CSV handling
from tqdm import tqdm  # Import tqdm for progress bars
from text_summarizer.entity import ModelEvaluationConfig  # Import configuration class for model evaluation


class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        """
        Initializes the ModelEvaluation class with configuration settings.
        
        :param config: ModelEvaluationConfig object containing configuration parameters.
        """
        self.config = config

    def generate_batch_sized_chunks(self, list_of_elements, batch_size):
        """
        Splits a list into smaller batches of a specified size for processing.
        
        :param list_of_elements: List to be divided into chunks.
        :param batch_size: Size of each batch.
        :return: Generator yielding batch-sized chunks.
        """
        for i in range(0, len(list_of_elements), batch_size):
            yield list_of_elements[i : i + batch_size]

    def calculate_metric_on_test_ds(self, dataset, metric, model, tokenizer, 
                                   batch_size=16, device="cuda" if torch.cuda.is_available() else "cpu", 
                                   column_text="article", 
                                   column_summary="highlights"):
        """
        Calculates evaluation metrics on the test dataset by generating summaries and comparing them with references.
        
        :param dataset: Dataset to evaluate.
        :param metric: Metric to compute (e.g., ROUGE).
        :param model: Pre-trained model used for generating summaries.
        :param tokenizer: Tokenizer for processing text.
        :param batch_size: Number of examples per batch.
        :param device: Computation device ("cuda" or "cpu").
        :param column_text: Column name in the dataset for input text.
        :param column_summary: Column name in the dataset for reference summaries.
        :return: Computed metric scores.
        """
        # Split dataset into batches
        article_batches = list(self.generate_batch_sized_chunks(dataset[column_text], batch_size))
        target_batches = list(self.generate_batch_sized_chunks(dataset[column_summary], batch_size))

        for article_batch, target_batch in tqdm(
            zip(article_batches, target_batches), total=len(article_batches)):
            
            # Tokenize input text
            inputs = tokenizer(article_batch, max_length=1024, truncation=True, 
                               padding="max_length", return_tensors="pt")
            
            # Generate summaries using the model
            summaries = model.generate(input_ids=inputs["input_ids"].to(device),
                                       attention_mask=inputs["attention_mask"].to(device), 
                                       length_penalty=0.8, num_beams=8, max_length=128)
            
            # Decode generated summaries
            decoded_summaries = [tokenizer.decode(s, skip_special_tokens=True, 
                                                  clean_up_tokenization_spaces=True) 
                                 for s in summaries]      
            
            decoded_summaries = [d.replace("", " ") for d in decoded_summaries]
            
            # Add generated summaries and references to metric
            metric.add_batch(predictions=decoded_summaries, references=target_batch)
            
        # Compute and return the ROUGE scores
        score = metric.compute()
        return score

    def evaluate(self):
        """
        Loads model and tokenizer, evaluates the model on the test dataset, and saves the metrics to a CSV file.
        """
        # Set computation device
        device = "cuda" if torch.cuda.is_available() else "cpu"
        
        # Load tokenizer and model
        tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_path)
        model_pegasus = AutoModelForSeq2SeqLM.from_pretrained(self.config.model_path).to(device)
       
        # Load dataset
        dataset_samsum_pt = load_from_disk(self.config.data_path)

        # Define ROUGE metrics
        rouge_names = ["rouge1", "rouge2", "rougeL", "rougeLsum"]
        # rouge_metric = load_metric('rouge')
        rouge_metric = load_metric('rouge', trust_remote_code=True)
        # Calculate metrics on the test dataset
        score = self.calculate_metric_on_test_ds(
            dataset_samsum_pt['test'][0:10], rouge_metric, model_pegasus, tokenizer, batch_size=2, 
            column_text='dialogue', column_summary='summary'
        )

        # Convert metric scores to DataFrame
        rouge_dict = dict((rn, score[rn].mid.fmeasure) for rn in rouge_names)
        df = pd.DataFrame(rouge_dict, index=['pegasus'])
        
        # Save metrics to CSV
        df.to_csv(self.config.metric_file_name, index=False)
