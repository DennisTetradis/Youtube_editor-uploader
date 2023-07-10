import os
import random
import time

def rename_clips():
    print("renamming...")
    directory = './videos'
    files = os.listdir(directory)
    random.shuffle(files)
    for i, file in enumerate(files):
        new_name = 'files{}.mp4'.format(i + 1)
        old_path = os.path.join(directory, file)
        new_path = os.path.join(directory, new_name)
        os.rename(old_path, new_path)

    time.sleep(1)
    directory = './videos'
    files = os.listdir(directory)
    random.shuffle(files)

    # Loop through the files
    for i, file in enumerate(files):
        new_name = '{}.mp4'.format(i + 1)
        old_path = os.path.join(directory, file)
        new_path = os.path.join(directory, new_name)

        # Rename the file
        os.rename(old_path, new_path)

