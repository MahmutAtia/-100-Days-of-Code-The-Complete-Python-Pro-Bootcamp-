from tkinter import *
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"



question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


class interface:
    Score = 0
    def __init__(self, quizbrain: QuizBrain):
        self.quiz = quizbrain

        self.window = Tk()
        self.window.config(bg= THEME_COLOR,pady=20, padx=20)

        self.lable = Label(text= f"Score : {interface.Score} ", bg= THEME_COLOR, fg="white")
        self.lable.grid(row=0, column=0)

        self.canvas = Canvas(height= 250 , width= 300, bg= "white")
        self.text = self.canvas.create_text(150, 125,
                                            text= self.quiz.next_question(),
                                            font= ("Ariel", 20 , "bold"), width= 200)
        self.canvas.grid(row=1,column=0, columnspan= 2, pady=50)

        imgT= PhotoImage(file= "images/true.png")
        imgF=PhotoImage(file= "images/false.png")
        self.b1 = Button(image=imgT,highlightthickness=0, command= self.true)
        self.b1.grid(row= 3, column=0)
        self.b2 = Button(image=imgF,highlightthickness=0, command= self.false)
        self.b2.grid(row=3, column=1)

        self.window.mainloop()

    def true(self):
        is_right = True
        self.give_feedback(is_right)
        self.quiz.check_answer("true")
        interface.Score+=1

    def false(self):
        is_right = False
        self.give_feedback(is_right)
        self.quiz.check_answer("false")

    def next(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.lable.config(text=f"Score : {interface.Score} " )
            self.canvas.itemconfig(self.text,text= self.quiz.next_question())
        else:
            self.canvas.itemconfig(self.text, text= "you have reached to end of the questions")

            self.b1.config(state= "disabled")
            self.b2.config(state= "disabled")

    def give_feedback(self,is_right:bool):
        if is_right == True:
            self.canvas.config(bg= "green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, func= self.next)









