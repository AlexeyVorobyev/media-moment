from model.CustomEngPytesseractWithAugmentation import CustomEngPytesseractWithAugmentation
from model_executor import ModelExecutor
from val_type.FullValType import FullValType
from val_type.LevensteinValType import LevensteinValType

model_executor = ModelExecutor(
    model=CustomEngPytesseractWithAugmentation(),
    val_types=[
        FullValType(),
        LevensteinValType()
    ]
)

if __name__ == '__main__':
    model_executor.execute(
        input_data_folder_path="./dataset/processed",
        output_folder_path="./results",
        postfix="processed"
    )