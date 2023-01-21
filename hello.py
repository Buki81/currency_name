import requests
import json
from flask import Flask


# text = requests.get('http://www.cbr-xml-daily.ru/daily_json.js').text # курс валют
# currency = json.loads(text)
# for key, value in currency['Valute'].items():
#     print(key)
#     print(value['Name'], value['Value'], '\n')


app = Flask(__name__)

@app.route("/")
def hello():
    text = requests.get('http://www.cbr-xml-daily.ru/daily_json.js').text  # курс валют
    # currency = json.loads(text)
    result = text
    # for key, value in currency['Valute'].items():
    #     v = value['Name'], value['Value'], '\n'
    #     # return "<h1>{k}<h1>"
    #     result += str(key) + '<br>' + value['Name']+ ': ' + str(value['Value']) + '\n' + '<br>' +'<br>'

    return result

# print(hello())
if __name__ == "__main__":
    app.run()