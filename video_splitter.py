import cv2
import os
import sys
#import pkg_resources.py2_warn


name_of_file = os.listdir()
name_of_videos = []
for file in name_of_file:
    if file.find(".mp4"):
        name_of_videos.append(file)
        
if len(name_of_videos) == 0:
    print("videos not found")
    print("only: mp4, ...")
    sys.exit(1)
    
    

for video in name_of_videos:
    cap = cv2.VideoCapture(video)
    name_folder = video.split(".")[0]
    
    if not os.path.isdir(name_folder):
        os.mkdir(name_folder)
   
        fps = int(cap.get(cv2.CAP_PROP_FPS))
        widht = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        
        
        print(video + " | fps: " + str(fps) + ", frame count: " + str(frame_count) + ", shape: " + str(widht) + "x" + str(height))
        num_frame = 0

        while(cap.isOpened()):
            ret, frame = cap.read()
            if not ret:
                break
    
            if num_frame % (fps * 2) == 0:
                cv2.imwrite(name_folder + "/frame_" + str(int(num_frame / (fps * 2) + 1)) + ".png", frame)
                
                percent_frames = 100 / frame_count
                
                print('\r', end = '')
                print(str(int(percent_frames * num_frame)) + "%",  end = '')
        
            num_frame += 1
        
        
        print('\r', end = '')
        print("image count " + str(int(num_frame / (fps * 2) + 1)))
        print("")
    else:
        print("folder already exists: " + name_folder)
        print("")
    
cap.release()
#print("press any button to close")