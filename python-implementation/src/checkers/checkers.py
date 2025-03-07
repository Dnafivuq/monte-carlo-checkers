import numpy as np

from .board import CheckersPiece, Board
from .state import CheckersPlayer, CheckersState
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
        # go over all possible pieces and create a list of all possible moves until
        # a) we find a move where a player can take a piece - if so, we stop saving regular moves
        # b) we have found all possible moves
        # whenever we find a move, we save it in a list (?) using PDN
        pass

    def _get_standard_moves(self, game_state: GameState) -> list[Move]:
        player = game_state.get_player()       
        board = game_state.get_board()

        moves = []
        for index, slot in enumerate(board.squares):

            if slot == CheckersPiece.WHITE and player == CheckersPlayer.WHITE:
                tl_index, tr_index = self.board.get_top_indexes(index)
                if tl_index is not None and self.board.get_piece(tl_index) == CheckersPiece.NONE:
                    moves.append(str(index)+"-"+str(tl_index))

            elif slot == CheckersPiece.BLACK and player == CheckersPlayer.BLACK:
                tl_index, tr_index = self.board.get_top_indexes(index)
                if tr_index is not None and self.board.get_piece(tr_index) == CheckersPiece.NONE:
                    moves.append(str(index)+"-"+str(tl_index))

        return moves

    def _get_captures(self, game_state: GameState) -> list[Move]:
        player = game_state.get_player()
        board = game_state.get_board()

        moves = []
        for index, slot in enumerate(board.squares):
            if player == CheckersPlayer.WHITE:
                if slot == CheckersPiece.WHITE:
                    moves.append(self._get_captures_piece(index, board))
                elif slot == CheckersPiece.WHITE_QUEEN:
                    moves.append(self._get_captures_queen(index, board))
            else:
                if slot == CheckersPiece.BLACK:
                    moves.append(self._get_captures_piece(index, board))
                elif slot == CheckersPiece.BLACK_QUEEN:
                    moves.append(self._get_captures_queen(index, board))

        return moves

    def _get_captures_piece(self, string: str, index: int) -> list[Move]:
        pass
        # piece = board.get_piece(index)
        # neighbours = board.get_neighbour_indexes(index)

        # for direction, neighbour_idx in enumerate(neighbours):
        #     neighbour_piece = board.get_piece(neighbour_idx)     
        #     if neighbour_idx is not None and neighbour_piece in self.get_oponent_pieces(piece):
        #         next_idx = board.get_single_neighbour_index(neighbour_idx, direction)
        #         if board.get_piece(next_idx) == CheckersPiece.EMPTY:

                

    @staticmethod
    def get_oponent_pieces(piece: CheckersPiece) -> tuple[CheckersPiece, CheckersPiece]:
        if piece in (CheckersPiece.WHITE, CheckersPiece.WHITE_QUEEN):
            return (CheckersPiece.BLACK, CheckersPiece.BLACK_QUEEN)
        elif piece in (CheckersPiece.BLACK, CheckersPiece.BLACK_QUEEN):
            return (CheckersPiece.WHITE, CheckersPiece.WHITE_QUEEN)

    def _get_captures_queen(index) -> list[Move]:
        pass

    def make_move(self, game_state: CheckersState, move: Move) -> GameState:
        # if we got here, we assume the move is a LEGAL one!

        # setup things to make code player-agnostic
        queen_piece = CheckersPiece.WHITE_QUEEN
        pawn_piece = CheckersPiece.WHITE
        promotion_fields = [0, 1, 2, 3]
        if game_state.active_player == CheckersPlayer.BLACK:
            queen_piece = CheckersPiece.BLACK_QUEEN
            pawn_piece = CheckersPiece.BLACK
            promotion_fields = [28, 29, 30, 31]

        # if move doesn't contain 'x', that means no capture took place.
        if 'x' not in move:
            move_fields = move.split('-')
            # non-jump move can only have 2 fields, subtract one from each to make them indexes
            start_field_idx, final_field_idx = tuple(map(lambda x: int(x)-1, move_fields))

            if game_state.board[start_field_idx] == queen_piece or final_field_idx in promotion_fields:
                game_state.board[final_field_idx] = queen_piece
            else:
                game_state.board[final_field_idx] = pawn_piece

            game_state.board[start_field_idx] == CheckersPiece.EMPTY
            return game_state
        else:
            move_fields = move.split('x')
            start_field_idx, *mid_fields_idx, final_field_idx = tuple(map(lambda x: int(x)-1, move_fields))

            # at least one jump took place. Remove pieces from fields which were hopped over.
            hopped_fields = self._get_hopped_fields(move_fields)
             
    def make_random_move(self, game_state: GameState) -> GameState:
        random_move = np.random.choice(self.get_moves(game_state))
        return self.make_move(game_state, random_move)

    def get_starting_state(self) -> GameState:
        # white starts at the bottom
        active_player = CheckersPlayer.WHITE
        board = np.reshape([32], np.array([
            [2, 2, 2, 2],
            [2, 2, 2, 2],
            [2, 2, 2, 2],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1]
        ])                        
        )
        return GameState(active_player, board)

    def reward(self) -> int:
        pass
