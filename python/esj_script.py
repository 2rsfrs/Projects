import webbrowser as web
import datetime
import pyautogui as auto
import time

# url for esj huddle room
url = "https://esjbooked.umd.edu/Web/schedule.php?sid=2&sd="

# get today's date and get 2 weeks from now
today = datetime.date.today()
# print(today)

# add 2 weeks to the date
two_week = datetime.timedelta(days=14)
future = today + two_week

# get the date then put into url
future = future.strftime("%Y-%m-%d")
url += future

# open the web browser
web.open(url)

# move to log in button and click
auto.moveTo(853, 555)
time.sleep(1)
auto.click()

# move to 1:00 1212
auto.moveTo(1060, 865)
# make this sleep timer 5-7 
time.sleep(5)
auto.click()

# move to end time
auto.moveTo(1100, 495)
time.sleep(0.5)
auto.click()

auto.press('3')
auto.press('enter')

# move to title of reservation
auto.moveTo(71, 670)
auto.click()
auto.press(['t', 'o', 'n', 'e', 'y'])

auto.moveTo(71, 780)
auto.click()
auto.press(['s', 't', 'u', 'd', 'y'])

auto.moveTo(1849, 970)
auto.click()
