from flask import Flask
from flask import request
from amazon.api import AmazonAPI
import re
import json

app = Flask(__name__)

def isAvailable(inputStr):
    inputStr = inputStr.replace('\n', '');
    m = re.match(r'.*<TotalNew>(\d*)</TotalNew>', inputStr, re.I)
    if m:
        if m.group(1) > 0:
            return True
        else:
            return False
    else:
        return False

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/amazon', methods=['GET'])
def product():
    isbn = request.args.get('isbn', '')
    data = {}

    try:
        AMAZON_ACCESS_KEY = 'AKIAJUE7O3QM7ZFIA67A'
        AMAZON_SECRET_KEY = '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'
        AMAZON_ASSOC_TAG = 'csrgxtu-23'
        amazon_cn = AmazonAPI(AMAZON_ACCESS_KEY, AMAZON_SECRET_KEY, AMAZON_ASSOC_TAG, region="CN")
        product = amazon_cn.lookup(IdType='ISBN', ItemId=isbn, SearchIndex='Books')

        data['isbn'] = product.isbn
        data['author'] = product.author
        data['price'] = product.price_and_currency[0]
        data['publisher'] = product.publisher
        data['available'] = isAvailable(product.to_string())
        data['error'] = False

        # return json.dumps(data)
    except:
        data['error'] = True
        # return json.dumps(data)
    finally:
        return json.dumps(data)

if __name__ == "__main__":
    app.debug = True
    app.run()
