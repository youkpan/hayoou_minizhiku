import os 
import subprocess
import time
import datetime

screenshots_cnt = 300

def runcmd(command,timeout=20):
    #print(command)
    ret = subprocess.run(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,encoding="utf-8",timeout=timeout)
    '''
    if ret.returncode == 0:
        print("success:",ret)
    else:
        print("error:",ret)
	'''

    return ret

def adb_cmd(cmd1,device,cmd):
	return runcmd(["adb  -s "+device+ " "+cmd1+" "+cmd])

runcmd(["adb start-server" ])#
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
fname =  "/data/apps/wechat/getting_moment"
if os.path.isfile(fname):
	exit()
fo = open(fname, "a+")
fo.write(  "1\n" )
fo.close()
try:
#am force-stop com.tencent.mm","sleep 1","am start -n com.tencent.mm/.plugin.sns.ui.SnsUserUI 
# --ei sns_source 0 --ez Contact_NeedShowChangeRemarkButton false  -e sns_title  moment -e sns_userName  
#"+wxid+" -e sns_nickName  "+wxid+" -e sns_signature  test -e Contact_User  "+wxid+" --ez Contact_NeedShowChangeSnsPreButton false -e  Contact_Mobile_MD5 \"\"",
#read all
#am force-stop com.tencent.mm","sleep 1","am start -n com.tencent.mm/.plugin.sns.ui.SnsTimeLineUI
#runcmd(["adb -s "+device+" shell am force-stop com.tencent.mm;sleep 3;am start -n com.tencent.mm/.plugin.sns.ui.SnsTimeLineUI" ])
	starttime = datetime.datetime.now()
	dumpsys_ret = adb_cmd("shell",device, "dumpsys window displays")
	width = 1080
	height = 1920
	#init=1080x2340

	if len(dumpsys_ret.stdout.split("\n"))>3 :
		display = dumpsys_ret.stdout.split("\n")[2].split("=")[1].split(" ")[0]
		width = int(display.split("x")[0])
		height = int(display.split("x")[1])

	print("device width:",width,"height",height)
	adb_cmd("shell",device,"mkdir -p /sdcard/wechat/screenshots")
	runcmd(["mkdir /data/apps/wechat/screenshots -p"])
	runcmd(["rm /data/apps/wechat/screenshots/* -rf"])

	for i in range(screenshots_cnt):
		print("第 ",i,"张 截图" ,("%2.2f")%(i/screenshots_cnt*100),"%")
		adb_cmd("shell",device,"input swipe 1 "+str(int((1-300/2100)*height)) + " 1 "+str(int((300/2100)*height))+" 1000")
		time.sleep(1)
		adb_cmd("shell",device,"/system/bin/screencap -p /sdcard/wechat/screenshots/t.png")
		adb_cmd("shell",device,"cp /sdcard/wechat/screenshots/t.png  /sdcard/wechat/screenshots/"+str(i)+".png")
		adb_cmd( "pull",device,"/sdcard/wechat/screenshots/t.png /data/apps/wechat/screenshots/"+str(i)+".png ")

	#lock screen
	adb_cmd("shell",device,"input keyevent 26")
	print("识别文字中。。 大约需要：",72 *screenshots_cnt,"秒")
	runcmd(["rm /data/apps/wechat/moment_ocr/* "] )
	runcmd(["cd /data/apps/chinese_ocr ;py3 wechat_OCR.py"],timeout=100 *screenshots_cnt	)
	 
except Exception as e:
	print(e)
except KeyboardInterrupt as e:
	print(e)


runcmd(["py3 process_moment.py -k500 -w1"])


runcmd(["adb start-server" ])#
adb_cmd("push",device,"/data/apps/wechat/moment_result.txt /sdcard/wechat/moment_result.txt")

print("完成！")

runcmd(["rm  "+fname] )
