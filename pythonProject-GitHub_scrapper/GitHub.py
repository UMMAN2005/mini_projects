from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
# from webdriver_manager.chrome import ChromeDriverManager

# ANSI colors
RESET_COLOR = "\033[0m"
RED_COLOR = "\033[0;31m"
GREEN_COLOR = "\033[0;32m"
BLUE_COLOR = "\033[0;34m"
YELLOW_COLOR = "\033[1;33m"


def initialize_driver():
    """
    Initialize Google Chrome driver
    :return: The initialized driver
    """
    chrome_driver_path = r"C:\Users\user\AppData\Local\Programs\Google Chrome Drivers\chromedriver.exe"
    chrome_binary_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = chrome_binary_path
    chrome_options.add_argument(f"webdriver.chrome.driver={chrome_driver_path}")
    driver_ = webdriver.Chrome(options=chrome_options)
    # driver_ = webdriver.Chrome(ChromeDriverManager().install())
    return driver_


def scrape_github_repo(page, driver_):
    """
    Scrape a GitHub repo for files and check for passwords.
    :param driver_: The Constructed driver
    :param page: The page to scrape
    :return: None
    """
    # noinspection PyGlobalUndefined
    global new_result
    driver_.get(page)
    new_results = driver_.find_elements(By.CLASS_NAME, "js-navigation-open")

    for new_result in new_results:
        pass
    if "py" in new_result.text:
        new_page = f"{page}/blob/main/{new_result.text}"
        going_for_raw(new_page, driver_)


def going_for_raw(page, driver__):
    """
    Visit the raw view of a page and check for passwords.
    :param driver__: The Constructed driver
    :param page: The URL of the page to check in raw view
    :return: None
    """
    driver__.get(page)

    # Locate the "Raw" button using partial link text
    raw_button = driver__.find_element(By.PARTIAL_LINK_TEXT, "Raw")

    # Click the "Raw" button
    raw_button.click()
    sleep(3)

    # Get the current URL after clicking
    current_url = driver__.current_url

    html = driver__.page_source

    if "pass" in html or "key" in html:
        print(GREEN_COLOR, f"[+] Found password: {current_url}", RESET_COLOR)

    if "user" in html or "mail" in html:
        print(GREEN_COLOR, f"[+] Found username: {current_url}", RESET_COLOR)


def main():
    """
    Start other functions and get the details. At the end close the driver
    :return: None
    """
    print(BLUE_COLOR, "[*] The URL to GitHub repo: ", RESET_COLOR, end="")
    url_to_repo = input()
    driver = initialize_driver()
    driver.get(url_to_repo)

    results = driver.find_elements(By.CLASS_NAME, "repo")
    links = []
    flinks = []

    for result in results:
        links.append(result.text)

    for link in links:
        next_page = f"{url_to_repo}/{link}"
        flinks.append(next_page)
        scrape_github_repo(next_page, driver)

    driver.close()


if __name__ == "__main__":
    github_link = "https://github.com/usernam121"
    main()
