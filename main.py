import json
from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI()

class Image(BaseModel):
    url: str

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/image_to_text")
async def image_to_text(image: Image):
    try:
        image_to_text = pipeline("image-to-text", model="nlpconnect/vit-gpt2-image-captioning")
        result = image_to_text(image.url)
        return {"message": result[0]["generated_text"]}
    except:
        return {"message": "Something went wrong"}