import os
import random
import time

def rename_clips():
    print("renamming...")
    # Directory where the files are located
    directory = './videos'

    # Get a list of all the files in the directory
    files = os.listdir(directory)

    # Shuffle the list of files
    random.shuffle(files)

    # Loop through the files
    for i, file in enumerate(files):
        # Construct the new file name
        new_name = 'files{}.mp4'.format(i + 1)

        # Get the full path of the file
        old_path = os.path.join(directory, file)

        # Construct the full path of the new file name
        new_path = os.path.join(directory, new_name)

        # Rename the file
        os.rename(old_path, new_path)

    time.sleep(1)

    # Directory where the files are located
    directory = './videos'

    # Get a list of all the files in the directory
    files = os.listdir(directory)

    # Shuffle the list of files
    random.shuffle(files)

    # Loop through the files
    for i, file in enumerate(files):
        # Construct the new file name
        new_name = '{}.mp4'.format(i + 1)

        # Get the full path of the file
        old_path = os.path.join(directory, file)

        # Construct the full path of the new file name
        new_path = os.path.join(directory, new_name)

        # Rename the file
        os.rename(old_path, new_path)

