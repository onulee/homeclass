from selenium import webdriver
browser = webdriver.Chrome()

## class name이 link_login
elem = browser.find_element_by_class_name("link_login")
elem  
elem.click()          ## 로그인 버튼 클릭
browser.back()    ## 뒤로 가기
browser.forward()  ## 앞으로 가기
browser.refresh()   ## 새로고침
elem = browser.find_element_by_id("query")    ## 네이버 검색창 찾음.

from selenium.webdriver.common.keys import Keys
elem.send_keys("시가총액")
elem.send_keys(Keys.ENTER)

