import re

from .BaseModel import BaseModel
import pytesseract


class TesseractWithPostProcessing(BaseModel):

    def __clear_from_specific_symbols(self, input: str) -> str:
        return re.sub(r'[^a-zA-Z0-9]', '', input)

    def image_to_string(self, image, **params):
        return self.__clear_from_specific_symbols(
            pytesseract.image_to_string(image)
        )
