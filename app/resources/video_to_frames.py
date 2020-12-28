from __future__ import absolute_import
# pip install opencv-contrib-python
import cv2
import os
from VideotoTextSummarization.app.utils.config import Config


def video_to_frames(path):
    try:
        try:
            cap = cv2.VideoCapture(path)

            # creating a folder named data
            if not os.path.exists('frames'):
                os.makedirs('frames')

            # if not created then raise error
        except OSError as e:
            cap = None
            print('Error: Creating directory of frames' + str(e))

        # frame
        currentframe = 0

        while True:

            # reading from frame
            ret, frame = cap.read()

            if ret:
                # if video is still left continue creating images
                name = Config.Directories.SAVE_FRAMES_DIRECTORY + str(currentframe) + '.jpg'
                print('Creating...........' + name)

                # writing the extracted images
                cv2.imwrite(name, frame)

                # increasing counter so that it will
                # show how many frames are created
                currentframe += 1
            else:
                break

        # Release all space and windows once done
        cap.release()
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    except Exception as e:
        print('Error:  Converting video to frames' + str(e))


if __name__ == "__main__":
    video_to_frames(path=Config.Directories.VID_PATH)
