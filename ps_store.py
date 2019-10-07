from selenium import webdriver
import time 

link = "https://id.sonyentertainmentnetwork.com/create_account/?entry=%2Fcreate_account&state=returning&disableLinks=SENLink&ui=pr&client_id=f6c7057b-f688-4744-91c0-8179592371d2&hidePageElements=SENLogo&no_captcha=false&prompt=login&redirect_uri=https%3A%2F%2Fstore.playstation.com%2Fen-ca%2Fhome%2Fgames%3Ferror%3Dinvalid_token%26error_%26error_description%3DToken%2Bnot%2Bfound&request_locale=en_CA&response_type=code&scope=kamaji%3Acommerce_native%2Ckamaji%3Acommerce_container%2Ckamaji%3Alists&service_entity=urn%3Aservice-entity%3Apsn#/create_account/wizard/entrance?entry=%2Fcreate_account"

browser = webdriver.Chrome()
browser.get(link)
time.sleep(3)
button = browser.find_element_by_class_name("caption.row-button-flex-container")
button.click()
time.sleep(3)
input1 = browser.find_element_by_id("ember41")
input1.send_keys("test@test.ru")
input2 = browser.find_element_by_id("ember44")
input2.send_keys("Selenium!")
input3 = browser.find_element_by_id("ember46")
input3.send_keys("Selenium!")
time.sleep(3)
button = browser.find_element_by_class_name("wrapper-fitparent.wrapper-centeralign")
button.click()
time.sleep(3)
input4 = browser.find_element_by_class_name("data-ember-action-330")
input4.send_keys("1")
