# This is my WHITE WHALE programming project :)
import random


class UNO:
    # Declaring variables needed across multiple scopes
    comp_cards_color = []
    comp_cards_number = []
    comp_special_cards_function = []
    comp_special_cards_color = []
   
    first_color = ""
    first_number = 0
    colors = ["red", "yellow", "green", "blue", "wild"]
    # Randomly pick from 4 colors
    first_card_color = colors[random.randint(1, 4)]
    # Randomly pick from 9 numbers(See the note below about randrange in the "turnpicker" function)
    first_card_number = random.randint(0, 10)
    your_cards_number = []
    your_cards_color = []
    your_special_cards_function = []
    your_special_cards_color = []
    num_to_draw = 1
    def turnpicker(self):
        # This randrange doesn't include the latter number for some reason, so this is a number between 0 and 1
        turn = random.randint(0, 2)
        # Temporary variable used to cast the int of the "coin" to a string.
        str_turn = str(turn)
        print("The number is " + str_turn)
        if turn == 1:
            print("CT!")
            uno.comp_turn()
        else:
            print("YT!")
            uno.your_turn()

    def your_deal(self):
        # But the "for" loop DOES include the latter number in the range for a total of 7
        for i in range(0, 6):
            for i in range(1,num_to_draw):
                card_type=random.randint(1,108)
                str(card_type)
                if card_type in range(1,76):
                        uno.your_cards_color.append(self.colors[random.randint(1, 4)])
                        uno.your_cards_number.append(random.randint(0, 9))
                if card_type in range(73,81):
                    uno.your_special_cards_color.append(self.colors[random.randint(1,4)])
                    uno.your_special_cards_function.append("skip")
                if card_type in range(82,90):
                    uno.your_special_cards_color.append(self.colors[random.randint(1,4)])
                    uno.your_special_cards_function.append("reverse")
                if card_type in range(91,99):
                    uno.your_special_cards_color.append(self.colors[random.randint(1,4)])
                    uno.your_special_cards_function.append("draw 2")
                if card_type in range(100,104):
                    uno.your_special_cards_function.append("wild")
                    uno.your_cards_color.append("wild")
                if card_type in range(105,109):
                    uno.your_special_cards_color.append("wild")
                    uno.your_special_cards_function.append("draw_4")

    def your_draw(self, num_to_draw):
        for i in range(1,num_to_draw):
            card_type=random.randint(1,108)
            str(card_type)
            if card_type in range(1,76):
                    uno.your_cards_color.append(self.colors[random.randint(1, 4)])
                    uno.your_cards_number.append(random.randint(0, 9))
            if card_type in range(73,81):
                uno.your_special_cards_color.append(self.colors[random.randint(1,4)])
                uno.your_special_cards_function.append("skip")
            if card_type in range(82,90):
                uno.your_special_cards_color.append(self.colors[random.randint(1,4)])
                uno.your_special_cards_function.append("reverse")
            if card_type in range(91,99):
                uno.your_special_cards_color.append(self.colors[random.randint(1,4)])
                uno.your_special_cards_function.append("draw 2")
            if card_type in range(100,104):
                uno.your_special_cards_function.append("null")
                uno.your_cards_color.append("wild")
            if card_type in range(105,109):
                uno.your_special_cards_color.append("wild")
                uno.your_special_cards_function.append("draw_4")
            # This game can get a LOT of cards FAST
        print("Your new total: ")
        print(len(self.your_cards_number))
        uno.comp_turn()

    def your_turn(self):
        # A quick reminder about *what* your cards are
        print(self.your_cards_number)
        print(self.your_cards_color)
        print("First card is: ")
        print(self.first_card_color)
        print(self.first_card_number)
        print("Can you play  :) ?")
        play = input()
        if play == "no":
            uno.your_draw(1)
        elif play == "yes" or "y":
            print(
                "Pick a card number to play, ensuring it matches the current card on the stack. Starting with 0"
            )
            draw_number = input()
            draw_number = int(draw_number)
            if (
                self.your_cards_color[draw_number] == self.first_card_color
                or self.your_cards_number[draw_number] == self.first_card_number
            ):
                self.first_card_color = self.your_cards_color[draw_number]
                self.first_card_number = self.your_cards_number[draw_number]
                del self.your_cards_color[draw_number]
                del self.your_cards_number[draw_number]
                print("The new card on the stack is: ")
                print(self.first_card_color)
                print(self.first_card_number)

                # If there are no more cards left, the game is over.
                if len(self.your_cards_number) == 0:
                    print("You win!")
                elif len(self.your_cards_number) > 66:
                    print("Game over, the computer wins.")
                    return 0
                else:
                    print("Your cards are now: ")
                    print(self.your_cards_color)
                    print(self.your_cards_number)
                    uno.comp_turn()
            elif self.your_special_cards_color == self.first_card_color:
               match(self.your_special_cards_function):
                   case "skip":
                       uno.your_turn()
                       del self.your_special_cards_color[draw_number]
                       del self.your_special_cards_function[draw_number]
                   case "reverse":
                       del self.your_special_cards_color[draw_number]
                       del self.your_special_cards_function[draw_number]
                       uno.your_turn()
                   case "draw_4":
                       uno.comp_draw(4)

            else:
                print(
                    "Silly goose, that card doesn't match, and now you forfeit a turn!"
                )
                uno.comp_turn()

    def comp_deal(self):
        for i in range(0, 6):
            print(i)
            card_type=random.randint(1,108)
            if card_type in range(1,76):
                    uno.comp_cards_color.append(self.colors[random.randint(1, 4)])
                    uno.comp_cards_number.append(random.randint(0, 9))
            if card_type in range(73,81):
                uno.comp_special_cards_color.append(self.colors[random.randint(1,4)])
                uno.comp_special_cards_function.append("skip")
            if card_type in range(82,90):
                uno.comp_special_cards_color.append(self.colors[random.randint(1,4)])
                uno.comp_special_cards_function.append("reverse")
            if card_type in range(91,99):
                uno.comp_special_cards_color.append(self.colors[random.randint(1,4)])
                uno.comp_special_cards_function.append("draw 2")
            if card_type in range(100,104):
                uno.comp_special_cards_function.append("null")
                uno.comp_cards_color.append("wild")
            if card_type in range(105,109):
                uno.comp_special_cards_color.append("wild")
                uno.comp_special_cards_function.append("draw_4")
            # This game can get a LOT of cards FAST
        print("Your new total: ")
        print(len(self.your_cards_number))
        uno.comp_turn()


    def comp_turn(self):
        print("First card is: ")
        print(self.first_card_color)
        print(self.first_card_number)
        if self.first_card_number in self.comp_cards_number:
            comp_index = self.comp_cards_number.index(self.first_card_number)
            print("The computer plays: ")
            print(self.comp_cards_number[comp_index])
            print(self.comp_cards_color[comp_index])
            self.first_card_number = self.comp_cards_number[comp_index]
            self.first_card_color = self.comp_cards_color[comp_index]
            self.comp_cards_color.pop(comp_index)
            self.comp_cards_number.pop(comp_index)
            if len(self.comp_cards_number) == 0:
                print("Computer wins!")
            # This fun line is to prevent stack overflow errors from recursion (:
            elif len(self.comp_cards_number) > 66:
                print("Game is over. Player wins.")
                return 0
            else:
                count = str(len(self.comp_cards_number))
                print("The computer now has " + count + " cards left")
                uno.your_turn()
        elif len(self.comp_special_cards_function):
            color=self.comp_special_cards_color(random.randint(len(self.special_cards_color)))
            if color in self.first_card_color:
                func=self.comp_special_cards_color.index(1)
                func_type=self.comp_special_cards_function(func)
                match func_type:
                    case "draw_4":
                        uno.your_draw(4)
                    case "draw_2":
                        self.comp_cards_color.pop(func)
                        uno.your_draw(2)
                    case "null":
                        if self.comp_special_cards_color(func) is "wild":
                            if self.comp_special_cards_function(func) is "draw_four":
                                self.first_card_color==color(random.randint(1,4))
                                uno.your_turn(1,4)
                            else:
                                self.first_card_color==color(random.randint(1,4))
                self.comp_special_cards_color.pop(color.index())
                
                self.comp_special_cards_color.pop(color)
        elif self.first_card_color in self.comp_cards_color:
            comp_index = self.comp_cards_color.index(self.first_card_color)
            print("The computer plays: ")
           
                    
            print(self.comp_cards_number[comp_index])
            print(self.comp_cards_color[comp_index])
            self.first_card_number = self.comp_cards_number[comp_index]
            self.first_card_color = self.comp_cards_color[comp_index]
            self.comp_cards_number.pop(comp_index)
            self.comp_cards_color.pop(comp_index)
            count = str(len(self.comp_cards_number))
            print("The computer now has " + count + " cards left")
            uno.your_turn()
        else:
            print("The computer cannot play, and must therefore draw.")
            uno.comp_draw(1)

    def comp_draw(self, num_to_draw):
         for i in range(1,num_to_draw):
            card_type=random.randint(1,108)
            str(card_type)
            if card_type in range(1,76):
                    uno.comp_cards_color.append(self.colors[random.randint(1, 4)])
                    uno.comp_cards_number.append(random.randint(0, 9))
            if card_type in range(73,81):
                uno.comp_special_cards_color.append(self.colors[random.randint(1,4)])
                uno.comp_special_cards_function.append("skip")
            if card_type in range(82,90):
                uno.comp_special_cards_color.append(self.colors[random.randint(1,4)])
                uno.comp_special_cards_function.append("reverse")
            if card_type in range(91,99):
                uno.comp_special_cards_color.append(self.colors[random.randint(1,4)])
                uno.comp_special_cards_function.append("draw 2")
            if card_type in range(100,104):
                uno.comp_special_cards_function.append("wild")
                uno.comp_cards_color.append("wild")
            if card_type in range(105,109):
                uno.comp_special_cards_color.append("wild")
                uno.comp_special_cards_function.append("draw_4")
            # This game can get a LOT of cards FAST
         print("comp new total: ")
         print(len(self.comp_cards_number))
         uno.your_turn()


    def init(self):
        uno.comp_deal()
        uno.your_deal()
        print("Now flipping a coin to see who goes first...")


uno = UNO()
uno.init()
