# Using Android IP Webcam video .jpg stream (tested) in Python2 OpenCV3

import urllib2
import cv2
import numpy as np
import time
import requests
# Replace the URL with your own IPwebcam shot.jpg IP:port
url='http://192.168.31.10:4747'




while True:
    # Use urllib to get the image from the IP camera
    #img  = requests.get(url)

    #img = r.text
    img = urllib2.urlopen(url).read()
    # Numpy to convert into a array
    imgNp = np.array(bytearray(img),dtype=np.uint8)
    print (imgNp.shape)
    # Finally decode the array to OpenCV usable format ;) 
    img = cv2.imdecode(imgNp,-1)
	
	
	# put the image on screen
    print (img.shape)
    cv2.imshow('IPWebcam',img)
    
    #To give the processor some less stress
    #time.sleep(0.1) 

    # Quit if q is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
