# encoding=utf-8
import sys
sys.path.append('../')

import jieba
import jieba.analyse
from optparse import OptionParser
import urllib
import urllib.request
import requests

import os 
import subprocess
import time
import datetime

import socket,struct,fcntl
 
def get_ip(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(s.fileno(), 0x8915, struct.pack('256s', bytes(ifname[:15],'utf-8')))[20:24])

ip = "hayoou.com"
try:
    ip = get_ip("wlan0")
    ip2 = get_ip("eth0")
    ip=ip2
except Exception as e:
    pass

print("ip:",ip)
#exit()      
ignorlist = ["朋友圈","天前","昨天","微信","每节","总活","汴昏","每入","小时","分钟"]
max_files = 1500
user="orangepi4_1"
withWeight = True
topK = 500
path = '/data/apps/wechat/'

ignordict = {}
for w in ignorlist:
    ignordict[w] = 1

'''
content = "你好好好asdfashfiuw在哪里好"
print(content.count("好" ))
print(len(content))
print(content.count("好" ,0,len(content)))
'''

def post(url,values):
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    #values = {'moment_result' : msg}
    headers = { 'User-Agent' : user_agent ,'Content-Type':'application/x-www-form-urlencoded'}

    #requests.post(url,values,headers)
    data = urllib.parse.urlencode(values).encode('utf-8')
    req = urllib.request.Request(url,data,headers)
    response = urllib.request.urlopen(req)
    the_page = response.read()
    return the_page.decode('UTF8')

def is_all_chinese(strs):
    for _char in strs:
        if not '\u4e00' <= _char <= '\u9fa5':
            return False
    return True

USAGE = "usage: python extract_tags_with_weight.py [file name] -k [top k] -w [with weight=1 or 0]"
'''
parser = OptionParser(USAGE)
parser.add_option("-k", dest="topK")
parser.add_option("-w", dest="withWeight")
opt, args = parser.parse_args()

if len(args) < 1:
    print(USAGE)
    sys.exit(1)

file_name = args[0]

if opt.topK is None:
    topK = 500
else:
    topK = int(opt.topK)
'''

file_name= path +"moment.txt"
moment_tags_file = path +"moment_tags.txt"

moment_tags_dict = {}
with open(moment_tags_file, 'r') as f:
    for line in f:
        #print(line)
        line =  line.replace("\n","")
        moment_tags_dict[line]=1

print("moment_tags_dict len",len(moment_tags_dict))
content = ""
'''
try:
    content = open(file_name, 'r').read()
except Exception as e:
    pass
'''
content0 = content
content0_pictures_text = {} #content0.split("-------\n")
content = content.replace("\n","")
content = content.replace("-------","\n")
yestoday_moment = 0
for i in range(max_files):
    try:
        content1 = open(path +"moment_ocr/"+str(i)+".txt", 'r').read()
        #print(path +"/moment_ocr/"+str(i)+".txt",content)
        '''
        content1 = content1.replace("\n!","\n")
        content1 = content1.replace("\n:","\n")
        content1 = content1.replace("\n：","\n")
        content1 = content1.replace("\n！","\n")
        content1 = content1.replace("\n{","\n")
        content1 = content1.replace("\n|","\n")
        '''
        content1  = content1.replace("\n","")
        if content1.find("2天前")!= -1 :
            yestoday_moment += 1
            print("yestoday_moment",yestoday_moment)
        else
            yestoday_moment = 0

        if yestoday_moment > 10:
            break

        content0_pictures_text[i] = content1
        print(content0_pictures_text[i])
        if content0 =="":
            content += content0_pictures_text[i]+"\n"
    except Exception as e:
        pass

content0 = content

tags = jieba.analyse.extract_tags(content, topK=topK, withWeight=withWeight)
new_word_add =""
outstringall = ""
outstring_csv = ""
print("len(content):",len(content))
upload_picture_ids = []
for tag in tags:
    word = tag[0]
    weight = tag[1]
    count = content.count(word )
    pictures = 0
    picture_ids = ""
    for i in range(len(content0_pictures_text)):
        if content0_pictures_text[i].count(word) > 0:
            picture_ids += str(i) + ","
            upload_picture_ids.append(str(i))

    new_word =0
    new_word_s = ""
    if is_all_chinese(word) or len(word)>2:
        try:
            t= moment_tags_dict[word]
        except Exception as e:
            new_word =1
            new_word_s ="新词"
            new_word_add += word +"\n"
            moment_tags_dict[word] = 1

        try:
            t = ignordict[word]
        except Exception as e:
            outstring = "%s\t\t  次数：%s  \t\t %s \t\t 权重: %f" % (word,count,new_word_s,weight)
            print(outstring)
            outstring = "%s \t 次数：%s  \t %s \t 权重： %f \t 图片：%s " % (word,count,new_word_s,weight,picture_ids)
            outstringall += outstring +"\n"
            outstring = "%s , 次数, %s , %s , 权重, %f , 图片：%s " % (word,count,new_word_s,weight,picture_ids)
            outstring_csv += outstring +"\n"

#open(moment_tags_file, 'a+').write(new_word_add)
ftags= open(moment_tags_file, 'w')
for w in moment_tags_dict:
    ftags.write(w+"\n")

open("moment_result.txt", 'w').write(outstringall)
open("moment_result.csv", 'w').write(outstring_csv)

print("结果写入：/data/apps/wechat/moment_result.csv")

def runcmd(command,timeout=20):
    #print(command)
    ret = subprocess.run(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,encoding="utf-8",timeout=timeout)
    return ret

def adb_cmd(cmd1,device,cmd):
    return runcmd(["adb  -s "+device+ " "+cmd1+" "+cmd])

devicesret = runcmd(["adb devices" ])#
device = "6QDDU20113008223"

if devicesret.returncode == 0:
    devices = devicesret.stdout
    if  len(devices.split("\n")) > 2 :
        device = devices.split("\n")[1].split("\t")[0]
        print("device:",device)
        if device =="":
            exit()
    else:
        exit()
else:
    exit()
    
runcmd(["adb start-server" ])#
adb_cmd("push",device,"/data/apps/wechat/moment_result.txt /sdcard/wechat/moment_result.txt")
adb_cmd("push",device,"/data/apps/wechat/moment_result.csv /sdcard/wechat/moment_result.csv")

try:
    values = {'moment_result' : outstringall}
    post("http://hayoou.com/minizhiku/wechat/recv.php?user="+user,values)
    values = {"content":content0}
    post("http://hayoou.com/minizhiku/wechat/recv.php?user="+user,values)
    values = {'moment_result' : outstringall}
    post("http://127.0.0.1:81/minizhiku/wechat/recv.php?user="+user,values)
    values = {"content":content0}
    post("http://127.0.0.1:81/minizhiku/wechat/recv.php?user="+user,values)

except Exception as e:
    #print(e)
    pass


#gen html
post("http://127.0.0.1:81/minizhiku/wechat/recv.php?user="+user+"&gen=1",{})

print("链接：http://"+ip+":81/minizhiku/wechat/recv.php?user="+user+"&gen=1")

html = open("/var/www/hayoou/minizhiku/wechat/result/moment_result-"+user+".html", 'r').read()
html = html.replace("./moment_pics.php","http://"+ip+":81/minizhiku/wechat/moment_pics.php")
open("/var/www/hayoou/minizhiku/wechat/result/moment_result.html", 'w').write(html)
adb_cmd("push",device,"/var/www/hayoou/minizhiku/wechat/result/moment_result.html /sdcard/wechat/moment_result.html")

print("正在写入图片")

for ids in upload_picture_ids:
    pic = open("/data/apps/wechat/screenshots/"+ids+".png", 'rb').read()
    values = {'pic' : pic,'filename' : ids+".png"}
    post("http://hayoou.com/minizhiku/wechat/recv.php?user="+user,values)
    #post("http://127.0.0.1:81/minizhiku/wechat/recv.php?user="+user,values)
    runcmd(["cp /data/apps/wechat/screenshots/"+ids+".png  /var/www/hayoou/minizhiku/wechat/result/screenshots/"+user+"-"+ids+".png" ])#
    #print(ids)
    print(".",end='')

'''
with  open(fname, "r+") as f:
    for line in f:
'''
