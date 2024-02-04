import json
import requests

headers = {
    'sec-ch-ua': '"Chromium";v="121", "Not A(Brand";v="99"',
    'X-Version': 'e48f8f5',
    'DNT': '1',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    'iris_session_id': '',
    'content-type': 'application/json',
    'accept': '*/*',
    'Referer': 'https://www.tokopedia.com/search?st=&q=iphone%2011&srp_component_id=02.01.00.00&srp_page_id=&srp_page_title=&navsource=',
    'X-Source': 'tokopedia-lite',
    'x-device': 'desktop-0.0',
    'X-Tkpd-Lite-Service': 'zeus',
    'sec-ch-ua-platform': '"macOS"',
}

json_data = [
    {
        'operationName': 'TopadsProductQuery',
        'variables': {
            'adParams': 'dep_id=&device=desktop&ep=product&fcity=&item=100&minimum_item=10&navsource=&ob=23&page=1&q=iphone%2011&shipping=&src=search&srp_component_id=02.01.00.00&srp_page_id=&srp_page_title=&st=product&user_addressId=&user_cityId=176&user_districtId=2274&user_id=0&user_lat=&user_long=&user_postCode=&user_warehouseId=12210375&variants=&warehouses=12210375%232h%2C0%2315m',
        },
        'query': 'query TopadsProductQuery($adParams: String) {\n  displayAdsV3(displayParams: $adParams) {\n    data {\n      clickTrackUrl: product_click_url\n      product_wishlist_url\n      product {\n        id\n        name\n        wishlist\n        image {\n          imageUrl: s_ecs\n          trackerImageUrl: s_url\n          __typename\n        }\n        url: uri\n        relative_uri\n        price: price_format\n        wholeSalePrice: wholesale_price {\n          quantityMin: quantity_min_format\n          quantityMax: quantity_max_format\n          price: price_format\n          __typename\n        }\n        count_talk_format\n        countReviewFormat: count_review_format\n        category {\n          id\n          __typename\n        }\n        categoryBreadcrumb: category_breadcrumb\n        preorder: product_preorder\n        product_wholesale\n        free_return\n        isNewProduct: product_new_label\n        cashback: product_cashback_rate\n        rating: product_rating\n        ratingAverage: product_rating_format\n        top_label\n        bottomLabel: bottom_label\n        labelGroups: label_group {\n          position\n          type\n          title\n          url\n          __typename\n        }\n        campaign {\n          discountPercentage: discount_percentage\n          originalPrice: original_price\n          __typename\n        }\n        customvideo_url\n        __typename\n      }\n      shop {\n        shopId: id\n        name\n        domain\n        city\n        tagline\n        uri\n        isOfficial: shop_is_official\n        isPowerBadge: gold_shop\n        badges {\n          title\n          imageURL: image_url\n          show\n          __typename\n        }\n        __typename\n      }\n      tag\n      __typename\n    }\n    header {\n      meta {\n        ab_test\n        templating\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n',
    },
]

response = requests.post('https://gql.tokopedia.com/graphql/TopadsProductQuery', headers=headers, json=json_data)


with open("response.json", "w") as f:
    f.write(json.dumps(response.json(), indent=4))
# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '[{"operationName":"TopadsProductQuery","variables":{"adParams":"dep_id=&device=desktop&ep=product&fcity=&item=20&minimum_item=10&navsource=&ob=23&page=1&q=iphone%2011&shipping=&src=search&srp_component_id=02.01.00.00&srp_page_id=&srp_page_title=&st=product&user_addressId=&user_cityId=176&user_districtId=2274&user_id=0&user_lat=&user_long=&user_postCode=&user_warehouseId=12210375&variants=&warehouses=12210375%232h%2C0%2315m"},"query":"query TopadsProductQuery($adParams: String) {\\n  displayAdsV3(displayParams: $adParams) {\\n    data {\\n      clickTrackUrl: product_click_url\\n      product_wishlist_url\\n      product {\\n        id\\n        name\\n        wishlist\\n        image {\\n          imageUrl: s_ecs\\n          trackerImageUrl: s_url\\n          __typename\\n        }\\n        url: uri\\n        relative_uri\\n        price: price_format\\n        wholeSalePrice: wholesale_price {\\n          quantityMin: quantity_min_format\\n          quantityMax: quantity_max_format\\n          price: price_format\\n          __typename\\n        }\\n        count_talk_format\\n        countReviewFormat: count_review_format\\n        category {\\n          id\\n          __typename\\n        }\\n        categoryBreadcrumb: category_breadcrumb\\n        preorder: product_preorder\\n        product_wholesale\\n        free_return\\n        isNewProduct: product_new_label\\n        cashback: product_cashback_rate\\n        rating: product_rating\\n        ratingAverage: product_rating_format\\n        top_label\\n        bottomLabel: bottom_label\\n        labelGroups: label_group {\\n          position\\n          type\\n          title\\n          url\\n          __typename\\n        }\\n        campaign {\\n          discountPercentage: discount_percentage\\n          originalPrice: original_price\\n          __typename\\n        }\\n        customvideo_url\\n        __typename\\n      }\\n      shop {\\n        shopId: id\\n        name\\n        domain\\n        city\\n        tagline\\n        uri\\n        isOfficial: shop_is_official\\n        isPowerBadge: gold_shop\\n        badges {\\n          title\\n          imageURL: image_url\\n          show\\n          __typename\\n        }\\n        __typename\\n      }\\n      tag\\n      __typename\\n    }\\n    header {\\n      meta {\\n        ab_test\\n        templating\\n        __typename\\n      }\\n      __typename\\n    }\\n    __typename\\n  }\\n}\\n"}]'
#response = requests.post('https://gql.tokopedia.com/graphql/TopadsProductQuery', headers=headers, data=data)