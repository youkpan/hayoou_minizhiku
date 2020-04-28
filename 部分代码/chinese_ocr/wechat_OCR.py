# coding:utf-8
#-*- coding:utf-8 -*-
import os
import ocr
import time
import shutil
import numpy as np
from PIL import Image
from glob import glob
image_files = glob('/data/apps/wechat/*.*')


if __name__ == '__main__':
    result_dir = './test_result'
    if os.path.exists(result_dir):
        shutil.rmtree(result_dir)
    os.mkdir(result_dir)

    outstring = ""
    fo = open("/data/apps/wechat/moment.txt", "w")
    for i in range(1000):
        image_file = "/data/apps/wechat/screenshots/"+str(i)+".png"
        focr = open("/data/apps/wechat/moment_ocr/"+str(i)+".txt", "w")
        try:
            image = np.array(Image.open(image_file).convert('RGB'))
        except Exception as e:
            continue
        t = time.time()
        result, image_framed = ocr.model(image)
        #output_file = os.path.join(result_dir, image_file.split('/')[-1])
        #Image.fromarray(image_framed).save(output_file)
        print("it took {:.3f}s".format(time.time() - t))
        print("\nRecognition Result:\n")

        fo.write(  "-------\n" )
        for key in result:
            print(result[key][1])
            outstring = result[key][1]
            outstring = outstring.replace(" ","")
            fo.write( outstring +"\n" )
            focr.write( outstring +"\n" )

        try:
            focr.close()
        except Exception as e:
            pass
        