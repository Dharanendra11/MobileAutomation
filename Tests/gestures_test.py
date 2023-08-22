import time
from random import Random
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from RandomWordGenerator import RandomWord
capabilities = {
  "platformName": "Android",
  "appium:deviceName": "emulator-5554",
  "appium:appPackage": "com.google.android.dialer",
  "appium:appActivity": "com.google.android.dialer.extensions.GoogleDialtactsActivity",
  "newCommandTimeout" : 120
}
try:
  driver= webdriver.Remote(command_executor="http://127.0.0.1:4723/wd/hub",desired_capabilities=capabilities)
  driver.implicitly_wait(15)
  WebDriverWait(driver,60).until(ec.visibility_of_element_located((AppiumBy.ID,"com.google.android.dialer:id/tab_contacts")))
  driver.find_element(AppiumBy.ID,"com.google.android.dialer:id/tab_contacts").click()
  time.sleep(5)
  driver.find_element(AppiumBy.ID,"com.google.android.dialer:id/dialpad_fab").click()
  time.sleep(5)
  ph_num = str(Random().randint(1000,10000))
  driver.find_element(AppiumBy.ID,"com.google.android.dialer:id/digits").send_keys(ph_num)
  time.sleep(3)
  action = TouchAction(driver)
  action.tap(x=378,y=141).perform()
  time.sleep(5)
  rw = RandomWord(max_word_size=5)
  first_name = rw.generate()
  last_name = rw.generate()
  driver.find_element(AppiumBy.XPATH,"//android.widget.EditText[@text='First name']").send_keys(first_name)
  driver.find_element(AppiumBy.XPATH,"//android.widget.EditText[@text='Last name']").send_keys(last_name)
  driver.find_element(AppiumBy.ID,"com.google.android.contacts:id/text_input_end_icon").click()
  time.sleep(3)
  action.tap(x=245,y=298).perform()
  time.sleep(2)
  driver.hide_keyboard()
  #driver.find_element(AppiumBy.ID,"com.google.android.contacts:id/save_button").click()

except(Exception):
  print(Exception)

finally:
  driver.quit()

