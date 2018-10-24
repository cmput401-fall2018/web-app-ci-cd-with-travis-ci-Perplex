from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def test_home():
	driver = webdriver.Chrome()
	driver.get("http://127.0.0.1:8000")
	
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
