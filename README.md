things to do:

1. create something that allows user to interactively use the program with a GUI
2. create something for collecting sudoku data -- a scraper that reads from somewhere and stores sudoku strongs in our format
3. solver 1: use simple logic to create a state space model --> for each empty space, we look at all possible elements


the problem with the current data model that whwn we intialize the sudoku, then there are a number of EmptyCells that have possible values = [1...9]
in a stable state of the sudoku this means that there is not guarantee that these values are stable
==> the solution to this could be a sudoku.balance() function that updates all the EmptyCell values everytime somethig get's updated... this takes away a lot of the power of manipulating the different kinds of solutions... ideally i want more flexibility in this updatation process.


-- ok so the backtracking works!
1. turn this into a visual thing on desktop that can show updates in real-time
2. then think about making this an interactive GUI/game
3. then think about running this on a hosted website -- so that it can be a real-time comparison
4. create metrics for comparison of techniques
5. hybird optimizations
6. scrape multiple sudoku's from somewhere online and extablish a dataset
7. think about other AI solutions like genetic algorithms, bayesian models and reinforcement learning

How would one generate a sudoku puzzle??
1. create a random grid
2. remove a random number 
3. check if the grid is UNIQUE and solvable
4. repeat step 2

I feel that generating puzzles at this time is not the best idea...
instead work on:
--> bringing this in front of people. implement a GUI
--> exploring different AI techniques for solving the problem
