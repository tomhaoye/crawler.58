import cv2
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# browser = webdriver.Chrome(executable_path="C:\Program Files (x86)\Google\Chrome\Application\chromedriver")
# browser.implicitly_wait(5)
# wait = WebDriverWait(browser, 10)
# browser.get("http://www.geetest.com/type/")
# browser.find_elements_by_xpath("//div[@class='products-content']/ul/li")[1].click()
# button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "geetest_radar_tip")))
# browser.find_elements_by_class_name("geetest_radar_tip")[1].click() if len(
#     browser.find_elements_by_class_name("geetest_radar_tip")) > 1 else button.click()
# time.sleep(2)
# browser.save_screenshot("../pic/screenshot.png")

img_gray = cv2.imread("../pic/screenshot.png", cv2.IMREAD_GRAYSCALE)
gradX = cv2.Sobel(img_gray, ddepth=cv2.CV_32F, dx=1, dy=0, ksize=-1)
gradY = cv2.Sobel(img_gray, ddepth=cv2.CV_32F, dx=0, dy=1, ksize=-1)
img_gradient = cv2.subtract(gradX, gradY)
img_gradient = cv2.convertScaleAbs(img_gradient)
blurred = cv2.blur(img_gradient, (9, 9))
(_, thresh) = cv2.threshold(blurred, 90, 255, cv2.THRESH_BINARY)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (25, 25))
closed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

closed = cv2.erode(closed, None, iterations=4)
closed = cv2.dilate(closed, None, iterations=4)

cv2.imshow('', closed)
cv2.waitKey(3000)
cv2.destroyAllWindows()

# slider = browser.find_element_by_class_name("geetest_slider_button")
# ActionChains(browser).click_and_hold(slider).perform()
# ActionChains(browser).move_by_offset(100, yoffset=0).perform()
# ActionChains(browser).release().perform()
# time.sleep(2)
# browser.close()
