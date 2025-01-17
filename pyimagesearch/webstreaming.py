'''
https://pyimagesearch.com/2019/09/02/opencv-stream-video-to-web-browser-html-page/
PyImage/singlemotiondetector.py
'''
# import the necessary packages
# from webstreaming import SingleMotionDetector
from motion_detection.singlemotiondetector import SingleMotionDetector
from imutils.video import VideoStream
from flask import Response
from flask import Flask
from flask import render_template
import threading
import argparse
import datetime
import imutils
import time
import cv2


# initialize the output frame and a lock used to ensure thread-safe
# exchanges of the output frames (useful when multiple browsers/tabs
# are viewing the stream)
outputFrame = None
##  create a lock on Line 23 which will be used to ensure thread-safe behavior when updating the ouputFrame (i.e., ensuring that one thread isn’t trying to read the frame as it is being updated).
lock = threading.Lock()
# initialize a flask object
app = Flask(__name__)
# initialize the video stream and allow the camera sensor to
# warmup
#vs = VideoStream(usePiCamera=1).start()
vs = VideoStream(src=0).start()
### f you are using a USB webcam, you can leave the code as is.
### However, if you are using a RPi camera module you should uncomment Line 25 and comment out Line 26.
time.sleep(2.0)


@app.route("/")
def index():
	# return the rendered template
	return render_template("index.html")
### all it’s doing is calling the Flask render_template on our HTML file.

### next function is responsible for:

# Looping over frames from our video stream
# Applying motion detection
# Drawing any results on the outputFrame
# And furthermore, this function must perform all of these operations in a thread safe manner to ensure concurrency is supported.

def detect_motion(frameCount):
	# grab global references to the video stream, output frame, and
	# lock variables
	global vs, outputFrame, lock
	# initialize the motion detector and the total number of frames
	# read thus far
	md = SingleMotionDetector(accumWeight=0.1)
	total = 0
    
### Our detection_motion function accepts a single argument, frameCount, which is the minimum number of required frames to build our background bg in the SingleMotionDetector class:

### If we don’t have at least frameCount frames, we’ll continue to compute the accumulated weighted average.
### Once frameCount is reached, we’ll start performing background subtraction.
# Line 37 grabs global references to three variables:

# vs: Our instantiated VideoStream object
# outputFrame: The output frame that will be served to clients
# lock: The thread lock that we must obtain before updating outputFrame
# Line 41 initializes our SingleMotionDetector class with a value of accumWeight=0.1, implying that the bg value will be weighted higher when computing the weighted average.

# Line 42 then initializes the total number of frames read thus far — we\ll need to ensure a sufficient number of frames have been read to build our background model.

# From there, we\/ll be able to perform background subtraction.

# With these initializations complete, we can now start looping over frames from the camera:

    # loop over frames from the video stream
    
while True:
    # read the next frame from the video stream, resize it,
    # convert the frame to grayscale, and blur it
    frame = vs.read()
    frame = imutils.resize(frame, width=400)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (7, 7), 0)
    # grab the current timestamp and draw it on the frame
    timestamp = datetime.datetime.now()
    cv2.putText(frame, timestamp.strftime(
        "%A %d %B %Y %I:%M:%S%p"), (10, frame.shape[0] - 10),
        cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)
    		# if the total number of frames has reached a sufficient
		# number to construct a reasonable background model, then
		# continue to process the frame
    if total > frameCount:
        # detect motion in the image
        motion = md.detect(gray)
        # check to see if motion was found in the frame
        if motion is not None:
            # unpack the tuple and draw the box surrounding the
            # "motion area" on the output frame
            (thresh, (minX, minY, maxX, maxY)) = motion
            cv2.rectangle(frame, (minX, minY), (maxX, maxY),
                (0, 0, 255), 2)
    
    # update the background model and increment the total number
    # of frames read thus far
    md.update(gray)
    total += 1
    # acquire the lock, set the output frame, and release the
    # lock
    with lock:
        outputFrame = frame.copy()

# if the total number of frames has reached a sufficient
# number to construct a reasonable background model, then
# continue to process the frame
   
def generate():
	# grab global references to the output frame and lock variables
	global outputFrame, lock
	# loop over frames from the output stream
	while True:
		# wait until the lock is acquired
		with lock:
			# check if the output frame is available, otherwise skip
			# the iteration of the loop
			if outputFrame is None:
				continue
			# encode the frame in JPEG format
			(flag, encodedImage) = cv2.imencode(".jpg", outputFrame)
			# ensure the frame was successfully encoded
			if not flag:
				continue
		# yield the output frame in the byte format
		yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + 
			bytearray(encodedImage) + b'\r\n')

@app.route("/video_feed")
def video_feed():
	# return the response generated along with the specific media
	# type (mime type)
	return Response(generate(),
		mimetype = "multipart/x-mixed-replace; boundary=frame")
# check to see if this is the main thread of execution
if __name__ == '__main__':
	# construct the argument parser and parse command line arguments
	ap = argparse.ArgumentParser()
	ap.add_argument("-i", "--ip", type=str, required=True,
		help="ip address of the device")
	ap.add_argument("-o", "--port", type=int, required=True,
		help="ephemeral port number of the server (1024 to 65535)")
	ap.add_argument("-f", "--frame-count", type=int, default=32,
		help="# of frames used to construct the background model")
	args = vars(ap.parse_args())
	# start a thread that will perform motion detection
	t = threading.Thread(target=detect_motion, args=(
		args["frame_count"],))
	t.daemon = True
	t.start()
	# start the flask app
	app.run(host=args["ip"], port=args["port"], debug=True,
		threaded=True, use_reloader=False)
# release the video stream pointer
vs.stop()
