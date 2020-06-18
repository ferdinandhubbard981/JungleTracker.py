import test_deep_league as DL
from ctypes import windll
user32 = windll.user32
user32.SetProcessDPIAware()
import PIL.ImageGrab
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.animation import FuncAnimation
import time
import cv2
import sys


def grab_frame():
    image = PIL.ImageGrab.grab()
    output = DL._main(image, "testjpg.png", "Graves")
    if output == "nochamp":
        print(output)
        # causes error which is caught

    return output


firstappearance = False
count = 0

ax1 = plt.subplot(111)
while firstappearance == False:
    count += 0.1
    failed = False
    try:
        im1 = ax1.imshow(grab_frame())
        print("jungler appeared")
    except :
        time.sleep(0.1)
        print("no first appearance of jungler" + str(count))
        print(sys.exc_info())
        failed = True
    if failed == False:
        firstappearance = True





def update(i):
    try:
        im1.set_data(grab_frame())

    except TypeError:
        print("jungler not there")

if __name__ == "__main__":

    animation = FuncAnimation(plt.gcf(), update, interval = 1000)
    plt.show()
