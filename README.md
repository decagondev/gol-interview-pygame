# Conway's Game of Life - Python Coding Challenge

## Overview
Implement Conway's Game of Life, a cellular automaton simulation where cells live, die, or multiply based on simple rules. This challenge tests your ability to work with 2D arrays, implement algorithms, and handle GUI programming with pygame.

## The Rules
Conway's Game of Life follows these rules for each generation:

1. **Survival**: A live cell with 2 or 3 live neighbors survives to the next generation
2. **Death by Isolation**: A live cell with fewer than 2 live neighbors dies
3. **Death by Overcrowding**: A live cell with more than 3 live neighbors dies
4. **Birth**: A dead cell with exactly 3 live neighbors becomes alive

Neighbors are the 8 cells surrounding a given cell (horizontally, vertically, and diagonally).

## Requirements

### Grid
- Create a 30×40 grid of cells
- Each cell can be either alive (filled) or dead (empty)
- Users should be able to click cells to toggle them on/off when the simulation is stopped

### Controls
Implement the following buttons:
- **Start**: Begin the simulation (advance generations automatically)
- **Stop**: Pause the simulation
- **Clear**: Reset the grid to all dead cells
- **Random**: Fill the grid with a random pattern

### Additional Features
- **Speed Control**: A slider to adjust simulation speed (50ms to 1000ms between generations)
- **Generation Counter**: Display the current generation number
- **Button States**: Disable/enable buttons appropriately (e.g., can't clear while running)

## Technical Specifications

### Grid Dimensions
- Rows: 30
- Columns: 40
- Cell size: 15px × 15px

### Data Structure
- Use a 2D list to represent the grid state
- `True` = alive cell, `False` = dead cell

### Algorithm
- For each generation, calculate the next state based on the current state
- Count neighbors for each cell (check all 8 surrounding cells)
- Apply the rules to determine which cells live or die
- Update the entire grid simultaneously (don't update cells one at a time)

## Setup

### Prerequisites
- Python 3.7 or higher
- pygame library

### Installation
```bash
pip install pygame
```

### Running the Code
```bash
python game_of_life.py
```

## Files Provided

### `game_of_life.py`
Starter code with:
- Complete pygame setup and window initialization
- Button and UI element definitions
- Drawing functions for grid, buttons, and info
- Event handling structure
- Function stubs for you to implement

## What You Need to Implement

Complete the following methods in the `GameOfLife` class:

1. **`init_grid()`** - Initialize the grid list with all dead cells
2. **`count_neighbors(row, col)`** - Count live neighbors for a given cell
3. **`next_generation()`** - Apply Game of Life rules and update the grid
4. **`toggle_cell(row, col)`** - Toggle a cell's state when clicked
5. **`start()`** - Begin the simulation
6. **`stop()`** - Pause the simulation
7. **`clear()`** - Reset the grid
8. **`randomize()`** - Generate a random pattern
9. **`update_speed(value)`** - Handle speed slider changes

## Tips

- Remember to create a **new grid** for the next generation rather than modifying the current one in place
- Don't forget to check list bounds when counting neighbors
- Use `pygame.time.get_ticks()` to track time for generation updates
- Make sure to update `self.last_update` when starting the simulation
- The grid is accessed as `self.grid[row][col]` where `row` is 0-29 and `col` is 0-39
- Use list comprehensions for creating 2D lists: `[[False for _ in range(COLS)] for _ in range(ROWS)]`

## Evaluation Criteria

Your solution will be evaluated on:
- **Correctness**: Does it follow the Game of Life rules accurately?
- **Code Quality**: Is the code clean, readable, and well-organized?
- **Edge Cases**: Does it handle boundary conditions properly?
- **User Experience**: Do the controls work smoothly?
- **Efficiency**: Is the algorithm reasonably performant?
- **Python Best Practices**: Proper use of type hints, docstrings, and Python idioms

## Time Limit
You have **20-30 minutes** to complete this challenge.

## Testing Your Solution

Try these patterns to verify your implementation:
- **Blinker**: 3 horizontal cells that oscillate between horizontal and vertical
- **Glider**: A 5-cell pattern that moves across the grid diagonally
- **Block**: A 2×2 square that remains stable

To test patterns manually:
1. Stop the simulation
2. Click cells to create the pattern
3. Start the simulation and observe the behavior

## Example Patterns

### Blinker (Oscillator)
```
[ ][ ][ ]
[#][#][#]
[ ][ ][ ]
```

### Glider
```
[ ][#][ ]
[ ][ ][#]
[#][#][#]
```

### Block (Still Life)
```
[#][#]
[#][#]
```

Good luck!

