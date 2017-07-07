import abc
import math

class Field():
    "Field class"
    def __init__(self):
        self.field  = [(letter,number) for letter in "ABCDEFGH" for number in range(1,9)]
        self.letter_to_numb = {key:value for key,value in zip(list("ABCDEFGH"),range(1,9))}
        self.numb_to_letter = {key:value for key,value in zip(range(1,9),list("ABCDEFGH"))}
    def opponent_color(color):
        if color == "white":
            return "black"
        if color == "black":
            return "white"

    def get_start_position(self,color):
        if color == "black":
            numb = (7,8)
        if color == "white":
            numb = (1,2)
        return [cell for cell in self.field if cell[1] in numb]


class Figure():

    def __init__(self,name,color,position):
        self.field = Field()
        self.name = name
        self.position = position
        self.color = color

    @abc.abstractmethod
    def get_move_list(self):
        "Return all possible move for figure"
        pass

    def is_possible_move(self,move):
        "Check is move possible"
        if move in self.get_move_list() == False:
            return False
        if other_figures.position == move:
            return False
    def __str__(self):
        return "%s at %s%d"%(self.name,self.position[0],self.position[1])

class Pawn(Figure):
    "Pawn figure class"
    def get_move_list(self):
        letter,number = self.position
        if self.position in self.field.get_start_position(self.color):
            if self.color == "black":
                return [(letter,number-1),(letter,number-2)]
            if self.color == "white":
                return [(letter,number+1),(letter,number+2)]
        else:
            if self.color == "black":
                return [(letter,number-1)]
            if self.color == "white":
                return [(letter,number+1)]


class Rook(Figure):
    def get_move_list(self):
        letter,number = self.position
        return [(x[0],x[1]) for x in self.field.field if x[0]==letter or x[1] == number and x != self.position]

class Knight(Figure):
    def get_move_list(self):
        result = []
        letter,number = self.position
        letter_to_numb = self.field.letter_to_numb[letter]
        for cell in self.field.field:
            move = (math.fabs(self.field.letter_to_numb[cell[0]]-letter_to_numb),math.fabs(cell[1]-number))
            if move[0] !=0 and move[1] !=0 and move[0]+move[1]==3:
                result.append(cell)
        return result

class Bishop(Figure):
    def get_move_list(self):
        result = []
        letter,number = self.position
        letter_to_numb = self.field.letter_to_numb[letter]
        for cell in self.field.field:
            move = (math.fabs(self.field.letter_to_numb[cell[0]]-letter_to_numb),math.fabs(cell[1]-number))
            if move[0]==move[1] and cell != self.position:
                result.append(cell)
        return result

class Queen(Figure):
    def get_move_list(self):
        letter,number = self.position
        letter_to_numb = self.field.letter_to_numb[letter]
        result = [(x[0],x[1]) for x in self.field.field if x[0]==letter or x[1] == number and x != self.position]
        for cell in self.field.field:
            move = (math.fabs(self.field.letter_to_numb[cell[0]]-letter_to_numb),math.fabs(cell[1]-number))
            if move[0]==move[1] and cell != self.position:
                result.append(cell)
        return result

class King(Figure):
    def get_move_list(self):
        result = []
        letter,number = self.position
        letter_to_numb = self.field.letter_to_numb[letter]
        for cell in self.field.field:
            move = (math.fabs(self.field.letter_to_numb[cell[0]]-letter_to_numb),math.fabs(cell[1]-number))
            if move == (0,1) or move == (1,0) or move == (1,1):
                result.append(cell)
        return result




class Command():

    def __init__(self,color):
        self.color = color
        self.field = Field()
        self.start_position = self.field.get_start_position(self.color)
        self.command = self.get_start_command()
    def get_start_command(self):
        if self.color == "black":
            pawn_field = sorted(self.start_position,key = lambda x: x[1])[:8]
            cool_figures = sorted(self.start_position,key = lambda x: x[1])[8:]
        if self.color == "white":
            pawn_field = sorted(self.start_position,key = lambda x: x[1])[8:]
            cool_figures = sorted(self.start_position,key = lambda x: x[1])[:8]
        result = [Pawn("pawn"+str(x+1),self.color,cell) for x,cell in enumerate(pawn_field)]
        result += [Rook("rook"+str(x+1),self.color,cell) for x,cell in enumerate(cool_figures)\
                                                                    if cell[0] == "A" or cell[0] == "H"]
        result += [Knight("knight"+str(x+1),self.color,cell) for x,cell in enumerate(cool_figures)\
                                                                    if cell[0] == "B" or cell[0] == "G"]
        result += [Bishop("bishop"+str(x+1),self.color,cell) for x,cell in enumerate(cool_figures)\
                                                                    if cell[0] == "C" or cell[0] == "F"]
        result += [Queen("queen"+str(x+1),self.color,cell) for x,cell in enumerate(cool_figures)\
                                                                    if cell[0] == "D"]
        result += [King("king"+str(x+1),self.color,cell) for x,cell in enumerate(cool_figures)\
                                                                    if cell[0] == "E"]
        return result
    def is_possible_move(self,origin,move):
        for figure in self.command:
            if figure.position == move and figure.position != origin:
                return False
            else:
                return True
    def delete_figure(position):
        for figure in self.command:
            if figure.position == position:
                self.command.remove(figure)
    def __str__(self):
        result = ""
        for figure in self.command:
            result += str(figure)+"\n"
        return result

class Game():
    def __init__(self):
        self.white_command = Command("white")
        self.black_command = Command("black")
        self.field = Field()
    def get_command_by_color(self,color):
        if color == "black":
            return self.black_command
        if color == "white":
            return self.white_command
    def maketurn(self,color,origin,destination):
        for figure in self.get_command_by_color(color).command:
            if figure.position == origin and self.get_command_by_color(color).is_possible_move(destination):
                figure.position = destination
        opponent_color = self.field.opponent_color(color)
        for figure in self.get_command_by_color(opponent_color).command:
            if figure.position == destination:
                self.get_command_by_color(opponent_color).delete_figure(figure)
    def is_check(color):
        opponent_color = self.field.opponent_color(color)
        king_position = [x for x in self.get_command_by_color(color).command if x.name == "king5"]
        king_position = king_position[0]
        for figure in self.get_command_by_color(opponent_color).command:
            if king_position in figure.get_move_list():
                return True
        return False
    def __str__(self):
        for figure in self.black_command.command:
            print(str(figure.position)+" ")
            if figure.name == "pawn8":
                print("\n")
        for i in range(6):
            print("***"*8)
        for figure in self.white_command.command:
            print(str(figure.position)+" ")
            if figure.name == "pawn8":
                print("\n")






game = Game()
game.maketurn("black",("A",8),("A",9))
print(game)



"""command = Command("white")
command.get_start_command()
print(command)
for figure in command.command:
    print(str(figure)+":\n")
    print(figure.get_move_list())
    print("\n")
"""
