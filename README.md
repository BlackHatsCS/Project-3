 Project-3
============
Sorting Algorithms
-----------------
The main target of this project is to implement a sorting algorithm.
It will be used to sort the order of treasures once they have all been collected by the robot.
So we need to decide on the algorithm that we are going to be using.
There are a few good choices that we could use that would all work as well as each other.

-----------
Pathfinding
------------
There are slight changes that need to be made to the pathfinding of the robot.
It now is going to have multiple treasures on the screen at a time that it can go to.
But it needs to go to the closest treasure to itself at the current moment in time.

------------
Traps
---------
There are going to be randomly spawning traps at locations and when the robot goes over them it will remove the most recent treasure added.
We have also decided that we are are going to add a few more traps that each do a different thing to the list of treasures.

---------
User inputs
--------
The user is required to be able to choose the spawn locations of their robot and all of the treasures.
We are planning on making it so that they do this before anything on the screen has spawning meaning that the program will run smoother.
