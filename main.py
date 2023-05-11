from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from openpyxl import Workbook
from datetime import datetime
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

import datetime
import os
from datetime import datetime as dt
from bs4 import BeautifulSoup

from dateutil.parser import parse

import feedparser

import requests
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import shutil

chrome_options = Options()

# chrome_options.add_argument('user-agent="MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"')
chrome_options.add_argument("window-size=1920x1080")
# chrome_options.add_argument("--dns-prefetch-disable")
# chrome_options.add_argument("start-maximized")
# chrome_options.add_argument("enable-automation")
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--no-sandbox")
# chrome_options.add_argument("--disable-infobars")
# chrome_options.add_argument('--disable-extensions')
# chrome_options.add_argument("--disable-dev-shm-usage")
# chrome_options.add_argument("--disable-browser-side-navigation")
# chrome_options.add_argument("--disable-gpu")
# chrome_options.add_argument('--ignore-certificate-errors')
# chrome_options.add_argument('--ignore-ssl-errors')
chrome_options.add_argument("lang=ko_KR")

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),options=chrome_options
)

def find_iframe_name(driver, name, second):
    conf=0
    for l in range(second):
        time.sleep(1)
        try:
            iframe_list = driver.find_elements(by=By.TAG_NAME, value="iframe")
            for i in iframe_list:
                if name in i.get_attribute("title") or "�쇱씠釉뚮━ - �볤��곸뿭" in i.get_attribute("title"):
                    conf=1
        except:
            continue
        if conf:
            break




def driver_wait(driver, selector, path, cnt=10):
    """
    selenium을 이용한 크롤링 시 사용됩니다. 해당 요소가 있을때까지 기다리는 함수입니다.
    """
    while cnt < 60:
        try:
            element = WebDriverWait(driver, cnt).until(
                EC.presence_of_element_located((selector, path))
            )
            return element
        except:
            time.sleep(1)
            return driver_wait(driver, selector, path, cnt + 1)
    raise NoSuchElementException()


def driver_button_wait(driver, selector, path, cnt=10):
    """
    selenium을 이용한 크롤링 시 사용됩니다. 해당 요소가 있을때까지 기다리는 함수입니다.
    """
    while cnt < 60:
        try:
            element = WebDriverWait(driver, cnt).until(
                EC.element_to_be_clickable((selector, path))
            )
            if element==False:
                raise NoSuchElementException()
            return element
        except:
            time.sleep(1)
            return driver_button_wait(driver, selector, path, cnt + 1)
    raise NoSuchElementException()


def driver_text_wait(driver, selector, path, cnt=10):
    """
    selenium을 이용한 크롤링 시 사용됩니다. 해당 요소가 있을때까지 기다리는 함수입니다.
    """
    while cnt < 60:
        try:
            element = WebDriverWait(driver, cnt).until(
                EC.text_to_be_present_in_element((selector, path))
            )
            if element==False:
                raise NoSuchElementException()
            return element
        except:
            time.sleep(1)
            return driver_text_wait(driver, selector, path, cnt + 1)
    raise NoSuchElementException()

def find_element(driver, selector, retry=10):
    while retry < 20:
        time.sleep(retry)
        try:
            return selector
        except:
            return find_element(driver, selector, retry + 1)
    raise NoSuchElementException()



def webdriver_reload():
    global driver
    driver.quit()
    driver= webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),options=chrome_options
    )

link_function_dic={
    "news.kmib.co.kr":"scrap_kmib",
    "24hz.kr":"scrap_mlb",
    "bbs.ruliweb.com":"scrap_ruli",
    "gall.dcinside.com":"scrap_dc",
    "hankookilbo.com":"scrap_hkib",
    "imnews.imbc.com":"scrap_imbc",
    "mlbpark.donga.com":"scrap_mlb",
    "news.imaeil.com":"scrap_kmib",
    "news.kbs.co.kr":"scrap_kbs",
    "news.mk.co.kr":"scrap_mk",
    "news.sbs.co.kr":"scrap_sbs",
    "n.news.naver.com":"scrap_naver",
    "nownews.seoul.co.kr":"scrap_seoul",
    "pann.nate.com":"scrap_nate",
    "www.ajunews.com":"scrap_aj",
    "www.bobaedream.co.kr":"scrap_bobae",
    "www.busan.com":"scrap_kbs",
    "www.ccdailynews.com":"scrap_ccdai",
    "www.cctoday.co.kr":"scrap_cctoday",
    "www.clien.net":"scrap_clien",
    "www.daejonilbo.com":"scrap_daejon",
    "www.ddanzi.com":"scrap_ddanzi",
    "www.domin.co.kr":"scrap_domin",
    "www.donga.com":"scrap_donga",
    "www.fmkorea.com":"scrap_fm",
    "www.gnnews.co.kr":"scrap_gn",
    "www.hani.co.kr":"scrap_hani",
    "www.hankyung.com":"scrap_hankyung",
    "www.idomin.com":"scrap_idomin",
    "www.inven.co.kr":"scrap_inven",
    "www.jemin.com":"scrap_jemin",
    "www.jeonmae.co.kr":"scrap_jeonmae",
    "www.jjan.kr":"scrap_jjan",
    "www.joongang.co.kr":"scrap_joongang",
    "www.joongboo.com":"scrap_sbs",
    "www.kado.net":"scrap_kado",
    "www.khan.co.kr":"scrap_sbs",
    "www.kjilbo.co.kr":"scrap_kado",
    "www.kookje.co.kr":"scrap_sbs",
    "www.korea.kr":"scrap_korea",
    "www.ksilbo.co.kr":"scrap_ksilbo",
    "www.kwnews.co.kr":"scrap_sbs",
    "www.kyeongin.com":"scrap_sbs",
    "www.mk.co.kr":"scrap_mk",
    "www.munhwa.com":"scrap_sbs",
    "www.ppomppu.co.kr":"scrap_ppomppu",
    "www.sedaily.com":"scrap_sedaily",
    "www.seoul.co.kr":"scrap_seoul",
    "www.slrclub.com":"scrap_slr",
    "www.todayhumor.co.kr":"scrap_humor",
    "www.yeongnam.com":"scrap_sbs",

}


def get_comment(link):
    target=link.split('/')[2]
    return eval(link_function_dic[target]+"(link)")


def scrap_kmib(url):
    # url = "https://news.kmib.co.kr/article/view.asp?arcid=0017589614&code=61141411&sid1=eco"
    driver.get(url=url)
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    iframe_list = driver.find_elements(by=By.TAG_NAME, value="iframe")

    comment_list=[]

    for i in iframe_list:
        # print(i.get_attribute("src"))
        if "/was.livere.me/comment" in i.get_attribute("src"):

            driver.switch_to.frame(i)
            while(1):
                # driver_wait(driver, By.CLASS_NAME, "reply-content")
                time.sleep(1)
                temp = driver.find_elements(by=By.CLASS_NAME, value="reply-comment-btn")
                for j in temp:
                    j.send_keys(Keys.ENTER)
                temp=driver.find_elements(by=By.CLASS_NAME, value="reply-content")
                for j in temp:
                    comment_list.append(j.text)
                try:
                    more_button = driver.find_element(by=By.CLASS_NAME, value="page-current-btn")
                    next_sibling = driver.execute_script("""
                        return arguments[0].nextElementSibling
                    """, more_button)
                    # print(next_sibling.text)
                    next_sibling.send_keys(Keys.ENTER)

                except:
                    break

            driver.switch_to.default_content()
    return comment_list

def scrap_mlb(url):
    driver.get(url=url)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    comment_list = list(map(lambda x:x.text,driver.find_elements(by=By.CLASS_NAME, value="re_txt")))
    return comment_list

def scrap_aj(url):
    driver.get(url=url)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    comment_list = list(map(lambda x:x.text,driver.find_elements(by=By.CLASS_NAME, value="comment_txt")))
    return comment_list

def scrap_domin(url):
    driver.get(url=url)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    comment_list = list(map(lambda x:x.text,driver.find_elements(by=By.CLASS_NAME, value="comments-content")))
    return comment_list

def scrap_donga(url):
    driver.get(url=url)

    for i in range(10):
        time.sleep(0.3)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight*0.1*"+str(i)+");")

    driver_button_wait(driver, By.CLASS_NAME, "btn_more")

    more_btn=driver.find_element(by=By.CLASS_NAME, value="btn_more")
    more_btn.send_keys(Keys.ENTER)

    driver_wait(driver, By.CLASS_NAME, "reply_layer_con")


    comment_tag = driver.find_element(by=By.CLASS_NAME, value="reply_layer_con")
    print(comment_tag.get_attribute("innerHTML"))
    ls=comment_tag.find_elements(by=By.CLASS_NAME, value='comment')
    comment_list = list(map(lambda x:x.text,comment_tag.find_elements(by=By.CLASS_NAME, value='comment')))[3:]
    return comment_list

def scrap_ccdai(url):
    driver.get(url=url)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    comment_list = list(map(lambda x:x.text,driver.find_elements(by=By.CLASS_NAME, value="comments-content")))
    return comment_list

def scrap_cctoday(url):
    driver.get(url=url)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    comment_list = list(map(lambda x:x.text,driver.find_elements(by=By.CLASS_NAME, value="comments-content")))
    return comment_list

def scrap_jemin(url):
    driver.get(url=url)
    try:
        driver_button_wait(driver, By.CLASS_NAME, "reply-more")
        more_btn = driver.find_element(by=By.CLASS_NAME, value="reply-more")
        more_btn.send_keys(Keys.ENTER)
    except:
        pass

    comment_list=[]
    while(1):
        try:
            comment_list += list(map(lambda x:x.text,driver.find_elements(by=By.CLASS_NAME, value="comments-content")))
            paging=driver.find_element(by=By.CLASS_NAME, value="pagination")
            atag=paging.find_elements(by=By.TAG_NAME, value="a")[1]
            atag.click()
        except:
            break
    return comment_list

def scrap_ruli(url):
    driver.get(url=url)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    comment_list = list(map(lambda x:x.text,driver.find_elements(by=By.CLASS_NAME, value="text_wrapper")))
    return comment_list

def scrap_dc(url):
    driver.get(url=url)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    comment_tag=driver.find_element(by=By.CLASS_NAME, value="all-comment")
    comment_list = list(map(lambda x:x.text,comment_tag.find_elements(by=By.CLASS_NAME, value="txt")))[:-1]
    return comment_list

def scrap_ppomppu(url):
    driver.get(url=url)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    comment_tag=driver.find_element(by=By.ID, value="quote")
    comment_list = list(map(lambda x:x.text,comment_tag.find_elements(by=By.CLASS_NAME, value="mid-text-area")))
    return comment_list

def scrap_clien(url):
    driver.get(url=url)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    comment_tag=driver.find_element(by=By.CLASS_NAME, value="post_comment")
    comment_list = list(map(lambda x:x.text,comment_tag.find_elements(by=By.CLASS_NAME, value="comment_view")))
    return comment_list

def scrap_slr(url):
    driver.get(url=url)
    comment_tag=driver.find_element(by=By.CLASS_NAME, value="list")
    comment_list = list(map(lambda x:x.text,comment_tag.find_elements(by=By.CLASS_NAME, value="cmt-contents")))
    return comment_list

def scrap_humor(url):
    driver.get(url=url)
    comment_tag=driver.find_element(by=By.ID, value="memoContainerDiv")
    comment_list = list(map(lambda x:x.text,comment_tag.find_elements(by=By.CLASS_NAME, value="memoContent")))
    return comment_list

def scrap_joongang(url):
    driver.get(url=url)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    comment_tag=driver.find_element(by=By.CLASS_NAME, value="comment_wrap")
    comment_list = list(map(lambda x:x.text,comment_tag.find_elements(by=By.CLASS_NAME, value="comment_text")))
    return comment_list

def scrap_inven(url):
    driver.get(url=url)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    comment_tag=driver.find_element(by=By.ID, value="powerbbsCmt2")
    comment_list = list(map(lambda x:x.text,comment_tag.find_elements(by=By.CLASS_NAME, value="cmtContentOne")))
    return comment_list

def scrap_ddanzi(url):
    driver.get(url=url)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    comment_tag=driver.find_element(by=By.ID, value="cmt_list")
    comment_list = list(map(lambda x:x.text,comment_tag.find_elements(by=By.CLASS_NAME, value="fdComment")))
    return comment_list


def scrap_gn(url):
    driver.get(url=url)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    try:
        more_btn = driver.find_element(by=By.CLASS_NAME, value="reply-more")
        more_btn.click()
    except:
        pass
    comment_list=[]
    while(1):
        try:
            comment_list += list(map(lambda x:x.text,driver.find_elements(by=By.CLASS_NAME, value="comments-content")))
            paging=driver.find_element(by=By.CLASS_NAME, value="pagination")
            atag=paging.find_elements(by=By.TAG_NAME, value="a")[1]
            atag.click()
        except:
            break
    return comment_list

def scrap_daejon(url):
    driver.get(url=url)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    comment_tag=driver.find_element(by=By.ID, value="comment")
    comment_list = list(map(lambda x:x.text,comment_tag.find_elements(by=By.CLASS_NAME, value="comment-content-view")))
    return comment_list

def scrap_jeonmae(url):
    driver.get(url=url)
    driver_wait(driver, By.CLASS_NAME, "reply-list")
    comment_tag=driver.find_element(by=By.CLASS_NAME, value="reply-list")
    comment_list = list(map(lambda x:x.text,comment_tag.find_elements(by=By.CLASS_NAME, value="comments-content")))
    return comment_list

def scrap_hkib(url):
    driver.get(url=url)
    driver_wait(driver, By.CLASS_NAME, "comment-box")
    comment_tag=driver.find_element(by=By.CLASS_NAME, value="comment-box")
    comment_list = list(map(lambda x:x.text,comment_tag.find_elements(by=By.CLASS_NAME, value="text")))
    return comment_list

def scrap_ksilbo(url):
    driver.get(url=url)
    driver_wait(driver, By.ID, "comment-list")
    comment_tag=driver.find_element(by=By.ID, value="comment-list")

    more_btn=driver.find_elements(by=By.CLASS_NAME, value="btn-comment-sub")
    for i in more_btn:
        try:
            if i.get_attribute("title")=="답글":
                i.click()
        except:
            continue

    comment_list = list(map(lambda x:x.text,comment_tag.find_elements(by=By.CLASS_NAME, value="comment-content-view")))
    return comment_list

def scrap_jjan(url):
    driver.get(url=url)

    comment_list=[]
    while(1):
        try:
            comment_list += list(map(lambda x:x.text,driver.find_elements(by=By.CLASS_NAME, value="reply_txt")))
            paging=driver.find_element(by=By.CLASS_NAME, value="pagination")
            atag=paging.find_elements(by=By.TAG_NAME, value="a")[2]
            atag.click()
            time.sleep(1)
        except:
            break
    return comment_list

def scrap_fm(url):
    driver.get(url=url)
    driver_wait(driver, By.ID, "cmtPosition")
    comment_tag=driver.find_element(by=By.ID, value="cmtPosition")
    comment_list = list(map(lambda x:x.text,comment_tag.find_elements(by=By.CLASS_NAME, value="comment-content")))
    return comment_list

def scrap_idomin(url):
    driver.get(url=url)
    driver_wait(driver, By.CLASS_NAME, "container")
    comment_tag=driver.find_elements(by=By.CLASS_NAME, value="container")[1]
    comment_list = list(map(lambda x:x.text,comment_tag.find_elements(by=By.CLASS_NAME, value="comments-content")))
    return comment_list

def scrap_kado(url):
    driver.get(url=url)
    driver_wait(driver, By.CLASS_NAME, "reply-list")
    comment_tag=driver.find_element(by=By.CLASS_NAME, value="reply-list")
    comment_list = list(map(lambda x:x.text,comment_tag.find_elements(by=By.CLASS_NAME, value="comments-content")))
    return comment_list

def scrap_hankyung(url):
    driver.get(url=url)
    driver.switch_to.frame(driver.find_element(by=By.ID, value="hk-comment-client"))

    driver_wait(driver, By.CLASS_NAME, "hk__comment-list")
    comment_tag=driver.find_element(by=By.CLASS_NAME, value="hk__comment-list")
    comment_list = list(map(lambda x:x.text,comment_tag.find_elements(by=By.CLASS_NAME, value="cmt__txt-box")))
    return comment_list

def scrap_bobae(url):
    driver.get(url=url)
    driver_wait(driver, By.CLASS_NAME, "commenticontype")
    comment_tag=driver.find_element(by=By.CLASS_NAME, value="commenticontype")

    comment_list = []
    for i in comment_tag.find_elements(by=By.TAG_NAME, value="dd"):
        if "small" in i.get_attribute("id") and "bepl" not in i.get_attribute("id"):
            comment_list.append(i.text)

    return comment_list

def scrap_imbc(url):
    driver.get(url=url)
    while(1):
        try:
            more_btn=driver.find_element(by=By.CLASS_NAME, value="btn_more")
            more_btn.click()
        except:
            break

    comment_list = list(map(lambda x:x.text,driver.find_elements(by=By.CLASS_NAME, value="user_text")))
    return comment_list

def scrap_kbs(url):

    driver.get(url=url)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    find_iframe_name(driver,"라이브리 - 댓글영역",10)

    comment_list=[]

    iframe_list = driver.find_elements(by=By.TAG_NAME, value="iframe")
    for i in iframe_list:
        # print(i.get_attribute("src"))
        if "라이브리 - 댓글영역" in i.get_attribute("title"):
            driver.switch_to.frame(i)
            while(1):
                try:
                    time.sleep(1)
                    more_btn=driver.find_element(by=By.CLASS_NAME, value="more-btn")
                    more_btn.click()
                except:
                    break
            # driver_wait(driver, By.CLASS_NAME, "reply-content")

            comment_list = list(map(lambda x:x.text,driver.find_elements(by=By.CLASS_NAME, value="reply-content")))
            driver.switch_to.default_content()
            break

    return comment_list

def scrap_sbs(url):
    driver.get(url=url)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    find_iframe_name(driver,"라이브리 - 댓글영역",10)

    comment_list=[]

    iframe_list = driver.find_elements(by=By.TAG_NAME, value="iframe")
    for i in iframe_list:
        # print(i.get_attribute("src"))
        if "라이브리 - 댓글영역" in i.get_attribute("title") or "�쇱씠釉뚮━ - �볤��곸뿭" in i.get_attribute("title"):
            driver.switch_to.frame(i)
            while(1):
                try:
                    time.sleep(1)
                    more_btn=driver.find_element(by=By.CLASS_NAME, value="more-btn")
                    more_btn.click()
                except:
                    break
            # driver_wait(driver, By.CLASS_NAME, "reply-content")

            comment_list = list(map(lambda x:x.text,driver.find_elements(by=By.CLASS_NAME, value="reply-content")))
            driver.switch_to.default_content()
            break

    return comment_list

def scrap_korea(url):
    driver.get(url=url)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    for i in range(5):
        time.sleep(1)
        try:
            more_btn = driver.find_element(by=By.CLASS_NAME, value="livere_comment").find_element(by=By.TAG_NAME,value="button")
            more_btn.click()
            break
        except:
            continue

    find_iframe_name(driver,"라이브리 - 댓글영역",10)

    comment_list=[]

    iframe_list = driver.find_elements(by=By.TAG_NAME, value="iframe")
    for i in iframe_list:
        # print(i.get_attribute("src"))
        if "라이브리 - 댓글영역" in i.get_attribute("title"):
            driver.switch_to.frame(i)
            while(1):
                try:
                    time.sleep(1)
                    more_btn=driver.find_element(by=By.CLASS_NAME, value="more-btn")
                    more_btn.click()
                except:
                    break
            # driver_wait(driver, By.CLASS_NAME, "reply-content")

            comment_list = list(map(lambda x:x.text,driver.find_elements(by=By.CLASS_NAME, value="reply-content")))
            driver.switch_to.default_content()
            break

    return comment_list

def scrap_hani(url):
    driver.get(url=url)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    find_iframe_name(driver,"라이브리 - 댓글영역",10)

    comment_list=[]

    iframe_list = driver.find_elements(by=By.TAG_NAME, value="iframe")
    for i in iframe_list:
        # print(i.get_attribute("src"))
        if "라이브리 - 댓글영역" in i.get_attribute("title"):
            driver.switch_to.frame(i)
            while(1):
                try:
                    time.sleep(1)
                    more_btn=driver.find_element(by=By.CLASS_NAME, value="more-btn")
                    more_btn.click()
                except:
                    break
            # driver_wait(driver, By.CLASS_NAME, "reply-content")

            comment_list = list(map(lambda x:x.text,driver.find_elements(by=By.CLASS_NAME, value="reply-content")))
            driver.switch_to.default_content()
            break

    return comment_list

def scrap_seoul(url):
    driver.get(url=url)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    driver_wait(driver, By.NAME, "new_iframeLivere")
    driver.switch_to.frame(driver.find_element(by=By.NAME, value="new_iframeLivere"))

    find_iframe_name(driver,"라이브리 - 댓글영역",10)
    iframe_list = driver.find_elements(by=By.TAG_NAME, value="iframe")

    comment_list=[]

    for i in iframe_list:
        # print(i.get_attribute("src"))
        if "라이브리 - 댓글영역" in i.get_attribute("title"):
            driver.switch_to.frame(i)
            while(1):
                try:
                    time.sleep(1)
                    more_btn=driver.find_element(by=By.CLASS_NAME, value="more-btn")
                    more_btn.click()
                except:
                    break
            # driver_wait(driver, By.CLASS_NAME, "reply-content")

            comment_list = list(map(lambda x:x.text,driver.find_elements(by=By.CLASS_NAME, value="reply-content")))
            driver.switch_to.default_content()

    return comment_list

def scrap_sedaily(url):
    driver.get(url=url)
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight*0.6);")

    driver_wait(driver, By.NAME, "realTalk")
    driver.switch_to.frame(driver.find_element(by=By.NAME, value="realTalk"))

    time.sleep(1)
    try:
        driver_wait(driver, By.CLASS_NAME, "btn-outline-more")
        more_btn = driver.find_element(by=By.CLASS_NAME, value="btn-outline-more")
        more_btn.click()
    except:
        pass

    temp=0
    conf=0
    for i in range(10):
        print(temp)
        try:
            now = len(driver.find_elements(by=By.CLASS_NAME, value="close"))
        except:
            time.sleep(1)
            continue
        if now==temp:
            conf+=1
        else:
            temp=now
            conf=0
        if conf>3:
            break

    more_btn = driver.find_elements(by=By.CLASS_NAME, value="close")

    for i in more_btn:
        try:
            print(i.find_element(by=By.CLASS_NAME, value="txt").text)
            if "답글" in i.find_element(by=By.CLASS_NAME, value="txt").text:
                i.click()
                time.sleep(1)
        except:
            continue

    comment_list = list(map(lambda x:x.text,driver.find_elements(by=By.CLASS_NAME, value="message")))
    return comment_list




def scrap_mk(url):
    driver.get(url=url)
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    try:
        more_btn=driver.find_element(by=By.CLASS_NAME, value="basic")[2]
        more_btn.click()
    except:
        pass

    comment_list = list(map(lambda x: x.text, driver.find_elements(by=By.CLASS_NAME, value="cmt_area")))
    return comment_list

def scrap_nate(url):
    driver.get(url=url)
    driver_wait(driver, By.CLASS_NAME, "cmtList-wrap")
    try:
        comment_tag=driver.find_elements(by=By.CLASS_NAME, value="cmtList-wrap")[1]
        comment_list = list(map(lambda x:x.text,comment_tag.find_elements(by=By.CLASS_NAME, value="usertxt")))
    except:
        comment_list=[]
    return comment_list

def scrap_naver(url):
    driver.get(url=url)
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    try:
        driver_button_wait(driver, By.CLASS_NAME, "u_cbox_in_view_comment")
        more_btn=driver.find_element(by=By.CLASS_NAME, value="u_cbox_in_view_comment")
        more_btn.click()
    except:
        pass

    while (1):
        try:
            time.sleep(1)
            more_btn = driver.find_element(by=By.CLASS_NAME, value="u_cbox_page_more")
            more_btn.click()
        except:
            break
    driver_wait(driver, By.CLASS_NAME, "u_cbox_contents")

    comment_list = list(map(lambda x: x.text, driver.find_elements(by=By.CLASS_NAME, value="u_cbox_contents")))
    return comment_list

# print(get_comment("https://news.kmib.co.kr/article/view.asp?arcid=0017589614&code=61141411&sid1=eco"))
# print(get_comment("https://24hz.kr/board/bbs/link.php?bo_table=mlbpark&wr_id=8798164&no=1"))
# print(get_comment("https://bbs.ruliweb.com/community/board/300148/read/36335170?page=4"))
# print(get_comment("https://gall.dcinside.com/board/view/?id=dcbest&no=133707&_dcbest=1&page=1"))
# print(get_comment("https://hankookilbo.com/News/Read/A2023042814000005674"))
# print(get_comment("https://imnews.imbc.com/replay/2023/nw1200/article/6478622_36170.html"))
# print(get_comment("https://mlbpark.donga.com/mp/b.php?id=202304280080548728&p=1&b=mlbtown&m=view&select=&query=&user=&site=donga.com"))
# print(get_comment("https://news.imaeil.com/page/view/2023042716533940030"))
# print(get_comment("https://news.kbs.co.kr/news/view.do?ncd=7669443"))
# print(get_comment("https://news.sbs.co.kr/news/endPage.do?news_id=N1007172370"))
# print(get_comment("https://n.news.naver.com/mnews/article/001/0013381110?sid=100"))
# print(get_comment("https://nownews.seoul.co.kr/news/newsView.php?id=20230507601003"))
# print(get_comment("https://www.busan.com/view/busan/view.php?code=2023043016330228903"))
# print(get_comment("https://www.ccdailynews.com/news/articleView.html?idxno=2162612"))
# print(get_comment("https://www.cctoday.co.kr/news/articleView.html?idxno=2177659#reply"))
# print(get_comment("https://www.clien.net/service/board/park/17530099"))
# print(get_comment("http://www.daejonilbo.com/news/articleView.html?idxno=2061243"))
# print(get_comment("https://www.ddanzi.com/index.php?mid=free&page=2&document_srl=770649778"))
# print(get_comment("https://www.donga.com/news/Society/article/all/20230510/119216740/1"))
# print(get_comment("https://www.fmkorea.com/5122403422"))
# print(get_comment("http://www.gnnews.co.kr/news/articleView.html?idxno=527873"))
# print(get_comment("https://www.hani.co.kr/arti/society/society_general/1089816.html"))
# print(get_comment("https://www.hankyung.com/realestate/article/2023042814301?rss=r"))
# print(get_comment("https://www.idomin.com/news/articleView.html?idxno=823988"))
# print(get_comment("https://www.inven.co.kr/board/webzine/2097/2064411?iskin=webzine"))
# print(get_comment("http://www.jemin.com/news/articleView.html?idxno=754471"))
# print(get_comment("https://www.jeonmae.co.kr/news/articleView.html?idxno=956230"))
# print(get_comment("https://www.jjan.kr/article/20230509580322"))
# print(get_comment("https://www.joongang.co.kr/article/25159017#home"))
# print(get_comment("http://www.joongboo.com/news/articleView.html?idxno=363590192"))
# print(get_comment("http://www.kado.net/news/articleView.html?idxno=1152872"))
# print(get_comment("https://www.khan.co.kr/politics/assembly/article/202305012110005/?utm_source=khan_rss&utm_medium=rss&utm_campaign=total_news"))
# print(get_comment("https://www.korea.kr/news/policyNewsView.do?newsId=148914671&pWise=mostViewNewsSub&pWiseSub=B1"))
# print(get_comment("http://www.kwnews.co.kr/page/view/2023051008233946461"))
# print(get_comment("https://www.mk.co.kr/news/stock/10723775"))
# print(get_comment("https://www.munhwa.com/news/view.html?no=2023043001039930295003"))
# print(get_comment("https://www.ppomppu.co.kr/zboard/view.php?id=freeboard&no=8305871"))
# print(get_comment("https://www.sedaily.com/NewsView/29OI5L5T7Y"))
# print(get_comment("https://www.seoul.co.kr/news/newsView.php?id=20230501500162"))
# print(get_comment("http://www.slrclub.com/bbs/vx2.php?id=hot_article&no=1077506"))
# print(get_comment("https://www.todayhumor.co.kr/board/view.php?table=humorbest&no=1728922&s_no=1728922"))
print(get_comment("https://www.yeongnam.com/web/view.php?key=20220914010001784"))