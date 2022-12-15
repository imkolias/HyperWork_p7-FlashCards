# Write your code here


class FlashCard:

    def __init__(self, card_ql, card_al):
        self.questionsl = card_ql
        self.answersl = card_al

    def ask_question(self, question):
        print(f'Print the definition of "{question}"')
        return input()

    def check_answer(self, question, answer):
        if question == answer:
            print("Correct!")
        else:
            print(f'Wrong. The right answer is "{answer}"')

    def begingame(self):
        if len(self.questionsl) != len(self.answersl):
            print("Missing items in Q or A list")
            exit()
        for n in range(len(self.questionsl)):
            self.check_answer(self.ask_question(self.questionsl[n]), self.answersl[n])


class Setup:
    q_list = []
    a_list = []
    q_count = 0

    def __init__(self):
        print("Input the number of cards:")
        self.q_count = int(input())
        for n in range(self.q_count):
            print(f"The term for card #{n+1}")
            self.q_list.append(input())
            print(f"The definition for card #{n+1}")
            self.a_list.append(input())


fg_config = Setup()
first_game = FlashCard(fg_config.q_list, fg_config.a_list)

first_game.begingame()
