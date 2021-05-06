import datetime

import cv2
import numpy as np
from PIL import ImageGrab, Image
from win32api import GetSystemMetrics
import win32gui
import ctypes

ctypes.windll.user32.SetProcessDPIAware() # for DPI scaling -- needed for mouse pointer

imCursor = Image.open('cursor.png')
width = GetSystemMetrics(0)
height = GetSystemMetrics(1)
time_stamp = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
#for h264 use mkv instead of mp4
#file_name = f'{time_stamp}.mp4'
file_name = f'{time_stamp}.mkv'
#fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
# For Compression use h264 instead of mp4
# To add the H264 codec download 'openh264-1.8.0-win64msvc.dll.bz2' from
# https://github.com/cisco/openh264/releases/tag/v1.8.0.
# Extract the file and move the extracted DLL to the same directory as your python file.
# OpenCV should now be able to find the DLL and load the H264 codec.

fourcc = cv2.VideoWriter_fourcc('H', '2', '6', '4')
captured_video = cv2.VideoWriter(file_name, fourcc, 20.0, (width, height))

print(width)
print(height)


while True:
    img = ImageGrab.grab(bbox=(0, 0, width, height))
    curX, curY = win32gui.GetCursorPos()
    img.paste(imCursor, box=(curX, curY), mask=imCursor)
    img_np = np.array(img)
    frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)

    cv2.namedWindow("Screen Capture", cv2.WINDOW_NORMAL)  # Create a named window
    cv2.resizeWindow("Screen Capture", 10, 10)  # Move it to (0,0)
    cv2.imshow("Screen Capture", frame)

    #cv2.imshow("Screen Capture", frame)
    captured_video.write(frame)
    if cv2.waitKey(10) & 0Xff == ord('q'):
        break

cv2.destroyAllWindows()