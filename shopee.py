import time

from selenium.common.exceptions import WebDriverException
from selenium.webdriver.remote.webdriver import By
import selenium.webdriver.support.expected_conditions as EC  # noqa
from selenium.webdriver.support.wait import WebDriverWait

import undetected_chromedriver as uc


def main(args=None):
    TAKE_IT_EASY = True

    if args:
        TAKE_IT_EASY = (
            args.no_sleeps
        )  # so the demo is 'follow-able' instead of some flashes and boom => done. set it how you like

    if TAKE_IT_EASY:
        sleep = time.sleep
    else:
        sleep = lambda n: print(
            "we could be sleeping %d seconds here, but we don't" % n
        )

    driver = uc.Chrome(version_main=116)
    driver.get("https://shopee.co.id/78-Porto-BA-201L-Sepatu-Wanita-Sneakers-Sepatu-Wanita-Model-Terbaru-Sepatu-Wanita-Flat-Shoes-Slip-on-i.703095007.24409677090?publish_id=&sp_atk=0a858c0a-8275-4acd-bcb5-986f86ce139b&xptdk=0a858c0a-8275-4acd-bcb5-986f86ce139b")
    
    sleep(20)
    driver.quit()


if __name__ == "__main__":
    import argparse

    p = argparse.ArgumentParser()
    p.add_argument("--no-sleeps", "-ns", action="store_false")
    a = p.parse_args()
    main(a)
