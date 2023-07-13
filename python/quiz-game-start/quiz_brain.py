class QuizBrain:

    def __init__(self, q_list):
        self.answer = None
        self.question_number = 0
        self.list = q_list
        self.score = 0

    def next_question(self):
        self.answer = input(f"Q{self.question_number+1} {self.list[self.question_number].text}. (True/False)? ")
        while not self.answer == "true" and not self.answer == "false":
            print("Incorrect input. Try again.")
            self.answer = input(f"Q{self.question_number + 1} {self.list[self.question_number].text}. (True/False)? ")
        else:
            self.check_answer(self.answer)
            self.question_number += 1

    def still_has_question(self):
        return self.question_number < len(self.list)
#     Tommy, notice that len(self.list) == 12, but self.question_number (or the index number) won't be larger than 11.
#     Therefore, index_number < length must exhaust all the iterables

    def check_answer(self, answer):
        if self.list[self.question_number].answer.lower() == answer.lower():
            print(f"You got it! The correct answer is {self.list[self.question_number].answer}")
            self.score += 1
            print(f"Your current score is {self.score}/{self.question_number+1}")
        else:
            print(f"You missed it. The correct answer is {self.list[self.question_number].answer}")
            print(f"Your current score is {self.score}/{self.question_number+1}")
        print("\n")


    def final(self):
        print (f"The final round is completed\nYour final score is {self.score}")

# TODO 1: asking the que stions
# TODO 2: checking if the answer was correct
# TODO 3: checking if we're at the end of the quiz

