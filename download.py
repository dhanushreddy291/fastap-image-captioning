# In this file, we define download_model
# It runs during container build time to get model weights built into the container

# Download model weights
from transformers import pipeline

def download_model():
    image_to_text = pipeline("image-to-text", model="nlpconnect/vit-gpt2-image-captioning")
    image_to_text("https://unsplash.com/photos/L1GTsRbwbss/download?ixid=MnwxMjA3fDB8MXxhbGx8MzR8fHx8fHwyfHwxNjc5NzIyMjQ2&force=true&w=2400")

# Run download_model
if __name__ == "__main__":
    download_model()