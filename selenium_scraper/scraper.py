import time
import os

from selenium import webdriver
from selenium.webdriver.support.ui import Select


def scrape():
    driver = webdriver.Firefox(
        executable_path=os.environ.get("GECKODRIVER_PATH", "geckodriver")
    )
    driver.maximize_window()
    driver.get("http://spys.one/free-proxy-list/BR/")
    for _ in range(3):
        select = Select(driver.find_element_by_id("xpp"))
        select.select_by_value("5")
        time.sleep(3)
    tr_list = []
    tr_spy1xx = driver.find_elements_by_class_name("spy1xx")
    tr_spy1x = driver.find_elements_by_class_name("spy1x")
    for tr in tr_spy1xx + tr_spy1x:
        columns = tr.find_elements_by_class_name("spy14")
        if len(columns) > 0:
            columns = columns[0]
            tr_list.append(columns)

    for tr in tr_list:
        print(tr.text)
    print(len(tr_list))
    driver.close()
