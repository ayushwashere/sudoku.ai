# Sudoku.ai

## How to Use
```
python run.py [mode] [method]
```

Available Modes: easy, medium, hard, evil  
Available Methods: reduction, backtracking, hybrid  

## Rules of Sudoku
1. Each row, column and block will have numbers 1-9 without repitition
2. There is a unique solution to each puzzle

## 1. State Space Reduction
According to the rules of the game, a single number can only be present once in a row, column and block.  
Thus, for each cell, we evaluate values present in its row, column and block and eliminate all possible options which will create a conflict with this rule. After this elimination process, if only one value is possible then we've found the solution for this cell.

Finding the solution for a single cell propogates changes for several cells related to it. Thus, we repeatedly keep checking all possible cells (as long as a cell was updated in the previous layer)

## 2. Backtracking
Using the same idea as the State Space Reduction technique but with different mechanics, backtracking assigns a number to an empty cell and recursively keeps doing so as long as the new grid doesn't violate the rules about no repition of numbers in a row, column or block. If there is a violation in the rules, we go back one step and modify the assigned number.

This approach creates a tree of possibilities where each node can have 9 children, one for each guess number in the selected empty cell. 

## 3. Hybrid Backtracking 
In this Sudoku solution, I implement a combination of the above techniques.  

We start with a backtracking approach where the algorithm makes a valid guess in an empty cell. Based on the value of the guess, there will be changes propagated in the grid. These changes are solved based on the State Space Reduction technique 
and at each step of the backtracking, we obtain a grid where the maximum number of cells are filled.

This approach successively reduces the number of empty cells, effectively reducing the number of nodes needed in the backtracking tree and reducing the height of the tree. This approach is significantly faster that the previous approaches.

## Data Structure
This implementation uses two main classes:

### Sudoku
1. Takes a row-major string formatted such that each empty cell is a '-' and the end of a row is denoted by a semicolon (;)
2. The Sudoku object has access to the grid as well as functions for accessing values in any row, column or block
3. Each empty cell is stored as an EmptyCell object which keeps track of which possible values can be placed in that position.


### EmptyCell
1. The EmptyCell stores its location in the grid as well as a list of possible values for the cell
2. It is not aware of its surrounding cells but it has fields for indicating when the final value of a cell has been reached

## Metrics for Comparison
While there are several interesting metrics for comparison of techniques (number of nodes in backtracking, memory used etc.), I decided to use total time as a reasonable metric for comparison between different techniques.


## Future Work
As a competitive Sudoku enthusiast, I established several personal tricks and techniques to make smart inferences for filling out empty cells. The methods mentioned above are purely computational and do not take into account locality as well as patterns in the grid that can avoid a lot of computational comparison work.

My long term goal with this project is to try several bayesian, statistical, neural network or reinforced learning techniques that can learn various tricks and patterns in the Sudoku and help me discover new cool shortcuts to improve my own Sudoku game.