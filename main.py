from shutil import get_terminal_size
import os
import curses
from random import randint
from time import time


def set_term_by_grid(cons, grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            cons.addch(i, j, grid[i][j])


def border_to_grid(grid, border, corner) -> None:
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if i == 0 and j == 0:
                grid[i][j] = corner[0]
            elif i == 0 and j == len(grid[i]) - 1:
                grid[i][j] = corner[1]
            elif i == len(grid) - 1 and j == 0:
                grid[i][j] = corner[2]
            elif i == len(grid) - 1 and j == len(grid[i]) - 1:
                grid[i][j] = corner[3]
            elif i == 0 or i == len(grid) - 1:
                grid[i][j] = border[0]
            elif j == 0 or j == len(grid[i]) - 1:
                grid[i][j] = border[1]


def main(cons):
    # Get the terminal size
    terminal_size = get_terminal_size()
    valid_area = {"lines": range(1, terminal_size.lines - 1), "columns": range(1, terminal_size.columns - 2)}
    curses.curs_set(0)

    curses.start_color()
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(5, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    curses.init_pair(6, curses.COLOR_CYAN, curses.COLOR_BLACK)


    # Clear screen
    cons.clear()

    screen_grid = [[" " for _ in range(terminal_size.columns - 1)] for _ in range(terminal_size.lines)]
    border_to_grid(screen_grid, ["═", "║"], ["╔", "╗", "╚", "╝"])
    set_term_by_grid(cons, screen_grid)

    frame_start_prev = time()
    fps_prev = 0.0
    frame_count = 0
    update_rate = 250  # Update FPS display every 10 frames
    for _ in range(10000000000):
        frame_start = time()
        for _ in range(2):
            cons.addch(randint(1, terminal_size.lines - 2), randint(1, terminal_size.columns - 3), "H", curses.color_pair(1))
            cons.addch(randint(1, terminal_size.lines - 2), randint(1, terminal_size.columns - 3), "X", curses.color_pair(2))
            cons.addch(randint(1, terminal_size.lines - 2), randint(1, terminal_size.columns - 3), "0", curses.color_pair(3))
            cons.addch(randint(1, terminal_size.lines - 2), randint(1, terminal_size.columns - 3), "M", curses.color_pair(4))
            cons.addch(randint(1, terminal_size.lines - 2), randint(1, terminal_size.columns - 3), "T", curses.color_pair(5))
            cons.addch(randint(1, terminal_size.lines - 2), randint(1, terminal_size.columns - 3), "+", curses.color_pair(6))
        for _ in range(40):
            cons.addch(randint(1, terminal_size.lines - 2), randint(1, terminal_size.columns - 3), " ")
        frame_time = frame_start - frame_start_prev
        if frame_time > 0:
            fps = 1.0 / frame_time
            fps_prev = fps
        else:
            fps = fps_prev
        frame_count += 1
        if frame_count >= update_rate:
            cons.addstr(0, 0, f"FPS: {fps:.0f}")
            frame_count = 0
        cons.refresh()
        frame_start_prev = frame_start

    # Wait for user input
    cons.getkey()


if __name__ == '__main__':
    os.system('cls')

    curses.wrapper(main)
