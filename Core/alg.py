import os
import matplotlib.image as mpimg
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
from blind_watermark import WaterMark


def calculate(pic):
    bwm1 = WaterMark(password_img=1, password_wm=1)
    bwm1.read_img(pic)
    wm = "@guofei9987 开源万岁！"
    bwm1.read_wm(wm, mode="str")
    bwm1.embed("output/embedded.png")
    len_wm = len(bwm1.wm_bit)
    # print('Put down the length of wm_bit {len_wm}'.format(len_wm=len_wm))

    # 作者：幼鹰me
    # 链接：https: // www.zhihu.com / question / 50735753 / answer / 3102078277
    # 来源：知乎
    # 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
