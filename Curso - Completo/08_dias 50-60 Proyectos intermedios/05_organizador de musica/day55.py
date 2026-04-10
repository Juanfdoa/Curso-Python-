# Bibliotecas Necesarias:
# Mutagen: pip install mutagen -> Sirve para extraer los metadatos de los archivos

import os
import re
import shutil
import json
from mutagen import File

import re

def clean_name(name, max_length=50):
    if not name:
        return "Unknown"

    # Eliminar TODO lo que esté entre paréntesis (incluidos)
    name = re.sub(r'\(.*?\)', '', name)

    # Eliminar caracteres especiales (dejar solo letras, números y espacios)
    name = re.sub(r'[^a-zA-Z0-9\s\-]', '', name)

    # Reemplazar múltiples espacios por uno
    name = re.sub(r'\s+', ' ', name)

    # 🔥 Quitar espacios al inicio y final (MUY IMPORTANTE)
    name = name.strip()

    # Evitar vacío
    if not name:
        return "Unknown"

    # Limitar longitud
    return name[:max_length]

def scan_directory(directory, extensions=('.mp3','.flac','.wav')):
    music_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(extensions):
                music_files.append(os.path.join(root, file))
    return music_files

def organize_files(music_files, output_directory):
    for file in music_files:
        metadata = extract_metadata(file)
        if metadata:
            album = clean_name(metadata.get('album'))
            if not album:
                album = "Unknown Album"

            # Define the destination folder
            album_folder = os.path.join(output_directory, album)

            # Create the directories if they don't exist
            os.makedirs(album_folder, exist_ok=True)

            # Move files
            filename = clean_name(os.path.basename(file), 80)

            # asegurar extensión
            if not filename.lower().endswith(".mp3"):
                filename += ".mp3"

            destination = os.path.join(album_folder, filename)
            shutil.move(file, destination)
            print(f'Moved: {file} -> {destination}')

def save_summary_to_json(music_files, output_file):
    summary = []
    for file in music_files:
        metadata = extract_metadata(file)
        if metadata:
            summary.append(metadata)
    
    with open(output_file, "w") as json_file:
        json.dump(summary, json_file, indent=4)
    print(f'Summary saved to {output_file}')

def extract_metadata(file_path):
    try:
        audio = File(file_path, easy=True)
        return{
            "title": audio.get("title", ["Unknown Title"])[0],
            "artist": audio.get("artist", ["Unknown Artist"])[0],
            "album": audio.get("album", ["Unknown Album"])[0],
            "genre": audio.get("genre", ["Unknown Genre"])[0],
        }
    except Exception as e:
        print(f'Error extracting metadata for {file_path}: {e}')
        return None


def main():
    print('Welcome to the Music Playlist organizer!')
    music_directory = input('Enter the path to your music directory: ')
    output_directory = input('Enter the path for the organized music directory: ')

    music_files = scan_directory(music_directory)
    if not music_files:
        print('No music files found')
        return
    
    print(f'Found {len(music_files)} music files')
    save_summary_to_json(music_files, "Music_summary.json")
    organize_files(music_files, output_directory)
    print('Music organization complete!')

if __name__ == '__main__':
    main()