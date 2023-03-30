import json
import time
from encodings import undefined
import driver as driver
import requests as requests
import wait as wait
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import keyboard
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.support.wait import WebDriverWait
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '12'
desired_caps['deviceName'] = 'vivo 1915'
desired_caps['appPackage'] = 'com.flipkart.android'
desired_caps['appActivity'] = 'com.flipkart.android.activity.HomeFragmentHolderActivity'
desired_caps['noReset'] = True

driver=webdriver.Remote("http://localhost:4723/wd/hub",desired_caps)


# ele_Xpath = driver.find_element(AppiumBy.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout")
# ele_Xpath.click()

# ele_lang = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,"UiSelector().index(3)")
# ele_lang.click()

# ele_continue = driver.find_element(AppiumBy.ID, "com.flipkart.android:id/select_btn")
# ele_continue.click()

# location= driver.find_element(AppiumBy.ID,"com.flipkart.android:id/allow_button")
# location.click()

searchBar=driver.find_element(AppiumBy.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup")
searchBar.click()

Search=driver.find_element(AppiumBy.ID, "com.flipkart.android:id/search_autoCompleteTextView")
Search.send_keys("poco c31")
time.sleep(5)

# Search=driver.find_element(AppiumBy.ID, "com.flipkart.android:id/search_autoCompleteTextView")
# Search.send_keys("pogo c31 ")
# time.sleep(5)

mobile= driver.find_element(AppiumBy.XPATH,"//android.widget.TextView[@text='poco c31']")
mobile.click()
time.sleep(5)
# mobile= driver.find_element(AppiumBy.ID,"com.flipkart.android:id/txt_title")
# mobile.click()
# time.sleep(5)

my_Dict = {}

# # ----view_ALl= driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,"UiSelector().text('View All Variants')").click()
# viewAll=driver.find_element(AppiumBy.XPATH,"//android.widget.TextView[@text='View All Variants']")
# viewAll.click()
# time.sleep(5)
#
# #--- touch=TouchAction(driver)
# #--- touch.long_press(x=507, y=1470).move_to(x=478, y=452).release().perform()
# #--- time.sleep(2)
#
for i in range(1):
    touch = TouchAction(driver)
    touch.long_press(x=507, y=1470).move_to(x=478, y=452).release().perform()
    time.sleep(10)

# #--- wait = WebDriverWait(driver, timeout=50, poll_frequency=1)
# #--- element = wait.until(lambda x: x.find_elements(AppiumBy.XPATH, f"//android.widget.TextView[@index={i}]"))
    for i in range(1,3):
        wait = WebDriverWait(driver, timeout=10, poll_frequency=1)
        element = wait.until(lambda x: x.find_elements(AppiumBy.XPATH, f"//android.view.ViewGroup[@index={i}]/android.widget.TextView[@index=2]"))
        for x in element:
            l=x.text
            my_Dict[i]=[l]
            time.sleep(10)
# Mobile_List = list(my_Dict.items())
print(my_Dict)

user_input=int(input("Enter a number"))
if user_input == 1:
   driver.find_element(AppiumBy.XPATH,"//android.view.ViewGroup[@index=0]").click()
   wait = WebDriverWait(driver, timeout=100, poll_frequency=1)
   wait.until(lambda x: x.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Buy Now']")).click()
   touch = TouchAction(driver)
   touch.long_press(x=507, y=1470).move_to(x=478, y=452).release().perform()
   wait.until(lambda x: x.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='SKIP & CONTINUE']")).click()

   wait.until(lambda x: x.find_element(AppiumBy.XPATH, "//android.view.ViewGroup[@index=1]/android.view.ViewGroup[@index=1]")).click()
   # driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, "UiSelector().index(3)")
   wait.until(lambda x: x.find_element(AppiumBy.XPATH,"//android.view.ViewGroup[@index= 3]/android.view.ViewGroup[@index= 0]/android.view.ViewGroup[@index= 0]")).click()
   time.sleep(10)

   for i in range(1):
       touch = TouchAction(driver)
       touch.long_press(x=507, y=1470).move_to(x=478, y=452).release().perform()
       time.sleep(10)

   wait.until(lambda x: x.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Cash on Delivery']")).click()
   wait.until(lambda x: x.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='PLACE ORDER']")).click()

   time.sleep(5)

elif user_input == 2:
    driver.find_element(AppiumBy.XPATH, "//android.view.ViewGroup[@index=1]").click()
    wait = WebDriverWait(driver, timeout=100, poll_frequency=1)
    wait.until(lambda x: x.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Buy Now']")).click()
    touch = TouchAction(driver)
    touch.long_press(x=507, y=1470).move_to(x=478, y=452).release().perform()
    wait.until(lambda x: x.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='SKIP & CONTINUE']")).click()

    wait.until(lambda x: x.find_element(AppiumBy.XPATH,"//android.view.ViewGroup[@index=1]/android.view.ViewGroup[@index=1]")).click()
    # driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, "UiSelector().index(3)")
    wait.until(lambda x: x.find_element(AppiumBy.XPATH,"//android.view.ViewGroup[@index= 3]/android.view.ViewGroup[@index= 0]/android.view.ViewGroup[@index= 0]")).click()
    time.sleep(10)

    for i in range(1):
        touch = TouchAction(driver)
        touch.long_press(x=507, y=1470).move_to(x=478, y=452).release().perform()
        time.sleep(10)

    wait.until(lambda x: x.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Cash on Delivery']")).click()
    wait.until(lambda x: x.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='PLACE ORDER']")).click()

    time.sleep(5)
driver.quit()
time.sleep(50)