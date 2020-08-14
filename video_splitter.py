import cv2
import os
import sys

# 0. CV_CAP_PROP_POS_MSEC Current position of the video file in milliseconds.
# 1. CV_CAP_PROP_POS_FRAMES 0-based index of the frame to be decoded/captured next.
# 2. CV_CAP_PROP_POS_AVI_RATIO Relative position of the video file
# 3. CV_CAP_PROP_FRAME_WIDTH Width of the frames in the video stream.
# 4. CV_CAP_PROP_FRAME_HEIGHT Height of the frames in the video stream.
# 5. CV_CAP_PROP_FPS Frame rate.
# 6. CV_CAP_PROP_FOURCC 4-character code of codec.
# 7. CV_CAP_PROP_FRAME_COUNT Number of frames in the video file.
# 8. CV_CAP_PROP_FORMAT Format of the Mat objects returned by retrieve() .
# 9. CV_CAP_PROP_MODE Backend-specific value indicating the current capture mode.
# 10. CV_CAP_PROP_BRIGHTNESS Brightness of the image (only for cameras).
# 11. CV_CAP_PROP_CONTRAST Contrast of the image (only for cameras).
# 12. CV_CAP_PROP_SATURATION Saturation of the image (only for cameras).
# 13. CV_CAP_PROP_HUE Hue of the image (only for cameras).
# 14. CV_CAP_PROP_GAIN Gain of the image (only for cameras).
# 15. CV_CAP_PROP_EXPOSURE Exposure (only for cameras).
# 16. CV_CAP_PROP_CONVERT_RGB Boolean flags indicating whether images should be converted to RGB.
# 17. CV_CAP_PROP_WHITE_BALANCE Currently unsupported
# 18. CV_CAP_PROP_RECTIFICATION Rectification flag for stereo cameras (note: only supported by DC1394 v 2.x backend currently)


path = r'E:\Download\pubg'
result_folder = os.path.join(path, 'result')
SECONDS     = 15
FIRST_FRAME = 2
LAST_SECOND = -10

name_of_file = os.listdir(path)
name_of_videos = []
for file in name_of_file:
    if file.endswith('.mp4'):
        name_of_videos.append(file)

if len(name_of_videos) == 0:
    print('videos not found')
    print('only: mp4, ...')
    sys.exit(1)

if not os.path.isdir(result_folder):
    os.mkdir(result_folder)

for video in name_of_videos:
    cap = cv2.VideoCapture(os.path.join(path, video))
    name_video = video.split('.')[0]

    fps    = int(cap.get(cv2.CAP_PROP_FPS))
    widht  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    num_frame = FIRST_FRAME

    if cap.isOpened():
        print(video + ' | fps: ' + str(fps) + ', frame count: ' + str(frame_count) + ', shape: ' + str(widht) + 'x' + str(height))

    while cap.isOpened():
        frame_no = num_frame * SECONDS * 1000
        if frame_no > (frame_count / fps - LAST_SECOND) * 1000:
            break

        cap.set(cv2.CAP_PROP_POS_MSEC, frame_no)
        ret, frame = cap.read()
        if not ret:
            break

        name_img = os.path.join(result_folder, name_video + str(num_frame) + '.png')
        cv2.imwrite(name_img, frame)

        print('\r', end='')
        print(str(int(round(frame_no / ((frame_count / fps - LAST_SECOND) * 1000) * 100))) + '%',  end='')

        num_frame += 1

    print('\r', end='')
    print('image count ' + str(num_frame - 1))
    print('')

    cap.release()

print('Well done!')
