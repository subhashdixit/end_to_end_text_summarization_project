from fastapi import FastAPI
import uvicorn
import sys
import os
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse
from fastapi.responses import Response
from text_summarizer.pipeline.prediction import PredictionPipeline

# Sample text to be used for predictions (this is just an example and isn't used in the API).
text: str = "What is Text Summarization?"

# Initialize the FastAPI application.
app = FastAPI()

# Route for the root URL. Redirects to the FastAPI documentation page.
@app.get("/", tags=["authentication"])
async def index():
    return RedirectResponse(url="/docs")

# Route for training the model.
@app.get("/train")
async def training():
    try:
        # Execute the training script (`main.py`) using the system shell.
        os.system("python main.py")
        # Return a success message if training completes without exceptions.
        return Response("Training successful !!")
    except Exception as e:
        # Return an error message if an exception occurs during training.
        return Response(f"Error Occurred! {e}")

# Route for making predictions.
@app.post("/predict")
async def predict_route(text: str):
    try:
        # Create an instance of the PredictionPipeline class.
        obj = PredictionPipeline()
        # Use the pipeline to generate a summary of the provided text.
        text = obj.predict(text)
        # Return the generated summary as the response.
        return text
    except Exception as e:
        # Raise an exception if an error occurs during prediction.
        raise e

# Entry point for running the application. Starts the Uvicorn server.
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
