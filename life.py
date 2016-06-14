import pandas as pd
import numpy as np
import db_handling

# Constants for board size.
# TODO, turns these into preferences / options / something not hardcoded
WIDTH = 6
HEIGHT = 6

# This is the life implementation

def neighbors(array, i, j):
    #above = sum(array[i-1:i+1, j-1])
    #below = sum(array[i-1:i+1, j+1])
    above = sum(array[i-1:i+2, j-1])
    below = sum(array[i-1:i+2, j+1])
    sides = array[i-1,j] + array[i+1,j]
    return above + below + sides

def breed(array, i, j):
    ALIVE = array[i,j]
    nbs = neighbors(array, i, j)
    if ALIVE:
        if nbs < 2:
            return 0
        elif nbs in (2,3):
            return 1
        else:
            return 0
    elif nbs == 3:
        return 1
    else:
        return 0

def iterate(board):
    next_gen = np.zeros(shape=(WIDTH+2, HEIGHT+2), dtype=int)
    for i in range(1,1+WIDTH):
        for j in range(1,1+HEIGHT):
            next_gen[i,j] = breed(board,i,j)
    return next_gen

def rand_start(WIDTH, HEIGHT):
    board = np.zeros(shape=(WIDTH+2, HEIGHT+2), dtype=int)
    rand_in = np.round(np.random.rand(WIDTH,HEIGHT)).astype(int)
    board[1:1+WIDTH, 1:1+HEIGHT] = rand_in
    return board

def track_life(board, stop_iteration=100):
    history = []
    for gen_number in range(0,stop_iteration):
        next_gen = iterate(board)
        for index, element in enumerate(history):
            if np.array_equal(next_gen,element):
                cycle_length = gen_number - index
                return cycle_length, gen_number
        history.append(next_gen)
        board = next_gen
    return 0, stop_iteration


if __name__ == '__main__':
	board = rand_start(WIDTH, HEIGHT)
	generations = [board]
	main()