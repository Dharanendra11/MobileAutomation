import base64
import os.path
import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

desired_capabilities = {
  "platformName": "Android",
  "appium:deviceName": "emulator-5554",
  "appium:appPackage": "com.android.settings",
  "appium:appActivity": "com.android.settings.Settings"
}

driver=webdriver.Remote(command_executor="http://127.0.0.1:4723/wd/hub",desired_capabilities=desired_capabilities)


driver.find_element(AppiumBy.ID,"com.android.settings:id/search_action_bar_title").click()

driver.start_recording_screen()

WebDriverWait(driver,10).until(ec.visibility_of_element_located((AppiumBy.ID,'com.google.android.settings.intelligence:id/open_search_view_edit_text')))
time.sleep(3)
driver.find_element(AppiumBy.ID,'com.google.android.settings.intelligence:id/open_search_view_edit_text').send_keys('Network')
WebDriverWait(driver,10).until(ec.visibility_of_element_located((AppiumBy.XPATH,"//android.widget.TextView[@text='Network & internet']")))
driver.find_element(AppiumBy.XPATH,"//android.widget.TextView[@text='Network & internet']").click()
driver.implicitly_wait(10)

raw_video = driver.stop_recording_screen()
#video_name = driver.current_activity + time.strftime('%H%M%S')
video_path = os.path.join("../Recordings","sample.mp4")
with open(video_path,'wb') as v:
  v.write(base64.b64decode(raw_video))


# 84 is the code for search button in the keyboard taken from Android KeyEvent website
#driver.keyevent(84)
# driver.execute_script('mobile:performEditorAction',{'action':'search'})

#TouchAction class
# action=TouchAction(driver)
# action.press(x=483,y=1818).move_to(x=495,y=1319).release().perform()

actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(483, 1818)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.move_to_location(495, 1319)
actions.w3c_actions.pointer_action.release()
actions.perform()
time.sleep(5)
driver.find_element(AppiumBy.XPATH,"//android.widget.RelativeLayout[@bounds='[66,1939][1036,2154]']").click()
driver.implicitly_wait(10)
print(driver.find_element(AppiumBy.ID,"android:id/title").text)

driver.quit()





