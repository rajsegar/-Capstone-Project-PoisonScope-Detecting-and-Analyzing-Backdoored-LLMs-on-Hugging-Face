import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import gradio as gr
import os

MODEL_PATH = r"outputs/2025-11-01-09-44-22-099720/best_model"

tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_PATH)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

model.eval()

def predict_sentiment(text):
    if not text or text.strip() == "":
        return "Type a review first."
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True).to(device)
    with torch.no_grad():
        outputs = model(**inputs)
        probs = torch.nn.functional.softmax(outputs.logits, dim=-1)
    label = int(torch.argmax(probs, dim=1).cpu().numpy()[0])
    conf = float(probs[0][label].cpu().numpy())
    return ("Positive" if label == 1 else "Negative") + f" (confidence: {conf:.2f})"

demo = gr.Interface(
    fn=predict_sentiment,
    inputs=gr.Textbox(lines=3, placeholder="Type a text here..."),
    outputs="text",
    title="Text Attack",
    description=f"Model loaded from: {MODEL_PATH}"
)

if __name__ == "__main__":
    def same_auth(username, password):
        return username == "admin" and password == "pass1234"
demo.launch(auth=same_auth)



