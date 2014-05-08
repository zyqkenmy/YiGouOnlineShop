#!C:\Python27  
#-*-coding:utf-8-*- 
'''
Created on 2014-4-18

@author: Fred
'''



# def Page_load(Url):
#     Driver=webdriver.Firefox()
#     #Chrome("C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
#     Driver.get(Url)  
#     return Driver
# 
# def YiGou_login(driver):
#     WebDriverWait(driver,10).until(lambda  driver: Findbyxptah(driver,Element_Location.LoginXpath).is_displayed())
#     #link to login page
#     element=Findbyxptah(driver, Element_Location.LoginXpath)
#     element.click()
#     WebDriverWait(driver,10).until(lambda  driver: FindbyId(driver,Element_Location.Frame_id).is_displayed())
#      #¿ò¼ÜÇÐ»»
#     driver.switch_to_frame(Element_Location.Frame_id)
#     driver.switch_to_frame(Element_Location.Frame_id)
#    
#     #WebDriverWait(driver,10).until(lambda  driver: Xpath_interface.Findbyxptah(driver,Element_Location.Besttong_id).is_displayed())
#     #element=Xpath_interface.FindbyId(driver,Element_Location.Besttong_id).click()
#     #input user name 
#     #element=Xpath_interface.FindbyId(driver, Element_Location.User_id)
#     #element.send_keys(Element_Location.UserName)
#     #input password
#     #element=Xpath_interface.FindbyId(driver, Element_Location.PWD_id)
#     #element.send_keys(Element_Location.Password)
#     #input check code
#     #checkcode=raw_input("ÇëÊäÈëÕýÈ·µÄÑéÖ¤Âë£º").encode('GBK') 
#     #element=Xpath_interface.FindbyId(driver,Element_Location.CheckCode_id)
#     #element.send_keys(checkcode)
#     element=FindbyId(driver,Element_Location.Tianyi_UserID).send_keys(Element_Location.Tianyi_username)
#     element=FindbyId(driver,Element_Location.Tianyi_userPWD_id).send_keys(Element_Location.Tianyi_pwd)
#     #click ¡°µÇÂ½¡± button
#     #element=Xpath_interface.FindbyId(driver,Element_Location.Login_id).click()
#     element=FindbyId(driver,Element_Location.Tianyi_login_bt_id).click()
#     driver.implicitly_wait(30)
#     
#     #input check code
#     #element=Xpath_interface.FindbyId(driver,Element_Location.CheckCode_id)
#     #checkcode=raw_input()
#     #element.send_keys(checkcode)
#     #time.sleep(5)
#     #click ¡°µÇÂ½¡± button
#   
'''find element by it's id property'''
def FindbyId(driver,Id):
    return driver.find_element_by_id(Id)

'''find element by it's xpath'''
def Findbyxptah(driver,path):
    return driver.find_element_by_xpath(path)

'''find element by it's class name property'''
def FindbyClassName(driver,name):
    return driver.find_element_by_class_name(name)

#find element by it's link text'''
def FindbyLinkText(driver,text):
    return driver.find_element_by_link_text(text)

#find elemens by it's class name property
def FindelementsbyClassName(driver,name):
    return driver.find_elements_by_class_name(name)

#find elemens by it's class name property
def FindelementsbyTagName(driver,name):
    return driver.find_elements_by_tag_name(name)



