from amazon.api import AmazonAPI

AMAZON_ACCESS_KEY = 'AKIAJUE7O3QM7ZFIA67A'
AMAZON_SECRET_KEY = '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'
AMAZON_ASSOC_TAG = 'csrgxtu-23'

amazon_cn = AmazonAPI(AMAZON_ACCESS_KEY, AMAZON_SECRET_KEY, AMAZON_ASSOC_TAG, region="CN")
#product = amazon_cn.lookup(ItemId='9787540472238')
product = amazon_cn.lookup(IdType='ISBN', ItemId='9787540472238', SearchIndex='Books')

print product.title, product.price_and_currency[0]
