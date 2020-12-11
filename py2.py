from selenium import webdriver
from time import sleep

wd=webdriver.Chrome(r'e:\chromedriver.exe')

wd.get('https://baidu.com')
wd.maximize_window()


el=wd.find_element_by_id('kw')
el.send_keys('英雄联盟')
el=wd.find_element_by_id('su')
el.click()

sleep(3)

el=wd.find_element_by_class_name('c-img-border.c-img-radius-large')
el.click()

sleep(3)

for handle in wd.window_handles:
    # 先切换到该窗口
    wd.switch_to.window(handle)
    if wd.title=='英雄联盟全新官方网站-腾讯游戏':
        break

el=wd.find_element_by_link_text('下载游戏')
el.click()

for handle in wd.window_handles:
    # 先切换到该窗口
    wd.switch_to.window(handle)
    if wd.title=='下载中心-英雄联盟官方网站-腾讯游戏':
        break

sleep(3)
el=wd.find_element_by_class_name('downbtn.dxzq.blk.sub_spr')
el.click()

sleep(3)
picpath=wd.get_screenshot_as_file('E:\\1.png')
print(picpath)

wd.quit()