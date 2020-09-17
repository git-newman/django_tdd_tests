from selenium import webdriver

browser = webdriver.Firefox(firefox_binary='/home/user/win/firefox/firefox')
browser.get("http://localhost:8000")

assert 'Django' in browser.title
