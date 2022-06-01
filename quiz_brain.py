
class QuizBrain:
    
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.correct = 0

    def check_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_ans = input(F"Q.{self.question_number}. {current_question.text}? (True / False) ")
        self.check_answer(user_ans, current_question.answer)


    def check_answer(self, user_ans, correct_ans):  
        if user_ans.title() == correct_ans.title():
            print('Correct, that is right')
            self.correct += 1
        else:
            print('Wrong')
            print(f"The correct answer was {correct_ans}")
        print(f'You have answered {self.correct} / {self.question_number} correct')
        print('\n')

    def final_score(self):
        print('Congratulations, You have completed the quiz!')
        print(f"Your final score is {self.correct} / {len(self.question_list)}")