from enum import Enum
from ..interfaces import GameState

class CheckersPiece(Enum):
    EMPTY = 0
    WHITE = 1
    BLACK = -1
    WHITE_QUEEN = 2
    BLACK_QUEEN = -2


class CheckersBoard(GameState):
    def __init__(self, squares):
        self.squares = squares

    def get_piece(self, index: int) -> CheckersPiece:
        """
        Get the piece at the given index.
        """
        return self.squares[index]

    def get_closest_index(self, indx, direction_id: int) -> list[int | None]:
        """
        1 = TL, 2 = TR, 3 = BL, 4 = BR
        """
        # Didn't bother with enum :3
        if direction_id == 0:  # TL
            return self._get_left_up(indx)
        elif direction_id == 1:  # TR
            return self._get_right_up(indx)    
        elif direction_id == 2:  # BL
            return self._get_left_down(indx)
        elif direction_id == 3:  # BR
            return self._get_left_down(indx)

    def get_closest_indexes(self, indx: int) -> list[int | None]:
        """
        Retuns the indexes of four diagonal neighbors,
        or Nones in case some are out of bounds.
        """
        return [
            self._get_left_up(indx),
            self._get_right_up(indx),
            self._get_left_down(indx),
            self._get_right_down(indx)
        ]
    
    def get_closest_occupied_indexes(self, indx: int) -> list[int]:
        """
        Returns the indexes of the closest occupied
        diagonal squares of the given index.
        """
        all_indxs = []
        for new_indx, direction_id in zip(self.get_closest_indexes(indx), range(4)):
            
            while new_indx is not None and self.squares[new_indx] == CheckersPiece.EMPTY:
                new_indx = self.get_closest_index(new_indx, direction_id)
            
            all_indxs.append(new_indx)
        return all_indxs

    @staticmethod
    def _get_left_up(indx: int) -> int | None:
        row = int(indx / 4)
        if indx % 8 == 4 or indx <= 3:
            return None
        elif row % 2 == 0:
            return indx - 4
        else:
            return indx - 5

    @staticmethod
    def _get_right_up(indx: int) -> int | None:
        row = int(indx / 4)
        if indx % 8 == 3 or indx <= 3:
            return None
        elif row % 2 == 0:
            return indx - 3
        else:
            return indx - 4

    @staticmethod
    def _get_left_down(indx: int) -> int | None:
        row = int(indx / 4)
        if indx % 8 == 4 or indx >= 28:
            return None
        elif row % 2 == 0:
            return indx + 4
        else:
            return indx + 3

    @staticmethod
    def _get_right_down(indx: int) -> int | None:
        row = int(indx / 4)
        if indx % 8 == 3 or indx >= 28:
            return None
        elif row % 2 == 0:
            return indx + 5
        else:
            return indx + 4

    # def _get_diagonals(self, center_field_idx: int) -> tuple[list[int], list[int]]:
    #     '''
    #     Given a field indx, will return a list of indx which are on the diagonals
    #     with it at the center.
    #     '''
    #     diagonal_tl, diagonal_tr = [], []
    #     diagonal_bl, diagonal_br = [], []

    #     conv_idx = center_field_idx * 2 + 1  # convert indx to be 0-63 for ease of use here

    #     # get diagonals on left side of center field
    #     if conv_idx % 8 != 0:
    #         temp_idx = conv_idx
    #         # get bottom left
    #         while temp_idx % 8 != 0 and temp_idx < 56:
    #             temp_idx += 7
    #             diagonal_bl.append(temp_idx)
    #         # get top left
    #         temp_idx = conv_idx
    #         while temp_idx % 8 != 0 and temp_idx > 7:
    #             temp_idx -= 9
    #             diagonal_tl.append(temp_idx)
    #     # get diagonals on right side of center field
    #     if conv_idx % 7 != 0:
    #         temp_idx = conv_idx
    #         # get top right
    #         while temp_idx % 7 != 0 and temp_idx > 7:
    #             temp_idx -= 7
    #             diagonal_tr.append(temp_idx)
    #         # get bottom right
    #         temp_idx = conv_idx
    #         while temp_idx % 7 != 0 and temp_idx < 56:
    #             temp_idx += 9
    #             diagonal_br.append(temp_idx)

    #     # convert back to indx
    #     diagonal_tl = tuple(map(lambda x: (x-1)/2, diagonal_tl))
    #     diagonal_tr = tuple(map(lambda x: (x-1)/2, diagonal_tr))
    #     diagonal_bl = tuple(map(lambda x: (x-1)/2, diagonal_bl))
    #     diagonal_br = tuple(map(lambda x: (x-1)/2, diagonal_br))
    #     return diagonal_tl, diagonal_tr, diagonal_bl, diagonal_br

    def __str__(self):
        empty = " "
        white = "⛂"
        black = "⛀"
        top = " ┌─" + 7*"┬─" + "┐\n"
        mid = " ├─" + 7*"┼─" + "┤\n"
        bot = " └─" + 7*"┴─" + "┘\n"

        string = top
        for i in range(8):
            row = " │"
            for column in range(8):
                if row % 2 == 0:
                    if column % 2 == 0:
                        piece = self.squares[i*8 + column]
                    else:    
                        piece = CheckersPiece.EMPTY
                else:  
                    if column % 2 == 0:
                        piece = CheckersPiece.EMPTY
                    else:    
                        piece = self.squares[i*8 + column]

                if piece == CheckersPiece.EMPTY:
                    string += empty
                elif piece in CheckersPiece.WHITE:
                    string += white
                elif piece == CheckersPiece.BLACK:
                    string += black
                row += "│"

            string += row + "│\n" 
            if i != 7:
                string += mid
        string += bot
        return string