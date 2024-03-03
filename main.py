from flask import Flask, render_template, request
from googletrans import Translator

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    translator = Translator()
    text = request.form['text']
    dest_lang = request.form['dest_lang']
    translated_text = translator.translate(text, dest=dest_lang).text
    return render_template('translate.html', text=text, dest_lang=dest_lang, translated_text=translated_text)

if __name__ == '__main__':
    app.run(debug=True)
