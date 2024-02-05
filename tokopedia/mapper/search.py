from utils.functional import soldConverter , tokpedSellMapper, getTimestampNowMillis

def mapper_search(datas: list):
    if len(datas) == 0:
        return []
    results = []
    for data in datas:
        item = data.get('data')
        if 'displaAdsV3' not in item:
            return None
        data = item['displaAdsV3'].get('data')
        if not data:
            return None
        shop:dict = data.get("shop")
        product:dict = data.get("product")
        campaign: dict = data.get("campaign")
        mapper = {
            "marketplace": "tokopedia",
            "productName": product.get('name'),
            "images": [product.get('image').get('imageUrl')],
            "brand": "",
            "merchantName": shop.get('name'),
            "price":  {
                "originalPrice": soldConverter(campaign.get('originalPrice')),
                "discount": campaign.get('discountPercentage'),
                "finalPrice": soldConverter(product.get('price')),
            },
            "category": product.get('categoryBreadcrumb').split(' / ')[-1],
            "sell" : tokpedSellMapper(product.get('sale')),
            "categoryList": product.get('categoryBreadcrumb').split(' / '),
            "url": product.get('url'),
            "crawlAt": getTimestampNowMillis()
        }
        results.append(mapper)
    return results