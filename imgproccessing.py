import cv2
import numpy as np
from matplotlib import pyplot as plt

"""
notes

- open cv image shapes are (H,W,C)
    * read in with img.shape

"""
video = cv2.VideoCapture('recordings/output_Yubo_video_21.mp4')

# fps = video.get(cv2.CAP_PROP_FPS)
# total_frames = video.get(cv2.CAP_PROP_FRAME_COUNT)
# print(f'frames per second = {fps}')
# print(f'total frames = {total_frames}')


# video.set(cv2.CAP_PROP_POS_FRAMES,0)

ret, frame = video.read()
# print(frame)
# cv2.imshow('frame',frame)
# cv2.waitKey(0)
# cv2.imwrite('test_video_frame.png',frame)

i = 0
while ret:
    cv2.imwrite('test_video_frame_'+str(i)+'.png',frame)
    cv2.waitKey(0)
    i+=1
    ret, frame = video.read()



# video = cv2.VideoCapture('recordings/output_Yubo_video_21.mp4')

# # Initialize frame counter
# i = 0

# while True:
#     ret, frame = video.read()
#     if not ret:
#         break

#     # Save the frame
#     cv2.imwrite('test_video_frame_'+str(i)+'.png', frame)

#     # If it's the first frame, select the ROI
#     if i == 0:
#         r = cv2.selectROI(frame)
#         cv2.destroyAllWindows()

#     # Crop the frame to get the ROI
#     roi = frame[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]

#     # Calculate the mean color of each channel
#     mean_color = cv2.mean(roi)[:3]

#     # Calculate the Euclidean distance
#     euclidean_distance = np.sqrt(np.sum([np.square(mc - np.mean(mean_color)) for mc in mean_color]))

#     # Apply threshold (replace 'threshold_value' with your threshold)
#     _, thresholded = cv2.threshold(frame, euclidean_distance, 255, cv2.THRESH_BINARY)

#     # Save the thresholded frame
#     cv2.imwrite('thresholded_frame_'+str(i)+'.png', thresholded)

#     i += 1

# video.release()
# cv2.destroyAllWindows()

















""" 
define area by mouse
"""
# img = cv.imread('test_video_frame_0.png')
# cv.namedWindow('ROI') 

# r=cv.selectROI('ROI', img,False,False)
# imROI = img[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]
# cv.destroyWindow('ROI')
# cv.imshow("ROI", imROI)
# cv.waitKey(0)
# cv.destroyAllWindows()
# print(imROI)

"""
colour converter

"""

# img = cv2.imread('test_video_frame_20.png')

# hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
# cv2.imshow('HSV',hsv)
# cv2.waitKey(0)

# def select_lips(image):
    
#     cv2.namedWindow('Select Lips')
#     cv2.imshow('Select Lips', image)

#     selected_colour = None
#     def mouse_callback(event,x,y,flags, param):
#         nonlocal selected_colour

#         if event == cv2.EVENT_LBUTTONDOWN:
#             selected_colour = image[y,x]
#             print('selected colour (bgr):',selected_colour)

#     cv2.setMouseCallback('Select lips', mouse_callback)

#     while True:
#         key = cv2.waitKey(0)
#         if key ==27:
#             break
#     cv2.destroyAllWindows()

#     return selected_colour

# selected_colour = select_lips(img)
























