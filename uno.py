import random
global you
global comp


first_color = ""
first_number = 0
global colors
colors = ["red", "yellow", "green", "blue"]

class UNO():
    class FirstCard:
        def draw_first_card(self, self2):
            global first_card_color
            global first_card_number   
            first_card_color = colors[random.randrange(1, 4)]
            first_card_number = random.randrange(0, 9)
            print("First card is: ")
            print(first_card_color)
            print(first_card_number)
            super(init, uno).you.your_turn()
    
    class Your_Class:
    
        global your_cards_number
        global your_cards_color
        your_cards_number = []
        your_cards_color = []
        def your_deal(self):
            for i in range(0, 6):
                your_cards_number.append(random.randrange(0, 9))
                your_cards_color.append(colors[random.randrange(1, 4)])
            print("Okay, your cards are: ")
            print(your_cards_color)
            print(your_cards_number)
        def your_turn(self):
            print("Can you play  :) ?")
            play = input()
            if play == "no":
                comp.comp_turn()
            elif play == "yes" or "y":
                print(
                    "Pick a card number to play, ensuring it matches the current card on the stack. Starting with 0"
                )
                draw_number = input()
                draw_number = int(draw_number)
                if (
                    your_cards_color[draw_number] == fc.first_card_color
                    or your_cards_number[draw_number] == fc.first_card_number
                ):
                    fc.first_card_color = your_cards_color[draw_number]
                    fc.first_card_number = your_cards_number[draw_number]
                    del your_cards_color[draw_number]
                    del your_cards_number[draw_number]
                    print("The new card on the stack is: ")
                    print(fc.first_card_color)
                    print(fc.first_card_number)

                else:
                    print(
                        "Silly goose, that card doesn't match, and now you forfeit a turn!"
                    )
                    comp.comp_turn()


    class Computer:
        global comp_cards_number
        global comp_cards_color
        comp_cards_number = []
        comp_cards_color = []

        def comp_deal(self):
            for i in range(0, 6):
                comp_cards_number.append(random.randrange(0, 9))
                comp_cards_color.append(colors[random.randrange(1, 4)])
                comp_cards = {
                    comp_cards_number[i]: comp_cards_color[i]
                    for i in range(len(comp_cards_color))
                }

        def comp_turn():
            print(comp_cards_color)
            print(comp_cards_number)
            if first_card_color in comp_cards_color:
                comp_cards_color.index(first_card_color)

    def init(self):
        you = self.Your_Class()
        fc=self.FirstCard()
        comp=self.Computer()
        print("Test")
        # Place the first card, the whole output starts here
        comp.comp_deal()
        you.your_deal
        fc.draw_first_card(self)
        global values
        global keys
        
        global comp_cards_color
        global comp_cards_number

        values = []
        keys = []

        comp_cards_color = []
        comp_cards_number = []


uno=UNO()

uno.init()
