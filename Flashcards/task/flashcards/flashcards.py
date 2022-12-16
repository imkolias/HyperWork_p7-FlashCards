# FlashCard simple game
import json
import os
import random


class FlashCard:
    cards_list = dict()

    def __init__(self):
        pass

    def add_card(self):

        print("The card:")
        qdata = input()
        while True:

            if qdata in self.cards_list.keys():
                print('The <term/definition> already exists. Try again:')

                print("The card:")
                qdata = input()

            else:
                break

        print("The definition of the card:")
        adata = input()
        while True:
            if adata in self.cards_list.values():
                print('The <term/definition> already exists. Try again:')
                print("The definition of the card:")
                adata = input()
            else:
                break

        self.cards_list[qdata] = adata
        print(f'The pair ("{qdata}":"{adata}") has been added.')

    def remove_card(self):
        print("Which card?")
        adata = input()
        if adata not in self.cards_list.keys():
            print(f'Can\'t remove "{adata}": there is no such card.')
            # adata = input()
        else:
            self.cards_list.pop(adata)
            print("The card has been removed.")

    def ask_question(self):
        print("How many times to ask?")
        try_number = int(input())

        for _ in range(try_number):
            sel_qa_item = random.choice(list(self.cards_list.items()))
            print(f'Print the definition of "{sel_qa_item[0]}"')
            u_answer = input()
            self.check_answer(u_answer, sel_qa_item[1])

    def check_answer(self, u_answer, right_answer):
        if u_answer == right_answer:
            print("Correct!")
        elif u_answer in self.cards_list.values():
            wcardval = [i for i, v in self.cards_list.items() if v == u_answer]
            print(f'Wrong. The right answer is "{right_answer}", but your definition is correct for "{wcardval}".')
        else:
            print(f'Wrong. The right answer is "{right_answer}"')

    def saveload(self, action):
        if action == "i":
            print("File name:")
            file_name = input()
            if os.path.exists(file_name):
                with open(file_name) as js_f:
                    self.cards_list = json.load(js_f)
                    print(f"{len(self.cards_list)} cards have been loaded")
            else:
                print("File not found.")

        elif action == "e":
            print("File name:")
            file_name = input()
            with open(file_name, "w") as js_f:
                json.dump(self.cards_list, js_f)
                print(f"{len(self.cards_list)} cards have been saved")

    def show_menu(self):
        while True:
            print("Input the action (add, remove, import, export, ask, exit):")
            u_select = input()

            if u_select == "add":
                self.add_card()
            elif u_select == "remove":
                self.remove_card()
            elif u_select == "import":
                self.saveload("i")
            elif u_select == "export":
                self.saveload("e")
            elif u_select == "ask":
                self.ask_question()
            elif u_select == "exit":
                print("bye bye")
                exit()


first_game = FlashCard()
first_game.show_menu()
