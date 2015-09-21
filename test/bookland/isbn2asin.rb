include 'bookland'

isbn = '9780262011532'
asin = ASIN.from_isbn(isbn) # => "0262011530"
print asin
ASIN.to_isbn(asin) # => "9780262011532"
