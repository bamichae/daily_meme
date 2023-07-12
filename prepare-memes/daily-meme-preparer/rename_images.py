import os
import pathlib
import glob2
import shutil

def get_this_directory():
    return pathlib.Path(__file__).parent.resolve()

def get_input_directory():
    this_directory = get_this_directory()
    return os.path.join(this_directory, 'input')

def get_output_directory():
    this_directory = get_this_directory()
    return os.path.join(this_directory, 'output')
def get_images():
    images = []

    input_directory = get_input_directory()
    for file in glob2.glob(os.path.join(input_directory, '*')):
        images.append(file)
    return images

def rename_images():
    output_directory = get_output_directory()

    images = get_images()
    image_increment = 0
    for image in images:
        shutil.copy(image, os.path.join(output_directory, f'{image_increment}.png'))
        image_increment += 1

def main():
    rename_images()


if __name__ == "__main__":
    main()