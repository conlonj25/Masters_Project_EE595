import cv2
import numpy as np
import time

# check opencv is working
print('Currently running OpenCV', cv2.__version__)

file_list = ['Videos/Hallway_002.avi','Videos/Hallway_003.avi','Videos/Shop_Corridor.mp4','Videos/Shop_Front.mp4','Videos/Student_Services.mp4']
title_list = ['Hallway_002','Hallway_003','Shop_Corridor','Shop_Front','Student_Services']

# Grayscale opeation
results = open('Grayscale Results.txt', "w+")
for file, title in zip(file_list,title_list):

    # open capture
    cap = cv2.VideoCapture(file)

    # get length of sequence
    cap_length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    cap_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    cap_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    start = time.time()
    for frame in range(cap_length):

        # read frame
        read_ok, frame = cap.read()

        # apply grayscale
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

        # display
        #cv2.imshow('Video',frame)
        # Exit on ESC
        #k = cv2.waitKey(1) & 0xff
        #if k == 27: break
    end = time.time()

    acc_time = end-start
    fps = cap_length/acc_time

    print(title, 'completed')
    results.write(title + '\n')
    results.write('==================================================\n')
    results.write('Frame Size: ' + str(cap_width) + 'x' + str(cap_height) + '\n')
    results.write('Number of Frames: ' + str(cap_length) + '\n')
    results.write('Sequence executed in: ' + str(round(acc_time,2)) + ' seconds\n')
    results.write('FPS: '+ str(round(fps,2)) + '\n')
    results.write('\n')

results.close()