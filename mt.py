# import time
# import urllib
import time

from appium import webdriver

# from bs4 import BeautifulSoup
# from appium.options.android import UiAutomator2Options

# from selenium import webdriver
# from selenium.webdriver.common.by import By
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.by import By

from mitmproxy import ctx

# def request(flow):
# print('-----------进入request-------')
# info = ctx.log.info
# print(str(flow.request.host))
# getNum = False
from save_info import save_Info1

imag = []


def response(flow):
    print('****************')
    imag.append(flow.request.url)
    url = 'img-1.pddpic.com'
    if url in flow.request.url:
        print('找到了图片')
        print(flow.request.url)


def request(flow):
    print('----------------')
    imag.append(flow.request.url)
    url = 'img-1.pddpic.com'
    if url in flow.request.url:
        print('找到了图片')
        imag.append(flow.request.url)

        ops = ctx.log.info()
        ops(str(flow.request.url))
        print(flow.request.url)


def loadHtml(search):
    try:
        desire_cap = {
            'platformName': 'Android',
            'platformVersion': '9',
            'deviceName': 'duoduomaicai',
            'appPackage': 'com.xunmeng.pinduoduo',
            'appActivity': '.ui.activity.MainFrameActivity',
            'unicodeKeyboard': True,
            'resetKeyboard': True,
            'noReset': True,
            'newCommandTimeout': 6000,
            # 'automationName': 'UiAutomatoappiumr2',
        }
        options = UiAutomator2Options().load_capabilities(desire_cap)
        driver = webdriver.Remote('http://192.168.100.29:4723/wd/hub', options=options)

        driver.implicitly_wait(1000)
        print('------进入页面------')
        driver.find_element(By.XPATH, '//android.widget.TextView[@text="多多买菜"]').click()
        print('------点击多多买菜-----')
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH,
                            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout').click()

        print('------进入多多买菜----')
        driver.implicitly_wait(1000)
        driver.find_element(By.XPATH,
                            '//android.webkit.WebView[@text="多多买菜"]/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View').click()
        # pass
        print('-------触发多多买菜的搜索框-----')
        driver.implicitly_wait(30)
        driver.find_element(By.XPATH,
                            '//android.webkit.WebView[@text="搜索"]/android.view.View/android.view.View/android.view.View[4]/android.view.View[1]/android.view.View/android.view.View/android.widget.EditText').send_keys(
            search)
        driver.implicitly_wait(30)
        driver.find_element(By.XPATH, '//android.widget.Button[@text="搜索"]').click()
        print('-----点击搜索-----')
        driver.implicitly_wait(10)
        time.sleep(5)
        kls = pldsend(driver)
        print('+++++++++++++++++++++')
        # name1s = driver.find_elements(By.CLASS_NAME, 'android.widget.Button')
        arraylist = []
        name_list = []

        # images = driver.find_element(By)

        # for i in range(len(name1s)):
        #     print(name1s[i].text)
        #     if '，' in name1s[i].text:
        #         kts = name1s[i].text.split('，')
        #         ischeck = duplicate_check(name_list, kts[0])
        #         if not ischeck:
        #             arraylist.append([kts[0], kts[1]])
        #             name_list.append(kts[0])

        if not kls:
            kl = True
            while kl:

                # numd = numd + 1
                names = driver.find_elements(By.CLASS_NAME, 'android.widget.Button')
                if len(names) > 0:
                    for i in range(len(names)):
                        try:
                            print(names[i].text)
                            if '，' in names[i].text:
                                kts = names[i].text.split('，')
                                ischeck = duplicate_check(name_list, kts[0])
                                if not ischeck:
                                    print(names[i].text)
                                    arraylist.append([kts[0], kts[1]])
                                    name_list.append(kts[0])
                        except Exception as e:
                            print(e)
                iskl = pldsend(driver)

                if iskl:
                    kl = False
                else:
                    swipeDown(driver, 0)
                    time.sleep(3)
        time.sleep(3)
        print(imag)
        driver.quit()
        return arraylist
    except Exception as e:
        print(imag)
        print(e)


def duplicate_check(name_list, name):
    ischeck = False
    if name in name_list:
        ischeck = True
    # for i in name_list:
    #     if i == name:
    #         print('*******')
    #         print(i)
    #         ischeck = True
    #         break
    # if name in name_list:
    #     ischeck = True
    return ischeck


def pldsend(driver):
    iskl = False
    ende = driver.find_elements(By.CLASS_NAME, 'android.view.View')
    for i in ende:
        if i.text == '精选':
            iskl = True
    return iskl


# 获得机器屏幕大小x,y
def getSize(driver):
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return (x, y)


# 屏幕向下滑动---->刷新
def swipeDown(driver, t):
    size = getSize(driver)
    x1 = int(size[1] * 0.5)
    y1 = int(size[0] * 1)
    y2 = int(size[0] * 0.05)
    driver.swipe(x1, y1, x1, y2, t)


if __name__ == '__main__':
    search = '生抽'
    txtlist = loadHtml(search)
    print(txtlist)
    listHeader = ['标题', '价格']
    # print(listdata)
    save_Info1(listHeader, txtlist, search + '.xls')
    # time.sleep(500000)
