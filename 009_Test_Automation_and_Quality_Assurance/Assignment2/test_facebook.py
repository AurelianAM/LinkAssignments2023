from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
# # Define options for opening Chrome webdriver
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)

# # Instantiate Chrome webdriver
driver = webdriver.Chrome(options=options)

# # Instantiate implicit wait
wait = WebDriverWait(driver, 10)

# # Open in Chrome: "https://www.google.com/"
driver.get('https://www.google.com/')

# # Reject the cookies policies for google webpage
denyCookies = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="W0wltc"]/div')))
denyCookies.click()

# # Go to the input search box and input "facebook"
wait.until(EC.presence_of_element_located((By.ID, "APjFqb")))
searchInput = driver.find_element(by=By.ID, value="APjFqb")
searchInput.send_keys("facebook\n")

# # Try to find the search button to click it
# # Depending on the system, the \n character (return) will activate the search
# # For MacOS it is necessary to click the search button
try:
    driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]').click()
except NoSuchElementException:
    pass
# # From the search results, get the first link that contains "facebook" and click it
facebookLink = driver.find_element(by=By.PARTIAL_LINK_TEXT, value="facebook")
facebookLink.click()

# # Deny the cookes policy from Facebook
denyCookies = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[2]/div/div/div/div/div[4]/button[1]')))
denyCookies.click()

# # Find the input boxes for email and password
emailInput = wait.until(EC.presence_of_element_located((By.ID, 'email')))
passInput = wait.until(EC.presence_of_element_located((By.ID, 'pass')))

# # Input a fake email and a fake password
emailInput.send_keys('test_selenium@test.com')
passInput. send_keys('testpassword')
# # Click the login button
driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button').click()

# # Capture the login error message
emailErrorMessage = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div[1]/div/div[2]/div[2]/form/div/div[1]/div[2]')))

# # Get the login page lanaguage
language = driver.find_element(by=By.TAG_NAME, value='html').get_attribute('lang')

expected_eng = "The email address you entered isn't connected to an account. Find your account and log in."
expected_ro = "Adresa de e-mail introdusă nu este asociată unui cont. Găseşte-ţi contul şi conectează-te."

# # Test if the received error message is the same with the expected one
# # assuming that the site language is romanian or english
if language == 'ro':
    assert emailErrorMessage.text == expected_ro
else:
    assert emailErrorMessage.text == expected_eng

# # Close the driver (the browser)
driver.close()