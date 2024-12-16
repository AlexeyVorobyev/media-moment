from .BaseModel import BaseModel
import pytesseract

class CustomEngProcessedPytesseract(BaseModel):

    def image_to_string(self, image, **params):
        return pytesseract.image_to_string(
            image,
            config="--oem 1 --psm 6 -l custom_eng_processed",
        )
