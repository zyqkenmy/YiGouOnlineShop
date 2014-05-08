#!C:\Python27  
#-*-coding:utf-8-*-

'''
Created on 2014年5月6日

@author: Fred
'''
import Zhuliucheng_Auto.Common_Method
import Zhuliucheng_Auto.Xpath_interface
import Zhuliucheng_Auto.Element_Location
from selenium.common.exceptions import NoSuchElementException
import sys
reload(sys)

comm_method=Zhuliucheng_Auto.Common_Method
element_location=Zhuliucheng_Auto.Element_Location
interface=Zhuliucheng_Auto.Xpath_interface

def Manager_Ship_Address():
    driver=comm_method.Page_load(element_location.Base_url)
    comm_method.YiGou_login(driver)
    #鼠标移动到我的翼购按钮事件
    try:
        element=interface.FindbyClassName(driver, element_location.My_YiGou_ClassName)
        comm_method.Move_to_element(element, driver)
        interface.FindbyLinkText(driver, element_location.My_address_link_text.decode("GBK")).click()
        driver.implicitly_wait(30)
        elements=interface.FindelementsbyClassName(driver, element_location.Common_Address_ClassName)
        if len(elements)==4:
            interface.FindbyLinkText(elements[0],element_location.Delete_Address_Link_Name.decode("GBK")).click()
            element=interface.FindbyClassName(driver,element_location.Alert_ClassName).click()  
            print "delete a user address"                       
        interface.FindbyId(driver, element_location.New_Add_address_bt_id).click()
    except NoSuchElementException, e: return False
    finally:
        driver.save_screenshot("D:\BaiduYunDownload\exception.png")
        #driver.quit()
        
    #选择省
    element=interface.FindbyId(driver, element_location.Province_Select_id)
    comm_method.Select_element(element)
    #选择市
    element=element=interface.FindbyId(driver, element_location.City_id)
    comm_method.Select_element(element)
    #选择地区
    element=element=interface.FindbyId(driver, element_location.Area_id)
    comm_method.Select_element(element)
    #详细地址
    element=interface.FindbyId(driver, element_location.Street_id).send_keys(element_location.Street_Detail_text.decode("GBK"))
    element=interface.FindbyId(driver, element_location.PostCode_id).send_keys(element_location.PostCode)
    element=interface.FindbyId(driver, element_location.Persion_Phone_id).send_keys(element_location.Phone_Num)
    element=interface.FindbyId(driver, element_location.Conntect_persion_id).send_keys(element_location.Persion_name.decode("GBK"))
    element=interface.FindbyClassName(driver,element_location.Save_Bt_ClassName).click()
    print "add a new address"
    driver.quit()
#Add_Ship_Address()

def Modify_Ship_address():
    driver=comm_method.Page_load(element_location.Base_url)
    comm_method.YiGou_login(driver)
    #鼠标移动到我的翼购按钮事件
    try:
        element=interface.FindbyClassName(driver, element_location.My_YiGou_ClassName)
        comm_method.Move_to_element(element, driver)
        interface.FindbyLinkText(driver, element_location.My_address_link_text.decode("GBK")).click()
        driver.implicitly_wait(30)
        elements=interface.FindelementsbyClassName(driver, element_location.Common_Address_ClassName)
        interface.FindbyLinkText(elements[0], element_location.Modify_Address_link_Name.decode("GBK")).click()
        element=interface.FindbyId(driver, element_location.Street_id).send_keys(element_location.Modify_Street_Detail_text.decode("GBK"))
        element=interface.FindbyClassName(driver,element_location.Save_Bt_ClassName).click()
        print "modify ship address:"+element_location.Modify_Street_Detail_text.decode("GBK")
    except NoSuchElementException, e: return False
    finally:
        driver.save_screenshot("D:\BaiduYunDownload\exception.png")
        driver.quit()
        
    driver.quit()
    
Modify_Ship_address()