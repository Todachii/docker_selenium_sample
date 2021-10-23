#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# Chrome のオプションを設定する
options = webdriver.ChromeOptions()
options.add_argument('--headless')

# Selenium サーバーへ接続する。
driver = webdriver.Remote(
    command_executor=os.environ["SELENIUM_URL"],
    options=options,
)

# 任意のHTMLの要素が特定の状態になるまで待つ
# ドライバとタイムアウト値を指定
wait = WebDriverWait(driver, 10)

driver.get("https://www.time-j.net/worldtime/country/jp")

print(driver.find_element(By.XPATH,
                          "/html/body/div/div[6]/div[1]/div/p[5]").text)
driver.quit()
