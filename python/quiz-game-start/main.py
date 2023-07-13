from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for i in question_data:
    question = i['question']
    answer = i['correct_answer']
    new_object = Question(question, answer)
    question_bank.append(new_object)

quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()

quiz.final()
