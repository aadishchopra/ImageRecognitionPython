#set environment 
import kickstart
#

from PIL import Image
import numpy as np

i=Image.open('D:/Projects/Python/ImageRecognition/images/dot.png')
iar=np.asarray(i)
print(iar)


