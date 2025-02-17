from pydantic import BaseModel

class ImageModel(BaseModel):
    image_path: str
    page_number: int
    metadata: dict = {}  # Optional metadata for the image, can be extended as needed