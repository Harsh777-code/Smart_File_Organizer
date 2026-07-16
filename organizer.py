import os
import shutil

from extensions import *

def get_unique_filename(destination_folder, filename):

    name, extension = os.path.splitext(filename)

    counter = 1

    new_filename = filename

    while os.path.exists(os.path.join(destination_folder, new_filename)):
        new_filename = f"{name}({counter}){extension}"
        counter += 1

    return new_filename

def organize_folder(folder_path):

    categories = {
        "Images": IMAGE_EXTENSIONS,
        "Documents": DOCUMENT_EXTENSIONS,
        "Videos": VIDEO_EXTENSIONS,
        "Music": MUSIC_EXTENSIONS,
        "Archives": ARCHIVE_EXTENSIONS
    }

    count = {
        "Images": 0,
        "Documents": 0,
        "Videos": 0,
        "Music": 0,
        "Archives": 0,
        "Others": 0
    }

    for file in os.listdir(folder_path):

        source = os.path.join(folder_path, file)

        if os.path.isdir(source):
            continue

        extension = os.path.splitext(file)[1].lower()

        moved = False

        for folder_name, extensions in categories.items():

            if extension in extensions:

                destination_folder = os.path.join(folder_path, folder_name)

                os.makedirs(destination_folder, exist_ok=True)

                filename = get_unique_filename(destination_folder, file)

                destination = os.path.join(destination_folder, filename)

                shutil.move(source, destination)

                count[folder_name] += 1

                moved = True

                break

        if not moved:

            other_folder = os.path.join(folder_path, "Others")

            os.makedirs(other_folder, exist_ok=True)

            filename = get_unique_filename(other_folder, file)

            destination = os.path.join(other_folder, filename)

            shutil.move(source, destination)

            count["Others"] += 1

    return count