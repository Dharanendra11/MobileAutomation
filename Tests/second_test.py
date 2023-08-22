from appium import webdriver



capabilities = {
  "platformName": "Android",
  "appium:deviceName": "emulator-5554",
  "app":"C:/Users/dhara/Downloads/com.flipkart.android_apkdone.com.apk",
  "appium:appPackage": "com.flipkart.android",
  "appium:appActivity": "com.flipkart.android.activity.HomeFragmentHolderActivity"
}

remote_url = "http://127.0.0.1:4723/wd/hub"

driver = webdriver.Remote(remote_url,capabilities)
driver.implicitly_wait(10)

driver.quit()