#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from selenium import webdriver

# Chrome のオプションを設定する
options = webdriver.ChromeOptions()
options.add_argument('--headless')

# Selenium Server に接続する
# Selenium サーバーへ接続する。
driver = webdriver.Remote(
    command_executor=os.environ["SELENIUM_URL"],
    options=options,
)

# Selenium 経由でブラウザを操作する
driver.get('https://qiita.com')
print(driver.current_url)

# ブラウザを終了する
driver.quit()
