
board = list(range(1, 10))
wins_coord = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7),
              (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]


class TicTacGame:

    def show_board(self):
        print('-------------')
        for i in range(3):
            print('|', board[0+i*3], '|', board[1+i*3], '|', board[2+i*3], '|')
        print('-------------')

    def validate_input(self, player_token):
        while True:
            value = input('Куда поставить: ' + player_token + ' ? ')
            if not value in '123456789':
                print('Ошибочный ввод. Повторите.')
                continue
            value = int(value)
            if str(board[value-1]) in 'XO':
                print('Эта клетка уже занята')
                continue
            board[value-1] = player_token
            break

    def start_game(self):
        counter = 0
        while True:
            self.show_board()
            if counter % 2 == 0:
                self.validate_input('X')
            else:
                self.validate_input('O')
            if counter > 3:
                winner = self.check_winner()
                if winner:
                    self.show_board()
                    print(winner + " выиграл!")
                    break
            counter += 1
            if counter > 8:
                self.show_board()
                print('ничья')
                break

    def check_winner(self):
        for each in wins_coord:
            if (board[each[0]-1]) == (board[each[1]-1]) == (board[each[2]-1]):
                return board[each[1]-1]
        return False


if __name__ == '__main__':
    game = TicTacGame()
    game.start_game()
