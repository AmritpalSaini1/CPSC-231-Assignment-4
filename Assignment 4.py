#Amritpal Saini, 30039983, Catalin, Lec 2

import sys #used for importing game

class Car: #used to make Car objects
    def __init__(self, orientation, length, x, y):
        self.orientation = orientation #vertical vs horizontal
        self.length = length #length of car
        self.x = x #row of car
        self.y = y #column of car

class game:
    def __init__(self, path):
        self.path = path #the location of the file
        self.board =[['.','.','.','.','.','.'],
                     ['.','.','.','.','.','.'],
                     ['.','.','.','.','.','.'],
                     ['.','.','.','.','.','.'],
                     ['.','.','.','.','.','.'],
                     ['.','.','.','.','.','.']]
        #this code is from https://github.com/ryanwilsonperkin/rushhour/blob/master/rushhour.py#L66
        #board is used to make the text of the game
        self.carList = [] #empty list for car objects

    def makeCars(self): #is function is used to open the file and make a list of all the cars
        file_reader = open(self.path, 'r')
        for line in file_reader:
            split_line = line.split(',')
            self.car = Car(split_line[0], int(split_line[1]), int(split_line[2]), int(split_line[3]))
            self.carList.append(self.car)
        return self.carList

    def loadGame(self): #this function is used to initally load the game
        self.carList = self.makeCars()
        j = 0 #used to give cars id
        for self.car in self.carList:
            x = self.car.x
            y = self.car.y
            if self.car.orientation == 'h':
                for i in range(self.car.length):
                    self.board[x][y + i] = str(j)
            elif self.car.orientation == 'v':
                for i in range(self.car.length):
                    self.board[x + i][y] = str(j)
            j+=1
        print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in self.board])) #prints board
        return self.board

    def gameOver(self): #checks to see if main vehicle is at the end of the game
        if self.board[2][5] == 0:
            exit()
            return False
        else:
            return True

    def CheckMove(self): #used to ensure the correct values are given for each vehicle
        while True:
            # https://stackoverflow.com/questions/41832613/python-input-validation-how-to-limit-user-input-to-a-specific-range-of-integers
            try:
                user_input = input("Enter car, row, column: ")
                org_list = user_input.split(',') #used to split the inputs given by the user
                if org_list[0] == "exit":
                    exit()
                # https://stackoverflow.com/questions/7378091/taking-multiple-inputs-from-user-in-python
                input_list = list(map(int, org_list)) #converted to int for use in checking moves
                carList = self.makeCars()
                # code from https://stackoverflow.com/questions/7368789/convert-all-strings-in-a-list-to-int
                if input_list[0] > len(carList) or input_list[1] > 5 or input_list[1] < 0 or input_list[2] < 0 or \
                                input_list[2] > 5:
                    raise ValueError
                InputOri = carList[input_list[0]].orientation
                CarX = carList[input_list[0]].x
                CarY = carList[input_list[0]].y

                if InputOri == "h" and CarX != input_list[1]:
                    raise ValueError
                if InputOri == "v" and CarY != input_list[2]:
                    raise ValueError

                if InputOri == "h":
                    if CarY > input_list[2]:
                        while CarY >= input_list[2]:
                            if self.board[CarX][CarY] != '.' and self.board[CarX][CarY] != org_list[0]:
                                raise ValueError
                            CarY -= 1
                    elif CarY < input_list[2]:
                        while CarY <= input_list[1]:
                            if self.board[CarX][CarY] != '.' and self.board[CarX][CarY] != org_list[0]:
                                raise ValueError
                            CarY += 1
                elif InputOri == 'v':
                    if CarX > input_list[1]:
                        while CarX >= input_list[1]:
                            if self.board[CarX][CarY] != '.' and self.board[CarX][CarY] != org_list[0]:
                                raise ValueError
                            CarX -= 1
                    elif CarX < input_list[1]:
                        while CarX <= input_list[1]:
                            if self.board[CarX][CarY] != '.' and self.board[CarX][CarY] != org_list[0]:
                                raise ValueError
                            CarX += 1
            except ValueError:
                print("Invalid input... Try again.")
                continue
            else:
                break
        return input_list

    def MoveCar(self): #function is used to move the card on the board
        input_list = self.CheckMove()
        self.carList = self.makeCars()
        InputOri = self.carList[input_list[0]].orientation
        CarX = self.carList[input_list[0]].x
        CarY = self.carList[input_list[0]].y
        carLen = self.carList[input_list[0]].length
        j = str(input_list[0])
        if InputOri == 'v': #first the original car is replaced with '.' and the new car is replaced with it's id number
            if CarX < input_list[1]:
                for i in range(carLen):
                    self.board[CarX + i][CarY] = '.'
                for i in range(carLen):
                    self.board[input_list[1] - i][CarY] = j
            elif CarX > input_list[1]:
                for i in range(carLen):
                    self.board[CarX + i][CarY] = '.'
                for i in range(carLen):
                    self.board[input_list[1] + i][CarY] = j
        elif InputOri == 'h':
            if CarY < input_list[2]:
                for i in range(carLen):
                    self.board[CarX][CarY + i] = '.'
                for i in range(carLen):
                    self.board[CarX][input_list[2] - i] = j

            elif CarY > input_list[2]:
                for i in range(carLen):
                    self.board[CarX][CarY + i] = '.'
                for i in range(carLen):
                    self.board[CarX][input_list[2] + i] = j
        print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in self.board]))
        # code from https://stackoverflow.com/questions/17870612/printing-a-two-dimensional-array-in-python
        return self.board

def main(): #used to run the game
    one = game(sys.argv[1])
    one.loadGame()
    while one.gameOver():
        one.MoveCar()

main()
