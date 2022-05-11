from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://lms.uiu.ac.bd/login/index.php")
print(driver.title)
input_box = driver.find_element_by_xpath('//*[@id="username"]')
input_box.send_keys('011182130')
elem = driver.find_element_by_id('password')
elem.send_keys('123ahmed' + Keys.RETURN)
while True:
	pass