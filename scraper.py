import pandas as pd
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import chromedriver_autoinstaller
from db import database

chromedriver_autoinstaller.install()

def scrape_data(username, password, page_url):
    # Initialize Chrome driver with notifications disabled
    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications": 2}
    chrome_options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(options=chrome_options)

    try:
        # Log in to Facebook
        driver.get("https://www.facebook.com/")
        username_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='email']")))
        password_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='pass']")))
        username_field.clear()
        username_field.send_keys("")
        password_field.clear()
        password_field.send_keys('')
        login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[name='login']")))
        login_button.click()
        sleep(1)

        # Navigate to the Facebook page
        driver.get(page_url)
        sleep(2)  # Wait for page to load

        # Extract posts
        posts = driver.find_elements(By.XPATH, "//div[contains(@class, 'du4w35lb k4urcfbm l9j0dhe7 sjgh65i0')]")
        # Initialize lists to store data
        post_data = []

        # Loop through each post
        for post in posts:
            # Extract post details
            try:
                post_content = post.find_element(By.XPATH, ".//div[contains(@class, 'ecm0bbzt hv4rvrfc ihqw7lf3 dati1w0a')]//div[contains(@class, 'j83agx80 cbu4d94t buofh1pr l9j0dhe7')]//span").text
            except:
                post_content = ""

            try:
                likes = post.find_element(By.XPATH, ".//a[contains(@href, '/ufi/reaction/profile/browser/')]//span").text
            except:
                likes = ""

            try:
                shares = post.find_element(By.XPATH, ".//a[contains(@href, '/ufi/sharer.php')]//span").text
            except:
                shares = ""

            # Extract number of comments
            try:
                comment_path = post.find_element(By.XPATH, ".//a[contains(@href, '/ufi/reaction/profile/browser/')]//span").click()
                WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "d2edcug0 hpfvmrgz qv66sw1b c1et5uql")))
                comments_count = len(post.find_elements(By.XPATH, ".//div[contains(@class, 'kvgmc6g5 jb3vyjys rz4wbd8a qt6c0cv9 a8c37x1j')]//span[contains(@dir, 'auto')]"))
            except:
                comments_count = 0

            # Extract number of users who commented
            try:
                users_commented = len(post.find_elements(By.XPATH, ".//a[contains(@href, '/ufi/reaction/profile/browser/')]"))
            except:
                users_commented = 0

            # Store post data
            post_data.append({"Post Content": post_content, "Likes": likes, "Shares": shares, "Comments Count": comments_count, "Users Commented": users_commented})

        # Store scraped data into the database
        database(post_data)

    finally:
        # Close the browser
        driver.quit()

# Test the function
username = ""
password = ""
page_url = "https://www.facebook.com/amazonwebservices"
scrape_data(username, password, page_url)
