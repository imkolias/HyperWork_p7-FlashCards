# FlashCard simple game

class Setup:
    q_list = []
    a_list = []
    q_count = 0

    def __init__(self):
        print("Input the number of cards:")
        self.q_count = int(input())
        for n in range(self.q_count):

            print(f"The term for card #{n+1}")
            qdata = input()
            while True:
                if qdata in self.q_list:
                    print(f'The term "{qdata}" already exists. Try again:')
                    qdata = input()
                else:
                    self.q_list.append(qdata)
                    break

            print(f"The definition for card #{n + 1}")
            adata = input()
            while True:
                if adata in self.a_list:
                    print(f'The definition "{adata}" already exists. Try again:')
                    adata = input()
                else:
                    self.a_list.append(adata)
                    break

class FlashCard:

    def __init__(self, card_ql, card_al):
        self.questionsl = card_ql
        self.answersl = card_al

    def ask_question(self, question):
        print(f'Print the definition of "{question}"')
        return input()

    def check_answer(self, u_answer, right_answer):
        if u_answer == right_answer:
            print("Correct!")
        elif u_answer in self.answersl:
            print(f'Wrong. The right answer is "{right_answer}", but your definition is correct for "{self.questionsl[self.answersl.index(u_answer)]}".')
        else:
            print(f'Wrong. The right answer is "{right_answer}"')


    def begingame(self):
        if len(self.questionsl) != len(self.answersl):
            print("Missing items in Q or A list")
            exit()

        for n in range(len(self.questionsl)):
            self.check_answer(self.ask_question(self.questionsl[n]), self.answersl[n])







fg_config = Setup()
first_game = FlashCard(fg_config.q_list, fg_config.a_list)

first_game.begingame()
