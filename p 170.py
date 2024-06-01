from tkinter import *

root = Tk()
root.geometry("600x600")

pg3 = Label(root)
pg5 = Label(root)
pg10 = Label(root)

class grade_3():
    def __init__(self,la,math):
        self.la = la
        self.math = math
        
    def percentage(self):
        total_marks = self.la+self.math
        total_marks_100 = total_marks*100
        g3p = total_marks_100/200
        pg3["text"] = g3p
        
class grade_5():
    def __init__(self,la,math,ss):
        self.la = la
        self.math = math
        self.ss = ss
        
    def percentage(self):
        total_marks = self.la+self.math+self.ss
        total_marks_100 = total_marks*100
        g5p = total_marks_100/300
        pg5["text"] = g5p
        
class grade_10():
    def __init__(self,la,math,ss,eco):
        self.la = la
        self.math = math
        self.ss = ss
        self.eco = eco
        
    def percentage(self):
        total_marks = self.la+self.math+self.ss+self.eco
        total_marks_100 = total_marks*100
        g10p = total_marks_100/400
        pg10["text"] = g10p
        


og3 = grade_3(78, 89)
g3b = Button(root,text = "grade_3",command=og3.percentage)
g3b.pack()
pg3.pack()

og5 = grade_5(78, 89,90)
g5b = Button(root,text = "grade_5",command=og5.percentage)
g5b.pack()
pg5.pack()

og10 = grade_10(78, 89, 90, 97)
g10b = Button(root,text = "grade_10",command=og10.percentage)
g10b.pack()
pg10.pack()

root.mainloop()







