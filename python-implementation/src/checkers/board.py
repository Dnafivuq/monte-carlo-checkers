from enum import Enum


class CheckersPiece(Enum):
    EMPTY = 0
    WHITE = 1
    BLACK = -1
    WHITE_QUEEN = 2
    BLACK_QUEEN = -2


class Board:
    def __init__(self, squares):
        self.squares = squares

    def get_piece(self, index: int) -> CheckersPiece:
        return self.squares[index]

    def get_single_neighbour_index(self, idx, direction: int) -> list[int | None]:
        """
        """
        if direction == 0:  # TL
            return self._get_left_up(idx)
        elif direction == 1:  # TR
            return self._get_right_up(idx)    
        elif direction == 2:  # TL
            return self._get_left_down(idx)
        else:  # TL
            return self._get_left_down(idx)

    def get_neighbour_indexes(self, idx: int) -> list[int | None]:
        # Returns the indexes of four diagonal neighbors or None if the move
        # is not possible due to the board constraints.
        moves = []

        moves.append(self._get_left_up(idx))
        moves.append(self._get_right_up(idx))
        moves.append(self._get_left_down(idx))
        moves.append(self._get_right_down(idx))

        return moves

    @staticmethod
    def _get_left_up(idx: int) -> int | None:
        row = idx / 4
        if idx % 8 == 4 or idx <= 3:
            return None
        elif row % 2 == 0:
            return idx - 4
        else:
            return idx - 5

    @staticmethod
    def _get_right_up(idx: int) -> int | None:
        row = idx / 4
        if idx % 8 == 3 or idx <= 3:
            return None
        elif row % 2 == 0:
            return idx - 3
        else:
            return idx - 4

    @staticmethod
    def _get_left_down(idx: int) -> int | None:
        row = idx / 4
        if idx % 8 == 4 or idx >= 28:
            return None
        elif row % 2 == 0:
            return idx + 4
        else:
            return idx + 3

    @staticmethod
    def _get_right_down(idx: int) -> int | None:
        row = idx / 4
        if idx % 8 == 3 or idx >= 28:
            return None
        elif row % 2 == 0:
            return idx + 5
        else:
            return idx + 4

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
