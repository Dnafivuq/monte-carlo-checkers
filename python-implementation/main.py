from tqdm import tqdm
from collections import Counter
from os import system
import random
import time
from copy import deepcopy

from src.mcts import MCTSTree as MCTS
from src.checkers import (
    Checkers,
    CheckersBoard,
    CheckersPiece,
    CheckersState,
    CheckersPlayer,
)

# import os
ttt = Checkers()
mcts1 = MCTS(ttt, 1.41, 1600)
mcts2 = MCTS(ttt, 1.41, 1600)


def run_sim():
    game_state = ttt.get_starting_state()
    while True:
        move = mcts1.mcts_search(game_state)
        game_state = ttt.make_move(game_state, move)
        # ttt.print_board(game_state)
        if ttt.is_terminal(game_state):
            if ttt.reward(game_state, Player.CIRCLE) != 0:
                ttt.print_board(game_state)
            return ttt.reward(game_state, Player.CROSS)
        move = mcts2.mcts_search(game_state)
        game_state = ttt.make_move(game_state, move)
        # ttt.print_board(game_state)
        if ttt.is_terminal(game_state):
            if ttt.reward(game_state, Player.CIRCLE) != 0:
                ttt.print_board(game_state)
            return ttt.reward(game_state, Player.CROSS)


def play_checkers():
    game = Checkers()
    state = game.get_starting_state()
    while True:
        moves = game.get_moves(state)
        move = random.choice(moves)
        state = game.make_move(state, move)
        BRUH = deepcopy(state)

        if state.get_player() == CheckersPlayer.WHITE:
            state.active_player = CheckersPlayer.BLACK
        else:
            state.active_player = CheckersPlayer.WHITE

        system("clear")
        print(state.board)
        print(moves)
        print(move)

        if game.is_terminal(state):
            game.make_move(BRUH, move)
            print(game.reward(state))
            break


def main():
    # os.system("clear")
    # game_state = ttt.get_starting_state()

    # while (True):
    #     # get mcts move

    #     move = mcts1.mcts_search(game_state)
    #     print(f"MCTS move: {move}")
    #     ttt.make_move(game_state, move)
    #     ttt.print_board(game_state)
    #     player_move = input("Your Move: ")
    #     os.system("clear")
    #     game_state = ttt.make_move(game_state, player_move)
    # outcomes = []
    # for _ in tqdm(range(100)):
    #     outcomes.append(run_sim())
    # print(Counter(outcomes))
    play_checkers()


if __name__ == "__main__":
    main()
