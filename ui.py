THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain

class QuizInterface:
    def __init__(self, quiz_brain:QuizBrain):
        self.quiz=quiz_brain
        self.window=Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20,pady=20, bg=THEME_COLOR)
        self.score_label=Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)
        self.canvas=Canvas(width=300, height=250,bg= "white")
        self.question_text=self.canvas.create_text(
            150,
            125,
            width=280,
            text="bla bla bla",
            fill=THEME_COLOR,
            font=("Arial",20,"italic")
        )

        self.canvas.grid(row=1,column=0,columnspan=2, pady=50)
        true_image=PhotoImage(file="images/true.png")
        self.true_button=Button(image=true_image, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(row=2,column=0)
        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0,command=self.false_pressed)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()


        # print(self.quiz.current_question.answer)
        self.window.mainloop()


    def get_next_question(self):
        self.canvas.config(bg="white")
        if (self.quiz.question_number)==10:
            self.score_label.config(text=f"Score: {self.quiz.score}")
            self.canvas.itemconfig(self.question_text, text="The End")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
        else:
            q_text = self.quiz.next_question()
            self.score_label.config(text=f"Score: {self.quiz.score}")
            self.canvas.itemconfig(self.question_text, text=q_text)

    def true_pressed(self):
        is_right= self.quiz.check_answer("true")
        # print(is_right)
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right=self.quiz.check_answer("false")
        # print (is_right)
        self.give_feedback(is_right)

    def give_feedback(self,is_right):
        if is_right==True:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

