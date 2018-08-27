from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
import datetime
import sys
import time
class Bot():
	def __init__(self,data_list,email,password,proxy):
		self.url = "https://shop.adidas.ae/en/customer/account/login/"
		self.proudct_url = "https://shop.adidas.ae/en/ultra-boost-shoes/BA8923.html"
		self.product_list = []
		self.email = email
		self.password = password
		self.proxy = proxy
		for item in data_list:
			self.product_list.append(item)

	def login(self):
		email = self.email	
		password = self.password
		msg = ""
		try:
			loginBtn = WebDriverWait(self.browser, 10).until(
			    EC.presence_of_element_located((By.XPATH, ".//button[@id='send2']"))
			)
			# enter user name & passwd
			emailInput = self.browser.find_element_by_xpath(".//input[@id='email']")
			self.browser.execute_script("arguments[0].value = "+"'"+email+"'", emailInput)
		
			passwdInput = self.browser.find_element_by_xpath(".//input[@id='pass']")
			print("========")
			print(passwdInput)
			print(passwdInput.get_attribute("innerHTML"))
			self.browser.execute_script("arguments[0].value = "+"'"+password+"'", passwdInput)
			# loginBtn.click()
			self.browser.execute_script("arguments[0].click()", loginBtn)
			WebDriverWait(self.browser, 10).until(
			    EC.presence_of_element_located((By.XPATH, ".//p[@class ='not-user']"))
			)
		except (TimeoutException , WebDriverException) as e:
			msg = str(e)+"\n"+"if you have some question, Contact to Malinin"
			print("Contact Me iF you have TimeOUt error")
			return False
			# self.exitApp(msg,1)
		return True
	def get_product_check(self,proudct_info):
		self.browser.get(proudct_info['url'])
		try:
			elem = WebDriverWait(self.browser, 10).until(
			    EC.presence_of_element_located((By.XPATH, ".//span[@id = 'qty-button']/span[@class = 'ui-selectmenu-text']")))	
			self.browser.execute_script("arguments[0].innerHTML  = "+"'"+proudct_info['amount']+"'", elem)
		except (TimeoutException , WebDriverException) as e:
			return False
		contents = self.browser.find_elements_by_css_selector('li.js-size-value')
		print(contents)
		flag = False
		for item in contents:
			x = item.get_attribute('innerHTML')
			if (x == proudct_info['size']):
				self.browser.execute_script("arguments[0].click()", item)
				flag = True
		if not flag:
			return False
	# Add Bag
		elem = self.browser.find_element_by_xpath(".//button[@id = 'product-addtocart-button']")
		self.browser.execute_script("arguments[0].click()", elem)
		
		return flag
	def start(self):
		self.browser = webdriver.Firefox(executable_path="./webdriver/geckodriver")
		if self.proxy['type'] =='proxy':		
			HOST = self.proxy['host']
			port = self.proxy['port']
			profile = webdriver.FirefoxProfile()
			profile.set_preference("network.proxy.type", 1)
			profile.set_preference("network.proxy.http", HOST)
			profile.set_preference("network.proxy.http_port", port)
			profile.set_preference("network.proxy.ssl", HOST)
			profile.set_preference("network.proxy.ssl_port", port)
			self.browser = webdriver.Firefox(firefox_profile=profile,executable_path="./webdriver/geckodriver")
		for item in self.product_list:
			if not self.get_product_check(item):
				print("get Product Failed"+":Product:"+item['url'])
				return False
			time.sleep(1)
		try:
			self.browser.get(self.url)
			if(not self.login()):
				print("Login Fails")
				return False

			# WebDriverWait(self.browser, 10).until(
			#     EC.presence_of_element_located((By.XPATH, ".//div[@class='minicart__popup is-active']"))
			# )
	#Check Out
			self.browser.get("https://shop.adidas.ae/en/checkout/onepage/")
			# elem = self.browser.find_element_by_xpath(".//div[@id = 'deliverydetails-buttons-container']/button[@title = 'Review & Pay']")			    
			elem = WebDriverWait(self.browser, 10).until(
				EC.presence_of_element_located((By.XPATH,".//div[@id = 'deliverydetails-buttons-container']/button[@title = 'Review & Pay']"))
			)						
			self.browser.execute_script("arguments[0].click()", elem)
			elem = WebDriverWait(self.browser, 10).until(
				EC.presence_of_element_located((By.XPATH,".//input[@id = 'p_method_cashondelivery']"))
			)	

			self.browser.execute_script("arguments[0].click()", elem)
			
			# elem = self.browser.find_element_by_xpath(".//div[@id = 'payment-buttons-container']/button")
			# self.browser.execute_script("arguments[0].click()", elem)
		except (TimeoutException , WebDriverException) as e:
			print("Check Out Error")
			return False
if __name__ == "__main__":
	proudct_info = {}
	proudct_info['url'] = "https://shop.adidas.ae/en/ultra-boost-shoes/BA8923.html"
	proudct_info['amount'] = "1"
	proudct_info['size'] = "40 2/3"
	init_Info={'name':'aj.cob@yahoo.com',
	'pwd':'t20forlife',
	'product':[{'url':'https://shop.adidas.ae/en/eqt-support-ultra-primeknit-king-push-shoes/DB0181.html',
	            'amount':'1',
	            'size':'40 2/3'},
                {'url':'https://shop.adidas.ae/en/eqt-support-ultra-primeknit-king-push-shoes/DB0181.html',
	            'amount':'1',
	            'size':'42'}]
	}
	proxy = {}
	proxy['host'] = "localhost"
	proxy['port'] = 100
	proxy['type'] = 'localhost'
	bot = Bot(init_Info['product'],"aj.cob@yahoo.com","t20forlife",proxy)

	bot.start()
	# browser = webdriver.Firefox(executable_path="./webdriver/geckodriver")
	# browser.get('https://shop.adidas.ae/en/customer/account/login/')
	# time.sleep(10)
	# usernameElement = browser.find_element_by_id("email");
	# passwordElement = browser.find_element_by_id("pass");
	# formElement  = browser.find_element_by_id("login-form");
	# email = "aj.cob@yahoo.com"	
	# password = "t20forlife"
	# usernameElement.sendKeys(email)
	# passwordElement.sendKeys(password)
