# Terminal Breaker
#### Video Demo:  https://youtu.be/giMj0HukBWk

## Overview
A classic brick breaker game written in Python using the Blessed library, that can be played in any terminal emulator. The game allows you to control a paddle (racket) and bounce a ball to break bricks. The objective is to clear all the bricks on the screen while keeping the ball from falling.

## Features
- Control the paddle (racket) using the left and right arrow keys.
- Launch the ball by pressing the spacebar.
- Restart the game by pressing 'r'.
- Quit the game by pressing 'q'.
- Break bricks by bouncing the ball off them.

## Requirements
- Python 3
- Blessed library 

## Installation and Usage
1. Download the Python script and the lvl folder.
2. Install the Blessed library by running `pip install blessed`.
3. Run the script using `python terminal_breaker.py`.
4. Follow the on-screen instructions to play the game.

## Coding Approach
The coding approach taken in this Brick Breaker game demonstrates a structured and procedural style of programming:

1. **Modular Design**: The code is organized into functions, each responsible for a specific aspect of the game. For example, there are functions for creating the game board, moving the paddle, updating the ball's position, and rendering elements on the screen. This modular design enhances code readability and maintainability.

2. **Data Abstraction**: The game uses a variety of data types to represent game elements, such as the paddle, ball, level, and board. These data abstractions make it easier to manage and manipulate game data, improving code clarity.

3. **Game Loop**: The core of the game is a game loop that continuously updates the game state and renders it on the screen. This loop listens for player input, updates the ball's position, handles collisions, and manages game events, such as restarting or quitting.

4. **File Handling**: The game reads level data from text files to generate the game board dynamically. This approach allows for the creation of custom levels by modifying these text files. It also separates the game content from the code, promoting flexibility.

5. **User Interface**: The Blessed library is used for rendering the game's user interface. It provides a text-based UI that allows the game to run in a terminal. The code takes care of positioning and rendering elements on the screen, creating a user-friendly interface for the player.

6. **Error Handling**: The code includes error handling, such as checking if the game board's dimensions fit within the terminal's size. This ensures a smoother player experience and avoids potential issues with oversized levels.

7. **Randomization**: Randomization is used for determining the initial direction and speed of the ball when it hits the paddle or bricks. This introduces an element of unpredictability and challenge to the game.

8. **Customization**: The code is built with the ability to create custom levels and even extend the game's features in mind. By modifying the level text files, players can design their own levels with varying brick layouts.

## Acknowledgments
This game is created using the Python Blessed library and inspired by classic brick breaker games.
