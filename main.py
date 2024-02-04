from blibli import main

if __name__ == '__main__':
    print('Welcome to the price comparison tool!')
    print('Please select a marketplace:')
    print('1. Blibli')
    print('2. Tokopedia')
    service = int(input('Service: '))
    if service == 1:
        print('You have selected Blibli')
        print('Select a service:')
        print('1. Search')
        print('2. Product')
        subservice = int(input('Service: '))
        if subservice == 1:
            product_name = input('Enter product name: ')
            print(main.search(product_name))
        elif subservice == 2:
            product_url = input('Enter product URL: ')
            # print(main.product(product_url))
    elif service == 2:
        print('You have selected Tokopedia')
        print('Select a service:')
        print('1. Search')
        print('2. Product')
        service = int(input('Service: '))
        if service == 1:
            product_name = input('Enter product name: ')
            print(main.search(product_name))
        elif service == 2:
            product_url = input('Enter product URL: ')
            print(main.product(product_url))