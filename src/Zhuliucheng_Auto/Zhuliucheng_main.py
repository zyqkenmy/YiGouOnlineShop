#!C:\Python27  
#-*-coding:utf-8-*-


'''
Created on 2014年4月18日

@author: Fred
'''
import Xpath_interface
import Element_Location
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
import time
from selenium.webdriver.common.action_chains import ActionChains
import Common_Method
import sys
reload(sys)
#sys.setdefaultencoding('GBK')
    
def Generate_Order():  
    #base_url = "http://www.114yg.cn/userCenterAction.do?actions=intoUserLogin/"
    driver=Common_Method.Page_load(Element_Location.Base_url)
    WebDriverWait(driver,10).until(lambda  driver: Xpath_interface.Findbyxptah(driver,Element_Location.LoginXpath).is_displayed())
    #link to login page
    Common_Method.YiGou_login(driver)
    #鼠标悬停事件
    element=Xpath_interface.FindbyId(driver,Element_Location.Dianqi_id)
    Common_Method.Move_to_element(element, driver)   
    #click product 
    element=Xpath_interface.Findbyxptah(driver,Element_Location.weibolu_xpath).click()
    driver.implicitly_wait(30)
    #加入购物车
    element=Xpath_interface.Findbyxptah(driver,Element_Location.Shopping_xpath).click()
    #accept alert dialog
    time.sleep(1)
    element=Xpath_interface.FindbyClassName(driver,Element_Location.Alert_ClassName).click()
   
    #购物车
    #driver.implicitly_wait(30)
    driver.refresh()
    
    #鼠标触摸弹出购物车
    element=Xpath_interface.FindbyId(driver,Element_Location.ShopCard_id)
    Common_Method.Move_to_element(element, driver)
    time.sleep(2)
    WebDriverWait(driver,10).until(lambda  driver: Xpath_interface.Findbyxptah(driver,Element_Location.Bill_xpath).is_displayed())
    
    #去购物车结算
    #js="var q=document.getElementById('Cart'); q.style.display='block';"
    #driver.execute_script(js)
    #time.sleep(2)
    element=Xpath_interface.Findbyxptah(driver,Element_Location.Bill_xpath).click()
    time.sleep(1)
    driver.implicitly_wait(30)
    #结算形成订单
    element=Xpath_interface.FindbyId(driver,Element_Location.Goto_Billed_id).click()
    #输入手机号吗
    element=Xpath_interface.FindbyId(driver,Element_Location.Phone_number_id).send_keys("18623450251")
    element=Xpath_interface.FindbyId(driver,Element_Location.Generate_order_id).click()
    #选择翼支付
    element=Xpath_interface.Findbyxptah(driver,Element_Location.Yi_account_xpath).click()
    #立即支付
    element=Xpath_interface.FindbyId(driver,Element_Location.Order_pay_id).click()
    time.sleep(2)
    driver.close()

def Delete_order():
    #base_url = "http://www.114yg.cn/userCenterAction.do?actions=intoUserLogin/"
    driver=Common_Method.Page_load(Element_Location.Base_url)
    Common_Method.YiGou_login(driver)
    #进入我的翼页面
    element=Xpath_interface.FindbyClassName(driver, Element_Location.My_YiGou_ClassName).click()
    try:
       elements=Xpath_interface.FindelementsbyClassName(driver, Element_Location.Orders_className)
    except NoSuchElementException, e:  return False        
    if len(elements)=='1':
        Link_element=elements[0].find_element_by_link_text(Element_Location.Delete_order_Link_text.decode('GBK')).click()
        Xpath_interface.FindbyClassName(driver, Element_Location.Delete_ClassName).click()

    if len(elements)>1:
        for i in range(0,len(elements)):
            elements=Xpath_interface.FindelementsbyClassName(driver, Element_Location.Orders_className)
            Link_element=elements[0].find_element_by_link_text(Element_Location.Delete_order_Link_text.decode('GBK')).click()             
            Xpath_interface.FindbyClassName(driver, Element_Location.Delete_ClassName).click()

    driver.close()

def Bulk_purchase():
    #base_url = "http://www.114yg.cn/userCenterAction.do?actions=intoUserLogin/"
    driver=Common_Method.Page_load(Element_Location.Base_url)
    Common_Method.YiGou_login(driver)
    #点击批量采购链接
    element=Xpath_interface.FindbyId(driver, Element_Location.Bulk_purchase_id).click()
    #切换窗口
    all_handles=driver.window_handles
    now_handle=driver.current_window_handle
    for handle in all_handles:
        if handle!=now_handle:
            driver.switch_to_window(handle)
    #选择产品种类        
    Goodscatagory_elements=Xpath_interface.FindelementsbyClassName(driver, Element_Location.Goods_catagory_ClassName)
    Goods_elements=Xpath_interface.FindelementsbyClassName(Goodscatagory_elements[0],Element_Location.Goods_ClassName)
    link_elements=Xpath_interface.FindelementsbyTagName(Goodscatagory_elements[0],"a")
    link_elements[1].click()
    
    #立即购买按钮
    element=Xpath_interface.Findbyxptah(driver, Element_Location.Buy_Now_xpath).click()
    driver.implicitly_wait(30)
    element=Xpath_interface.FindbyId(driver,Element_Location.Phone_number_id).send_keys(Element_Location.Tianyi_username)
    element=Xpath_interface.FindbyId(driver,Element_Location.Generate_order_id).click()
    time.sleep(2)
    driver.close()
    driver.switch_to_window(now_handle)
    driver.close()
    
#Bulk_purchase()   
#Generate_Order()
#Delete_order()  