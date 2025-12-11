from tkinter import * #Import all of tkinter 
from tkinter import font as tkfont
import datetime
class MainGame(Tk): # Creates the GUI and catalogs and sets up the other classes
    def __init__(self,*args,**kwargs): # Takes itself, arguments, and keyword arguments
        Tk.__init__(self,*args,**kwargs) # Initializes itself, arguments, and keyword arguments
        
                                                
        self.title_font=tkfont.Font(family='Engravers MT',size=18,weight='bold') #title font set up here to be called in welcomePage
        self.instructions_font=tkfont.Font(family='Baskerville Old Face',size=14,weight='bold')
        
                                                
        container=Frame(self) #sets up the size of the window for the game
        container.pack(side="top",fill="both",expand=True)
        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0,weight=1)

                                                
        self.frames= {} #stores the frames in the empty dictionary
        for F in (welcomePage,homePage,sports1,sports2,locations1,locations2,symbols1,symbols2,lighthouses1,lighthouses2,incorrect,correct):
            page_name=F.__name__
            frame=F(parent=container,controller=self,root=self) # Current frame with specified parameters
            self.frames[page_name]=frame
            frame.grid(row=0,column=0,sticky='nsew')
            
        self.show_frame('welcomePage')

    score = 0

    def show_frame(self,page_name): #brings a specified frame to the front of the display
        frame=self.frames[page_name]
        frame.tkraise()

    def savenQuit(controller,self,root):
        date=datetime.datetime.now()
        scoreEntry = f"User played on {date} and earned {MainGame.score} points.\n"
        with open('scores.txt', 'a') as f:
            f.write(scoreEntry)
        root.destroy()
        
   
    def correctAnswer(controller,self):
        MainGame.score+=1
        correct_frame = controller.frames["correct"]
        correct_frame.points.config(text=f'Score: {MainGame.score} point(s)')
        controller.show_frame("correct")
                                                
class welcomePage(Frame):              
    def __init__(self,parent,controller,root):
        Frame.__init__(self,parent) # Enables it where it initializes the frame as well as 
        self.controller=controller
        self.root=root #defines the root of the game
        title=Label(self,text='Welcome to Our Trivia Game!',font=controller.title_font)
        title.pack()
        welcomeMessage=Label(self,text="Click Start to Test Your Trivia Knowledge!")
        welcomeMessage.pack()
        startbutton=Button(self,text='Start',command=lambda: controller.show_frame("homePage"))
        startbutton.pack()
        invalid=Label(self,text=' ')
        invalid.pack()

                                            
class homePage(Frame):
    def __init__(self,parent,controller,root):
        Frame.__init__(self,parent)
        self.controller=controller
        self.root=root #defines the root so we can use it to close the client
        header=Label(self,text='Please select a question from one of the categories below.')
        header.grid(row=0,column=3)

        category1=Label(self,text='Sports')
        category1.grid(row=1,column=1)
        sq1=Button(self,text='Q1',command=lambda: buttonClick(sq1,'sports1')) # switches to the sports100 frame
        sq2=Button(self,text='Q2',command=lambda: buttonClick(sq2,'sports2'))
        sq1.grid(row=2,column=1)
        sq2.grid(row=3,column=1)

        category2=Label(self,text='Locations in\nMichigan')
        category2.grid(row=1,column=2)
        lmq1=Button(self,text='Q1',command=lambda: buttonClick(lmq1,'locations1'))
        lmq2=Button(self,text='Q2',command=lambda: buttonClick(lmq2,'locations2'))
        lmq1.grid(row=2,column=2)
        lmq2.grid(row=3,column=2)

        category3=Label(self,text='Michigan\nSymbols')
        category3.grid(row=1, column=4)
        m1=Button(self,text='Q1',command=lambda: buttonClick(m1,'symbols1')) # switches to the sports100 frame
        m2=Button(self,text='Q2',command=lambda: buttonClick(m2,'symbols2'))
        m1.grid(row=2,column=4)
        m2.grid(row=3,column=4)

        category4=Label(self,text='Lighthouses')
        category4.grid(row=1,column=5)
        lq1=Button(self,text='Q1',command=lambda: buttonClick(lq1,'lighthouses1'))
        lq2=Button(self,text='Q2',command=lambda: buttonClick(lq2,'lighthouses2'))
        lq1.grid(row=2,column=5)
        lq2.grid(row=3,column=5)

        endgame=Button(self,text='Save and Quit',command=lambda: MainGame.savenQuit(controller,self,root)) # Closes the client
        endgame.grid(row=4,column=3)

        def buttonClick(button, frame):
            button.destroy()
            controller.show_frame(frame)
                                            
                                            
class sports1(Frame):
    def __init__(self,parent,controller,root):
        Frame.__init__(self,parent)
        self.controller=controller
        self.root=root #defines the root so we can use it to close the client

        question=Label(self,text="What was the name of the first stadium used by the Detroit tigers?")
        question.grid(row=0,column=2)

        answer1=Button(self,text='Comerica Park',command=lambda: controller.show_frame('incorrect')) # shows the incorrect answer page
        answer2=Button(self,text='Bennent Park',command=lambda: MainGame.correctAnswer(controller,self))
        answer3=Button(self,text='Navin Field',command=lambda: controller.show_frame('incorrect'))
        answer4=Button(self,text='Briggs Stadium',command=lambda: controller.show_frame('incorrect'))

        answer1.grid(row=1,column=1)
        answer2.grid(row=1,column=3)
        answer3.grid(row=2,column=1)
        answer4.grid(row=2,column=3)

        endgame=Button(self,text='End Game',command=root.destroy)# Closes the client
        endgame.grid(row=3,column=2)
                                             
class sports2(Frame):
    def __init__(self,parent,controller,root):
        Frame.__init__(self,parent)
        self.controller=controller
        self.root=root #defines the root so we can use it to close the client
        question=Label(self,text="Where did the Detroit Red Wings play before they moved to Little Caesars Arena?")
        question.grid(row=0,column=2)

        answer1=Button(self,text='Joe Louis Arena',command=lambda: MainGame.correctAnswer(controller,self)) # shows the incorrect answer page
        answer2=Button(self,text='Madison Square Garden',command=lambda: controller.show_frame('incorrect'))
        answer3=Button(self,text='Capital One Arena',command=lambda: controller.show_frame('incorrect'))
        answer4=Button(self,text='T-Mobile Arena',command=lambda: controller.show_frame('incorrect'))

        answer1.grid(row=1,column=1)
        answer2.grid(row=1,column=3)
        answer3.grid(row=2,column=1)
        answer4.grid(row=2,column=3)

        endgame=Button(self,text='End Game',command=root.destroy)# Closes the client
        endgame.grid(row=3,column=2)
                                        
class locations1(Frame):
    def __init__(self,parent,controller,root):
        Frame.__init__(self,parent)
        self.controller=controller
        self.root=root #defines the root so we can use it to close the client
        question=Label(self,text="What city in Michigan has the nickname \"Motor City\"?")
        question.grid(row=0,column=2)

        answer1=Button(self,text='Detroit',command=lambda: MainGame.correctAnswer(controller,self))
        answer2=Button(self,text='Grand Rapids',command=lambda: controller.show_frame('incorrect'))
        answer3=Button(self,text='Lansing',command=lambda: controller.show_frame('incorrect'))
        answer4=Button(self,text='Traverse',command=lambda: controller.show_frame('incorrect'))

        answer1.grid(row=1,column=1)
        answer2.grid(row=1,column=3)
        answer3.grid(row=2,column=1)
        answer4.grid(row=2,column=3)

        endgame=Button(self,text='End Game',command=root.destroy)# Closes the client
        endgame.grid(row=3,column=2)

class locations2(Frame):
    def __init__(self,parent,controller,root):
        Frame.__init__(self,parent)
        self.controller=controller
        self.root=root #defines the root so we can use it to close the client
        question=Label(self,text="What place in Michigan is called \"Place of the Great Turtle\"?")
        question.grid(row=0,column=2)

        answer1=Button(self,text='Tahquamenon Falls',command=lambda: controller.show_frame('incorrect'))
        answer2=Button(self,text='Pictured Rocks',command=lambda: controller.show_frame('incorrect'))
        answer3=Button(self,text='Mackinac Island',command=lambda: MainGame.correctAnswer(controller,self))
        answer4=Button(self,text='Kitch-iti-kipi',command=lambda: controller.show_frame('incorrect'))

        answer1.grid(row=1,column=1)
        answer2.grid(row=1,column=3)
        answer3.grid(row=2,column=1)
        answer4.grid(row=2,column=3)

        endgame=Button(self,text='End Game',command=root.destroy)# Closes the client
        endgame.grid(row=3,column=2)
        

class symbols1(Frame):
    def __init__(self,parent,controller,root):
        Frame.__init__(self,parent)
        self.controller=controller
        self.root=root #defines the root so we can use it to close the client
        question=Label(self,text="What is Michigan's state bird?")
        question.grid(row=0,column=2)

        answer1=Button(self,text='Cardinal',command=lambda: controller.show_frame('incorrect'))
        answer2=Button(self,text='American Robin',command=lambda: MainGame.correctAnswer(controller,self))
        answer3=Button(self,text='Blue Jay',command=lambda: controller.show_frame('incorrect'))
        answer4=Button(self,text='Mourning Dove',command=lambda: controller.show_frame('incorrect'))

        answer1.grid(row=1,column=1)
        answer2.grid(row=1,column=3)
        answer3.grid(row=2,column=1)
        answer4.grid(row=2,column=3)

        endgame=Button(self,text='End Game',command=root.destroy)# Closes the client
        endgame.grid(row=3,column=2)

class symbols2(Frame):
    def __init__(self,parent,controller,root):
        Frame.__init__(self,parent)
        self.controller=controller
        self.root=root #defines the root so we can use it to close the client
        question=Label(self,text="What is Michigan's state tree?")
        question.grid(row=0,column=2)

        answer1=Button(self,text='Tropical Palm',command=lambda: controller.show_frame('incorrect'))
        answer2=Button(self,text='Cherry Blossom',command=lambda: controller.show_frame('incorrect'))
        answer3=Button(self,text='Oak Tree',command=lambda: controller.show_frame('incorrect'))
        answer4=Button(self,text='White Pine',command=lambda: MainGame.correctAnswer(controller,self))

        answer1.grid(row=1,column=1)
        answer2.grid(row=1,column=3)
        answer3.grid(row=2,column=1)
        answer4.grid(row=2,column=3)

        endgame=Button(self,text='End Game',command=root.destroy)# Closes the client
        endgame.grid(row=3,column=2)

class lighthouses1(Frame):
    def __init__(self,parent,controller,root):
        Frame.__init__(self,parent)
        self.controller=controller
        self.root=root #defines the root so we can use it to close the client
        question=Label(self,text="What was the first lighthouse built in Michigan?")
        question.grid(row=0,column=2)

        answer1=Button(self,text='Fort Gratiot Lighthouse',command=lambda: MainGame.correctAnswer(controller,self))
        answer2=Button(self,text='Round Island',command=lambda: controller.show_frame('incorrect'))
        answer3=Button(self,text='Battery Point',command=lambda: controller.show_frame('incorrect'))
        answer4=Button(self,text='Little Sable Point',command=lambda: controller.show_frame('incorrect'))

        answer1.grid(row=1,column=1)
        answer2.grid(row=1,column=3)
        answer3.grid(row=2,column=1)
        answer4.grid(row=2,column=3)

        endgame=Button(self,text='End Game',command=root.destroy)# Closes the client
        endgame.grid(row=3,column=2)

class lighthouses2(Frame):
    def __init__(self,parent,controller,root):
        Frame.__init__(self,parent)
        self.controller=controller
        self.root=root #defines the root so we can use it to close the client
        question=Label(self,text="What is the tallest lighthouse in Michigan?")
        question.grid(row=0,column=2)

        answer1=Button(self,text='Round Island',command=lambda: controller.show_frame('incorrect'))
        answer2=Button(self,text='Rock of Ages',command=lambda: MainGame.correctAnswer(controller,self))
        answer3=Button(self,text='Charity Island',command=lambda: controller.show_frame('incorrect'))
        answer4=Button(self,text='Mackinac Point',command=lambda: controller.show_frame('incorrect'))

        answer1.grid(row=1,column=1)
        answer2.grid(row=1,column=3)
        answer3.grid(row=2,column=1)
        answer4.grid(row=2,column=3)

        endgame=Button(self,text='End Game',command=root.destroy)# Closes the client
        endgame.grid(row=3,column=2)

class incorrect(Frame):
    def __init__(self,parent,controller,root):
        Frame.__init__(self,parent)
        self.controller=controller
        self.root=root #defines the root so we can use it to close the client
        msg=Label(self,text="Sorry, that's incorrect")
        
        moveon=Button(self,text='Continue',command=lambda:controller.show_frame('homePage'))
        endgame=Button(self,text='End Game',command=root.destroy) # Closes page
        msg.grid(row=1,column=2)
        moveon.grid(row=2,column=1)
        endgame.grid(row=2,column=3)

class correct(Frame):
    def __init__(self,parent,controller,root):
        Frame.__init__(self,parent)
        self.controller=controller
        self.root=root #defines the root so we can use it to close the client
        msg=Label(self,text='Correct! You\'ve earned one point!')
        self.points=Label(self,text='') #self.points so it can be called by other classes, if i remove the "self" it only exists in the context of __init__
        filler=Label(self,text='                        ')
        moveon=Button(self,text='Continue',command=lambda:controller.show_frame('homePage')) 
        endgame=Button(self,text='End Game',command=root.destroy) # Closes the game
        msg.grid(row=1,column=3)
        self.points.grid(row=2,column=3)
        filler.grid(row=3,column=1)
        moveon.grid(row=3,column=2)
        endgame.grid(row=3,column=4)

root=MainGame()
root.mainloop()