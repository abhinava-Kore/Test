from fastapi import FastAPI
from pydantic import BaseModel, BaseSettings
from PIL import Image
from torchvision import transforms
import numpy as np
import torch
from transformers import pipeline


class Settings(BaseSettings):
    model_name: str = "distilbert-base-uncased-finetuned-sst-2-english"

    class Config:
        env_prefix = "VERSYKA_"


class TextRequest(BaseModel):
    text: str


settings = Settings()
app = FastAPI(title="Versyka Python upgrade fixture")
classifier = pipeline("text-classification", model=settings.model_name, framework="pt")
image_transform = transforms.Compose(
    [transforms.Resize((224, 224)), transforms.ToTensor()]
)


@app.post("/classify")
def classify(request: TextRequest) -> dict:
    # Pydantic v1 API: this is a deliberate migration point for Pydantic v2.
    legacy_payload = request.dict()
    prediction = classifier(legacy_payload["text"])[0]
    return {"label": prediction["label"], "score": float(prediction["score"])}


def image_to_tensor(image: Image.Image) -> torch.Tensor:
    """Convert an RGB image into a model-ready tensor using torchvision."""
    rgb = image.convert("RGB")
    pixels = np.asarray(rgb, dtype=np.float32) / 255.0
    return image_transform(Image.fromarray((pixels * 255).astype(np.uint8)))
