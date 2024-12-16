import csv

import cv2

from model.BaseModel import BaseModel
from utils.dataset.clear_from_chars import clear_from_extension
from utils.dataset.get_image_filenames import get_image_filenames
from val_type.BaseValType import BaseValType


class ModelExecutor:
    __model: BaseModel

    __val_types: list[BaseValType]

    def __init__(
            self,
            model: BaseModel,
            val_types: list[BaseValType],
    ):
        self.__model = model
        self.__val_types = val_types

    def execute(
            self,
            input_data_folder_path: str,
            output_folder_path: str
    ):

        answers: list[dict[str, str]] = []

        for img_filename in get_image_filenames(input_data_folder_path):
            img = cv2.imread(f'{input_data_folder_path}/{img_filename}')

            text_from_model = self.__model.image_to_string(img)

            answer = {
                "predict": text_from_model,
                "correct": clear_from_extension(img_filename),
            }

            for val_type in self.__val_types:
                answer[val_type.__class__.__name__] = val_type.check_value(
                    answer["predict"],
                    answer["correct"]
                )

            answers.append(answer)

        val_types_mark = ".".join([val_type.__class__.__name__ for val_type in self.__val_types])

        output_file_path = f"{output_folder_path}/{self.__model.__class__.__name__}.{val_types_mark}.csv"

        if len(answers) == 0:
            return

        with open(output_file_path, 'w') as file:
            writer = csv.DictWriter(
                f=file,
                fieldnames=answers[0].keys(),
                delimiter=';',
            )

            writer.writeheader()

            for row in answers:
                writer.writerow(row)
