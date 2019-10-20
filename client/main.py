from cameraManager import CameraManager
import client

#--------------Take a photo----------------#
cameraManager = CameraManager()
photoPath = cameraManager.takePhoto()

#-----------Send photo to the serveur-----#
client.start()
client.sendPhotoToServer(photoPath)

