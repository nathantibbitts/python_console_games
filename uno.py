import random
class UNO:
    comp_cards_color = []
    comp_cards_number = []
    first_color = ""
    first_number = 0
    colors = ["red", "yellow", "green", "blue"]
    first_card_color = colors[random.randrange(1, 4)]
    first_card_number = random.randrange(0, 9)
    your_cards_number = []
    your_cards_color = []
    def turnpicker(self):
        turn=random.randrange(0,2)
        str_turn=str(turn)
        print("The number is " + str_turn)
        if turn==1:
            print("CT!")
            uno.comp_turn()
        else:
            print("YT!")
            uno.your_turn
    def your_deal(self):
        for i in range(0, 6):
            self.your_cards_number.append(random.randrange(0, 9))
            self.your_cards_color.append(self.colors[random.randrange(1, 4)])
        print("Okay, your cards are: ")
        print(self.your_cards_color)
        print(self.your_cards_number)
    def your_draw(self):
        uno.your_cards_color.append(self.colors[random.randrange(1,4)])
        uno.your_cards_number.append(random.randrange(0,9))
        print("Computer card total: ")
        print(len(self.your_cards_number))
        uno.comp_turn()
    def your_turn(self):
        print(self.your_cards_number)
        print(self.your_cards_color)
        print("First card is: ")
        print(self.first_card_color)
        print(self.first_card_number)
        print("Can you play  :) ?")
        play = input()
        if play == "no":
            uno.your_draw()
        elif play == "yes" or "y":
            print(
                "Pick a card number to play, ensuring it matches the current card on the stack. Starting with 0"
            )
            draw_number = input()
            draw_number = int(draw_number)
            if (
                self.your_cards_color[draw_number] == self.first_card_color or self.your_cards_number[draw_number] == self.first_card_number
            ):
                self.first_card_color = self.your_cards_color[draw_number]
                self.first_card_number = self.your_cards_number[draw_number]
                del self.your_cards_color[draw_number]
                del self.your_cards_number[draw_number]
                print("The new card on the stack is: ")
                print(self.first_card_color)
                print(self.first_card_number)
                if not len(self.your_cards_number):
                    print("You win!")
                else:
                    print("Your cards are now: ")
                    print(self.your_cards_color)
                    print(self.your_cards_number)
                    uno.comp_turn()
            else:
                print(
                    "Silly goose, that card doesn't match, and now you forfeit a turn!"
                )
                uno.comp_turn()

    def comp_deal(self):
        for i in range(0, 6):
            self.comp_cards_number.append(random.randrange(0, 9))
            self.comp_cards_color.append(self.colors[random.randrange(1, 4)])
            comp_cards = {
                self.comp_cards_number[i]: self.comp_cards_color[i]
                for i in range(len(self.comp_cards_color))
            }

    def comp_turn(self):
        print("First card is: ")
        print(self.first_card_color)
        print(self.first_card_number)
        if self.first_card_number in self.comp_cards_number:
                comp_index=self.comp_cards_number.index(self.first_card_number)
                print("The computer plays: ")
                print(self.comp_cards_number[comp_index])
                print(self.comp_cards_color[comp_index])
                self.comp_cards_color.pop(comp_index)
                self.comp_cards_number.pop(comp_index)
                if not len(self.comp_cards_number):
                        print("Computer wins!")
                else:
                    count=str(len(self.comp_cards_number))
                    print("The computer now has "+count+" cards left")
                    uno.your_turn()

                
        elif self.first_card_color in self.comp_cards_color:
                comp_index=self.comp_cards_color.index(self.first_card_color)
               
                print("The computer plays: ")
                print(self.comp_cards_number[comp_index])
                print(self.comp_cards_color[comp_index])
                self.comp_cards_number.pop(comp_index)
                self.comp_cards_color.pop(comp_index)
                count=str(len(self.comp_cards_number))
                print("The computer now has "+count+" cards left")
                uno.your_turn()
        else:
            print("The computer cannot play, and must therefore draw.")
            uno.comp_draw()

    def comp_draw(self):
        uno.comp_cards_color.append(self.colors[random.randrange(1,4)])
        uno.comp_cards_number.append(random.randrange(0,9))
        print("Computer card total: ")
        print(len(self.comp_cards_number))
        uno.your_turn()
    def init(self):
        print("Test")
        # Place the first card, the whole output starts here
        uno.comp_deal()
        uno.your_deal()
        print("Now flipping a coin to see who goes first...")
        uno.turnpicker()
        uno.comp_turn()
uno = UNO()
uno.init()