from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

service = Service(executable_path='exe/chromedriver.exe')
chrome_options = Options()
chrome_options.add_argument(
    "user-data-dir=C:/Users/Franklin/Documents/Proyectos_Python/whatsapp/selenium")
driver = webdriver.Chrome(service=service, chrome_options=chrome_options)
driver.get("https://web.whatsapp.com/")


def msg():
    name = input("Enter Group/User Name: ")
    message = input("Enter your message to group/user")
    Count = int(input("enter the menssage count:"))

    # find who to mensage
    print(name)
    user = driver.find_element(
        By.XPATH, "//span[@title='Franchi']")

    user.click()
    text_box = driver.find_element(
        By.XPATH, "//div[@data-tab='10' and @role='textbox']")

    # Send Button
    for i in range(Count):
        text_box.send_keys(message)
        driver.find_element(
            By.XPATH, "//span[@data-testid='send']").click()


msg()


def reps():
    print("Do yo wsant to send more msg to anyone")
    askUser = input("Press y for yes and n for no")
    if(askUser == "Y" or askUser == "y"):
        msg()
        reps()
    if(askUser == "N" or askUser == "n"):
        print("Thank you see you soon")
    else:
        print("Enter a valid option: \n")
        reps()


reps()
