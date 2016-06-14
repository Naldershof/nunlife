import pandas as pd
import numpy as np
import sqlite3

def init_db(name='nun.db'):
    conn = sqlite3.connect(name)
    c = conn.cursor()

    # Create table
    c.execute('''CREATE TABLE games
                 (start text, width integer, height integer, 
                 halts integer, game_length integer, 
                 cyclical integer, cycle_length integer)''')

    # Save (commit) the changes
    conn.commit()

    # We can also close the connection if we are done with it.
    # Just be sure any changes have been committed or they will be lost.
    conn.close()
    

def write_to_db(start, width, height, halts, game_length, cyclical, cycle_length, name='nun.db'):
    conn = sqlite3.connect(name)
    c = conn.cursor()
    
    insert_template = '''INSERT INTO games (\
    start,\
    width,\
    height,\
    halts,\
    game_length,\
    cyclical,\
    cycle_length)\
     VALUES(\
    {},{},{},{},{},{},{});'''
    
    insert_statement = insert_template.format(start, width, height, halts, 
                                              game_length, cyclical, cycle_length)
    
    c.execute(insert_statement)
    
def db_result_debug(name='nun.db'):
    conn = sqlite3.connect(name)
    c = conn.cursor()
    return c.execute('SELECT * FROM games')


################################
### Serialization Components ###
################################
def create_key(board):
    d1_arr = board[1:board.shape[0]-1, 1:board.shape[1]-1].flatten()
    key = ''.join(str(x) for x in board)
    return key

def reconstruct_board(key):
    unpad = np.reshape(map(int, list(alice)), [HEIGHT, WIDTH])
    board = np.pad(unpad,((1,1),(1,1)), 'constant', constant_values=0)
    return board

if __name__ == '__main__':
    #TODO: Command line arguments for initiating all of this stuff
    main()
