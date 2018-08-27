from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
# Specifying incognito mode as you launch your browser[OPTIONAL]
option = webdriver.ChromeOptions()
# progressing with background status
# option.add_argument("--headless")
option.add_argument("--incognito")
# work start
def start():
    browser = webdriver.Chrome(executable_path='chromedriver', chrome_options=option)
    # Go to desired website
    browser.get("https://superperfumerias.com")

    # Wait 10 seconds for page to load
    timeout = 10
    try:
        button_perfume = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@class='wrapper-ul-table']/ul[1]/li[1]/a"))
            )     
        browser.execute_script("arguments[0].click()", button_perfume)
        
        perfume_greenTea = browser.find_elements_by_xpath("//*[@id='product_11060']/div/a[1]")
        browser.execute_script("arguments[0].click()", perfume_greenTea[0])
        
        button_Add_cart = browser.find_elements_by_xpath("//*[@id='add-to-cart-button']")
        browser.execute_script("arguments[0].click()", button_Add_cart[0])
        
        button_article = browser.find_elements_by_xpath("/html/body/div[1]/header/div/div[4]/a")
        browser.execute_script("arguments[0].click()", button_article[0])
        
        button_purchase = WebDriverWait(browser, 10).until(
              EC.presence_of_element_located((By.XPATH, ".//button[@id='checkout-link']"))
            )
        browser.execute_script("arguments[0].click()", button_purchase)
        element = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, ".//button[@id='checkout-link']"))
            )
        browser.execute_script("arguments[0].click()", element)
    #  Enter Without Registration
        element = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, ".//form[@id='checkout_form_registration']/button"))
            )
        browser.execute_script("arguments[0].click()", element)
    #   Enter Personal Information
        #  Contact Email
        element = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, ".//input[@id='order_email']"))
            )
        element_data = 'prueba@gmail.com'
        browser.execute_script("arguments[0].value = '%s'" % (element_data,) , element)
        # Confirm Email
        element = browser.find_elements_by_xpath('.//input[@id="order_email_confirmation"]')
        element_data = 'prueba@gmail.com'
        browser.execute_script('arguments[0].value = "%s"' % (element_data,) , element[0])
        #Name
        element = browser.find_elements_by_xpath('.//input[@id="order_ship_address_attributes_firstname"]')
        element_data = 'prueba'
        browser.execute_script("arguments[0].value = '%s'" % (element_data,) , element[0])
        #SurName
        element = browser.find_elements_by_xpath('.//input[@id="order_ship_address_attributes_lastname"]')
        element_data = 'prueba'
        browser.execute_script("arguments[0].value = '%s'" % (element_data,) , element[0])
        #Address
        element = browser.find_elements_by_xpath('.//input[@id="order_ship_address_attributes_address1"]')
        element_data = 'prueba'
        browser.execute_script("arguments[0].value = '%s'" % (element_data,) , element[0])
        #Number
        element = browser.find_elements_by_xpath('.//input[@id="order_ship_address_attributes_number"]')
        element_data = '2'
        browser.execute_script("arguments[0].value = '%s'" % (element_data,) , element[0])
        #PostalCode
        element = browser.find_elements_by_xpath('.//input[@id="order_ship_address_attributes_zipcode"]')
        element_data = '28001'
        browser.execute_script("arguments[0].value = '%s'" % (element_data,) , element[0])
        #City
        element = browser.find_elements_by_xpath('.//input[@id="order_ship_address_attributes_city"]')
        element_data = 'madrid'
        browser.execute_script("arguments[0].value = '%s'" % (element_data,) , element[0])
        # Province
        element = browser.find_element_by_xpath(".//select[@id='order_ship_address_attributes_state_id']")
        browser.execute_script("arguments[0].value = '3821'" , element)
        # Telephone
        element = browser.find_elements_by_xpath('.//input[@id="order_ship_address_attributes_phone"]')
        element_data = '639987568'
        browser.execute_script("arguments[0].value = '%s'" % (element_data,) , element[0])
        # Telephone
        element = browser.find_elements_by_xpath('.//form[@id="checkout_form_address"]/div/div[4]/p/label')
        browser.execute_script("arguments[0].click()", element[0])
        #submit button
        element = browser.find_elements_by_xpath('.//form[@id="checkout_form_address"]/div/div[5]/input[1]')
        browser.execute_script("arguments[0].click()", element[0])
        #PAY BUTTON    
        element = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, ".//form[@id='checkout_form_delivery']/div/div[7]/button"))
            )
        browser.execute_script("arguments[0].click()", element)
        #Transfer
        element = browser.find_elements_by_xpath('.//div[@id="payment"]/span/label[2]')
        browser.execute_script("arguments[0].click()", element[0])
        #Accept Payment
        element = browser.find_elements_by_xpath('.//fieldset[@id="payment_fieldset_3"]/div/input')
        browser.execute_script("arguments[0].click()", element[0])
    except TimeoutException:
        print("Timed out waiting for page to load")
        browser.quit()
if(__name__=="__main__"):
    start()
    print("finished")


