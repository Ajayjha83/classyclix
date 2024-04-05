import time

from selenium import webdriver

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


# Initialize the WebDriver
driver = webdriver.Chrome()
driver.implicitly_wait(10)  # Set implicit wait time to 10 seconds

# Example: Open a webpage
driver.get("https://www.classyclix.com/")
driver.implicitly_wait(10)


userName = "Ajay"
password = "Ajayjha@123"

# Example: Find an element and interact with it
driver.find_element(By.LINK_TEXT, "Sign In").click()
driver.find_element(By.XPATH, "//*[@id='customer_login']/div[1]/form[2]/button[2]").click()
driver.find_element(By.ID, "username").send_keys(userName)
driver.find_element(By.ID, 'password').send_keys(password)
driver.find_element(By.NAME, 'login').click()


# Function to navigate top navigation links
def homePage_topNavigation():
    driver.find_element(By.CSS_SELECTOR, ".wpb_wrapper > .vc_row .logo img").click()
    driver.find_element(By.LINK_TEXT, "Earrings").click()
    driver.find_element(By.LINK_TEXT, "Necklaces").click()
    driver.find_element(By.LINK_TEXT, "Rings").click()
    driver.find_element(By.LINK_TEXT, "Bracelets").click()
    driver.find_element(By.LINK_TEXT, "Bangles").click()


# Call the function to navigate top navigation links
homePage_topNavigation()


def homePage_topNavigation_earring():
    # Find the page element to hover over
    page_element = driver.find_element(By.XPATH, "//a[@class='sf-with-ul'][normalize-space()='Earrings']")

    # Find the main menu element to hover over
    main_menu_element = driver.find_element(By.XPATH, "//li[@id='menu-item-2483']//a[normalize-space()='Ethnic']")

    # Find the sub-menu elements
    sub_menu_elements = driver.find_elements(By.XPATH, "(//ul[@class='sub-menu'])[1]/li")

    # Create ActionChains object
    action = ActionChains(driver)

    # Move to the page element
    action.move_to_element(page_element).perform()

    # Move to the main menu element
    action.move_to_element(main_menu_element).perform()

    print('asdd')

    # Perform hover action on each sub-menu element
    try:

        for sub_menu_element in sub_menu_elements:
        # Reset action chain
            action = ActionChains(driver)
            aaa = action.move_to_element(sub_menu_element).perform()
            aaa.click()
            # Get the URL and title of the current page
            url = driver.current_url
            # Get the title of the current page
            page_title = driver.title

            # Print the page title and URL
            print(page_title, url)
    except:
        print("Some error")

# Call the function to navigate top navigation links for Earrings
homePage_topNavigation_earring()


def tab_Earring_all_link_check():
    links = [
        "https://www.classyclix.com/artificial-bangles/",
        "https://www.classyclix.com/artificial-bangles/",
        "https://www.classyclix.com/artificial-bangles/",
        "https://www.classyclix.com/artificial-bangles/",
        "https://www.classyclix.com/artificial-bangles/",
        "https://www.classyclix.com/artificial-bangles/",
        "https://www.classyclix.com/artificial-bangles/",
        "https://www.classyclix.com/artificial-bangles/",
        "https://www.classyclix.com/artificial-bangles/",
        "https://www.classyclix.com/artificial-bangles/"
    ]

    for link in links:
        driver.get(link)  # Navigate to the URL
        print(driver.title)  # Print the title of the page
        # Perform any action needed after navigating to the page


tab_Earring_all_link_check()




def homePage_topNavigation_earring(driver):
    action = ActionChains(driver)
    action.move_to_element(driver.find_element(By.XPATH, "//a[@class='sf-with-ul'][normalize-space()='Earrings']")).perform()

    sub_menu_items = driver.find_elements(By.XPATH, "(//ul[@class='sub-menu'])[1]/li")
    links = []
    for sub_menu_item in sub_menu_items:
        sub_menu_link = sub_menu_item.find_element(By.TAG_NAME, 'a').get_attribute('href')
        links.append(sub_menu_link)
        print(sub_menu_link)
    return links

    driver.get("https://www.classyclix.com/")
def link_click(driver, links):
    for link in links:
        driver.get(link)
        print(driver.title)

# Call the function passing the driver instance
links = homePage_topNavigation_earring(driver)

# Click on the links and print titles
link_click(driver, links)




def Necklaces_tab_submenu_check():
    driver.get("https://www.classyclix.com/")
    action = ActionChains(driver)
    action.move_to_element(driver.find_element(By.XPATH,'//*[@id="menu-item-2450"]/a')).perform()
    sub_menu_items = driver.find_elements(By.XPATH, '//li[@id="menu-item-2450"]/ul[@class="sub-menu"]/li/a[@previewlistener="true"]')
    list_sub=[]
    for menu in sub_menu_items:
        href = menu.get_attribute("href")
        list_sub.append(href)
    return list_sub

# Call the function and assign the result to a variable

list_sub1 = Necklaces_tab_submenu_check()

print(list_sub1)





def find_all_links_and_click_check_status_code():
    driver.get("https://www.classyclix.com/")
    links = driver.find_elements(By.TAG_NAME, 'a')
    for link in links:
        url = link.get_attribute("href")  # Get the URL from the href attribute
        if url:
            try:
                request = requests.head(url)
                status_code = request.status_code
                print(f"URL: {url}, Status Code: {status_code}")
            except Exception as e:
                print(f"Error checking {url}: {e}")
        else:
            print("Empty URL found")




def get_all_links_from_home_page():
    urls = []
    driver.get("https://www.classyclix.com/")
    links = driver.find_elements(By.TAG_NAME, 'a')
    print(len(links))
    for link in links:
        url = link.get_attribute('href')
        if url:
            print(url)
            urls.append(url)
    return urls



all_uls = get_all_links_from_home_page()
print(all_uls)

def search():
    search_text = driver.find_element(By.XPATH,'(//input[@placeholder="Search product..."])[1]')
    search_text.send_keys("rings")
    search = driver.find_element(By.XPATH,"/html/body/div[2]/div/div[1]/div[1]/div/div[1]/div/section/div[1]/div/div/div/div/div[3]/div/div/div/div/div[2]/form/div/button")
    search.click()
    text = driver.find_element(By.XPATH,"//h1[@class='entry-title']").text
    print(text)
    actual_text = 'Search results: “rings”'
    assert text == actual_text, f"Expected: '{actual_text}', Actual: '{text}'"


search()


driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.find_element(By.XPATH,"//a[@id='opentab']").click()
windows = driver.window_handles
driver.switch_to.window(windows[1])
print(driver.title)
driver.switch_to.window(windows[0])



driver=webdriver.Edge()


