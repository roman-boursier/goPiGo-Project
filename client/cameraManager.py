import picamera
import time

class CameraManager:

	def takePhoto(self):
		photoPath = "./photos/" + time.strftime("%y%m%d_%H-%M-%S") + ".jpg"
		camera = picamera.PiCamera()
		camera.resolution = (2592,1944)
		camera.capture(photoPath)
		return photoPath
