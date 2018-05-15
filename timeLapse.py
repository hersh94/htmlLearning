import os
import pyrebase
import pyimgur
import picamera
import time


#Setup imgur object?
CLIENT_ID = "5aa734cef2783b6"
CLIENT_SECRET = "c13b32149ce85883dbbf271b356e9a3fe3c36780"
imgurObj = pyimgur.Imgur(CLIENT_ID, CLIENT_SECRET)

config = {
    apiKey: "AIzaSyB0dLUinpRirN-UShJhAu1-8G3USPH4C-M",
    authDomain: "raspberrypitimelapse-26a1e.firebaseapp.com",
    databaseURL: "https://raspberrypitimelapse-26a1e.firebaseio.com",
    projectId: "raspberrypitimelapse-26a1e",
    storageBucket: "raspberrypitimelapse-26a1e.appspot.com",
    messagingSenderId: "415431995647"
  };
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
user = auth.sign_in_with_email_and_password("hersh994@gmail.com", "hello123")
db = firebase.database()

camera = picamera.PiCamera()

#IMGUR upload
#This will need to perform the loop to upload image
#Will need to set the image name as the current date/time
newImage = "testImage.jpg"
camera.capture(newImage)
uploaded_image = imgurObj.upload_image(newImage, title=newImage)
#os.remove(newImage)


#FIREBASE upload
data = {
	"Time": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
	"Image":{
		"Image_Title: uploaded_image.title"
		"Image_URL: uploaded_image.link"
	}
}


results = db.child("Images").push(data, user['idToken'])
print("pushed to firebase")
user = auth.refresh(user['refreshToken'])
