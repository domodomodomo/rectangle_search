OFF_FLAG = 0


def search_rectangle(board):
    """O(n^2) unique search algorithm for digital matrix.

    Original algorithm is here...
    https://www.ipsj.or.jp/07editj/promenade/4304.pdf
    """
    extended_board = _make_extended_board(board)
    m = len(extended_board)

    # The lists of top left corner.

    # the list of a row number.
    # the top row number of 0 seen from a current col in for-statement.
    # The list index is correspinding to the current col.
    lst_top_0_row = [0] * m
    lst_top_0_row[0] = m - 1

    # the list of a col number.
    # the left column number of 0 seen from a current col in for-statement.
    # The list index is corresponding to the current col.
    lst_left_0_col = [0] * m

    unique_rectangle_list = []
    for row in range(1, m - 1):
        left_0_col = 0
        for col in range(0, m - 1):
            # Update the lists of the top left coner.
            if extended_board[row][col + 1] == OFF_FLAG:
                lst_top_0_row[col + 1] = row
                lst_left_0_col[col + 1] = 0
                left_0_col = col + 1
            elif lst_left_0_col[col + 1] < left_0_col:
                # lst_top_0_row[col + 1]
                lst_left_0_col[col + 1] = left_0_col
                # left_0_col

            # Detect the bottom side.
            if extended_board[row + 1][col] == OFF_FLAG:
                # height_col will be used in a while loop below.
                # height_col indicate the coloumn
                #   which tell you the top row of the rectangle by...
                #     row0 = lst_top_0_row[height_col] + 1
                height_col = col
            # Detect the right side.
            if lst_top_0_row[height_col] < lst_top_0_row[col + 1]:
                # For checking proceasrues, print log.
                if __debug__:
                    if m <= MAX_M_FOR_FUNCTION_PRINT_DEBUG_BOARD:
                        print('The right bottom corner',
                              str((row, col)), 'detected.')
                #
                # This while conditions describes...
                #
                while lst_top_0_row[height_col] < lst_top_0_row[col + 1]:
                    row0 = lst_top_0_row[height_col] + 1
                    col0 = lst_left_0_col[height_col] + 1
                    row1 = row
                    col1 = col

                    org_row0 = row0 - 1
                    org_col0 = col0 - 1
                    org_row1 = row1 - 1
                    org_col1 = col1 - 1

                    unique_rectangle_list.append(
                        (org_row0, org_col0, org_row1, org_col1))

                    # For checking proceasrues, print log.
                    if __debug__:
                        if m <= MAX_M_FOR_FUNCTION_PRINT_DEBUG_BOARD:
                            _print_board_for_debug(
                                len(unique_rectangle_list),
                                row, col,
                                extended_board,
                                lst_top_0_row, lst_left_0_col,
                                height_col, left_0_col,
                                row0, col0, row1, col1)

                    # Find next rectangles by checking left side wall of 0.
                    height_col = lst_left_0_col[height_col]
                height_col = col + 1
    return unique_rectangle_list


def _make_extended_board(board):
    n = len(board)
    extended_board = [None] * (n + 2)
    extended_board[0] = [OFF_FLAG] * (n + 2)

    # Expand multiple lists into one list.
    for i in range(1, n + 1):
        extended_board[i] = []
        for sublist in [[OFF_FLAG], board[i - 1], [OFF_FLAG]]:
            for x in sublist:
                extended_board[i].append(x)
    extended_board[-1] = [OFF_FLAG] * (n + 2)
    return extended_board


def _input_board():
    """Read the board."""
    bit_list = list(map(int, list(input())))
    n = len(bit_list)
    board = [None] * n

    board[0] = bit_list
    for i in range(1, n):
        bit_list = list(map(int, list(input())))
        board[i] = bit_list

    return board


if __debug__:
    # IF m <= MAX_M_FOR_FUNCTION_PRINT_DEBUG_BOARD THEN
    #     execute_debug_print()
    MAX_M_FOR_FUNCTION_PRINT_DEBUG_BOARD = 10

    def _print_board_for_debug(
            num_of_rectangle,
            row, col,
            extended_board,
            lst_top_0_row, lst_left_0_col,
            height_col, left_0_col,
            row0, col0, row1, col1):
        m = len(extended_board)
        if m > MAX_M_FOR_FUNCTION_PRINT_DEBUG_BOARD:
            raise ValueError('This function is applicable, '
                             + 'when the m, n-2 is smaller '
                             + 'than MAX_M_FOR_FUNCTION_PRINT_DEBUG')
        print('-----')
        print('  num_of_rectangle = ' + str(num_of_rectangle))
        print('  (row, col) = ' + str((row, col)))
        print('  (row0, col0, row1, col1) = ' + str((row0, col0, row1, col1)))
        print('-----')
        print('extended_board = ')
        _print_board(extended_board, row, col)
        print()
        print('lst_top_0_row  = ', lst_top_0_row)
        print('lst_left_0_col = ', lst_left_0_col)
        print('height_col     = '
              + str(' ' * (1 + height_col * 3)) + str(height_col))
        print('left_0_col     = '
              + str(' ' * (1 + left_0_col * 3)) + str(left_0_col))
        print()
        print()
        print()

    def _print_board(board, row, col):
        for i in range(row):
            print('                 ', board[i])
        lst = board[row][:col + 1]
        print('                 ', lst)


if __name__ == '__main__':
    rectangle_list = search_rectangle(_input_board())
    for rectangle in rectangle_list:
        print(rectangle)
