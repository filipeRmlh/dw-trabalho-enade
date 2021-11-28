import errno
import os
import requests
import zipfile
from dictionaries.paths_dict import *


def split_file_name(uri):
    splitted_path = str(uri).split("/")
    return '/'.join(splitted_path[0:-1]), splitted_path[-1]


def open_or_create_file(directory, file_name):
    try:
        os.makedirs(directory)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
    return open('/'.join([directory, file_name]), 'wb')


def download_file(url, directory):
    print('Downloading {0} to {1}'.format(url, directory))
    url_path, file_name = split_file_name(url)
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open_or_create_file(directory, file_name) as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    return directory, file_name


def get_data():
    for year, url in dictionary_urls.items():
        dest_dir, file = download_file(
            url,
            zip_data_root_path)
        extract_zip(dest_dir + '/' + file, extracted_data_root_path + '/' + year)
    print('getting data finished')


def extract_zip(file_path, dest_path):
    print('Extracting {0} to {1}'.format(file_path, dest_path))
    with zipfile.ZipFile(file_path, 'r') as zip_ref:
        zip_ref.extractall(dest_path)


if __name__ == '__main__':
    get_data()
