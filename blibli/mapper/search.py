import json
from utils import functional as util

def mapper(data: dict, product_name: str = None, log:bool = False):
    products_result = []
    if 'products' in data.get('data') and len(data.get('data')['products']) > 0:
        products = data.get('data')['products']
        for item in products:
            price = item.get('price')
            root_category = item.get('rootCategory')
            soldRangeCount = item.get('soldRangeCount')
            template = {}
            template["marketplace"] = "blibli"
            template["productName"] = item.get('name', 'productName')
            template["brand"] = item.get('brand')
            template["images"] = item.get('images')
            template["price"] = {
                "originalPrice": util.stringPriceConverter(price.get('strikeThroughPriceDisplay',"0")),
                "discount": price.get('discount'),
                "finalPrice": util.stringPriceConverter(price.get('priceDisplay',"0"))
            }
            template["category"] = root_category.get('name') if root_category and 'name' in root_category else ''
            template["sell"] = util.soldConverter(soldRangeCount.get('en')) if soldRangeCount and 'en' in soldRangeCount else 0
            template["categoryList"] = item.get('categoryNameHierarchy')
            template["url"] = 'https://blibli.com'+item.get('url')
            template["crawlAt"] = util.getTimestampNowMillis()
            if log:
              print(template, "\n\n")
            products_result.append(template)

    if product_name:
        with(open(f'assets/blibli/blibli-{product_name}-mapped.json', 'w')) as f:
            f.write(json.dumps(products_result, indent=4))
    return products_result


def test_mapper():
    with open("response-samsung.json", "r") as file:
      res = mapper(json.load(file))
      with(open('blibli-mapped.json', 'w')) as f:
          f.write(json.dumps(res, indent=4))