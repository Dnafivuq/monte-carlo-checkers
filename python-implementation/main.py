from tqdm import tqdm
from collections import Counter

from src.mcts import MCTSTree as MCTS
from src.tictactoe import TictactoeGame, Player

# import os
ttt = TictactoeGame()
mcts1 = MCTS(ttt, 1.41, 1600)
mcts2 = MCTS(ttt, 1.41, 1600)


def run_sim():
    game_state = ttt.get_starting_state()
    while (True):
        move = mcts1.mcts_search(game_state)
        game_state = ttt.make_move(game_state, move)
        # ttt.print_board(game_state)
        if (ttt.is_terminal(game_state)):
            if (ttt.reward(game_state, Player.CIRCLE) != 0):
                ttt.print_board(game_state)
            return ttt.reward(game_state, Player.CROSS)
        move = mcts2.mcts_search(game_state)
        game_state = ttt.make_move(game_state, move)
        # ttt.print_board(game_state)
        if (ttt.is_terminal(game_state)):
            if (ttt.reward(game_state, Player.CIRCLE) != 0):
                ttt.print_board(game_state)
            return ttt.reward(game_state, Player.CROSS)


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
    outcomes = []
    for _ in tqdm(range(100)):
        outcomes.append(run_sim())
    print(Counter(outcomes))


if __name__ == "__main__":
    main()
