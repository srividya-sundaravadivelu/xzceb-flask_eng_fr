from machinetranslation import translator
from flask import Flask, render_template, request, send_from_directory
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    return translator.english_to_french(textToTranslate)
   

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    return translator.french_to_english(textToTranslate)

@app.route("/")
def renderIndexPage():
    # Write the code to render template
    return render_template('recommendations.html')

@app.route('/BX-Books.csv')
def serve_books_csv():
    return send_from_directory('.', 'BX-Books.csv')

@app.route('/book_details/<isbn>')
def book_details(isbn):
    # Read the BX-Books.csv file
    with open('BX-Books.csv', 'r') as file:
        csv_data = file.read()

    # Parse the CSV data and find the book with the matching ISBN
    books = parseCSV(csv_data)
    book = next((b for b in books if b['ISBN'] == isbn), None)

    if book:
        return render_template('book_details.html', book=book)
    else:
        return f'Book with ISBN {isbn} not found.'

def parseCSV(csv_data):
    # Parse the CSV data and return a list of dictionaries representing each book
    lines = csv_data.split('\n')
    headers = lines[0].split(';')
    books = []
    for line in lines[1:]:
        values = line.split(';')
        if len(values) == len(headers):
            book = {}
            for i in range(len(headers)):
                attribute_name = headers[i].strip('"')  # Remove leading and trailing quotes
                book[attribute_name] = values[i].strip('"')
            books.append(book)
    return books




if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
