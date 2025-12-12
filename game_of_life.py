"""
Conway's Game of Life - Coding Challenge

A cellular automaton simulation where cells live, die, or multiply
based on simple rules applied to each generation.
"""

import pygame
import sys
from typing import List

# Constants
ROWS = 30
COLS = 40
CELL_SIZE = 15
GRID_WIDTH = COLS * CELL_SIZE
GRID_HEIGHT = ROWS * CELL_SIZE
WINDOW_WIDTH = 650
WINDOW_HEIGHT = 650

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
INDIGO = (102, 126, 234)
INDIGO_DARK = (85, 104, 211)
GRAY_DISABLED = (200, 200, 200)
GRID_BG = (221, 221, 221)
TEXT_COLOR = (85, 85, 85)

# Button dimensions
BUTTON_WIDTH = 100
BUTTON_HEIGHT = 40
BUTTON_SPACING = 10


class GameOfLife:
    """Main Game of Life class that handles the simulation and pygame interface."""

    def __init__(self):
        """Initialize pygame and game state."""
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Conway's Game of Life")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 24)
        self.small_font = pygame.font.Font(None, 18)

        # Game state
        self.grid: List[List[bool]] = []
        self.running = False
        self.generation = 0
        self.speed = 200  # milliseconds
        self.last_update = 0

        # Button positions - centered and better spaced
        self.button_y = GRID_HEIGHT + 30
        button_start_x = 50
        button_spacing = 15
        self.start_button = pygame.Rect(button_start_x, self.button_y, BUTTON_WIDTH, BUTTON_HEIGHT)
        self.stop_button = pygame.Rect(button_start_x + BUTTON_WIDTH + button_spacing, self.button_y, BUTTON_WIDTH, BUTTON_HEIGHT)
        self.clear_button = pygame.Rect(button_start_x + 2 * (BUTTON_WIDTH + button_spacing), self.button_y, BUTTON_WIDTH, BUTTON_HEIGHT)
        self.random_button = pygame.Rect(button_start_x + 3 * (BUTTON_WIDTH + button_spacing), self.button_y, BUTTON_WIDTH, BUTTON_HEIGHT)
        
        # Speed slider positioned below buttons
        slider_y = self.button_y + BUTTON_HEIGHT + 20
        self.speed_slider = pygame.Rect(button_start_x, slider_y, 200, 20)
        self.speed_slider_handle = pygame.Rect(button_start_x + (self.speed - 50) * 200 // 950, slider_y - 5, 10, 30)

        # TODO: Initialize the grid with all dead cells (False)
        # Create a 2D list of size ROWS x COLS
        self.init_grid()

    def init_grid(self) -> None:
        """
        Initialize the grid array with all dead cells.
        Create a 2D list of size ROWS x COLS filled with False.
        """
        # Your code here
        pass

    def count_neighbors(self, row: int, col: int) -> int:
        """
        Count the number of live neighbors for a cell at (row, col).
        Check all 8 surrounding cells (including diagonals).
        Make sure to check list bounds.

        Args:
            row: Row index of the cell
            col: Column index of the cell

        Returns:
            Number of live neighbors
        """
        # Your code here
        return 0

    def next_generation(self) -> None:
        """
        Calculate and render the next generation.
        Rules:
        - Live cell with 2-3 neighbors: survives
        - Dead cell with exactly 3 neighbors: becomes alive
        - All other cells: die or stay dead

        Important: Create a new grid, don't modify the current one directly.
        """
        # Your code here
        pass

    def toggle_cell(self, row: int, col: int) -> None:
        """
        Toggle a cell's state when clicked (only when not running).

        Args:
            row: Row index of the cell
            col: Column index of the cell
        """
        # Your code here
        pass

    def start(self) -> None:
        """Start the simulation. Set running to True."""
        # Your code here
        pass

    def stop(self) -> None:
        """Stop the simulation. Set running to False."""
        # Your code here
        pass

    def clear(self) -> None:
        """Clear the grid (only when not running). Reset all cells to dead and generation to 0."""
        # Your code here
        pass

    def randomize(self) -> None:
        """
        Generate a random pattern (only when not running).
        Set each cell to alive with ~30% probability.
        Reset generation to 0.
        """
        # Your code here
        pass

    def update_speed(self, value: int) -> None:
        """
        Update the speed and restart if running.

        Args:
            value: New speed value in milliseconds (50-1000)
        """
        self.speed = value
        self.speed_slider_handle.x = self.speed_slider.x + (self.speed - 50) * 200 // 950

    def draw_grid(self) -> None:
        """Draw the grid of cells on the screen."""
        grid_x = 20
        grid_y = 20

        # Draw grid background
        pygame.draw.rect(self.screen, GRID_BG, (grid_x - 1, grid_y - 1, GRID_WIDTH + 2, GRID_HEIGHT + 2))

        for i in range(ROWS):
            for j in range(COLS):
                x = grid_x + j * CELL_SIZE
                y = grid_y + i * CELL_SIZE
                rect = pygame.Rect(x, y, CELL_SIZE - 1, CELL_SIZE - 1)

                if self.grid[i][j]:
                    pygame.draw.rect(self.screen, INDIGO, rect)
                else:
                    pygame.draw.rect(self.screen, WHITE, rect)

    def draw_buttons(self) -> None:
        """Draw all control buttons on the screen."""
        # Start button
        color = INDIGO if not self.running else GRAY_DISABLED
        pygame.draw.rect(self.screen, color, self.start_button)
        pygame.draw.rect(self.screen, BLACK, self.start_button, 2)
        text = self.font.render("Start", True, WHITE if not self.running else TEXT_COLOR)
        text_rect = text.get_rect(center=self.start_button.center)
        self.screen.blit(text, text_rect)

        # Stop button
        color = INDIGO if self.running else GRAY_DISABLED
        pygame.draw.rect(self.screen, color, self.stop_button)
        pygame.draw.rect(self.screen, BLACK, self.stop_button, 2)
        text = self.font.render("Stop", True, WHITE if self.running else TEXT_COLOR)
        text_rect = text.get_rect(center=self.stop_button.center)
        self.screen.blit(text, text_rect)

        # Clear button
        color = INDIGO if not self.running else GRAY_DISABLED
        pygame.draw.rect(self.screen, color, self.clear_button)
        pygame.draw.rect(self.screen, BLACK, self.clear_button, 2)
        text = self.font.render("Clear", True, WHITE if not self.running else TEXT_COLOR)
        text_rect = text.get_rect(center=self.clear_button.center)
        self.screen.blit(text, text_rect)

        # Random button
        color = INDIGO if not self.running else GRAY_DISABLED
        pygame.draw.rect(self.screen, color, self.random_button)
        pygame.draw.rect(self.screen, BLACK, self.random_button, 2)
        text = self.font.render("Random", True, WHITE if not self.running else TEXT_COLOR)
        text_rect = text.get_rect(center=self.random_button.center)
        self.screen.blit(text, text_rect)

        # Speed slider
        pygame.draw.rect(self.screen, GRAY, self.speed_slider)
        pygame.draw.rect(self.screen, BLACK, self.speed_slider, 1)
        pygame.draw.rect(self.screen, INDIGO, self.speed_slider_handle)
        pygame.draw.rect(self.screen, BLACK, self.speed_slider_handle, 1)

        # Speed label and value
        label = self.small_font.render("Speed:", True, TEXT_COLOR)
        self.screen.blit(label, (self.speed_slider.x, self.speed_slider.y - 20))
        speed_text = self.small_font.render(f"{self.speed}ms", True, INDIGO)
        self.screen.blit(speed_text, (self.speed_slider.x + self.speed_slider.width + 15, self.speed_slider.y - 5))

    def draw_info(self) -> None:
        """Draw generation counter and instructions."""
        gen_text = self.font.render(f"Generation: {self.generation}", True, TEXT_COLOR)
        self.screen.blit(gen_text, (20, WINDOW_HEIGHT - 40))

        instruction_text = self.small_font.render("Click cells to toggle them on/off", True, TEXT_COLOR)
        self.screen.blit(instruction_text, (20, WINDOW_HEIGHT - 20))

    def handle_click(self, pos: tuple) -> None:
        """
        Handle mouse clicks on buttons or grid cells.

        Args:
            pos: Mouse position (x, y)
        """
        x, y = pos

        # Check button clicks
        if not self.running and self.start_button.collidepoint(x, y):
            self.start()
        elif self.running and self.stop_button.collidepoint(x, y):
            self.stop()
        elif not self.running and self.clear_button.collidepoint(x, y):
            self.clear()
        elif not self.running and self.random_button.collidepoint(x, y):
            self.randomize()
        elif self.speed_slider.collidepoint(x, y):
            # Update speed based on slider position
            relative_x = x - self.speed_slider.x
            speed_value = 50 + (relative_x * 950 // self.speed_slider.width)
            speed_value = max(50, min(1000, speed_value))
            # Round to nearest 50
            speed_value = (speed_value // 50) * 50
            self.update_speed(speed_value)

        # Check grid cell clicks
        grid_x = 20
        grid_y = 20
        if grid_x <= x < grid_x + GRID_WIDTH and grid_y <= y < grid_y + GRID_HEIGHT:
            if not self.running:
                col = (x - grid_x) // CELL_SIZE
                row = (y - grid_y) // CELL_SIZE
                if 0 <= row < ROWS and 0 <= col < COLS:
                    self.toggle_cell(row, col)

    def run(self) -> None:
        """Main game loop."""
        while True:
            current_time = pygame.time.get_ticks()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.handle_click(event.pos)
                elif event.type == pygame.MOUSEMOTION:
                    if event.buttons[0] and self.speed_slider.collidepoint(event.pos):
                        relative_x = event.pos[0] - self.speed_slider.x
                        speed_value = 50 + (relative_x * 950 // self.speed_slider.width)
                        speed_value = max(50, min(1000, speed_value))
                        speed_value = (speed_value // 50) * 50
                        self.update_speed(speed_value)

            # Update generation if running
            if self.running and current_time - self.last_update >= self.speed:
                self.next_generation()
                self.last_update = current_time

            # Draw everything
            self.screen.fill(WHITE)
            self.draw_grid()
            self.draw_buttons()
            self.draw_info()

            pygame.display.flip()
            self.clock.tick(60)


if __name__ == "__main__":
    game = GameOfLife()
    game.run()

