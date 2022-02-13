import time
import random
from selenium import webdriver


# 다운받은 geckodriver다운후 경로를 지정
# executable_path='C:\pyFolder\js_work\geckodriver.exe'
# 크롬 드라이버 실행
# browser = webdriver.Firefox(eㄴxecutable_path = executable_path)
browser = webdriver.Chrome("./chromedriver.exe")
time.sleep(random.uniform(1,3)) # 자동화탐지를 우회 하기 위한 delay
# naver login page로 이동
browser.get("https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com")

input_js = ' \
        document.getElementById("id").value = "{id}"; \
        document.getElementById("pw").value = "{pw}"; \
    '.format(id = "lee***", pw = "*****")
time.sleep(random.uniform(1,3)) # 자동화탐지를 우회 하기 위한 delay
browser.execute_script(input_js)
time.sleep(random.uniform(1,3)) # 자동화탐지를 우회 하기 위한 delay
browser.find_element_by_id("log.login").click()