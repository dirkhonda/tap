import os
import csv
import re


def get_image_paths():
    images_names = get_image_names()
    traverse_path = "/home/dhonda/google_drive/turtle_and_pete/Products/Images/"
    dic = {}
    for traverse_path, dirnames, filenames in os.walk(traverse_path):
        parts = traverse_path.split('/')
        sku_id = parts[-1].lower()
        if sku_id == 'main idea' or not filenames:
            continue
        i_list = [images_names[sku_id] + '_' + f.lower() for f in sorted(filenames)]
        #dic[sku_id] = '|'.join(i_list)
        dic[sku_id] = i_list
    return dic

def get_image_names():
    csv_file = "/home/dhonda/google_drive/turtle_and_pete/code/import_with_images.csv"
    with open(csv_file, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        images = {row[0]: image_friendly_name(row[2].lower()) for row in reader}
    return images

def image_friendly_name(a):
    return re.sub('[\W_]+', '_', str.lstrip(str.rstrip(a)))


def write_csv_file():
    collection = get_image_paths()
    csv_file = "/home/dhonda/google_drive/turtle_and_pete/code/import_with_images.csv"
    csv_out = "/home/dhonda/google_drive/turtle_and_pete/code/import_with_images_1.csv"
    with open(csv_file, 'r') as csvfile:
        with open(csv_out, 'w') as csvout:
            reader = csv.reader(csvfile, delimiter=',', quotechar='"')
            writer = csv.writer(csvout, delimiter=',', quotechar='"')
            for row in reader:
                if row[0].isdigit() and collection.get(row[0], ''):
                    row[-7] = collection[row[0]][0]
                    if len(collection[row[0]]) > 1:
                        row[5] = '|'.join(collection[row[0]][1:])
                writer.writerow(row)


write_csv_file()