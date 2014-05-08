#!C:\Python27  
#-*-coding:utf-8-*- 
# coding=gbk

'''
Created on 2014年4月19日

@author: Fred
'''
Base_url="http://www.114yg.cn/userCenterAction.do?actions=intoUserLogin/"

#天翼用户
Tianyi_UserID="txtUserID"
Tianyi_userPWD_id="txtPwd"
Tianyi_username="18916204759"
Tianyi_pwd="123465 "
#
Tianyi_login_bt_id="ibtn_Login"
#首页登陆链接按钮
LoginXpath="//*[@id='logindiv1']/a[1]"
#百事通用户
UserName="zyqkenmy"
Password="justfortest"
Besttong_id="tabE1"
User_id="username"
PWD_id="password"

#验证码验证信息
checkCode_checkInfo_id="errorHint"
#log random check Code
CheckCode_id="checkCode"

#login id
Login_id="login"

#登陆frame
Frame_id="udbLoginFrame"

#家用电器id 
Dianqi_id="4"
weibolu_xpath="//*[@id='sort']/div[2]/div/ul/li[3]/div[2]/div[1]/ul[2]/li[2]/a[1]"

#加入购物车按钮
Shopping_xpath="//*[@id='main']/div[4]/div[3]/div[3]/div/div/div[2]/div[5]/ul/li[1]/a"

#Alert xpath
Alert_ClassName="aui_state_highlight"

#购物车 id
ShopCard_id="viewCartBtn"

#结算按钮 path
Bill_xpath="//*[@id='Cart']/div[2]/div[2]/a" 

#购物车中结算按钮ID
Goto_Billed_id="goPay"

#预定人手机号码
Phone_number_id="reserMoblie"

#生成订单按钮
Generate_order_id="submit_order"

#支付按钮Id
Order_pay_id="ljzf"

#翼支账号按钮
Yi_account_xpath="/html/body/div[5]/div[3]/div[3]/div/div[2]/div[2]/span[1]/input"


'''
#delete ordre location
'''
My_YiGou_ClassName="more"

#订单的class 名称
Orders_className="history"

#删除订单链接
Delete_order_Link_text="删除订单"

#删除订单确定按钮class 名称
Delete_ClassName="aui_state_highlight"


'''Bulk_purchase location '''
#批量采购link id
Bulk_purchase_id="chanel_05"
#商品种类 class 名称
Goods_catagory_ClassName="floor"
#商品的classname
Goods_ClassName="main"

#立即购买按钮XPath
Buy_Now_xpath="//*[@id='f1']/div[2]/div[1]/div[2]/label[1]/img"


'''Add new address location '''
#收货地址连接文本
My_address_link_text="收货地址"

#新增 收货地址按钮id
New_Add_address_bt_id="addButton"

#省下拉框id
Province_Select_id="province"

#city id
City_id="city"

#area id
Area_id="area"

#详细地址id
Street_id="street"
Street_Detail_text="东城区薄荷路33号"
Modify_Street_Detail_text="这是修改后的地址"
#邮政编码id
PostCode_id="postcode"
PostCode="100000"
#收货人id
Conntect_persion_id="memberRecipient"
Persion_name="祝于强"

#联系人电话id
Persion_Phone_id="mobilePhone"
Phone_Num="13487908765"

#保存按钮class name
Save_Bt_ClassName="aui_state_highlight"

#普通地址ClassName
Common_Address_ClassName="address2"

#删除link 文本
Delete_Address_Link_Name="删除"

#修改link文本
Modify_Address_link_Name="修改"
#Html Tag Name
Select_option_tag="option"


''' Navigation location'''
#全国特产导航 id
National_specialty_id="chanel_02"

#礼品兑换导航id
Gift_Exchange_id="chanel_06"

#翼游id
Yi_Tour_id="chanel_08"

#中华老子号导航Id
China_Laozi="chanel_09"

#手机兑换id
Phone_Exchange_id="chanel_07"

