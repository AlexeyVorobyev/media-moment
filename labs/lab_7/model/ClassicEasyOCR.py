import easyocr
from .BaseModel import BaseModel


class ClassicEasyOCR(BaseModel):

    def __init__(self, model: easyocr.easyocr.Reader = None):
        self.model = model or easyocr.Reader(['en'])

    def image_to_string(self, image, **params):
        results = self.model.readtext(image, allowlist='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', **params)

        if len(results) < 1:
            return None

        for (bbox, text, prob) in results:
            return text
