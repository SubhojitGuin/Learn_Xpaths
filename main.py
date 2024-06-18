from selenium import webdriver

driver = webdriver.Chrome("chromedriver.exe")
driver.get("https://theautomationzone.blogspot.com/2020/07/xpath-practice.html")

print(driver.find_element(by="xpath").text)