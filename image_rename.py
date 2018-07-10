import os, shutil, csv
import re, string



def get_image_paths():
    images_names = get_image_names()
    traverse_path = "/home/dhonda/google_drive/turtle_and_pete/Products/Images/"
    for traverse_path, dirnames, filenames in os.walk(traverse_path):
        parts = traverse_path.split('/')
        sku_id = parts[-1].lower()
        if sku_id == 'main idea' or not filenames:
            continue
        for f in filenames:
            origin = traverse_path + '/' + f
            destination = "/home/dhonda/Pictures/" + images_names[sku_id] + '_' + f.lower()
            old = "/home/dhonda/Pictures/old/" + images_names[sku_id] + '_' + f.lower()
            if not os.path.exists(old):
                shutil.copy(origin, destination)


def get_image_names():
    csv_file = "/home/dhonda/google_drive/turtle_and_pete/code/import_with_images.csv"
    with open(csv_file, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        images = {row[0]: image_friendly_name(row[2].lower()) for row in reader}
    return images

def image_friendly_name(a):
    return re.sub('[\W_]+', '_', str.lstrip(str.rstrip(a)))


get_image_paths()





