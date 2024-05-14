import cv2
import time
from keras.models import load_model
import numpy as np
import random

def get_computer_choice():
    '''
    This function gets the computer's choice for the game and returns it as a string
    '''
    actions = ['rock', 'paper', 'scissors']
    return random.choice(actions)

def countdown(start):
  duration = 3.5
  end_time = start + duration
  global timeCheck
  if int(end_time - time.time()) not in timeCheck:
    timeCheck.append(int(end_time - time.time()))
    print(f"Capturing image in {int(end_time - time.time())} seconds")

def display_webcam_and_capture_image(cap):
  """Displays the webcam feed for 3 seconds and captures the final image."""
  # Capture frames for 3 seconds
  start_time = time.time()
  while (time.time() - start_time) < 3.5:
    countdown(start_time)
    ret, frame = cap.read()

    # Check if frame was captured successfully
    if ret:
      cv2.imshow('Webcam Feed', frame)
      cv2.waitKey(1)  # Wait for 1 millisecond to display the frame
    else:
      print("Error capturing frame!")
      break
  cap.release()
  # Close the window
  cv2.destroyAllWindows()

  return frame

def get_winner(user, computer):
    global playerWins
    global computerWins
    if computer == 'rock' and user == 'paper':
        playerWins += 1
        print(f'User wins! Player threw {user}, Computer threw {computer}')
    elif computer == 'rock' and user == 'scissors':
        computerWins += 1
        print(f'Computer wins! Player threw {user}, Computer threw {computer}')
    elif computer == 'rock' and user == 'rock':
        print(f"It's a tie! Player threw {user}, Computer threw {computer}")
    elif computer == 'paper' and user == 'paper':
        print(f"It's a tie! Player threw {user}, Computer threw {computer}")
    elif computer == 'paper' and user == 'scissors':
        playerWins += 1
        print(f'User wins! Player threw {user}, Computer threw {computer}')
    elif computer == 'paper' and user == 'rock':
        computerWins += 1
        print(f"Computer wins! Player threw {user}, Computer threw {computer}")
    elif computer == 'scissors' and user == 'scissors':
        print(f"It's a tie! Player threw {user}, Computer threw {computer}")
    elif computer == 'scissors' and user == 'paper':
        computerWins += 1
        print(f'User wins! Player threw {user}, Computer threw {computer}')
    elif computer == 'scissors' and user == 'rock':
        playerWins += 1
        print(f"Computer wins! Player threw {user}, Computer threw {computer}")    


#These are global variables that are used in multiple functions
playerWins = 0
computerWins = 0
timeCheck = []

def main():
  """
  This is the main function, it contains the main loop for the game. Ends when someone wins 3 times. If you want to change number of wins, change the number at 
  the top of the while loop.
  """
  print("""
        Welcome to Rock Paper Scissors!
        Prepare to face off against the computer.
        When your webcam pops up, you will have 3 seconds before your picture is taken.
        So make sure you're ready!
        """)
  global playerWins
  global computerWins
  global timeCheck
  while playerWins < 3 and computerWins < 3:
    input("Press enter when you're ready for the round!")
    cap = cv2.VideoCapture(0)  # Open webcam

    # Display webcam feed and capture image
    frame = display_webcam_and_capture_image(cap)

    # Check if image was captured (might be None if there was an error)
    if frame is not None:
      # Process or save the captured frame (replace with your logic)
      cv2.imwrite("captured_image.jpg", frame)
      print("Image captured!")
      
    model = load_model('keras_model.h5')
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
    data[0] = normalized_image
    prediction = model.predict(data)

    choices = ["rock", "paper", "scissors", "nothing"]
    userChoice = choices[np.argmax(prediction)]
        
    computerChoice = get_computer_choice()

    get_winner(userChoice, computerChoice)
    print(f"Scoreboard: Player Wins - {playerWins}, Computer Wins - {computerWins}")
    timeCheck = []
  if playerWins == 3:
    print("You win!")
  else:
    print("Sorry you lose :(")
    
if __name__ == "__main__":
  main()