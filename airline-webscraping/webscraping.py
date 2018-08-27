from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Specifying incognito mode as you launch your browser[OPTIONAL]

option = webdriver.ChromeOptions()
option.add_argument("--incognito")
option.add_argument("--headless")
# Create new Instance of Chrome in incognito mode

# browser = webdriver.Firefox(executable_path='geckodriver')
browser = webdriver.Chrome(executable_path='chromedriver', chrome_options=option)
# Go to desired website
browser.get("https://www.interjet.com/en-us")

# Wait 10 seconds for page to load
timeout = 10
try:
    # definition of search_button
    search_button = WebDriverWait(browser, timeout).until(EC.presence_of_element_located((By.XPATH, "//*[@id='ControlGroupHomeView_AvailabilitySearchInputHomeView_ButtonSubmit']")))
    # clicking button OriginCity & DestinationCity
    OriginCity_button = browser.find_elements_by_xpath("//*[@id='marketCityPair_1']/div[1]/div[1]/div/span")
    browser.execute_script("arguments[0].click()", OriginCity_button[0]);
    SpanClick_origin_button = browser.find_elements_by_xpath("//*[@id='ModalListStations']/.//li/span")
    browser.execute_script("arguments[0].click()", SpanClick_origin_button[0])
 
    DestinationCity_button = browser.find_elements_by_xpath("//*[@id='marketCityPair_1']/div[2]/div[1]/div/span")
    browser.execute_script("arguments[0].click()", DestinationCity_button[0])
    SpanClick_dest_button = browser.find_elements_by_xpath("//*[@id='ModalDestinationsStations']/.//li/span")
    browser.execute_script("arguments[0].click()", SpanClick_dest_button[1])
    
    # clicking depature time & return time
    depature_btn = browser.find_elements_by_xpath("//*[@id='marketDate_1']/img")
    browser.execute_script("arguments[0].click()", depature_btn[0]);
    depature_date_click = browser.find_elements_by_xpath("//*[@id='ui-datepicker-div']/div/table/tbody/tr/td/a")
    browser.execute_script("arguments[0].click()", depature_date_click[0]);
    
    return_btn = browser.find_elements_by_xpath("//*[@id='marketDate_2']/img")
    browser.execute_script("arguments[0].click()", return_btn[0])
    return_date_click = browser.find_elements_by_xpath("//*[@id='ui-datepicker-div']/div/table/tbody/tr/td/a")
    browser.execute_script("arguments[0].click()", return_date_click[3])
   
    # click search flights button.
    browser.execute_script("arguments[0].click()", search_button)
   
    # get the date of current flight
    current_date_flight = browser.find_elements_by_xpath("//*[@id='selectMainBody']/div/div[15]/div[1]/div[1]/div[2]/span")
    contents_date_flight = current_date_flight[0].get_attribute('innerHTML')
    space_cat = contents_date_flight.split(",")
    space_cat_dm = space_cat[0].split("&nbsp;")
    space_cat_year = space_cat[1].split("&nbsp;")
   
    day = space_cat_dm[0].strip('\t\n\r')
    month = space_cat_dm[1].strip('\t\n\r')
    year = space_cat_year[0].strip('\t\n\r')
    date = day + "-" + month + "-" + year
    # print(date)
    
    # get the depature flight
    depature_flight = browser.find_elements_by_xpath("//*[@id='selectMainBody']/div/div[15]/div[1]/div[1]/div[1]")
    contents_depature_flight = depature_flight[0].get_attribute('innerHTML')
    comma_flight = contents_depature_flight.split("&nbsp;")
    direction_flight = comma_flight[1].split(",")
    direction_flight_noenter = direction_flight[0].strip("\t\n\<b>\</")
    flight_clear = direction_flight_noenter.split("-")
    Origin_City = flight_clear[0]
    Destination_City = flight_clear[1]
    # print("From(City):" + Origin_City + "To(City):" + Destination_City)
    
    # ID CASE RESULT Time Depature Stops Airline Flight Duration Price-Cheaper in Depature Flight
    div_list = browser.find_elements_by_xpath("//*[@class = 'schedule-container lay-v2 total-segments-1 ']/div")
    # make the list of flights which is Depature & return flight
    flight_list = []
    flights_number = browser.find_elements_by_xpath("//*[@class='flight']")
    for item in flights_number:
        flight_list.append(item.get_attribute('innerHTML'))
    # print(flight_list)
    
    
    # get the date of return flight
    return_date_flight = browser.find_elements_by_xpath("//*[@id='selectMainBody']/div/div[15]/div[2]/div[1]/div[2]/span")
    contents_return_flight = return_date_flight[0].get_attribute('innerHTML')
    space_no = contents_return_flight.split(",")
    space_no_dm = space_no[0].split("&nbsp;")
    space_no_year = space_no[1].split("&nbsp;")
   
    day_return = space_no_dm[0].strip('\t\n\r')
    month_return = space_no_dm[1].strip('\t\n\r')
    year_return = space_no_year[0].strip('\t\n\r')
    date_return = day_return + "-" + month_return + "-" + year_return
    # print(date_return)
    
    # get the depature_time
    depature_time_list = []
    depature_time = browser.find_elements_by_xpath("//*[@class='deptime1']")
    for item in depature_time:
        depature_time_list.append(item.get_attribute('innerHTML'))
    # print(depature_time_list)
    
    # get the stops
    stops_list = []
    stop = browser.find_elements_by_xpath("//*[@class='stops']")
   
    action1 = stop[0].get_attribute('innerHTML')
    action1 = action1[0].strip('\n')
    print(action1)
    # for item in stop:
    #     stop_action = item.get_attribute('innerHTML')
    #     i = 0
    #     while i < len(stop):
    #         stops_list.append(stop_action[i].strip('\n'))
    #         i = i + 1
        # stop_action = stop_action[0].split(" ")
        # stop_action = stop_action[0].strip('\t\n\r\<div>')
    # print(stops_list)
except TimeoutException:
    print("Timed out waiting for page to load")
    browser.quit()

# Get all of the titles for the pinned repositories
# We are not just getting pure titles but we are getting a selenium object
# with selenium elements of the titles.

# find_elements_by_xpath - Returns an array of selenium objects.
# titles_element = browser.find_elements_by_xpath("//a[@class='chosen-single']")
# # element = browser.find_elements_by_xpath("//@class='chosen-single'")
# # List Comprehension to get the actual repo titles and not the selenium objects.

# titles = [x.text for x in titles_element] 

# # text = [x.text for x in element]
# # print response in terminal
# print('TITLES:')
# print(titles, '\n')


