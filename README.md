## Rock-Paper-Scissors

###**Introduction**
This program uses Google's teachable machine visual learning model to create a rock, paper, scissors game where the player uses their webcam to play against the computer.

I used Google's Teachable Machine to create a model to determine whether the user is displaying rock, paper or scissors. The counter-part of the game where the computer chooses a shape at random to throw out was written in python. The way it works, when you run the file it will explain the rules to you, then after you press enter there will be a 3 second timer with a countdown in the terminal before your final image is taken to be run through the keras model.

###**Requirements**
There is a requirements file included that has all the dependencies you'll need to run this. Once you've created your conda environment (if you're using one), run the following command in your terminal --> pip install -r requirements.txt
If you want to install the dependencies manually, you will need:
*opencv-python
*ipykernel
*tensorflow (version 2.15.0)

###**Other Notes**
There is a bug that sometimes happens with the webcam window, where it won't automatically show after the first round. You'll have to click on the terminal in order to press enter and progress the rounds. When you do this the webcam window will be behind VSCode (or whichever interpreter you're using). You'll have the timer counting down in the terminal before the image is taken anyway, so you should be fine!

Be sure to display your hand quite close to your camera as this will improve the odds of the model determining the shape correctly. The match ends when you or the computer wins 3 times, if you want to change that you'll find the number at the beginning of the while loop in the 'main()' function. Also, your hand shape should be more vertical than when you play with someone in real life so that the model can differentiate the hand shapes. 


**When you're ready** just run the python file --> python camera_rps.py in your terminal

Have fun!

