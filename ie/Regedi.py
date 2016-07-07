#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#具体帮助请浏览https://support.microsoft.com/zh-cn/kb/182569

import winreg,os

#取消代理
def Proxy_disable():
    internet_path = r"Software\Microsoft\Windows\CurrentVersion\Internet Settings"
    key = winreg.OpenKey(key=winreg.HKEY_CURRENT_USER,
                         sub_key=internet_path, reserved=0,
                         access=winreg.KEY_SET_VALUE)
    winreg.SetValueEx(key, "ProxyEnable", 0, winreg.REG_DWORD, 0)
    winreg.SetValueEx(key, "ProxyOverride", 0, winreg.REG_SZ, "*.local")
    winreg.CloseKey(key)





# 1001     ActiveX 控件和插件：下载已签署的 ActiveX 控件
# 1004     ActiveX 控件和插件：下载未签署的 ActiveX 控件
# 1200     ActiveX 控件和插件：运行 ActiveX 控件和插件
# 1201     ActiveX 控件和插件：对没有标记为可安全执行脚本的 ActiveX 控件进行初始化和脚本运行
# 1208     ActiveX 控件和插件：允许以前未使用的 ActiveX 控件在没有提示的情况下运行
# 1209     ActiveX 控件和插件：允许脚本小程序
# 120A     ActiveX 控件和插件：ActiveX 控件和插件：覆盖每站点（基于域）ActiveX 限制
# 120B     ActiveX 控件和插件：覆盖每站点（基于域）ActiveX 限制
# 1405     ActiveX 控件和插件：对标记为可安全执行脚本的 ActiveX 控件执行脚本
# 2000     ActiveX 控件和插件：二进制和脚本行为
# 2201     ActiveX 控件和插件：ActiveX 控件自动提示
# 1406    通过域访问数据源
def change_Active(net=3):
    list = {"1001","1004","1200","1201","1208","1209","120A","120B","1405","2000","2201","1406"}
    internet_path = r"Software\Microsoft\Windows\CurrentVersion\Internet Settings\Zones" + "\\" + str(net)
    key = winreg.OpenKey(key=winreg.HKEY_CURRENT_USER,
                         sub_key=internet_path, reserved=0,
                         access=winreg.KEY_SET_VALUE)
    for li in list:
        winreg.SetValueEx(key, li, 0, winreg.REG_DWORD, 0)

    winreg.CloseKey(key)



    

# 可信站点,启用全部控件
# .NET Framework    2400=XAML 浏览器应用程序、2401=XPS 文档、2402=松散 XAML
# .NET Framework 相关组件   2007=带有清单的权限的组件、2004=运行未用 Authenticode 签名的组件、2001=运行已用 Authenticode 签名的组件
# ActiveX 控件和插件 见21行
# 脚本        1402=Java 小程序脚本、1400=活动脚本、1409=启用 XSS 筛选器（XP+IE6不存在此项）、1407=允许对剪贴板进行编程访问、2105=允许网站使用脚本窗口提示获得信息、2103=允许状态栏通过脚本更新
# 其他    1606=持续使用用户数据、1806= 加载应用程序和不安全文件、160A=将文件上载到服务器时包含本地目录路径、1607=跨域浏览窗口和框架、2100=启用 MIME 探查、2301=使用 SmartScreen 筛选器、1809=使用弹出窗口阻止程序、2101=特权较少的 Web 内容区域中的网站可以定位到该区域、1601=提交非加密表单数据、1406=通过域访问数据源、1802=拖放或复制和粘贴文件、1609=显示混合内容、1608=允许 META REFRESH、1206=允许 Microsoft 网页浏览器控件的脚本、2102=允许脚本初始化的窗口，不受大小或位置限制、2300=允许网页使用活动内容受限协议、2104=允许网站打开没有地址或状态栏的窗口、1804=在 IFRAME 中加载程序和文件、1A04=; 只存在一个证书时不提示进行客户端证书选择、1E05=软件频道权限、1800=软件频道权限
# 2600=启用 .NET Framework 安装程序
# 下载    1803=文件下载、2200=文件下载自动提示、1604=字体下载
# 1A00=登录
def change_believe(net=2):
    list={"2400","2401","2402","2007","2004","2001","1001","1004","1200","1201","1208","1209","120A","120B","1405","2000","2201","1406","1402","1400","1409","1407","2105","2103","1606","1806","160A","1607","2100","2301","2101","1809","1601","1406","1802","1609","1608","1206","2102","2104","1804","1A04","1E05","1800","2600","1803","2200","1604","1A00"}
    internet_path = r"Software\Microsoft\Windows\CurrentVersion\Internet Settings\Zones" + "\\" + str(net)
    key = winreg.OpenKey(key=winreg.HKEY_CURRENT_USER,
                         sub_key=internet_path, reserved=0,
                         access=winreg.KEY_SET_VALUE)
    for li in list:
        winreg.SetValueEx(key, li, 0, winreg.REG_DWORD, 0)

    winreg.CloseKey(key)




# 关闭保护模式(2和3)Internet域、受信任的站点域
def change_safe_module(net=3):
    internet_path = r"Software\Microsoft\Windows\CurrentVersion\Internet Settings\Zones" + "\\" + str(net)
    key = winreg.OpenKey(key=winreg.HKEY_CURRENT_USER,
                         sub_key=internet_path, reserved=0,
                         access=winreg.KEY_SET_VALUE)
    winreg.SetValueEx(key, "2500", 0, winreg.REG_DWORD, 3)
    winreg.CloseKey(key)


#修改internet安全级别,默认修改Internet 区change_safe_module域，级别中-高
# 0=我的电脑、1=本地 Intranet 区域、2=受信任的站点区域、3=Internet 区域、4=受限制的站点区域
# (12000=高、11500=中-高、11000＝中、10500＝中低、10000＝低、0=自定义)
def change_level(net=3, lev=0x11500):
    internet_path = r"Software\Microsoft\Windows\CurrentVersion\Internet Settings\Zones"+"\\" +str(net)

    # key = winreg.OpenKey(key=winreg.HKEY_CURRENT_USER,
    #                      sub_key=r"Software\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\3", reserved=0,
    #                      access=winreg.KEY_ALL_ACCESS)

    key = winreg.OpenKey(key=winreg.HKEY_CURRENT_USER,
                         sub_key=internet_path, reserved=0,
                         access=winreg.KEY_SET_VALUE)
    winreg.SetValueEx(key, 'CurrentLevel', 0, winreg.REG_DWORD, lev)
    winreg.CloseKey(key)


#注册表重新载入
def restart_explorer():
    kill_explorer = 'taskkill /f /im explorer.exe'
    start_explorer = 'start explorer.exe'
    os.system(kill_explorer)
    os.system(start_explorer)





if __name__ == '__main__':
    # Proxy_disable()
    # change_Active()
    # change_level()
    restart_explorer()
