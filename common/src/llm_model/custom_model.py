from transformers import DistilBertTokenizer, TFDistilBertForSequenceClassification
import tensorflow as tf


class CustomModel:
    def __init__(self, model_name: str):
        self.model_path = model_name
        self.load_model()

    def load_model(self):
        # Load the tokenizer and the model from the specified path
        self.tokenizer = DistilBertTokenizer.from_pretrained(self.model_path)
        self.model = TFDistilBertForSequenceClassification.from_pretrained(self.model_path)

    def invoke(self, prompt: str) -> str:
        # Tokenize the input prompt
        inputs = self.tokenizer(prompt, return_tensors="tf")
        
        # Perform inference with the model
        outputs = self.model(inputs)
        
        # Get the predicted class index
        predicted_class_idx = tf.argmax(outputs.logits, axis=-1).numpy()[0]
        
        # Optionally, you can map the predicted class index to a label if you have a label mapping
        return str(predicted_class_idx)