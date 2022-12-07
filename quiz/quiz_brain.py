class QuizBrain:

    def __init__(self, question_list):
        self.question_num = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        current_answer = self.question_list[self.question_num].answer
        question_text = self.question_list[self.question_num].text
        self.question_num += 1
        user_answer = input(f"Q.{self.question_num + 1} {question_text} (True or False)")
        self.check(user_answer, current_answer)


    def check(self, user, q_answer):
        if user == q_answer:
            self.score += 1
            print(f"well done\n your score {self.score}")
        else :
            print(f"you lose \n your score : {self.score} ")

    def has_question(self):
      return  self.question_num < len(self.question_list)