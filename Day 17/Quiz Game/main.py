from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
question_datas = question_data

for i in question_datas:
    question_bank.append(Question(i["text"], i["answer"]))

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{len(quiz.question_list)}")