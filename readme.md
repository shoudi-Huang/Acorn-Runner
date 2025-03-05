# Acorn Runner: An Escape to Survive

## Project Overview
**Acorn Runner** is a 2D maze navigation game developed as part of the INFO1110/COMP9001 course. The game revolves around an acorn, the heir to the Honourable Furious Forest Throne, who must navigate a treacherous maze filled with obstacles such as walls, fire, water buckets, and teleport pads. The goal is to escape the maze and reclaim the throne, restoring the forest to its former glory.

The project consists of three main components:
1. **Game Component**: A playable 2D maze game where the player controls the acorn to navigate from the start to the end of the maze.
2. **Solver Component**: An automated solver that uses Depth-First Search (DFS) and Breadth-First Search (BFS) algorithms to find a path through the maze.
3. **Report**: A brief analysis of testing strategies and solver algorithms.

## Demo
[Demo Vedio](Demo_Arcon-Runner.mp4)

## Features
- **Interactive Gameplay**: Players can move the acorn using commands (`w`, `a`, `s`, `d`, `e`, `q`) to navigate the maze.
- **Dynamic Maze Elements**:
  - **Fire Cells**: Require water buckets to pass; otherwise, the game ends.
  - **Water Bucket Cells**: Provide water buckets to extinguish fires.
  - **Teleport Cells**: Transport the acorn to another teleport pad.
  - **Wall Cells**: Block the acorn's path.
- **Solver Modes**: The solver can find a path through the maze using either DFS or BFS algorithms.
- **ASCII-Based Interface**: The game is displayed using ASCII characters, making it lightweight and easy to run.

## Technical Details
- **Programming Language**: Python 3
- **Key Libraries**: Only built-in Python modules (`sys`, `os`) are allowed.
- **File Structure**:
  - `game.py`: Contains the game engine and logic.
  - `cells.py`: Defines cell behaviors (e.g., fire, water, teleport).
  - `player.py`: Manages the player's position and water bucket count.
  - `grid.py`: Handles grid rendering and string conversion.
  - `game_parser.py`: Parses the maze configuration file.
  - `run.py`: Entry point for the game.
  - `solver.py`: Entry point for the solver.

## Maze Configuration
The maze is defined in a text file using ASCII characters:
- `X`: Starting position.
- `Y`: Ending position.
- `*`: Wall.
- `W`: Water bucket.
- `F`: Fire.
- `1-9`: Teleport pads (must come in pairs).

## How to Run
1. **Game Mode**:
   ```bash
   python3 run.py <maze_file> [play]
- Replace <maze_file> with the path to your maze configuration file.
- Use the optional play argument to enable screen clearing after each move.

2. **Solver Mode**:
   ```bash
   python3 solver.py <maze_file> <mode>
- Replace <maze_file> with the path to your maze configuration file.
- Replace <mode> with DFS or BFS to choose the solver algorithm.

## Acknowledgments
This project was developed as part of the INFO1110/COMP9001 course at the University of Sydney. Special thanks to the course instructors and tutors for their guidance and support. 🚀
