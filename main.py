from pupil_apriltags import Detector
import cv2
  
# define a video capture object
vid = cv2.VideoCapture(0)
  
while(True):
	#Capture frame from camera
	ret, frame = vid.read()
  
	formatFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY);

	at_detector = Detector(
		families='tag16h5',
  		nthreads=1,
   		quad_decimate=1.0,
   		quad_sigma=0.0,
   		refine_edges=1,
   		decode_sharpening=0.25,
   		debug=0
	)

	try:
		detectedTags = at_detector.detect(formatFrame, estimate_tag_pose=True, tag_size=0.0762, camera_params=[502.8289, 503.4731, 319.3317, 230.6123])
		if len(detectedTags) > 0:
			for detectedTag in detectedTags:
				print(detectedTag.center)
				finalFrame = cv2.circle(frame, (round(detectedTag.center[0]), round(detectedTag.center[1])), radius=5, color=(0, 0, 255), thickness=-1)
		else:
			finalFrame = frame
	except:
		print("Couldn't find any AprilTags")
	
	#Display the frame
	cv2.imshow('frame', finalFrame)

	#Define escape key
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
  
#Release the video object after loop is complete & destroy the windows
vid.release()
cv2.destroyAllWindows()