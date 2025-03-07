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
                    pass

        elif player == CheckersPlayer.BLACK:
            pass

    def _get_four_diagonal_neighbours(self, idx: int) -> list[int | None]:
        # Returns the indexes of four diagonal neighbors or None if the move is not possible due to the board constraints.
        moves = []
        row = (idx - 1)/4

        moves.append(self._get_left_up(idx, row))
        moves.append(self._get_right_up(idx, row))
        moves.append(self._get_left_down(idx, row))
        moves.append(self._get_right_down(idx, row))

    @staticmethod
    def _get_left_up(idx: int, row: int) -> int | None:
        if idx % 8 == 5 or idx <= 4:
            return None
        elif row % 2 == 0:
            return idx - 4
        else:
            return idx - 5

    @staticmethod
    def _get_right_up(idx: int, row: int) -> int | None:
        if idx % 8 == 4 or idx <= 4:
            return None
        elif row % 2 == 0:
            return idx - 3
        else:
            return idx - 4

    @staticmethod
    def _get_left_down(idx: int, row: int) -> int | None:
        if idx % 8 == 5 or idx >= 29:
            return None
        elif row % 2 == 0:
            return idx + 4
        else:
            return idx + 3

    @staticmethod
    def _get_right_down(idx: int, row: int) -> int | None:
        if idx % 8 == 4 or idx >= 29:
            return None
        elif row % 2 == 0:
            return idx + 5
        else:
            return idx + 4

    def _get_captures(self, game_state: GameState) -> list[Move]:
        pass

    def _get_diagonals(self, center_field_idx: int) -> tuple[list[int], list[int]]:
        '''
        Given a field idx, will return a list of idx which are on the diagonals
        with it at the center.
        '''
        diagonal_tl_br = []  # top left to bottom right
        diagonal_bl_tr = []  # bottom left to top right

        conv_idx = center_field_idx * 2 + 1  # convert idx to be 0-63 for ease of use here

        # get diagonals on left side of center field
        if conv_idx % 8 != 0:
            temp_idx = conv_idx
            # get bottom left
            while temp_idx % 8 != 0 and temp_idx < 56:
                temp_idx += 7
                diagonal_bl_tr.append(temp_idx)
            # get top left
            temp_idx = conv_idx
            while temp_idx % 8 != 0 and temp_idx > 7:
                temp_idx -= 9
                diagonal_tl_br.append(temp_idx)
        # get diagonals on right side of center field
        if conv_idx % 7 != 0:
            temp_idx = conv_idx
            # get top right
            while temp_idx % 7 != 0 and temp_idx > 7:
                temp_idx -= 7
                diagonal_bl_tr.append(temp_idx)
            # get bottom right
            temp_idx = conv_idx
            while temp_idx % 7 != 0 and temp_idx < 56:
                temp_idx += 9
                diagonal_tl_br.append(temp_idx)

        # convert back to idx
        diagonal_bl_tr = tuple(map(lambda x: (x-1)/2, diagonal_bl_tr))
        diagonal_tl_br = tuple(map(lambda x: (x-1)/2, diagonal_tl_br))

        return diagonal_tl_br, diagonal_bl_tr

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
            [1, 1, 1, 1]
        ])
                               
        )
        return GameState(active_player, board)

    def reward(self) -> int:
        pass
