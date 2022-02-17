import time
import random
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=1920x1080")

browser = webdriver.Chrome(options=options)
browser.maximize_window() # 창 최대화
url="https://flight.naver.com/"
browser.get(url)

# 출발 선택
browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[4]/div/div/div[2]/div[1]/button[1]/b").click()
browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[9]/div[2]/section/section/button[1]").click()
browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[9]/div[2]/section/section/div/button[1]").click()

# 도착 선택
browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[4]/div/div/div[2]/div[1]/button[2]/b").click()
browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[9]/div[2]/section/section/button[1]").click()
browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[9]/div[2]/section/section/div/button[2]").click()

# 가는 날 선택
browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[4]/div/div/div[2]/div[2]/button[1]").click()
time.sleep(1)
browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[9]/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr[4]/td[2]").click()
# 오는 날 선택
time.sleep(1)
browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[9]/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr[4]/td[5]").click()

# 항공권 검색 버튼 클릭
browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[4]/div/div/button").click()


# import해야 함 최대10초 대기, 또는 xpath의 내용이 나타날때 까지 대기. 
WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div/div[1]/div[5]/div/div[2]/div[2]")))
# time.sleep(10)


interval = 2 # 2초에 한번씩 스크롤 내림

# 현재 문서 높이를 가져와서 저장
prev_height = browser.execute_script("return document.body.scrollHeight")

# 반복 수행
while True:
    # 스크롤을 가장 아래로 내림
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    # 페이지 로딩 대기
    time.sleep(interval)
    # 현재 문서 높이를 가져와서 저장
    curr_height = browser.execute_script("return document.body.scrollHeight")
    if curr_height == prev_height:
        break

    prev_height = curr_height

print("스크롤 완료")




# 크롬드라이버의 현재 페이지의 url 얻기
page_url = browser.page_source
# 현재 url 주소의 html 데이터를 파싱
soup = BeautifulSoup(page_url, "lxml")
flights = soup.find_all("div",{"class":"result"})
# flights = soup.find_all(class_='result')

# 항공권 정보가 리스트로 저장되어 있습니다.
for flight in flights:
    print(flight.b.get_text())
    print(flight.find("div",{"class":"route"}).get_text())
    print(flight.find("div",{"class":"domestic_item__2B--k"}).get_text())
    print("-"*10)

print("개수 : ",len(flights))

# 브라우저를 최대 10초 동안 대기, xpath가 나타날때까지 기다림. 10초 이상이면 error처리
# elem = WebDriverWait(browser,10).until(EC.presence_of_element_located(By.XPATH,"//*[@id='__next']/div/div[1]/div[5]/div/div[2]/div[2]"))
# print(elem.text)
    
    

# 결과 출력
# elem = browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[4]/div/div/button")
# print(elem.text)
# browser.find_elements_by_link_text("21")[0].click()
# browser.find_elements_by_link_text("25")[0].click()
# browser.find_element_by_link_text("항공권 검색").click()





