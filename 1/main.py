from selenium import webdriver

# Initialize the webdriver object
driver_path = "/tmp/chromedriver"
driver = webdriver.Chrome(driver_path)

# Getting a page and viewing the title
driver.get("https://google.com")
print(f"Page's name is: {driver.title}")

# Exit
driver.quit()