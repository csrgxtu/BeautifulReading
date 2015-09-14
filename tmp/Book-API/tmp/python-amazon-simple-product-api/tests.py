import unittest

from nose.tools import assert_equals, assert_true, assert_false

import datetime
from amazon.api import (AmazonAPI,
                        CartException,
                        CartInfoMismatchException,
                        SearchException,
                        AsinNotFound)
from test_settings import (AMAZON_ACCESS_KEY,
                           AMAZON_SECRET_KEY,
                           AMAZON_ASSOC_TAG)


TEST_ASIN = "B007HCCNJU"

PRODUCT_ATTRIBUTES = [
    'asin', 'author', 'binding', 'brand', 'browse_nodes', 'ean', 'edition',
    'editorial_review', 'eisbn', 'features', 'get_parent', 'isbn', 'label',
    'large_image_url', 'list_price', 'manufacturer', 'medium_image_url',
    'model', 'mpn', 'offer_url', 'parent_asin', 'part_number',
    'price_and_currency', 'publication_date', 'publisher', 'region',
    'release_date', 'reviews', 'sku', 'small_image_url', 'tiny_image_url',
    'title', 'upc'
]

CART_ATTRIBUTES = [
    'cart_id', 'purchase_url', 'amount', 'formatted_price', 'currency_code',
    'url_encoded_hmac', 'hmac'
]

CART_ITEM_ATTRIBUTES = [
    'cart_item_id', 'asin', 'title', 'amount', 'formatted_price',
    'currency_code', 'quantity', 'product_group',
]

CACHE = {}


def cache_writer(url, response):
    CACHE[url] = response


def cache_reader(url):
    return CACHE.get(url, None)


def cache_clear():
    global CACHE
    CACHE = {}


class TestAmazonApi(unittest.TestCase):
    """Test Amazon API

    Test Class for Amazon simple API wrapper.
    """

    def setUp(self):
        """Set Up.

        Initialize the Amazon API wrapper. The following values:

        * AMAZON_ACCESS_KEY
        * AMAZON_SECRET_KEY
        * AMAZON_ASSOC_TAG

        Are imported from a custom file named: 'test_settings.py'
        """
        self.amazon = AmazonAPI(
            AMAZON_ACCESS_KEY,
            AMAZON_SECRET_KEY,
            AMAZON_ASSOC_TAG,
            CacheReader=cache_reader,
            CacheWriter=cache_writer,
            MaxQPS=0.5
        )

    def test_lookup(self):
        """Test Product Lookup.

        Tests that a product lookup for a kindle returns results and that the
        main methods are working.
        """
        product = self.amazon.lookup(ItemId="B00I15SB16")
        assert_true('Kindle' in product.title)
        assert_equals(product.ean, '0848719039726')
        assert_equals(
            product.large_image_url,
            'http://ecx.images-amazon.com/images/I/51XGerXeYeL.jpg'
        )
        assert_equals(
            product.get_attribute('Publisher'),
            'Amazon'
        )
        assert_equals(product.get_attributes(
            ['ItemDimensions.Width', 'ItemDimensions.Height']),
            {'ItemDimensions.Width': '469', 'ItemDimensions.Height': '40'})
        assert_true(len(product.browse_nodes) > 0)
        assert_true(product.price_and_currency[0] is not None)
        assert_true(product.price_and_currency[1] is not None)
        assert_equals(product.browse_nodes[0].id, 2642129011)
        assert_equals(product.browse_nodes[0].name, 'eBook Readers')

    def test_lookup_nonexistent_asin(self):
        """Test Product Lookup with a nonexistent ASIN.

        Tests that a product lookup for a nonexistent ASIN raises AsinNotFound.
        """
        self.assertRaises(AsinNotFound, self.amazon.lookup, ItemId="ABCD1234")

    def test_batch_lookup(self):
        """Test Batch Product Lookup.

        Tests that a batch product lookup request returns multiple results.
        """
        asins = ['B007HCCNJU', 'B00BWYQ9YE',
                 'B00BWYRF7E', 'B00D2KJDXA']
        products = self.amazon.lookup(ItemId=','.join(asins))
        assert_equals(len(products), len(asins))
        for i, product in enumerate(products):
            assert_equals(asins[i], product.asin)

    def test_search(self):
        """Test Product Search.

        Tests that a product search is working (by testing that results are
        returned). And that each result has a title attribute. The test
        fails if no results where returned.
        """
        products = self.amazon.search(Keywords='kindle', SearchIndex='All')
        for product in products:
            assert_true(hasattr(product, 'title'))
            break
        else:
            assert_true(False, 'No search results returned.')

    def test_search_n(self):
        """Test Product Search N.

        Tests that a product search n is working by testing that N results are
        returned.
        """
        products = self.amazon.search_n(
            1,
            Keywords='kindle',
            SearchIndex='All'
        )
        assert_equals(len(products), 1)

    def test_search_no_results(self):
        """Test Product Search with no results.

        Tests that a product search with that returns no results throws a
        SearchException.
        """
        products = self.amazon.search(Title='HarryPotter',
                                      SearchIndex='Automotive')
        self.assertRaises(SearchException, (x for x in products).next)

    def test_amazon_api_defaults_to_US(self):
        """Test Amazon API defaults to the US store."""
        amazon = AmazonAPI(
            AMAZON_ACCESS_KEY,
            AMAZON_SECRET_KEY,
            AMAZON_ASSOC_TAG
        )
        assert_equals(amazon.api.Region, "US")

    def test_search_amazon_uk(self):
        """Test Poduct Search on Amazon UK.

        Tests that a product search on Amazon UK is working and that the
        currency of any of the returned products is GBP. The test fails if no
        results were returned.
        """
        amazon = AmazonAPI(
            AMAZON_ACCESS_KEY,
            AMAZON_SECRET_KEY,
            AMAZON_ASSOC_TAG,
            region="UK"
        )
        assert_equals(amazon.api.Region, "UK", "Region has not been set to UK")

        products = amazon.search(Keywords='Kindle', SearchIndex='All')
        currencies = [product.price_and_currency[1] for product in products]
        assert_true(len(currencies), "No products found")

        is_gbp = 'GBP' in currencies
        assert_true(is_gbp, "Currency is not GBP, cannot be Amazon UK, though")

    def test_similarity_lookup(self):
        """Test Similarity Lookup.

        Tests that a similarity lookup for a kindle returns 10 results.
        """
        products = self.amazon.similarity_lookup(ItemId=TEST_ASIN)
        assert_true(len(products) > 5)

    def test_product_attributes(self):
        """Test Product Attributes.

        Tests that all product that are supposed to be accessible are.
        """
        product = self.amazon.lookup(ItemId=TEST_ASIN)
        for attribute in PRODUCT_ATTRIBUTES:
            getattr(product, attribute)

    def test_browse_node_lookup(self):
        """Test Browse Node Lookup.

        Test that a lookup by Brose Node ID returns appropriate node.
        """
        bnid = 2642129011
        bn = self.amazon.browse_node_lookup(BrowseNodeId=bnid)[0]
        assert_equals(bn.id, bnid)
        assert_equals(bn.name, 'eBook Readers')
        assert_equals(bn.is_category_root, False)

    def test_obscure_date(self):
        """Test Obscure Date Formats

        Test a product with an obscure date format
        """
        product = self.amazon.lookup(ItemId="0933635869")
        assert_equals(product.publication_date.year, 1992)
        assert_equals(product.publication_date.month, 5)
        assert_true(isinstance(product.publication_date, datetime.date))

    def test_single_creator(self):
        """Test a product with a single creator
        """
        product = self.amazon.lookup(ItemId="B00005NZJA")
        creators = dict(product.creators)
        assert_equals(creators[u"Jonathan Davis"], u"Narrator")
        assert_equals(len(creators.values()), 1)

    def test_multiple_creators(self):
        """Test a product with multiple creators
        """
        product = self.amazon.lookup(ItemId="B007V8RQC4")
        creators = dict(product.creators)
        assert_equals(creators[u"John Gregory Betancourt"], u"Editor")
        assert_equals(creators[u"Colin Azariah-Kribbs"], u"Editor")
        assert_equals(len(creators.values()), 2)

    def test_no_creators(self):
        """Test a product with no creators
        """
        product = self.amazon.lookup(ItemId="8420658537")
        assert_false(product.creators)

    def test_single_editorial_review(self):
        product = self.amazon.lookup(ItemId="1930846258")
        expected = u'In the title piece, Alan Turing'
        assert_equals(product.editorial_reviews[0][:len(expected)], expected)
        assert_equals(product.editorial_review, product.editorial_reviews[0])
        assert_equals(len(product.editorial_reviews), 1)

    def test_multiple_editorial_reviews(self):
        product = self.amazon.lookup(ItemId="B000FBJCJE")
        expected = u'Only once in a great'
        assert_equals(product.editorial_reviews[0][:len(expected)], expected)
        expected = u'From the opening line'
        assert_equals(product.editorial_reviews[1][:len(expected)], expected)
        # duplicate data, amazon user data is great...
        expected = u'Only once in a great'
        assert_equals(product.editorial_reviews[2][:len(expected)], expected)

        assert_equals(len(product.editorial_reviews), 3)

    def test_languages_english(self):
        """Test Language Data

        Test an English product
        """
        product = self.amazon.lookup(ItemId="1930846258")
        assert_true('english' in product.languages)
        assert_equals(len(product.languages), 1)

    def test_languages_spanish(self):
        """Test Language Data

        Test an English product
        """
        product = self.amazon.lookup(ItemId="8420658537")
        assert_true('spanish' in product.languages)
        assert_equals(len(product.languages), 1)

    def test_region(self):
        amazon = AmazonAPI(AMAZON_ACCESS_KEY, AMAZON_SECRET_KEY,
                           AMAZON_ASSOC_TAG)
        assert_equals(amazon.region, 'US')

        # old 'region' parameter
        amazon = AmazonAPI(AMAZON_ACCESS_KEY, AMAZON_SECRET_KEY,
                           AMAZON_ASSOC_TAG, region='UK')
        assert_equals(amazon.region, 'UK')

        # kwargs method
        amazon = AmazonAPI(AMAZON_ACCESS_KEY, AMAZON_SECRET_KEY,
                           AMAZON_ASSOC_TAG, Region='UK')
        assert_equals(amazon.region, 'UK')

    def test_kwargs(self):
        amazon = AmazonAPI(AMAZON_ACCESS_KEY, AMAZON_SECRET_KEY,
                           AMAZON_ASSOC_TAG, MaxQPS=0.7)

    def test_images(self):
        """Test images property

        Test that the images property has a value when using the
        Images ResponseGroup
        """
        product = self.amazon.lookup(ResponseGroup='Images',
                                     ItemId='B00TSVVNQC')
        assert_equals(type(product.images), list)
        assert_equals(len(product.images), 7)


class TestAmazonCart(unittest.TestCase):
    def setUp(self):
        self.amazon = AmazonAPI(
            AMAZON_ACCESS_KEY,
            AMAZON_SECRET_KEY,
            AMAZON_ASSOC_TAG,
            CacheReader=cache_reader,
            CacheWriter=cache_writer,
            MaxQPS=0.5
        )

    def test_cart_clear_required_params(self):
        self.assertRaises(CartException, self.amazon.cart_clear, None, None)
        self.assertRaises(CartException, self.amazon.cart_clear, 'NotNone',
                          None)
        self.assertRaises(CartException, self.amazon.cart_clear, None,
                          'NotNone')

    def build_cart_object(self):
        product = self.amazon.lookup(ItemId="B0016J8AOC")
        return self.amazon.cart_create(
            {
                'offer_id': product._safe_get_element(
                    'Offers.Offer.OfferListing.OfferListingId'),
                'quantity': 1
            }
        )

    def test_cart_create_single_item(self):
        cart = self.build_cart_object()
        assert_equals(len(cart), 1)

    def test_cart_create_multiple_item(self):
        product1 = self.amazon.lookup(ItemId="B0016J8AOC")
        product2 = self.amazon.lookup(ItemId="B007HCCNJU")
        asins = [product1.asin, product2.asin]

        cart = self.amazon.cart_create([
            {
                'offer_id': product1._safe_get_element(
                    'Offers.Offer.OfferListing.OfferListingId'),
                'quantity': 1
            },
            {
                'offer_id': product2._safe_get_element(
                    'Offers.Offer.OfferListing.OfferListingId'),
                'quantity': 1
            },
        ])
        assert_equals(len(cart), 2)
        for item in cart:
            assert_true(item.asin in asins)

    def test_cart_clear(self):
        cart = self.build_cart_object()
        new_cart = self.amazon.cart_clear(cart.cart_id, cart.hmac)
        assert_true(new_cart._safe_get_element('Cart.Request.IsValid'))

    def test_cart_clear_wrong_hmac(self):
        cart = self.build_cart_object()
        # never use urlencoded hmac, as library encodes as well. Just in case
        # hmac = url_encoded_hmac we add some noise
        hmac = cart.url_encoded_hmac + '%3d'
        self.assertRaises(CartInfoMismatchException, self.amazon.cart_clear,
                          cart.cart_id, hmac)

    def test_cart_attributes(self):
        cart = self.build_cart_object()
        for attribute in CART_ATTRIBUTES:
            getattr(cart, attribute)

    def test_cart_item_attributes(self):
        cart = self.build_cart_object()
        for item in cart:
            for attribute in CART_ITEM_ATTRIBUTES:
                getattr(item, attribute)

    def test_cart_get(self):
        # We need to flush the cache here so we will get a new cart that has
        # not been used in test_cart_clear
        cache_clear()
        cart = self.build_cart_object()
        fetched_cart = self.amazon.cart_get(cart.cart_id, cart.hmac)

        assert_equals(fetched_cart.cart_id, cart.cart_id)
        assert_equals(len(fetched_cart), len(cart))

    def test_cart_get_wrong_hmac(self):
        # We need to flush the cache here so we will get a new cart that has
        # not been used in test_cart_clear
        cache_clear()
        cart = self.build_cart_object()
        self.assertRaises(CartInfoMismatchException, self.amazon.cart_get,
                          cart.cart_id, cart.hmac + '%3d')

    def test_cart_add(self):
        cart = self.build_cart_object()
        product = self.amazon.lookup(ItemId="B007HCCNJU")
        item = {
            'offer_id': product._safe_get_element(
                'Offers.Offer.OfferListing.OfferListingId'),
            'quantity': 1
        }
        new_cart = self.amazon.cart_add(item, cart.cart_id, cart.hmac)
        assert_true(len(new_cart) > len(cart))

    def test_cart_modify(self):
        cart = self.build_cart_object()
        cart_item_id = None
        for item in cart:
            cart_item_id = item.cart_item_id
        item = {'cart_item_id': cart_item_id, 'quantity': 3}
        new_cart = self.amazon.cart_modify(item, cart.cart_id, cart.hmac)
        assert_equals(new_cart[cart_item_id].quantity, '3')

    def test_cart_delete(self):
        cart = self.build_cart_object()
        cart_item_id = None
        for item in cart:
            cart_item_id = item.cart_item_id
        item = {'cart_item_id': cart_item_id, 'quantity': 0}
        new_cart = self.amazon.cart_modify(item, cart.cart_id, cart.hmac)
        self.assertRaises(KeyError, new_cart.__getitem__, cart_item_id)

if __name__ == '__main__':
    unittest.main()