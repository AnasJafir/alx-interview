# Island Perimeter

## Project Description

This project involves calculating the perimeter of an island in a 2D grid. The grid is represented by a 2D array of integers where 0 represents water and 1 represents land. The goal is to determine the perimeter of the single island present in the grid.

## Problem Statement

You are given a map in the form of a 2D grid, where:

- 0 represents water
- 1 represents land

The grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells). The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, with its width and height not exceeding 100. Determine the perimeter of the island.

## Requirements

- Python 3.x


## Example

```python
grid = [
    [0,1,0,0],
    [1,1,1,0],
    [0,1,0,0],
    [1,1,0,0]
]

print(island_perimeter(grid))  # Should output: 16
```

## How to Run

1. Implement your solution in a file named `0-island_perimeter.py`.
2. Ensure your function is named `island_perimeter` and takes a single parameter `grid`.
3. Run your solution:

   ```
   python3 0-main.py
   ```

   Where `0-main.py` is a file that imports and calls your function.

## Testing

Create various test cases to verify your solution. Consider edge cases such as:

- Islands that touch the border of the grid
- Single cell islands
- Long, snake-like islands