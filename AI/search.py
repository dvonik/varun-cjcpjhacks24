import json
from fuzzywuzzy import process
from fuzzywuzzy import fuzz

#load api keys
with open('api_keys.json') as f:
    apikeys = json.load(f)

#instansiate a dictory with apikeys, company name and product

data = [{'api': "", 'company-name': "", "price": "", "product": ""}]

#fuzzy search algorithm

#def fuzzy_search(query):
 #   results = process.extract(query, [item['name'] for item in data], limit=10)
  #  return [{'name': item[0], 'email': item[1]['email'], 'score': item[2]} for item in results]


def search(query):
    response = requests.get(
        'https://api.example.com/products/search',
        params={'q': query, 'api_key': apikeys['product_api_key']}
    )
    products = response.json()

def compare_prices(existing_products, new_products):
    for new_product in new_products:
        lowest_price = None
        for existing_product in existing_products:
            # Use Jaro-Winkler algorithm to compare product names
            similarity = fuzz.jaro_winkler(new_product['name'], existing_product['name'])
            if similarity > 0.9:
                # If similar, compare prices
                if lowest_price is None or new_product['price'] < lowest_price:
                    lowest_price = new_product['price']
                    best_product = {
                        'name': new_product['name'],
                        'company': new_product['company'],
                        'price': new_product['price']
                    }
        if lowest_price is not None:
            # If lower price found, add to dictionary
            existing_products.append(best_product)

new_products = search('product x')
current_products = []
compare_prices(current_products, new_products)
print(current_products)

