import zipfile

mnist_zip_path = './mnist.zip'

extract_dir = './mnist_data'

with zipfile.ZipFile(mnist_zip_path, 'r') as zip_ref:
    zip_ref.extractall(extract_dir)