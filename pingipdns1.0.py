import os
#ipport 需要手动输入大量IP地址和端口
#outuseip输出经过测试可用的的IP+端口
#代理获取地址  https://www.89ip.cn/ 如果可以直接从网址获取ip那就更好了
count=0
c=[]

f=open('ipport.txt','r')
line=f.readlines()

for a in line:
    a=a[:-1]
    a=a.replace(':',' ')
    c.append(a)
for b in c:
    cc=os.system('tcping -n 1 '+b)
    if cc==0:
        count+=1
        g = open('outuseip.txt', 'a')
        g.write(b+ '\n')
        g.close()
    else:
        pass


print('总共%d个参数，成功%d个参数'%(len(line),count))
