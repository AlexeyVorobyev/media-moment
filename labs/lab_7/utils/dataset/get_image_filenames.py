import os


def get_image_filenames(folder_path: str) -> list[str]:
    image_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp')

    image_files = []

    for filename in os.listdir(folder_path):
        if filename.lower().endswith(image_extensions):
            image_files.append(filename)

    return image_files
