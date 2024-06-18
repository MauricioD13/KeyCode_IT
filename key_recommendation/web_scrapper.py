from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

def main():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get("https://hoopshype.com/salaries/players/")
    table_row = driver.find_element(By.TAG_NAME,"table")
    name = table_row.find_element(By.CLASS_NAME, 'name').text
    rank = table_row.find_element(By.CLASS_NAME, 'rank').text
    salaries = table_row.find_elements(By.TAG_NAME, 'td')[2:]  # The first two are 'rank' and 'name'

    # Get the text for each salary cell
    salary_data = []
    counter = 0
    toggle = 0
    mod = 4
    for idx in range(len(salaries)):
        if counter == 4:
            toggle = not toggle
            counter = 0
        if toggle == 0:
            salary_data.append(salaries[idx].text)
        if idx >= 20:
            break
        counter += 1
    # Print the extracted data
    print(f"Rank: {rank}")
    print(f"Name: {name}")
    print("Salaries:", salary_data)
    print(driver.title)
    driver.close()

main()