import os

def clear_from_extension_and_rotated(string: str) -> str:
    """
    Удалить расширение и поворот
    :param string:
    :return:
    """
    return string.split(".")[0].split('_')[0]

# Путь к папке с изображениями
image_folder = "./ground-truth"

# Получить список всех файлов .png в папке
image_files = [f for f in os.listdir(image_folder) if f.endswith('.png')]

# Генерация текстовых файлов-аннотаций
for image_file in image_files:
    # Удалить расширение
    base_name = os.path.splitext(image_file)[0]

    # Создать имя для текстового файла
    annotation_file = os.path.join(image_folder, f"{base_name}.gt.txt")

    text_content = clear_from_extension_and_rotated(os.path.splitext(image_file)[0])

    # Сохранить аннотацию
    with open(annotation_file, 'w', encoding='utf-8') as f:
        f.write(text_content)


    print(f"Создан файл аннотации: {annotation_file}")
