import zipfile

mnist_zip_path = './mnist.zip'
extract_dir = './mnist_data'
    
def unzip_dataset(zip_path, extract_dir):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_dir)