import os
import shutil

def create_folder(base_path):
    folders = ['Documents', 'Images', 'Videos', 'Audio', 'Others']
    for folder in folders:
        folder_path = os.path.join(base_path, folder)
        os.makedirs(folder_path, exist_ok=True)

    organize_files(base_path)

def move_file(file_path, base_path, folder_name):
    target_folder = os.path.join(base_path, folder_name)
    shutil.move(file_path, target_folder)

def get_folder_for_file(file_name):
    file_extentions = {
        "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".csv"],
        "Images": [".jpg", ".png", ".gif", ".bmp"],
        "Videos": [".mp4", ".mov", ".avi", ".mkv"],
        "Audio": [".mp3", ".wav", ".flac"]
    }
    for folder, extensions in file_extentions.items():
        if any(file_name.endswith(ext) for ext in extensions):
            return folder
    return "Others"

def organize_files(base_path):
    for file_name in os.listdir(base_path):
        file_path = os.path.join(base_path, file_name)
        if os.path.isfile(file_path):
            folder_name = get_folder_for_file(file_name)
            move_file(file_path, base_path, folder_name)