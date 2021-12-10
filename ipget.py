import os
import tkinter
import requests as req
import re
import time
import requests


window=tkinter.Tk()
window.geometry('800x600')
window.title('获取可用的代理地址')

#我尝试一次，不用安装tcping也可以
# tcping_get='https://download.elifulkerson.com//files/tcping/0.39/tcping.exe'
# r=requests.get(tcping_get)
# with open('C:\Windows\System32','wb')as f:
#     f.write(r.content)


def get_ip():
    #清除窗口
    text.delete('0.0',tkinter.END)
    text.update()

    iplist = []
    c = []
    #刷新text显示
    text.insert(tkinter.INSERT,'获取IP中\n')
    text.update()
    #获取IP网址元素
    url = 'https://www.89ip.cn/tqdl.html?num=60&address=%E9%9F%A9%E5%9B%BD&kill_address=&port=&kill_port=&isp='
    r = req.get(url)
    r = r.text
    #提取元素
    pattern = r'([\d]{1,3}\.[\d]{1,3}\.[\d]{1,3}\.[\d]{1,3}\:[\d]{1,5})'
    d = re.findall(pattern, r)
    text.insert(tkinter.INSERT,'获得%d个可用ip\n'%len(d))
    text.update()
    #去掉 IP和端口间的 ：
    for a in d:
        a=a.replace(':',' ')
        c.append(a)

    text.insert(tkinter.INSERT, '测试可用的ip中。。。。。。\n')
    text.update()
    for b in c:
        start=time.time()
        #测试ip+端口是否可用
        test_ip=os.system('tcping -n 1 '+b)
        if test_ip==0:
            now=time.time()
            #ct是运行时间
            ct=int((now-start)*1000)
            print(ct)
            text.insert(tkinter.INSERT, b+' ok,'+str(ct)+'ms\n')
            text.update()
            #储存列表没有作用
            iplist.append(b)
        else:
            pass

    text.insert(tkinter.INSERT, '测试结束\n')
    text.update()
    return iplist

#窗口 和按键
text=tkinter.Text(window,height=40,width=100)
text.pack(anchor='nw')
tkinter.Button(window,text='点我获取ip地址' ,command=get_ip).pack(anchor='nw')


window.mainloop()