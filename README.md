# Rock Paper Scissors
Using Google's Teachable Machine, a model was created to determine whether the user is displaying rock, paper or scissors. The counter-part of the game where the computer chooses a shape at random to throw out was written in python. Upon executing the `camera_rps.py` script, the rules of the game will be explained to the end user, afterwards, the user will be prompted to press the enter key on their keyboard.

There will be a 3 second timer with a countdown in the terminal before the final image is taken to be run through the `keras model`.
### **Prerequisites** 
- [Anaconda3](https://docs.anaconda.com/) or Miniconda
- Python 3.8 
- A Video Camera
 ### **Installation** 
 Clone the repository:
 
 ``` git clone https://github.com/shay-94/Rock-Paper-Scissors.git ```

Run the following command below to create the conda environment used for the project: 

``` conda env create -f environment.yml ```

 ``` # environment.yml name: rps channels: - defaults dependencies: - python=3.8.0 - pip=23.3.1 ```
 
There is a requirements file included, which includes the dependencies needed to run the project. run the following command in your terminal to install the dependencies for this project:

 ``` pip install -r requirements.txt ``` 

If you want to install the dependencies manually, you will need:
 - opencv-python
 - ipykernel
 - tensorflow (version 2.15.0)

### **Contributing** 
To contribute create a pull request on a new branch detailing the fix. All contributions are subject to review by the repository owner. To report bugs, please create a new [issue](https://github.com/shay-94/Rock-Paper-Scissors/issues)

### **Future Improvements** 
The success rate of the `keras model` in determining the user's choice is currently around 60%, resulting in times where the user will see a different choice reflected in the match outcome. As a way of preventing errors like this from occuring, a confidence threshold will be added. The check will be done on the number from the `keras model` matrix to ensure the model is at least 70% sure of the shape the user is choosing.

#### Current Issues 
 #1 [Bug with Webcam Window](https://github.com/shay-94/Rock-Paper-Scissors/issues/1#issue-2323301082)



