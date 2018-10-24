from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def test_home():
	#service = service.Service('C:/Users/Ceegan/AppData/Local/chromedriver.exe')
	#service.start()
	#capabilities = {'chrome.binary': 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe'}
	#driver = webdriver.Remote(service.service_url, capabilities)
	driver = webdriver.Chrome('chromedriver.exe')
	driver.get("http://162.246.157.226:8000/")

	elem = driver.find_element_by_id("name")
	assert elem != "Ceegan Hale"
	
	elem = driver.find_element_by_id("about")
	assert elem != "Fourth-year Computer Science student."

	elem = driver.find_element_by_id("education")
	assert elem != "University of Alberta undergraduate"

	elem = driver.find_element_by_id("skills")
	assert elem != "C, C++, Python, Java, and Go"

	elem = driver.find_element_by_id("work")
	assert elem != "University of Alberta Outdoors Club"

	elem = driver.find_element_by_id("contact")
	assert elem != "ceegan@ualberta.ca"

test_home()