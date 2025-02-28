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
        
        # if game_state.get_player() == CheckersPlayer.WHITE:
        #     for slot in game_state.get_board():
        #         if slot == CheckersPiece.WHITE:
               
        # pass

    def _get_standard_moves(self, game_state: GameState) -> list[Move]:
        player = game_state.get_player()        
        moves = []
        board = game_state.get_board()

        if player == CheckersPlayer.WHITE:
            for index, slot in enumerate(board, start=1):                        
                if slot == CheckersPiece.WHITE:

                    # Which row, affects the index change
                    if index/4 % 2 == 0:
                        if index % 8 != 5 and board[index-3]==CheckersPiece.EMPTY:
                            moves.append(str(index+"-"+index-3))

                        if index % 8 != 4 and board[index-4]==CheckersPiece.EMPTY:
                            moves.append(str(index+"-"+index-4))
                        
                    if index/4 % 2 == 1:
                        if index % 8 != 5 and board[index-4]==CheckersPiece.EMPTY:
                            moves.append(str(index+"-"+index-4))
                        if index % 8 != 4 and board[index-5]==CheckersPiece.EMPTY:
                            moves.append(str(index+"-"+index-5))
    
        elif player == CheckersPlayer.BLACK:



    def _get_captures(self, game_state: GameState) -> list[Move]:
        pass


    def make_move(self, game_state: CheckersState, move: Move) -> GameState:
        # if we got here, we assume the move is a LEGAL one!
        
        # if move doesn't contain 'x', that means no capture took place.
        if 'x' not in move:
            move_fields = move.split('-')
            # non-jump move can only have 2 fields, subtract one from each to make them indexes
            start_field_idx, final_field_idx = tuple(map(lambda x: int(x)-1, move_fields))

            if game_state.active_player == CheckersPlayer.WHITE:
                # check if queen made move or was created during move
                if game_state.board[start_field_idx] == CheckersPiece.WHITE_QUEEN or final_field_idx < 4:
                    game_state.board[final_field_idx] == CheckersPiece.WHITE_QUEEN
                else:
                    game_state.board[final_field_idx] == CheckersPiece.WHITE

            else:
                # same but for black
                if game_state.board[start_field_idx] == CheckersPiece.BLACK_QUEEN or final_field_idx > 27:
                    game_state.board[final_field_idx] == CheckersPiece.BLACK_QUEEN
                else:
                    game_state.board[final_field_idx] == CheckersPiece.BLACK

            game_state.board[start_field_idx] == CheckersPiece.EMPTY
            return game_state
        else:
            move_fields = move.split('x')
            start_field_idx, *mid_fields_idx, final_field_idx = tuple(map(lambda x: int(x)-1, move_fields))
            
            if game_state.active_player == CheckersPlayer.WHITE:
                


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
