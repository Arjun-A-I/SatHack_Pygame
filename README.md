# SatHack_Pygame

![Pygame GIthub](https://user-images.githubusercontent.com/64391274/229285417-80d68655-4282-4a33-87a2-20723c8dfcb0.png)

# SignLingo

Have you ever seen a game for non verbal people? 
Introducing SignLingo! An all in one app to learn and challenge ASL(American Sign Language)
Its an interactive game designed to help deaf individuals learn and master sign language. With its user-friendly interface and engaging gameplay, SignLingo makes learning sign language both fun and educational.

The game is divided into different levels, each with its own set of sign language lessons. Users can progress through the levels at their own pace, learning and practicing their skills as they go.Added voice assistance makes the lessons more interactive.

Currently there are two levels, Level 1 and Level 2.
Level 1 involves learning phase where users can learn each hand sign (from A-Z) by imitating the hand sign image displayed nearby.
Camera live feed is taken and analysed to check if the user is doing the sign right.
Level 2 is about challenging your knowlwdge. Some objects will be shown and the user needs to spell it correctly through ASL. If its shown right more objects will be displayed with growing difficulty.

SignLingo focusses on interactiveness and  is developed to bridge the gap caused by disability, ensuring equal posibilities to everyone. 

## Team members
1. Arjun A I [https://github.com/Arjun-A-I]
2. Manu NS [https://github.com/Manu-N-S]
3. Adithyan T [https://github.com/Adith628]

## Link to product walkthrough
[link to video]

## How it Works ?
1. Explaining the working of project
The game launches with a home screen that allows the user to select the game level.
Once the user selects a level, the game redirects to the level screen user interface for that specific level.
If the user selects level one, a basic level is displayed that shows a sign language letter.
The user is required to show that sign to the camera correctly to proceed to the next sub-levels.
The sign shown by the user is processed using OpenCV and a sign language detection machine learning model that is incorporated with the Pygame.
If the user's sign is correct, they are directed to the next sub-level. If it is incorrect, the level is reset.
If the user selects level two, an object is displayed, and the user is required to spell the object completely to the camera.
If the user inputs the correct spelling of the object, they are directed to the next sub-level. If they input the wrong spelling, the level is reset.
The game continues with increasingly challenging levels, and the user must complete each level to progress to the next.
The game ends when the user completes all levels or chooses to exit the game.
The user's score and progress can be displayed on the screen at all times.


2. Embed video of project demo

## Libraries used
Latest version of each library is used:
Pygame \n
OpenCV
Tensorflow
NumPy
pyttsx3

## How to configure
Install the above mentioned libraries in python using-
pip install pygame
pip install opencv
pip install tensorflow
pip install numpy
pip install pyttsx3
You need to have a webcam setup on your system.

## How to Run
Instructions for running
Just run final.py file and you're all set!
Happy Learning!
