import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




signin_url = "https://accounts.google.com/signin"
#Lines needed to be added in the code

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_experimental_option("useAutomationExtension", False)
options.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_argument('start-maximized')
# options.add_argument('disable-infobars')
options.add_argument("---disable-extensions")
# options.add_argument("-disable-javascript")

# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver = webdriver.Chrome(executable_path=r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\chromedriver.exe', options=options)
def signin(user):
	time.sleep(5)
	driver.get(signin_url)
	time.sleep(10)
	print("############################")
	email_input = driver.find_element(By.ID, "identifierId")  # Example: by ID
	# email_input.clear()  # Clear existing value (optional)
	email_input.send_keys(user['email'])
	next = driver.find_element(By.CLASS_NAME, "AjY5Oe").click()
	time.sleep(1)
	pass_input = driver.find_element(By.ID, "Passwd")  # Example: by ID
	pass_input.send_keys(user['password'])
	next = driver.find_element(By.CLASS_NAME, "AjY5Oe").click()
	time.sleep(5)





emails = [{'email': 'hameedmansor39@gmail.com', 'password': 'hameeddd7777'}, ]
signin(emails[0])  # make_vote()

# driver.quit()
