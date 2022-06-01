from data import questions
from qustion_model import Question
from quiz_brain import QuizBrain
import random

# Create an empty List 
question_bank = []

# Shuffle the Questions 
random.shuffle(questions)

# Generate a quiz with the first 10 random questions
for question in questions[:10]:
    new_question = Question(question['text'], question['answer'])
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.check_has_questions():
    quiz.next_question()

quiz.final_score()