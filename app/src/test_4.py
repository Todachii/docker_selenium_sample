#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import os
from selenium import webdriver

# Chrome のオプションを設定する
options = webdriver.ChromeOptions()
options.add_argument('--headless')

# Selenium サーバーへ接続する。
driver = webdriver.Remote(
    command_executor=os.environ["SELENIUM_URL"],
    options=options,
)
driver.set_window_size(1024, 768)

driver.get('https://www.amazon.co.jp/')
time.sleep(5)
driver.set_window_size(1250, 1036)
driver.execute_script("document.body.style.zoom='90%'")
driver.save_screenshot("./images/screenshot.png")
driver.quit()
