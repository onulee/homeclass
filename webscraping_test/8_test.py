from selenium import webdriver
import time
import random

# 다운받은 webdriver의 경로를 지정
executable_path='C:\pyFolder\js_work\geckodriver.exe'

# 크롬 드라이버 실행
browser = webdriver.Chrome("./chromedriver.exe")
# 1. 네이버 로그인 페이지 이동
browser.get("https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com")
time.sleep(random.uniform(1,3)) # 자동화탐지를 우회 하기 위한 delay

# 2. id, pw 입력
browser.find_element_by_id("id").send_keys("lee*****")
time.sleep(random.uniform(1,3)) # 자동화탐지를 우회 하기 위한 delay
browser.find_element_by_id("pw").send_keys("*****")
time.sleep(random.uniform(1,3)) # 자동화탐지를 우회 하기 위한 delay
# 4. 로그인 버튼 클릭
browser.find_element_by_id("log.login").click()






