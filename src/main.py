#!/usr/bin/env python
import numpy as np
import cv2
import datetime
from matplotlib import pyplot as plt


def TimestampMillisec64():
    return int((datetime.datetime.utcnow() - datetime.datetime(1970, 1, 1)).total_seconds() * 1000) 


## bouncing circle
r = 10
x = r
y = r
dx = 5
dy = 5
xmax = 300
ymax = 200
up = 0
left = 0

#
# START
#

font = cv2.FONT_HERSHEY_SIMPLEX
cap = cv2.VideoCapture(0)
old_time = TimestampMillisec64()

while(True):
    now_time = TimestampMillisec64()
    try:
        fps = 1000.0 / (now_time - old_time)
    except:
        fps = 0
    old_time = now_time

    ret, f = cap.read()
    ymax, xmax, _ = f.shape
    gray = cv2.cvtColor(f, cv2.COLOR_BGR2GRAY)

    cv2.line(f,(0,ymax/2),(xmax,ymax/2),(255,255,255),5)
    cv2.rectangle(f,(0,0),(xmax,ymax),(0,0,255),5)
    cv2.circle(f,(x, y), r, (0,255,0), +5)
    cv2.putText(f,'fps: {:5.1f}'.format(fps),(0,ymax-10), font, 1, (200,255,155), 2, cv2.CV_AA)

    cv2.imshow('frame', f)
    if cv2.waitKey(1) & 0xFF == ord('q'):
	break

    if left:
        if x > r:
            x -= dx
        else:
            left = 0
    else:
        if x < xmax - r:
            x += dx
        else:
            left = 1

    if up:
        if y > r:
            y -= dy
        else:
            up = 0
    else:
        if y < ymax - r:
            y += dy
        else:
            up = 1

cap.release()
cv2.destroyAllWindows()
