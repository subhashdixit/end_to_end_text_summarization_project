import os
from text_summarizer.logging import logger  # Importing the logging module for logging
from transformers import AutoTokenizer  # Importing AutoTokenizer from Hugging Face Transformers library
from datasets import load_dataset, load_from_disk  # Importing functions for loading datasets
from text_summarizer.entity import DataTransformationConfig  # Importing DataTransformationConfig for configuration


class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        """
        Initializes the DataTransformation class with configuration settings and tokenizer.
        
        Args:
            config (DataTransformationConfig): Configuration object for data transformation.
        """
        self.config = config
        self.tokenizer = AutoTokenizer.from_pretrained(config.tokenizer_name)  # Load the tokenizer specified in the config

    def convert_examples_to_features(self, example_batch):
        """
        Converts a batch of examples into model-ready features using the tokenizer.
        
        Args:
            example_batch (dict): A batch of examples containing 'dialogue' and 'summary'.

        Returns:
            dict: A dictionary containing tokenized input_ids, attention_mask, and labels.
        """
        # Tokenize the 'dialogue' text and handle truncation
        input_encodings = self.tokenizer(example_batch['dialogue'], max_length=1024, truncation=True)

        # Tokenize the 'summary' text with the target tokenizer
        with self.tokenizer.as_target_tokenizer():
            target_encodings = self.tokenizer(example_batch['summary'], max_length=128, truncation=True)
        
        return {
            'input_ids': input_encodings['input_ids'],  # Model input IDs
            'attention_mask': input_encodings['attention_mask'],  # Attention mask for input
            'labels': target_encodings['input_ids']  # Target labels for training
        }

    def convert(self):
        """
        Loads the dataset, applies the transformation, and saves the processed dataset to disk.
        """
        dataset_samsum = load_from_disk(self.config.data_path)  # Load dataset from disk
        dataset_samsum_pt = dataset_samsum.map(self.convert_examples_to_features, batched=True)  # Apply feature conversion
        dataset_samsum_pt.save_to_disk(os.path.join(self.config.root_dir, "samsum_dataset"))  # Save transformed dataset
