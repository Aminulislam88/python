from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.google.com")
print(driver.title)
input_box = driver.find_element_by_name('q')
input_box.send_keys("United University"+ Keys.RETURN)
elem = driver.find_element_by_id('result-stats')
print(elem.text)
while True:
	pass