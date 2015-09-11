from flask import Flask
from flask import request
from amazon.api import AmazonAPI

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/amazon', methods=['GET'])
def product():
    isbn = request.args.get('isbn', '')

    try:
        AMAZON_ACCESS_KEY = 'AKIAJUE7O3QM7ZFIA67A'
        AMAZON_SECRET_KEY = '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'
        AMAZON_ASSOC_TAG = 'csrgxtu-23'
        amazon_cn = AmazonAPI(AMAZON_ACCESS_KEY, AMAZON_SECRET_KEY, AMAZON_ASSOC_TAG, region="CN")
        product = amazon_cn.lookup(IdType='ISBN', ItemId=isbn, SearchIndex='Books')

        return product.to_string()
    except:
        return 'fuck it'

if __name__ == "__main__":
    app.debug = True
    app.run()
