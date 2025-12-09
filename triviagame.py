'''
This program uses tkinter to run a game in a graphical user interface. The user
is presented first with a welcome page, then many various scenarios. Each choice
they make brings them to a different page, where they either achieve an ending
or are presented with another choice.
'''
from tkinter import * #Import all of tkinter 
from tkinter import font as tkfont
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
        for F in (welcomePage,instructions,firstChoice,firstLeftChoice,firstCenterChoice,firstRightChoice,leftLeftChoice,leftRightChoice,rightOcean,rightPassageway,amuletEnding,rightHut,knock,centerLeftDoor,centerRightDoor,centerCenterDoor):
            page_name=F.__name__
            frame=F(parent=container,controller=self,root=self) # Current frame with specified parameters
            self.frames[page_name]=frame
            frame.grid(row=0,column=0,sticky='nsew')
            
        self.show_frame('welcomePage')

                                                
    def show_frame(self,page_name): #brings a specified frame to the front of the display
        frame=self.frames[page_name]
        frame.tkraise()

                                                
class welcomePage(Frame):              
    def __init__(self,parent,controller,root):

        Frame.__init__(self,parent) # Enables it where it initializes the frame as well as 
        self.controller=controller
        self.root=root #defines the root of the game
        title=Label(self,text='Escape the Dungeon',font=controller.title_font)
        title.pack()
        welcomeMessage=Label(self,text="Escape the dungeon, if you dare.\nMake a selection below.")
        welcomeMessage.pack()
        startbutton=Button(self,text='Start',command=lambda: controller.show_frame("firstChoice"))
        startbutton.pack()
        instructions=Button(self,text='Instructions',command=lambda: controller.show_frame("instructions"))
        instructions.pack()
        siglabel=Label(self,text="Type your name here to sign our guest book!")
        siglabel.pack()
        global signature
        signature=Text(self,height=1,width=10)
        signature.pack()
        name=StringVar()
        sign=Button(self,text='Sign',command=lambda: guest_book(controller,self))
        sign.pack()
        invalid=Label(self,text=' ')
        invalid.pack()

                                            
        def guest_book(controller,self): #used to "sign the guest book", or write the text entered by the user to a text file
                name = signature.get('1.0', 'end-1c')+'\n'
                with open('guestbook.txt', 'a') as f:
                    f.write(name)
                signature.delete('1.0','end')
                
                                            
class instructions(Frame): 
    def __init__(self,parent,controller,root):
        Frame.__init__(self,parent)
        self.controller=controller
        self.root=root
        try:
            with open('instructions.txt','r') as f: # Attempts to open instructions.txt
                instructions=f.read()   # Reads the text file
        except:
            instructions='ERROR: FILE NOT FOUND'    # If file doesn't exist, pops up with an error statement
        title=Label(self,text='Instructions',font=controller.instructions_font)
        readme=Label(self,text=instructions)
        goback=Button(self,text='Go Back',command=lambda: controller.show_frame('welcomePage')) # Enables the user to go back to the welcome page
        title.pack()
        readme.pack()
        goback.pack()

                                            
class firstChoice(Frame):
    def __init__(self,parent,controller,root):
        Frame.__init__(self,parent)
        self.controller=controller
        self.root=root #defines the root so we can use it to close the client
        scenario1=Label(self,text='You encounter three doors, all identical. What do you do?')
        scenario1.grid(row=0,column=2)
        leftdoor=Button(self,text='Left Door',command=lambda: controller.show_frame('firstLeftChoice')) # This button brings the leftdoor class to the front
        centerdoor=Button(self,text='Center Door',command=lambda: controller.show_frame('firstCenterChoice')) # This button brings the centerdoor class to the front
        rightdoor=Button(self,text='Right Door',command=lambda:controller.show_frame('firstRightChoice')) # This button brings the rightdoor class to the front
        returnToStart=Button(self,text='Return to Start',command=lambda: controller.show_frame("welcomePage")) # This button brings the start button 
        endgame=Button(self,text='End Game',command=root.destroy) # Closes the client
        restart=Button(self,text='Return to Start',command=lambda: controller.show_frame('welcomePage')) # Returns to the welcome page
        leftdoor.grid(row=2,column=1) #places the lefdoor button on the page at these coordinates; used to place almost every label and button
        centerdoor.grid(row=2,column=2)
        rightdoor.grid(row=2,column=3)
        restart.grid(row=3,column=1)
        endgame.grid(row=3,column=3)

                                            
class firstLeftChoice(Frame):
    def __init__(self,parent,controller,root):
        Frame.__init__(self,parent)
        self.controller=controller
        self.root=root #defines the root so we can use it to close the client
        scenario2=Label(self,text="You enter the left door, and discover another room with two more doors.\nThe left door is made of rough-hewn stone.\nThe right door is made of metal, and is hot to the touch.\nWhat do you do?")
        scenario2.grid(row=0,column=2)
        stonedoor=Button(self,text='Left Door',command=lambda: controller.show_frame('leftLeftChoice')) # This button brings the leftdoor class to the front   
        hotmetaldoor=Button(self,text='Right Door',command=lambda: controller.show_frame('leftRightChoice'))# This button brings the rightdoor class to the front
        restart=Button(self,text='Return to Start',command=lambda: controller.show_frame('welcomePage')) # Restarts the client to the welcome page
        endgame=Button(self,text='End Game',command=root.destroy)# Closes the client
        stonedoor.grid(row=3,column=1)
        hotmetaldoor.grid(row=3,column=3)
        restart.grid(row=4,column=1)
        endgame.grid(row=4,column=3)
                                             
class firstCenterChoice(Frame):
    def __init__(self,parent,controller,root):
        Frame.__init__(self,parent)
        self.controller=controller
        self.root=root #defines the root so we can use it to close the client
        scenario3=Label(self,text="You go down a long hallway.\nWhen you reach the end, it gets noticeably colder, and you discover three more doors.\nThe left and right doors seem to be frozen shut.\nThe center door is large and wooden. Although frosty, it looks like it will open.\nWhat do you do?")
        scenario3.grid(row=0,column=2)
        leftdoor=Button(self,text='Left Door',command=lambda:controller.show_frame('centerLeftDoor')) # This button brings the leftdoor class to the front  
        centerdoor=Button(self,text='Center Door',command=lambda:controller.show_frame('centerCenterDoor')) # This button brings the centerdoor class to the front
        rightdoor=Button(self,text='Right Door',command=lambda:controller.show_frame('centerRightDoor'))# This button brings the rightdoor class to the front
        restart=Button(self,text='Return to Start',command=lambda: controller.show_frame('welcomePage'))# Returns to the beginning or the welcome class
        endgame=Button(self,text='End Game',command=root.destroy) # Closes the client
        leftdoor.grid(row=3,column=1)
        centerdoor.grid(row=3,column=2)
        rightdoor.grid(row=3,column=3)
        restart.grid(row=4,column=1)
        endgame.grid(row=4,column=3)
                                        
class firstRightChoice(Frame):
    def __init__(self,parent,controller,root):
        Frame.__init__(self,parent)
        self.controller=controller
        self.root=root #defines the root so we can use it to close the client
        scenario4=Label(self,text="You step through the door, and the floor gives out from underneath you.\nYou fall for a few seconds, then land in a dark body of water.\nYou seem to be in some sort of cove.\nThere are torches along the shore\nAcross the water, you can see an opening that seems to lead to the ocean; the water looks rough.\nTo your right, the torches line the walls of a narrow passageway.\nOn the shoreline to your left there is a small hut. There is smoke coming out the chimney.\nWhat do you do?")
        scenario4.grid(row=1,column=2)
        ocean=Button(self,text='Try the ocean',command=lambda: controller.show_frame('rightOcean')) # This button brings the rightOcean class to the front  
        passageway=Button(self,text='Follow the passageway',command=lambda: controller.show_frame('rightPassageway'))# This button brings the rightPassageway class to the front
        hut=Button(self,text='Investigate the hut',command=lambda:controller.show_frame('rightHut')) # This button brings the rightHut class to the front
        restart=Button(self,text='Return to Start',command=lambda: controller.show_frame('welcomePage')) # Returns the user to the welcome class
        endgame=Button(self,text='End Game',command=root.destroy) # Closes the client
        ocean.grid(row=3,column=1)
        passageway.grid(row=3,column=2)
        hut.grid(row=3,column=3)
        restart.grid(row=4,column=1)
        endgame.grid(row=4,column=3)
                                    #--- Selecting the left door as the second option, intializes a different class ---
class leftLeftChoice(Frame):
    def __init__(self,parent,controller,root):
        Frame.__init__(self,parent)
        self.controller=controller
        self.root=root #defines the root so we can use it to close the client
        scenario5=Label(self,text="You force open the door, and discover a room carved out of stone. There are colored gems embedded in the wall in intricate patterns.\nAs you step in to take a closer look, the door swings shut behind you, leaving you in complete darkness.\nIn the darkness, the crystals begin to glow, and you are enamored with the beautiful mural.\nYou are so dazzled that you don't even realize you're trapped.\nGAME OVER\n(glowing tomb ending)")
        scenario5.grid(row=1,column=2)
        restart=Button(self,text='Try Again',command=lambda: controller.show_frame('welcomePage')) # Ends the game and enables the user to have a button to try again
        restart.grid(row=3,column=1)
        endgame=Button(self,text='End Game',command=root.destroy) # Closes the client
        endgame.grid(row=3,column=3)
        ending=1
        
        
        
class leftRightChoice(Frame):
    def __init__(self,parent,controller,root):
        Frame.__init__(self,parent)
        self.controller=controller
        self.root=root #defines the root so we can use it to close the client
        scenario7=Label(self,text="You enter the door, and are greeted by a very hungry fire-breathing dragon.\nFor what it's worth, the dragon is delighted to see you.\nGAME OVER\n(dragon ending)")
        scenario7.grid(row=1,column=2)
        restart=Button(self,text='Try Again',command=lambda: controller.show_frame('welcomePage')) # Ends the game and enables the user to have a button to try again
        restart.grid(row=2,column=1)
        endgame=Button(self,text='End Game',command=root.destroy) # Closes the client
        endgame.grid(row=2,column=3)

class rightOcean(Frame):
    def __init__(self,parent,controller,root):
        Frame.__init__(self,parent)
        self.controller=controller
        self.root=root #defines the root so we can use it to close the client
        scenario8=Label(self,text="You decide to swim toward the ocean. As you get closer, the water gets rougher.\nBefore you know it, the waves have carried you out to the open ocean.\nGAME OVER\n(watery grave ending)")
        scenario8.grid(row=1,column=2)
        restart=Button(self,text='Try Again',command=lambda:controller.show_frame('welcomePage')) # Button to enable the user to return to the welcome page class
        endgame=Button(self,text='End Game',command=root.destroy) # Closes the client
        restart.grid(row=2,column=1)
        endgame.grid(row=2,column=3)

class rightPassageway(Frame):
    def __init__(self,parent,controller,root):
        Frame.__init__(self,parent)
        self.controller=controller
        self.root=root #defines the root so we can use it to close the client
        scenario9=Label(self,text='You decide to follow the passageway.\nIt twists and turns, and seems to be leading you further underground.\nEventually, you reach a chamber with a pedestal in the middle of the room.\nOn the pedestal is a large gold amulet\nThe longer you look at it, the harder it is to tear your eyes away.\nWhat do you do?')
        amulet=Button(self,text='Take the amulet',command=lambda:controller.show_frame('amuletEnding')) # Button to pursue the amulet to enter the "amulet ending" taking you to a different class
        scenario9.grid(row=1,column=2)
        amulet.grid(row=2,column=2)

class amuletEnding(Frame):
    def __init__(self,parent,controller,root):
        Frame.__init__(self,parent)
        self.controller=controller
        self.root=root #defines the root so we can use it to close the client
        amulet=Label(self,text='The amulet consumes you, and you are grateful for it.\nGAME OVER\n(amulet ending)') # Pursuit of the amulet button 
        restart=Button(self,text='Try Again',command=lambda:controller.show_frame('welcomePage')) # Enables the user to return to the welcome page
        endgame=Button(self,text='End Game',command=root.destroy) # Closes the client 
        amulet.grid(row=1,column=2)
        restart.grid(row=2,column=1)
        endgame.grid(row=2,column=3)

class rightHut(Frame):
    def __init__(self,parent,controller,root):
        Frame.__init__(self,parent)
        self.controller=controller
        self.root=root #defines the root so we can use it to close the client
        scenario10=Label(self,text="You decide to approach the hut.\nAs you get closer, you smell something delicious.\nYou can hear someone moving inside.\nWhat do you do?")
        knock=Button(self,text='Knock on the door',command=lambda:controller.show_frame('knock')) # Button for the user to go to the "knock" class
        ocean=Button(self,text='Try the ocean instead',command=lambda:controller.show_frame('rightOcean')) # Button for the user to go to the "right Ocean" class
        passageway=Button(self,text='Follow the passageway instead',command=lambda:controller.show_frame('rightPassageway')) # Button for the user to go to the "right Passage way" class
        restart=Button(self,text='Return to Start',command=lambda:controller.show_frame('welcomePage'))# Allows the user to return to the welcome class page 
        endgame=Button(self,text='End Game',command=root.destroy) # Closes page
        scenario10.grid(row=1,column=2)
        knock.grid(row=2,column=1)
        ocean.grid(row=2,column=2)
        passageway.grid(row=2,column=3)
        restart.grid(row=3,column=1)
        endgame.grid(row=3,column=3)

class knock(Frame):
    def __init__(self,parent,controller,root):
        Frame.__init__(self,parent)
        self.controller=controller
        self.root=root #defines the root so we can use it to close the client
        knock=Label(self,text='You knock on the door, and an old woman answers it; she is overjoyed to have a visitor.\nShe invites you in, and offers you a bowl of what she is cooking.\nYou heartily agree, and she puts a large bowl of stew on the table in front of you.\nYou dig in, and you enjoy every last drop. At the bottom of the bowl, you discover a human toe.\nHorrified, you look back to the woman, to see her dumping a bowl of meat into the pot.\nShe gives you a knowing look, and offers you more. You accept.\nGAME OVER\n(cannibalism ending)')
        restart=Button(self,text='Try Again',command=lambda:controller.show_frame('welcomePage')) # Game ends and button allows the user to return to the welcome page 
        endgame=Button(self,text='End Game',command=root.destroy) # Closes client
        knock.grid(row=1,column=2)
        restart.grid(row=2,column=1)
        endgame.grid(row=2,column=3)

class centerLeftDoor(Frame):
    def __init__(self,parent,controller,root):
        Frame.__init__(self,parent)
        self.controller=controller
        self.root=root #defines the root so we can use it to close the client
        doorfailure=Label(self,text='The door is frozen shut. It might be worth trying a different door.')
        centerdoor=Button(self,text='Center Door',command=lambda:controller.show_frame('centerCenterDoor')) # Button for the user to go to the "Center center door" class
        rightdoor=Button(self,text='Right Door',command=lambda:controller.show_frame('centerRightDoor')) # Button for the user to go to the "Center right door" class
        restart=Button(self,text='Return to Start',command=lambda:controller.show_frame('welcomePage'))# Button for the user to retry and to head to the welcome page class
        endgame=Button(self,text='End Game',command=root.destroy)# Closes the client
        doorfailure.grid(row=1,column=2)
        centerdoor.grid(row=2,column=1)
        rightdoor.grid(row=2,column=3)
        restart.grid(row=3,column=1)
        endgame.grid(row=3,column=3)

class centerRightDoor(Frame):
    def __init__(self,parent,controller,root):
        Frame.__init__(self,parent)
        self.controller=controller
        self.root=root #defines the root so we can use it to close the client
        doorfailure=Label(self,text='The door is frozen shut. It might be worth trying a different door.')
        leftdoor=Button(self,text='Left Door',command=lambda:controller.show_frame('centerLeftDoor')) # Button for the user to go to the "center left door" class
        centerdoor=Button(self,text='Center Door',command=lambda:controller.show_frame('centerCenterDoor')) # Button for the user to go to the "center center door" class
        restart=Button(self,text='Return to Start',command=lambda:controller.show_frame('welcomePage')) # Button to return to the welcome page class
        endgame=Button(self,text='End Game',command=root.destroy) # Closes the client
        doorfailure.grid(row=1,column=2)
        leftdoor.grid(row=2,column=1)
        centerdoor.grid(row=2,column=3)
        restart.grid(row=3,column=1)
        endgame.grid(row=3,column=3)

class centerCenterDoor(Frame):
    def __init__(self,parent,controller,root):
        Frame.__init__(self,parent)
        self.controller=controller
        self.root=root #defines the root so we can use it to close the client
        scenario11=Label(self,text="You push open the door, and are temporarily blinded by bright sunlight. A gust of freezing air blows through the door.\nYou step through the door, and find yourself in a snowy tundra.\nYou go to turn around, and discover that the door is gone.\nYou won't last long out here.\nGAME OVER\n(frozen ending)")
        restart=Button(self,text='Try Again',command=lambda:controller.show_frame('welcomePage')) # Button to return to the welcome page class
        endgame=Button(self,text='End Game',command=root.destroy) # Closes the client
        scenario11.grid(row=1,column=2)
        restart.grid(row=2,column=1)
        endgame.grid(row=2,column=3)

root=MainGame()
root.mainloop()
