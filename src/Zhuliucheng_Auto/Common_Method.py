#!C:\Python27  
#-*-coding:utf-8-*- 
'''
Created on 2014��4��30��

@author: Fred
'''

from selenium import  webdriver
import Element_Location
from selenium.webdriver.support.ui import WebDriverWait
import Xpath_interface
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains

def Page_load(Url):
    Driver=webdriver.Firefox()
    #Chrome("C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
    Driver.get(Url)  
    return Driver
#�ж�Ԫ���Ƿ����
def isPresent(driver,id):
    try: driver.find_element_by_id(id)
    except NoSuchElementException, e: return False
    return True

def YiGou_login(driver):
    WebDriverWait(driver,10).until(lambda  driver: Xpath_interface.Findbyxptah(driver,Element_Location.LoginXpath).is_displayed())
    #link to login page
    element=Xpath_interface.Findbyxptah(driver, Element_Location.LoginXpath)
    element.click()
    WebDriverWait(driver,10).until(lambda  driver: Xpath_interface.FindbyId(driver,Element_Location.Frame_id).is_displayed())
    #����л� 
    driver.switch_to_frame(Element_Location.Frame_id)
    driver.switch_to_frame(Element_Location.Frame_id)
   
    #WebDriverWait(driver,10).until(lambda  driver: Xpath_interface.Findbyxptah(driver,Element_Location.Besttong_id).is_displayed())
    #element=Xpath_interface.FindbyId(driver,Element_Location.Besttong_id).click()
    #input user name 
    #element=Xpath_interface.FindbyId(driver, Element_Location.User_id)
    #element.send_keys(Element_Location.UserName)
    #input password
    #element=Xpath_interface.FindbyId(driver, Element_Location.PWD_id)
    #element.send_keys(Element_Location.Password)
    #input check code
    #checkcode=raw_input("��������ȷ����֤�룺").encode('GBK') 
    #element=Xpath_interface.FindbyId(driver,Element_Location.CheckCode_id)
    #element.send_keys(checkcode)
    element=Xpath_interface.FindbyId(driver,Element_Location.Tianyi_UserID).send_keys(Element_Location.Tianyi_username)
    element=Xpath_interface.FindbyId(driver,Element_Location.Tianyi_userPWD_id).send_keys(Element_Location.Tianyi_pwd)
    #click ����½�� button
    #element=Xpath_interface.FindbyId(driver,Element_Location.Login_id).click()
    element=Xpath_interface.FindbyId(driver,Element_Location.Tianyi_login_bt_id).click()
    driver.implicitly_wait(30)

#�����ͣ�¼�    
def Move_to_element(element,driver):
    chain=ActionChains(driver)
    chain.move_to_element(element).perform()

#��������

def Select_element(selects):
    elements=Xpath_interface.FindelementsbyTagName(selects,Element_Location.Select_option_tag)
    elements[1].click()
    
    
    