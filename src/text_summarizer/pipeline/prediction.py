from text_summarizer.config.configuration import ConfigurationManager
from transformers import AutoTokenizer
from transformers import pipeline

class PredictionPipeline:
    def __init__(self):
        # Initialize the class by loading configuration settings for model evaluation.
        self.config = ConfigurationManager().get_model_evaluation_config()

    def predict(self, text):
        # Load the tokenizer using the path specified in the configuration.
        tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_path)
        
        # Define generation parameters for the summarization model.
        # `length_penalty` controls the length of the output (lower value favors longer summaries).
        # `num_beams` sets the number of beams for beam search (higher values generally improve results).
        # `max_length` specifies the maximum length of the summary.
        gen_kwargs = {"length_penalty": 0.8, "num_beams": 8, "max_length": 128}

        # Create a summarization pipeline using the model and tokenizer specified in the configuration.
        pipe = pipeline("summarization", model=self.config.model_path, tokenizer=tokenizer)

        # Print the original dialogue/text to the console.
        print("Dialogue:")
        print(text)

        # Generate the summary using the pipeline and the specified generation parameters.
        # Extract the summary text from the pipeline output.
        output = pipe(text, **gen_kwargs)[0]["summary_text"]
        
        # Print the generated summary to the console.
        print("\nModel Summary:")
        print(output)

        # Return the generated summary text.
        return output
