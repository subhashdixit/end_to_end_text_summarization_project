from transformers import TrainingArguments, Trainer  # Importing TrainingArguments and Trainer for model training
from transformers import DataCollatorForSeq2Seq  # Importing DataCollatorForSeq2Seq for collating data
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer  # Importing pre-trained Seq2Seq model and tokenizer
from datasets import load_dataset, load_from_disk  # Importing functions to load datasets
from text_summarizer.entity import ModelTrainerConfig  # Importing configuration entity for model training
import torch  # Importing PyTorch for handling device and model operations
import os  # Importing os for file operations


class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        """
        Initializes the ModelTrainer class with configuration settings.
        
        Args:
            config (ModelTrainerConfig): Configuration settings for model training.
        """
        self.config = config

    def train(self):
        """
        Trains a sequence-to-sequence model using the provided configuration.
        1. Sets the device to CUDA if available; otherwise, uses CPU.
        2. Loads tokenizer and model from the specified checkpoint.
        3. Sets up data collator for sequence-to-sequence tasks.
        4. Loads the dataset from disk.
        5. Defines training arguments.
        6. Initializes and runs the Trainer.
        7. Saves the trained model and tokenizer.
        """
        # Set device to CUDA if available, else use CPU
        device = "cuda" if torch.cuda.is_available() else "cpu"
        
        # Load tokenizer and model from the specified checkpoint
        tokenizer = AutoTokenizer.from_pretrained(self.config.model_ckpt)
        model_pegasus = AutoModelForSeq2SeqLM.from_pretrained(self.config.model_ckpt).to(device)
        
        # Set up data collator for sequence-to-sequence tasks
        seq2seq_data_collator = DataCollatorForSeq2Seq(tokenizer, model=model_pegasus)
        
        # Load the dataset from disk
        dataset_samsum_pt = load_from_disk(self.config.data_path)
        
        # Define training arguments
        trainer_args = TrainingArguments(
            output_dir=self.config.root_dir,  # Directory to save model outputs
            num_train_epochs=1,  # Number of training epochs
            warmup_steps=500,  # Number of warmup steps
            per_device_train_batch_size=1,  # Training batch size per device
            per_device_eval_batch_size=1,  # Evaluation batch size per device
            weight_decay=0.01,  # Weight decay for regularization
            logging_steps=10,  # Steps interval for logging
            evaluation_strategy='steps',  # Evaluation strategy
            eval_steps=500,  # Steps interval for evaluation
            save_steps=1e6,  # Steps interval for saving checkpoints
            gradient_accumulation_steps=16  # Number of gradient accumulation steps
        )
        
        # Initialize the Trainer with the model, arguments, tokenizer, data collator, and datasets
        trainer = Trainer(
            model=model_pegasus,  # Model to be trained
            args=trainer_args,  # Training arguments
            tokenizer=tokenizer,  # Tokenizer for data processing
            data_collator=seq2seq_data_collator,  # Data collator for sequence-to-sequence tasks
            train_dataset=dataset_samsum_pt["test"],  # Training dataset | test because of short runtime. Ideally we should use train set
            eval_dataset=dataset_samsum_pt["validation"]  # Validation dataset
        )
        
        # Train the model
        trainer.train()

        # Save the trained model to disk
        model_pegasus.save_pretrained(os.path.join(self.config.root_dir, "pegasus-samsum-model"))
        
        # Save the tokenizer to disk
        tokenizer.save_pretrained(os.path.join(self.config.root_dir, "tokenizer"))
