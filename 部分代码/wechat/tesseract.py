try:
    from PIL import Image
except ImportError:
    import Image
#import pytesseract
import subprocess
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

if __name__ == '__main__':

    outstring = ""
    tesseract = '/usr/bin/tesseract'
    #pytesseract.pytesseract.tesseract_cmd = tesseract
    #print(pytesseract.image_to_string(Image.open('test.png')))


    fo = open("/data/apps/wechat/moment.txt", "w")
    for i in range(2000):
        image_file = "/data/apps/wechat/screenshots/"+str(i)+".png"
        if not os.path.isfile(image_file):
            continue

        outfile = "/data/apps/wechat/moment_ocr/"+str(i)+""
        try:
            runcmd(tesseract+" "+image_file + " " + outfile + " -l chi_sim+eng",100)
            out_text = open(outfile+".txt", "r").read()
            print(  "-------\n" )
            print(image_file)
            print(out_text)
            outstring = out_text
            outstring = outstring.replace(" ","")

            fo.write(  "-------\n" )
            fo.write( outstring + "\n" )
        except Exception as e:
            pass

