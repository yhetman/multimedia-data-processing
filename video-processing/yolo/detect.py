import cv2
#from darkflow.net.build import TFNet
from gluoncv import model_zoo, data, utils
import matplotlib.pyplot as plt
import numpy as np
import time
#options = {
# 'model': 'cfg/yolo.cfg',
# 'load': 'bin/yolov2.weights',
# 'threshold': 0.3   
#}
net = model_zoo.get_model('yolo3_darknet53_voc', pretrained=True)

#tfnet = TFNet(options)
cap = cv2.VideoCapture('../videos/IMG_0221.MOV')
colors=[tuple(255 * np.random.rand(3)) for i in range(5)]

while(cap.isOpened()):
    stime= time.time()
    ret, frame = cap.read()
    results = net.return_predict(frame)
    if ret:
        for color, result in zip(colors, results):
            tl = (result['topleft']['x'], result['topleft']['y'])
            br = (result['bottomright']['x'], result['bottomright']['y'])
            label = result['label']
            frame= cv2.rectangle(frame, tl, br, color, 7)
            frame= cv2.putText(frame, label, tl, cv2.FONT_HERSHEY_TRIPLEX, 1, (0,0,0), 2)
        cv2.imshow('frame', frame)
        print('FPS {:1f}'.format(1/(time.time() -stime)))
        if cv2.waitKey(1)  & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()
