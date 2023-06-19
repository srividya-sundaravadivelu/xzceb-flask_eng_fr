import requests
import zipfile

url = 'https://cdn.freecodecamp.org/project-data/books/book-crossings.zip'
filename = 'book-crossings.zip'

response = requests.get(url)
with open(filename, 'wb') as file:
    file.write(response.content)

# Extract the contents of the zip file
with zipfile.ZipFile(filename, 'r') as zip_ref:
    zip_ref.extractall()
