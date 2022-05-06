#!/usr/bin/python3
#-- coding: UTF-8 --
from selenium import webdriver
import time
import pyautogui
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains

#一个用于解决滑块验证的函数，搬运自CSDN @knighthood2001 大佬，用于计算滑动条数据
def get_track(distance):  # distance为传入的总距离
    # 移动轨迹
    track = []
    # 当前位移
    current = 0
    # 计算间隔
    t = 0.2
    # 初速度
    v = 0
    while current < distance:
        a = 50
        v0 = v
        # 当前速度
        v = v0 + a * t
        # 移动距离
        # move = v0 * t + 1 / 2 * a * t * t
        move = v0 * t + a * t
        # 当前位移
        current += move
        # 加入轨迹
        track.append(round(move))
    return track  # list 返回的是整个滑动条的多个焦点，可以模拟鼠标的缓慢滑动
#一个用于解决滑块验证的函数，搬运自CSDN，用于移动滑块 
def move_to_gap(slider, tracks):  # slider是要移动的滑块,tracks是要传入的移动轨迹
    ActionChains(driver).click_and_hold(slider).perform()
    for x in tracks:
        ActionChains(driver).move_by_offset(xoffset=x, yoffset=0).perform()
    time.sleep(0.1)
    ActionChains(driver).release().perform()
 
 
#这是用于处理单选题和多选题的函数，下面调用更方便，搬运自github @1759749908 大佬
def translate(choose):    #把ABCD转化成为0123
    if choose == 'A' or choose == 'a':
        return 0
    elif choose == 'B' or choose == 'b':
        return 1
    elif choose == 'C' or choose == 'c':
        return 2
    elif choose == 'D' or choose == 'd':
        return 3
    elif choose == 'E' or choose == 'e':
        return 4
    elif choose == 'F' or choose == 'f':
        return 5
    elif choose == 'G' or choose == 'g':
        return 6
    else:
        pass

#具体处理单选题、多选题、填空题、下划线的填空题、多空填空题、翻页、交卷，根据自身情况修改查找元素的方式（）内的值
def submit_choice(question_number, choose):    #单择题

    answer = questions[question_number].find_elements_by_css_selector('.ui-radio')
    answer[translate(choose)].click()
    

def submit_multi_choice(question_number, choose_list):    #多选题
    pass
    answer = questions[question_number].find_elements_by_css_selector('.ui-checkbox')
    for i in range(len(choose_list)):
        answer[translate(choose_list[i])].click()


def submit_text(question_number, text):    #填空题
    text_area = questions[question_number].find_element_by_css_selector(
        'td')
    text_area.send_keys(text)

def submit_underline_text(question_number, text):    #下划线的填空题
    text_area = questions[question_number].find_element_by_css_selector(
        'underline')
    text_area.send_keys(text)

def submit_multi_text(question_number, answers_list):    #多空填空题
    text_area = questions[question_number].find_elements_by_css_selector(
        '.ui-input-text>input[type="text"]')
    for i in range(len(answers_list)):
        text_area[i].send_keys(answers_list[i])


def next_page():    #翻页
    next_button = driver.find_element_by_css_selector('#divNext')
    next_button.click()
    questions = driver.find_elements_by_css_selector('div.ui-controlgroup.column1')

def submit():    #交卷
    driver.find_element_by_css_selector('#submit_button').click()

def main():
    submit_multi_text(0, ['李狗蛋', '20190136017', '11111111111'])
    driver.find_element_by_xpath('//*[@id="select2-q2-container"]').click()
    #用于根据文字内容进行下拉框选择
    driver.find_element_by_xpath('//*[@id="select2-q2-results"]/li[text()="产业学院"]').click()
    #第二种用于下拉框选择的方法，选择下拉框倒数第三项
    #driver.find_element_by_xpath('//*[@id="select2-q2-container"]').click()
    #ul = driver.find_element_by_xpath('//*[@id="select2-q2-results"]')
    #list = ul.find_elements_by_xpath('li')
    #len(list)
    #list[-3].text
    #list[-3].click()
    driver.find_element_by_xpath('//*[@id="divNext"]').click()#翻页
    submit_choice(2, 'B')
    submit_choice(3, 'B')
    submit_choice(4, 'C')
    submit_choice(5, 'A')
    submit_choice(6, 'B')
    submit_choice(7, 'C')
    submit_choice(8, 'A')
    submit_choice(9, 'B')
    submit_choice(10, 'A')
    submit_choice(11, 'C')
    submit_choice(12, 'C')
    submit_choice(13, 'A')
    submit_choice(14, 'C')
    submit_choice(15, 'B')
    submit_choice(16, 'C')
    submit_choice(17, 'B')
    submit_choice(18, 'A')
    submit_choice(19, 'C')
    submit_choice(20, 'A')
    submit_choice(21, 'D')
    submit_choice(22, 'A')
    submit_choice(23, 'A')
    submit_choice(24, 'C')
    submit_choice(25, 'B')
    submit_choice(26, 'A')
    submit_choice(27, 'B')
    submit_choice(28, 'C')
    submit_choice(29, 'A')
    submit_choice(30, 'D')
    submit_choice(31, 'C')
    submit_choice(32, 'A')
    submit_choice(33, 'A')
    submit_choice(34, 'A')
    submit_choice(35, 'A')
    submit_choice(36, 'C')
    submit_choice(37, 'B')
    submit_choice(38, 'C')
    submit_choice(39, 'B')
    submit_choice(40, 'B')
    submit_choice(41, 'C')
    submit_choice(42, 'B')
    submit_choice(43, 'A')
    submit_choice(44, 'B')
    submit_choice(45, 'C')
    submit_choice(46, 'A')
    submit_choice(47, 'C')
    submit_choice(48, 'B')
    submit_choice(49, 'C')
    submit_multi_choice(50, ['a', 'c', 'd'])
    submit_multi_choice(51, ['a', 'b'])
    driver.find_element_by_xpath('//*[@id="ctlNext"]').click()
    time.sleep(0.05)#等待智能验证弹窗“确认”按钮
    driver.find_element_by_xpath('//*[@id="alert_box"]/div[2]/div[2]/button').click()
    driver.find_element_by_xpath('//*[@id="rectMask"]').click()
    #下面用于处理滑块验证，但极易出现二次验证，如果要处理，可以关闭第二次出现的滑块并再次点击验证，一直点提交，如果写两次滑块验证，会出现难以处理的死循环
    btn = driver.find_element_by_xpath('//*[@id="nc_1_n1z"]')
    try:
        huakuai = driver.find_element_by_css_selector('#nc_1_n1z')
        move_to_gap(huakuai, get_track(328))
    except:
        pass
    finally:
        # 关闭页面
        handles = driver.window_handles
        driver.switch_to.window(handles[0])
        time.sleep(0.5)
        # 刷新页面（可要可不要）
        # driver.refresh()
        # 关闭当前页面，如果只有一个页面，则也关闭浏览器
        driver.close()
if __name__ == "__main__":
    driver = webdriver.Chrome()
    #通过将webdriver置空，伪装selenium，防止智能检测失败
    option = webdriver.ChromeOptions()
    option.add_experimental_option('excludeSwitches', ['enable-automation'])
    option.add_experimental_option('useAutomationExtension', False)
    driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument',
                                    {'source': 'Object.defineProperty(navigator, "webdriver", {get: () => undefined})'})
    #访问网址
    driver.get('https://ks.wjx.top/vm/Pl1obuQ.aspx')
    #通过所有标签（'.ui-field-contain'）定位题目“question”位置
    questions = driver.find_elements_by_css_selector('.ui-field-contain')
    main()
