from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
import time
import os

PHONE_NUM = os.environ.get("PHONE_NUM")
PASSWORD = os.environ.get("PASSWORD")

# This code is to allow the Firefox location prompt to be auto allowed
geo_location = webdriver.FirefoxOptions()
geo_location.set_preference('geo.prompt.testing', True)
geo_location.set_preference('geo.prompt.testing.allow', True)
# # This will mock a certain location:
# geo_location.set_preference('geo.provider.network.url',
#                             'data:application/json,{"location": {"lat": 10.0, "lng": 10.0}, "accuracy": 100.0}')

# Pass options into the profile and open your page
driver = webdriver.Firefox(options=geo_location)
driver.get('https://tinder.com/')

time.sleep(2)
login_button = driver.find_element(By.CSS_SELECTOR, 'a.c1p6lbu0 > div:nth-child(2) > div:nth-child(3)')
login_button.click()
time.sleep(2)
facebook_button = driver.find_element(By.CSS_SELECTOR, 'div.My\(12px\):nth-child(2) > button:nth-child(1) > '
                                                       'div:nth-child(2) > div:nth-child(3)')
facebook_button.click()
time.sleep(2)
# Switching to pop up login window
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]

# Selecting Facebook and entering login information
driver.switch_to.window(fb_login_window)
user_field = driver.find_element(By.CSS_SELECTOR, '#email')
password_field = driver.find_element(By.CSS_SELECTOR, '#pass')
user_field.send_keys(PHONE_NUM)
password_field.send_keys(PASSWORD)
time.sleep(2)
login_button = driver.find_element(By.CSS_SELECTOR, 'html#facebook body.login_page._4idf.booklet.gecko.x1'
                                                    '.Locale_en_US div#booklet._li div#content.fb_content.clearfix '
                                                    'div.login_form_container form#login_form div#loginform '
                                                    'div#buttons.form_row.clearfix '
                                                    'label#loginbutton.uiButton.uiButtonConfirm.uiButtonLarge input')
login_button.click()
time.sleep(2)
# continue_button = driver.find_element(By.CSS_SELECTOR, 'html#facebook._9dls.__fb-light-mode body._6s5d._71pn.system-fonts--body div#mount_0_0_9e div div div.x9f619.x1n2onr6.x1ja2u2z div.x9f619.x1n2onr6.x1ja2u2z div.x78zum5.xdt5ytf.x1n2onr6.x1ja2u2z div.x78zum5.xdt5ytf.x1n2onr6 div.x78zum5.xdt5ytf.x1n2onr6.xat3117.xxzkxad div.x14hiurz.x78zum5.xdt5ytf.x1iyjqo2.xexx8yu.x1pi30zi.x18d9i69.x1swvt13.x2b8uid div.xkrivgy.x1gryazu.xh8yej3 div.x78zum5.xdt5ytf div.x1r8uery.x1iyjqo2 div div.x1i10hfl.xjbqb8w.x6umtig.x1b1mbwd.xaqea5y.xav7gou.x1ypdohk.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x16tdsg8.x1hl2dhg.xggy1nq.x1o1ewxj.x3x9cwd.x1e5q0jg.x13rtm0m.x87ps6o.x1lku1pv.x1a2a7pz.x9f619.x3nfvp2.xdt5ytf.xl56j7k.x1n2onr6.xh8yej3 div.x1n2onr6.x1ja2u2z.x78zum5.x2lah0s.xl56j7k.x6s0dn4.xozqiw3.x1q0g3np.xi112ho.x17zwfj4.x585lrc.x1403ito.x972fbf.xcfux6l.x1qhh985.xm0m39n.x9f619.xn6708d.x1ye3gou.xtvsq51.x1fq8qgq div.x6s0dn4.x78zum5.xl56j7k.x1608yet.xljgi0e.x1e0frkt div.x9f619.x1n2onr6.x1ja2u2z.x193iq5w.xeuugli.x6s0dn4.x78zum5.x2lah0s.x1fbi1t2.xl8fo4v span.x193iq5w.xeuugli.x13faqbe.x1vvkbs.x10flsy6.x1lliihq.x1s928wv.xhkezso.x1gmr53x.x1cpjm7i.x1fgarty.x1943h6x.x1tu3fi.x41vudc.x1lkfr7t.x1lbecb7.x1s688f.xtk6v10 span')
# continue_button.click()
# time.sleep(2)

# Driver switch to tinder main window and click on all pop-ups.
driver.switch_to.window(base_window)
allow_location_button = driver.find_element(By.XPATH,
                                            '/html/body/div[2]/main/div/div/div/div[3]/button[1]/div[2]/div[2]')
allow_location_button.click()
time.sleep(2)
notifications = driver.find_element(By.XPATH, '/html/body/div[2]/main/div/div/div/div[3]/button[2]/div[2]/div[2]')
notifications.click()
time.sleep(2)
screen_click = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div')
screen_click.click()
time.sleep(2)
cookies_click = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div[1]/div[1]/button/div[2]/div[2]')
cookies_click.click()
time.sleep(2)
