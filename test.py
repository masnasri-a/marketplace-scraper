from blibli import main as Blibli
from blibli.mapper.search import test_mapper
from tokopedia import main as Tokopedia

if __name__ == '__main__':
    # data = Blibli.search('Iphone')
    data = Tokopedia.search('Samsung')
    print(data)