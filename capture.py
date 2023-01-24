from os.path import exists
import cv2
  
imageCount = 0  
# define a video capture object
vid = cv2.VideoCapture(0)
  
while(True):
	#Capture frame from camera
	ret, frame = vid.read()
	
	#Display the frame
	cv2.imshow('frame', frame)
	
	#Define escape key
	if cv2.waitKey(81) == ord('q'):
		break
  
	if cv2.waitKey(67) == ord('c'):
		cv2.imwrite(str(imageCount) + ".jpg", frame)
		print("Capturing...")
		while not exists(str(imageCount) + ".jpg"):
			print("Waiting to write file")
			
	imageCount += 1
	
#Release the video object after loop is complete & destroy the windows
vid.release()
cv2.destroyAllWindows()