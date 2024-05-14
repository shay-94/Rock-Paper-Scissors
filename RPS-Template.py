import cv2
from keras.models import load_model
import numpy as np
import time

model = load_model('keras_model.h5')

# Function to display countdown and capture image
def capture_image(cap):
  for i in range(3, 0, -1):
    print(f"Capturing image in {i} seconds...")
    time.sleep(1)  # Wait for 1 second

  # Capture the frame
  ret, frame = cap.read()
  return frame

cap = cv2.VideoCapture(0)


# Check if webcam opened successfully
if not cap.isOpened():
  print("Error opening webcam!")
  exit()

image = capture_image(cap)

data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

while True: 
    ret, frame = cap.read()
    resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
    data[0] = normalized_image
    prediction = model.predict(data)
    cv2.imshow('frame', frame)
    # Press q to close the window
    if prediction[0][0] > 0.7:
        print('Rock')
    elif prediction[0][1] > 0.7:
        print("Paper")
    elif prediction[0][2] > 0.7:
        print("Scissors")
    else:
        print("Nothing")
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
            
# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()
