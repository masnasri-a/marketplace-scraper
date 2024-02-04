import json
import requests
from blibli.config.base import get_config
from blibli.mapper.search import mapper

cookies, headers = get_config()

response = requests.get(
    'https://www.blibli.com/backend/search/products?sort=&page=1&start=0&searchTerm=iphone&intent=true&merchantSearch=true&multiCategory=true&customUrl=&&channelId=mobile-web&showFacet=false&isMobileBCA=false&isJual=false',
    cookies=cookies,
    headers=headers,
)

def search(product_name: str):
    product_name = product_name.replace(' ', '%20')
    page = 1
    start = 0
    results = []
    while True:
        response = requests.get(
            f'https://www.blibli.com/backend/search/products?sort=&page={page}&start={start}&searchTerm={product_name}&intent=true&merchantSearch=true&multiCategory=true&customUrl=&&channelId=mobile-web&showFacet=false&isMobileBCA=false&isJual=false',
            cookies=cookies,
            headers=headers,
        )
        if response.status_code != 200:
            print('Error: ', response.status_code)
            break
        json_response = response.json()
        result = mapper(data=json_response)
        if len(result) == 0:
            break
        with open("assets/blibli/response-"+product_name+"-"+str(page)+".json", "w") as f:
            f.write(json.dumps(result, indent=4))
        # results.extend(result)
        
        print('Page: ', page,' Success!')
        start += 20
        page += 1

    return results
