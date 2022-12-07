from question_model import *
from data import *
from quiz_brain import *
quiz_bank = []

for i in range(len(question_data)):
    q = Question(question_data[i]["text"], question_data[i]["answer"])
    quiz_bank.append(q)


new_quiz = QuizBrain(quiz_bank)
while new_quiz.has_question():
    new_quiz.next_question()
print(f"you have completed the quiz \n your final score is {new_quiz.score}")
