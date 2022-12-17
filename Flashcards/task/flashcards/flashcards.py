# FlashCard simple game
import json
import os
import random
import logging
import argparse

def cinput():
    temp_val = input()
    logging.debug(temp_val)
    return temp_val


def cprint(arg):
    print(arg)
    logging.debug(arg)


class FlashCard:
    need_to_save = 0
    cards_list = dict()
    wrong_list = dict()

    def __init__(self):

        parser = argparse.ArgumentParser("FlashGame")
        parser.add_argument("--import_from")
        parser.add_argument("--export_to")

        self.arg_data = parser.parse_args()

        if self.arg_data.import_from:
            self.saveload("i", self.arg_data.import_from)
        if self.arg_data.export_to:
            self.need_to_save = 1

    def add_card(self):

        cprint("The card:")
        qdata = cinput()
        while True:

            if qdata in self.cards_list.keys():
                cprint('The <term/definition> already exists. Try again:')

                cprint("The card:")
                qdata = cinput()

            else:
                break

        cprint("The definition of the card:")
        adata = cinput()
        while True:
            if adata in self.cards_list.values():
                cprint('The <term/definition> already exists. Try again:')
                cprint("The definition of the card:")
                adata = cinput()
            else:
                break

        self.cards_list[qdata] = adata
        cprint(f'The pair ("{qdata}":"{adata}") has been added.')

    def remove_card(self):
        cprint("Which card?")
        adata = cinput()
        if adata not in self.cards_list.keys():
            cprint(f'Can\'t remove "{adata}": there is no such card.')
        else:
            self.cards_list.pop(adata)
            cprint("The card has been removed.")

    def ask_question(self):

        cprint("How many times to ask?")
        try_number = int(cinput())
        if len(self.cards_list.items()) > 0:
            for _ in range(try_number):
                sel_qa_item = random.choice(list(self.cards_list.items()))
                cprint(f'Print the definition of "{sel_qa_item[0]}"')
                u_answer = cinput()
                self.check_answer(u_answer, sel_qa_item[1], sel_qa_item[0])

    def check_answer(self, u_answer, right_answer, question):
        if u_answer == right_answer:
            cprint("Correct!")
        elif u_answer in self.cards_list.values():
            wcardval = [i for i, v in self.cards_list.items() if v == u_answer]
            cprint(f'Wrong. The right answer is "{right_answer}", but your definition is correct for "{wcardval[0]}".')
            self.add_wrong_answer(u_answer)
        else:
            cprint(f'Wrong. The right answer is "{right_answer}"')
            self.add_wrong_answer(question)

    def saveload(self, action, file_name=""):
        if action == "i":
            if file_name == "":
                cprint("File name:")
                file_name = cinput()
            if os.path.exists(file_name):
                with open(file_name) as js_f:
                    self.cards_list = json.load(js_f)
                    cprint(f"{len(self.cards_list)} cards have been loaded")
            else:
                cprint("File not found.")

        elif action == "e":
            if file_name == "":
                cprint("File name:")
                file_name = cinput()
            with open(file_name, "w") as js_f:
                json.dump(self.cards_list, js_f)
                cprint(f"{len(self.cards_list)} cards have been saved")

    def add_wrong_answer(self, wrong_answer):
        if wrong_answer not in self.wrong_list:
            self.wrong_list[wrong_answer] = 1
        else:
            self.wrong_list[wrong_answer] += 1

    def show_hardestcard(self):
        # print(self.wrong_list.items())
        if len(self.wrong_list) == 0:
            cprint("There are no cards with errors")
        else:
            if len(self.wrong_list) == 1:
                cprint(f'The hardest card is "{str(*self.wrong_list.keys())}". '
                       f'You have {str(*self.wrong_list.values())} errors answering it.')
            else:
                errdict = sorted(self.wrong_list.items(), key=lambda x: (x[1], x[0]), reverse=True)

                if errdict[0][1] == errdict[1][1]:
                    cprint(f'The hardest cards are "{errdict[0][0]}", "{errdict[1][0]}"')
                else:
                    cprint(f'The hardest card is "{errdict[0][0]}". You have {errdict[0][1]} errors answering it.')
                    logging.debug(errdict, errdict[0][0], errdict[0][1])

    def reset_stats(self):
        self.wrong_list.clear()
        cprint("Card statistics have been reset.")

    def logging_start(self):
        cprint("File name:")
        log_file_name = cinput()

        with open("temp.log") as tmp_log:
            with open(log_file_name, "a") as log_file:
                log_file.writelines(tmp_log.readlines())
        cprint("The log has been saved.")

    def show_menu(self):
        while True:
            cprint("Input the action (add, remove, import, export, ask, exit, log, hardest card, reset stats):")
            u_select = cinput()

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
            elif u_select == "hardest card":
                self.show_hardestcard()
            elif u_select == "reset stats":
                self.reset_stats()
            elif u_select == "log":
                self.logging_start()

            elif u_select == "exit":
                if self.need_to_save == 1:
                    self.saveload("e", self.arg_data.export_to)
                cprint("bye bye")
                exit()


logging.basicConfig(filename="temp.log",
                    filemode='a',
                    format='%(asctime)s | %(levelname)s: %(message)s',
                    level='DEBUG')


first_game = FlashCard()
first_game.show_menu()
