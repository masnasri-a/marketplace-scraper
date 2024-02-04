import re
import time


def stringPriceConverter(price_string: str):
    """
    Converts a price string to an integer.

    Args:
        price_string (str): The price string to be converted.

    Returns:
        int: The converted price as an integer.
    """
    price_number = re.sub(r'\D', '', price_string)
    return int(price_number)


def getTimestampNowMillis():
    """
    Get the current timestamp in milliseconds.

    Returns:
        int: The current timestamp in milliseconds.
    """
    return int(time.time() * 1000)

def soldConverter(sold_string: str):
    """
    Converts a sold string to an integer.

    Args:
        sold_string (str): The sold string to be converted.

    Returns:
        int: The converted sold as an integer.
    """
    sold_number = re.sub(r'\D', '', sold_string)
    if "k" in sold_string:
        sold_number = sold_number + "000"
    elif "m" in sold_string:
        sold_number = sold_number + "000000"
    elif "b" in sold_string:
        sold_number = sold_number + "000000000"
    int_sold = int(sold_number)
    if "," in sold_string:
        int_sold = int_sold / 10
    return int(int_sold)
