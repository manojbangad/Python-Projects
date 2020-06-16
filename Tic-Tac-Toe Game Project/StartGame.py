
class tic_tac_toe:

    positions = []
    player_1 = ''
    player_2 = ''

    def initiate(self):
        self.positions = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

        while True:
            self.player_1 = input("Enter player 1 symbol ('x' / 'o') : ")
            if self.player_1 in ['x', 'o', 'X', 'O']:
                break
            else:
                print("Invalid input. Choose one from 'x' or 'o' only !")

        if self.player_1 == 'x' or self.player_1 == 'X':
            self.player_1 = 'X'
            self.player_2 = 'O'
        else:
            self.player_1 = 'O'
            self.player_2 = 'X'

        print('Player 1 is using ', self.player_1)
        print('Player 2 is using ', self.player_2)

    def print_board(self, positions):

        print(' -------------------')
        print(' |  ' + positions[0] + '  |  ' + positions[1] + '  |  ' + positions[2] + '  |')
        print(' -------------------')
        print(' |  ' + positions[3] + '  |  ' + positions[4] + '  |  ' + positions[5] + '  |')
        print(' -------------------')
        print(' |  ' + positions[6] + '  |  ' + positions[7] + '  |  ' + positions[8] + '  |')
        print(' -------------------')

    def isPositionAvailable(self, position_id):
        if self.positions[position_id - 1] not in ['X', 'O']:
            return True
        return False

    def getUserInput(self):
        while True:
            user_choice = input("Enter a position to mark : ")

            if user_choice.isdigit() and int(user_choice) in range(1, 10):
                if self.isPositionAvailable(int(user_choice)):
                    return int(user_choice)
                else:
                    print("Enter a number from available positions only !")
            else:
                print("Enter position number from 1 to 9 only !")


    # def ifGameWon2(self, positions):
    #
    #     if (positions[0] == 'x' and positions[1] == 'x' and positions[2] == 'x') or \
    #         (positions[3] == 'x' and positions[4] == 'x' and positions[5] == 'x') or \
    #         (positions[6] == 'x' and positions[7] == 'x' and positions[8] == 'x') or \
    #         (positions[0] == 'x' and positions[3] == 'x' and positions[6] == 'x') or \
    #         (positions[1] == 'x' and positions[4] == 'x' and positions[7] == 'x') or \
    #         (positions[2] == 'x' and positions[5] == 'x' and positions[8] == 'x') or \
    #         (positions[0] == 'x' and positions[4] == 'x' and positions[8] == 'x') or \
    #         (positions[2] == 'x' and positions[4] == 'x' and positions[6] == 'x') or \
    #         (positions[0] == 'o' and positions[1] == 'o' and positions[2] == 'o') or \
    #         (positions[3] == 'o' and positions[4] == 'o' and positions[5] == 'o') or \
    #         (positions[6] == 'o' and positions[7] == 'o' and positions[8] == 'o') or \
    #         (positions[0] == 'o' and positions[3] == 'o' and positions[6] == 'o') or \
    #         (positions[1] == 'o' and positions[4] == 'o' and positions[7] == 'o') or \
    #         (positions[2] == 'o' and positions[5] == 'o' and positions[8] == 'o') or \
    #         (positions[0] == 'o' and positions[4] == 'o' and positions[8] == 'o') or \
    #         (positions[2] == 'o' and positions[4] == 'o' and positions[6] == 'o') :
    #          return True
    #     return False

    def ifGameWon(self, positions, marker):
        if (positions[0] == marker and positions[1] == marker and positions[2] == marker) or \
                (positions[3] == marker and positions[4] == marker and positions[5] == marker) or \
                (positions[6] == marker and positions[7] == marker and positions[8] == marker) or \
                (positions[0] == marker and positions[3] == marker and positions[6] == marker) or \
                (positions[1] == marker and positions[4] == marker and positions[7] == marker) or \
                (positions[2] == marker and positions[5] == marker and positions[8] == marker) or \
                (positions[0] == marker and positions[4] == marker and positions[8] == marker) or \
                (positions[2] == marker and positions[4] == marker and positions[6] == marker) :
            return True
        return False


    def playGame(self):
        self.initiate()
        self.print_board(self.positions)

        player_turn = 1
        counter = 1

        # while True:
        # while self.isGameWon(self.positions):
        while counter < 10:

            # player_turn = counter % 2
            if player_turn == 1:
                print(" Player 1 turn. Symbol : ", self.player_1)
                marker = self.player_1
            else:
                print(" Player 2 turn. Symbol : ", self.player_2)
                marker = self.player_2

            user_input = self.getUserInput()
            self.positions[user_input-1] = marker

            if self.ifGameWon(self.positions, marker):
                print("\n\n Game Won by player ", str(player_turn) , "!!!! \n\n")
                break

            if player_turn == 1:
                player_turn = 2
            else:
                player_turn = 1

            self.print_board(self.positions)
            counter = counter + 1

        if counter == 10:
            print("\n\nGame Drawn !!!! \n\n")



t = tic_tac_toe()
positions = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
t.print_board(positions)
# t.playGame()