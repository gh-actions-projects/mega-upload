import os
import shutil
from mega import Mega

folder = os.environ['INPUT_FOLDER'] # dist
dest_dir = os.environ['INPUT_DEST-DIR'] # database
email = os.environ['INPUT_EMAIL'] # example@domain.com
password = os.environ['INPUT_PASSWORD'] # admin123

def zip(source_folder: str = './', output_zipfile: str = './data.zip'):
    return shutil.make_archive(output_zipfile.split('.zip')[0], 'zip', source_folder)

def mega_upload():
    mega = Mega()
    m = mega.login(email, password)
    m.create_folder(dest_dir)
    folder = m.find(dest_dir)
    file = m.upload("data.zip", folder[0])

    return m.get_upload_link(file)

def start():
    zip(folder)
    link = mega_upload()
    print(f"::set-output name=url::{link}")

if __name__ == '__main__':
    start()