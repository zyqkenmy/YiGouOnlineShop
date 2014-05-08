#!C:\Python27  
#-*-coding:utf-8-*-

'''
Created on 2014Äê4ÔÂ22ÈÕ

@author: Fred

'''
import sys
sys.path.append('D:\\GitHub\\YiGouOnlineShop\\src\Manage_Shipping_Address')
import unittest
import Zhuliucheng_main
import Manage_Shipping_Address
from src.Manage_Shipping_Address.ManageShippingAddress import *

class Test(unittest.TestCase):
    
    def test_Generate_Order(self):
        Zhuliucheng_main.Generate_Order()
        pass
    def test_zDelete_order(self):
        Zhuliucheng_main.Delete_order()
        pass
    def test_Bulk_purchase(self):
        Zhuliucheng_main.Bulk_purchase()
        
    def test_Add_Ship_Address(self):
        MAdd_Ship_Address();
        
    def test_Modify_Ship_Address(self):
        Modify_Ship_address();
    


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()