import numpy as np

from state import CheckersPlayer, CheckersPiece, CheckersState
from ..interfaces import GameSimulation, GameState, Move


class Checkers(GameSimulation):
    """
    BIG QUESTION - multimoves are possible in a game of checkers, when
    leaping over multiple pieces in succession.
    Should we store this a single move, or rather as a sequence?
    """

    def is_terminal(self, game_state: GameState) -> bool:
        cnt_white, cnt_black = 0, 0

        for slot in game_state.get_board():
            if slot == CheckersPiece.WHITE or slot == CheckersPiece.WHITE_QUEEN:
                cnt_white += 1
            elif slot == CheckersPiece.BLACK or slot == CheckersPiece.BLACK_QUEEN:
                cnt_black += 1

        return (cnt_white == 0 or cnt_black == 0)

    def get_moves(self, game_state: GameState) -> list[Move]:
        # przejscie po wszystkich pionkach i czy bicie?
        # ruchy zwykle

        # go over all possible pieces and create a list of all possible moves until
        # a) we find a move where a player can take a piece - if so, we stop saving regular moves
        # b) we have found all possible moves

        # whenever we find a move, we save it in a list (?) using PDN
        possible_moves = []
        
        if(game_state.get_player() == )
        
        for slot in game_state.get_board():
            if slot == CheckersPiece.WHITE:
                
                

    def make_move(self, game_state: CheckersState, move: Move) -> GameState:
        # if we got here, we assume the move is a LEGAL one!
        # if move doesn't contain 'x', that means no take took place.
        # that means we only have to check whether a pawn made its way to the last row
        if 'x' not in move:
            move_fields = move.split('-')

            if game_state.active_player == CheckersPlayer.WHITE and move_fields[-1] <= 4:
                game_state[move_fields[-1]] = CheckersPiece.WHITE_QUEEN
            if game_state.active_player == CheckersPlayer.BLACK and move_fields[-1] >= 29:
                game_state[move_fields[-1]] = CheckersPiece.BLACK_QUEEN
            
                game_state.active_player = CheckersPlayer.BLACK
                return game_state




    def make_random_move(self, game_state: GameState) -> GameState:
        random_move = np.random.choice(self.get_moves(game_state))
        return self.make_move(game_state, random_move)

    def get_starting_state(self) -> GameState:
        # white starts at the bottom
        active_player = CheckersPlayer.WHITE
        # board = np.reshape([64], np.array([
        #     [0, 2, 0, 2, 0, 2, 0, 2],
        #     [2, 0, 2, 0, 2, 0, 2, 0],
        #     [0, 2, 0, 2, 0, 2, 0, 2],
        #     [0, 0, 0, 0, 0, 0, 0, 0],
        #     [0, 0, 0, 0, 0, 0, 0, 0],
        #     [1, 0, 1, 0, 1, 0, 1, 0],
        #     [0, 1, 0, 1, 0, 1, 0, 1],
        #     [1, 0, 1, 0, 1, 0, 1, 0]
        # ]))
        board = np.reshape([32], np.array([
            [2, 2, 2, 2],
            [2, 2, 2, 2],
            [2, 2, 2, 2],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1 ,1]
        ])
                               
        )
        return GameState(active_player, board)

    def reward(self) -> int:
        pass
