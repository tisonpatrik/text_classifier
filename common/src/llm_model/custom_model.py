from transformers import DistilBertTokenizer, DistilBertForSequenceClassification
import torch

class CustomModel:
    def __init__(self, model_name: str):
        self.model_path = model_name
        self.load_model()

    def load_model(self):
        # Load the tokenizer and the model from the specified path
        self.tokenizer = DistilBertTokenizer.from_pretrained(self.model_path)
        self.model = DistilBertForSequenceClassification.from_pretrained(self.model_path)

    def invoke(self, prompt: str) -> str:
        # Tokenize the input prompt
        inputs = self.tokenizer(prompt, return_tensors="pt")
        
        # Perform inference with the model
        with torch.no_grad():
            outputs = self.model(**inputs)
        
        # Get the predicted class index
        predicted_class_idx = outputs.logits.argmax().item()
        
        # Optionally, you can map the predicted class index to a label if you have a label mapping
        return str(predicted_class_idx)