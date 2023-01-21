import requests
import json
from flask import Flask


app = Flask(__name__)

@app.route("/")
def hello():
    text = requests.get('http://www.cbr-xml-daily.ru/daily_json.js').text  # курс валют
    currency = json.loads(text)
    result = ''
    for key, value in currency['Valute'].items():
        result += str(key) + '<br>' + value['Name']+ ': ' + str(value['Value']) + '\n' + '<br>' +'<br>'

    return result

if __name__ == "__main__":
    app.run()
