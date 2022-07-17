from Board import Board
from Play import Play

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('Welcome To Chess')
    print('If you want to play please enter 1 else 2')
    play = input()
    if play == '1':
        board = Board()
        board.setAllPiece()
        board.printBoard()
        play: Play = Play(board)
        play.play()
    else:
        print('This is the End of this chess \n Goodbay')
