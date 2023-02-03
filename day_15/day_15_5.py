from day_15_2 import Question
from day_15_3 import question_data
from day_15_4 import QuizBrain
import random

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
    print("You have completed the quiz.")
    print(f"Your final score is: {quiz.score}/{len(question_bank)}")

