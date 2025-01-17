''' OpenCV - Stream video to web browser/HTML page
PyImage
https://pyimagesearch.com/2019/09/02/opencv-stream-video-to-web-browser-html-page/
'''
# import the necessary packages
import numpy as np
import imutils
import cv2
print(imutils.__version__)
print(cv2.__version__)
print(np.__version__)
class SingleMotionDetector:
	import imutils
	import cv2
	print(imutils.__version__)
	print(cv2.__version__)
	import numpy as np
	print(np.__version__)
	def __init__(self, accumWeight=0.5):
		# store the accumulated weight factor
		self.accumWeight = accumWeight
		# initialize the background model
        # The larger accumWeight is, the less the background (bg) will be factored in the weighted average
		self.bg = None
 
	def update(self,image):
		import imutils
		import cv2
		print(imutils.__version__)
		print(cv2.__version__)
		import numpy as np
		print(np.__version__)
        # if the background model is None, initialize it
        ##  Implying that update has never been called), we simply store the bg frame
		if self.bg is None:
			self.bg = image.copy().astype("float")
			return
        # update the background model by accumulating the weighted
        # average
		cv2.accumulateWeighted(image, self.bg, self.accumWeight)
        # Otherwise, we compute the weighted average between the input frame, the existing background bg, and our corresponding accumWeight factor.

        # Given our background bg we can now apply motion detection via the detect method:
	def detect(self, image, tVal=25):   ## tVal: The threshold value used      mark a particular pixel as “motion” or not
		import cv2,numpy as np,imutils
  # compute the absolute difference between the background model
		# and the image passed in, then threshold the delta image
		delta = cv2.absdiff(self.bg.astype("uint8"), image)## diff between image and background
		thresh = cv2.threshold(delta, tVal, 255, cv2.THRESH_BINARY)[1]
		# perform a series of erosions and dilations to remove small
		# blobs
		thresh = cv2.erode(thresh, None, iterations=2)
		thresh = cv2.dilate(thresh, None, iterations=2)
        # find contours in the thresholded image and initialize the
		# minimum and maximum bounding box regions for motion
		cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
			cv2.CHAIN_APPROX_SIMPLE)
		cnts = imutils.grab_contours(cnts)
		(minX, minY) = (np.inf, np.inf)
		(maxX, maxY) = (-np.inf, -np.inf)
#   Then initialize two sets of bookkeeping variables to keep track of the location where any motion is contained (Lines 40 and 41). These variables will form the “bounding box” which will tell us the location of where the motion is taking place.

# The final step is to populate these variables (provided motion exists in the frame
        # if no contours were found, return None
		if len(cnts) == 0:
			return None
		# otherwise, loop over the contours
		for c in cnts:
			# compute the bounding box of the contour and use it to
			# update the minimum and maximum bounding box regions
			(x, y, w, h) = cv2.boundingRect(c)
			(minX, minY) = (min(minX, x), min(minY, y))
			(maxX, maxY) = (max(maxX, x + w), max(maxY, y + h))
		# otherwise, return a tuple of the thresholded image along
		# with bounding box
		return (thresh, (minX, minY, maxX, maxY))           