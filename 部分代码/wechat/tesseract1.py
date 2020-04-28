try:
    from PIL import Image
except ImportError:
    import Image
#import pytesseract
import subprocess
from concurrent.futures import  ThreadPoolExecutor, wait, ALL_COMPLETED, FIRST_COMPLETED
# coding:utf-8
#-*- coding:utf-8 -*-
import os
import time
import numpy as np
from glob import glob
image_files = glob('/data/apps/wechat/*.*')
'''
sudo add-apt-repository ppa:alex-p/tesseract-ocr-devel
sudo apt-get update
sudo apt install tesseract-ocr
sudo apt install libtesseract-dev

'''


def runcmd(command,timeout=20):
 
    ret = subprocess.run(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,encoding="utf-8",timeout=timeout)
    return ret

def ocr(i):
    outstring = ""
    tesseract = '/usr/bin/tesseract'
    image_file = "/data/apps/wechat/screenshots/"+str(i)+".png"
    outfile = "/data/apps/wechat/moment_ocr/"+str(i)+""
    if not os.path.isfile(image_file):
        return
    try:
        runcmd(tesseract+" "+image_file + " " + outfile + " -l chi_sim+eng",100)
        print("finished:",outfile)
        #out_text = open(outfile+".txt", "r").read()
        #print(  "-------\n" )
        #print(image_file)
        #print(out_text)
        #outstring = out_text
        #outstring = outstring.replace(" ","")

        #fo.write(  "-------\n" )
        #fo.write( outstring + "\n" )
    except Exception as e:
        pass

if __name__ == '__main__':

    #pytesseract.pytesseract.tesseract_cmd = tesseract
    #print(pytesseract.image_to_string(Image.open('test.png')))
    pool = ThreadPoolExecutor(2)
    screenshots  = os.listdir("/data/apps/wechat/screenshots/")
    runcmd("rm /data/apps/wechat/moment.txt")

    fo = open("/data/apps/wechat/moment.txt", "w+")
    #fo.write("")
    all_task = []
    for fn in screenshots:
        cnt = fn.replace(".png","")
        
        all_task.append(pool.submit(ocr, (cnt)))
 
    wait(all_task, return_when=ALL_COMPLETED)

    print("finish")
    for fn in screenshots:
        #if not os.path.isfile(image_file):
        #    return
        cnt = fn.replace(".png","")
        outfile = "/data/apps/wechat/moment_ocr/"+str(cnt) +".txt"
        fout = open(outfile, "r")
        out_text = fout.read()
        fout.close()
        #print(outfile)
        #runcmd("cat "+outfile+ ">> /data/apps/wechat/moment.txt")
        fo.write(  "-------\n" )
        fo.write( out_text + "\n" )