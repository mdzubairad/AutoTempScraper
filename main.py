from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from datetime import datetime

def get_driver():
  # Set options to make browsing easier
  options = webdriver.ChromeOptions()
  options.add_argument("disable-infobars")
  options.add_argument("start-maximized")
  options.add_argument("disable-dev-shm-usage")
  options.add_argument("no-sandbox")
  options.add_experimental_option("excludeSwitches", ["enable-automation"])
  options.add_argument("disable-blink-features=AutomationControlled")

  driver = webdriver.Chrome(options=options)
  driver.get("https://automated.pythonanywhere.com/")
  #https://automated.pythonanywhere.com/login/
  return driver

def clean_text(text):
  """Extract only the temperature from text"""
  output = int(text.split(": ")[1])
  return output

def save_output_to_file(text):
  """Saves output_data to a file with the current date/time as the filename."""
  # Generate filename (e.g., "2024-03-29_15-45-30.txt")
  filename = datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".txt"
  with open(filename, "w") as file:
    file.write(text)

def main():
  driver = get_driver()

  ''' driver.find_element(by="id", value="id_username").send_keys("automated")
  time.sleep(2)
  print(driver.current_url)

  driver.find_element(by="id", value="id_password").send_keys("automatedautomated" + Keys.RETURN)
  time.sleep(2)

  driver.find_element(by="xpath", value="/html/body/nav/div/a").click()
  '''
  while True:
    time.sleep(2)
    element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[2]")
    text = str(clean_text(element.text))
    save_output_to_file(text)

print(main())