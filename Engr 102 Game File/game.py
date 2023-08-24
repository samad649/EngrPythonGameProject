from tkinter import *
from tkmacosx import *
from tkinter.font import Font
from functools import partial
import random


      
###this displays menu button
def menuButton(frame):
    button = CircleButton(window,text='Menu',borderless=1,radius=33,bg='#FF1E81',font=Font(family="Courier", size='23'),command=lambda:deleteFrame(frame))
    return button
        
        
        
    ####GAMES#####
def pattern(buttonFont,frame):
    frame1 = Frame(window,bg='#0F131E')
    frame1.pack(side="top",expand=True, fill="both")
    frame.pack_forget()
    #----mainmenu button----------------#
    menuButton(frame1).place(relx=.93,rely=.025)
    #------------------------------------#
    txt = 'We apologize for the inconvenience,\n but this game must be opened separately.'
    pvp = Label(frame1,text=txt,font=buttonFont,bg='#0F131E',fg='#23E1FF')
    pvp.place(relx=0,rely=.2)
    
    
    
    
    
 #----------------------------------------------------------------------------# 
####game function
def hangman(buttonFont,frame):
    global lives
    global hidden_list
    global num_lives
    global guesses
    guesses=0
    hidden_list = []
    button_identities = []
    frame.pack_forget()
    frame2 = Frame(window,bg='#0F131E')
    frame2.pack(side="top",expand=True, fill="both")
    def checker(label,word,num):
        correct=False
        global guesses
        guesses+=1
        global num_lives
        if guesses==1:
            for i in range(len(word)):
                hidden_list.append('_ ')       
        if '_ ' in hidden_list: 
            hidden=''
            global word_list
            word_list = []
            for letter in word:
                word_list.append(letter.upper())
            bname = (button_identities[num])
            letter = button_identities[num].cget('text')
            for i in range(len(word_list)):
                if word_list[i] == letter:
                    correct=True
                    hidden_list[i]=letter + " "
            for letter in hidden_list:
                        hidden+=letter 
            label.config(text=hidden)       
            bname.destroy()
        if not correct:
            num_lives-=1
        if '_ ' not in hidden_list: 
            frame2.pack_forget()
            win = Label(window,text='YOU WIN!',font=Font(family="Courier", size='60'),fg='#23E1FF',bg='#0F131E')
            win.place(relx=.1,rely=.4)
            win.config(anchor=CENTER)
        if num_lives != 0:
            attempts = 'you have '+ str(num_lives) +' lives'
            lives.config(text=attempts)
        else:
            frame2.pack_forget()
            lose = Label(window,text='YOU LOSE!',font=Font(family="Courier", size='60'),fg='#23E1FF',bg='#0F131E')
            lose.place(relx=.1,rely=.4)
            lose.config(anchor=CENTER)               
##checks if word is inputted correctly
    def buttons(guesses,word,label):
        letters=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        x = 0.32
        y = .75
        for i in range(26):
            button=CircleButton(frame2,text=letters[i],borderless=1,bg='#7874F8',font=Font(family="Courier", size='32'),command=partial(checker,label,word,i))
            button.place(relx=.075*x,rely=y)
            button_identities.append(button)
            x = x+1
            if x > 13:
                x = .32
                y = .9
    def word(word):
        guesses=0
        if word.isalpha():
            input_text.destroy()
            entry.destroy()
            done.destroy()
            length = len(word)
            hidden_word = '_ ' * length
            hangman_word = Label(frame2,text=hidden_word,font=Font(family="Courier", size='60'),fg='#23E1FF',bg='#0F131E')
            hangman_word.place(relx=.1,rely=.4)
            hangman_word.config(anchor=CENTER)  
            buttons(guesses,word,hangman_word)
        else:
            input_text['text']='Please enter a different word'
            
    #----removes main menu buttons----#
    #----places both titles of text onto screen----#
    start = Label(frame2,text='Welcome to Hangman!',bg='#0F131E',fg='#04F6E8',font=buttonFont)
    start.place(relx=.30,rely=0)
    global num_lives
    num_lives = 7
    attempts= 'you have '+ str(num_lives) +' lives'
    global lives
    lives = Label(frame2,text=attempts,bg='#0F131E',fg='#04F6E8',font=buttonFont)
    lives.place(relx=.33,rely=.17)
    
    ###########USER INPUT WORD###########
    input_text = Label(frame2,text='Enter a Word and Press Done!',bg='#0F131E',fg='#04F6E8',font=buttonFont)
    input_text.place(relx=.23,rely=.3)
    entry = Entry(frame2,font=buttonFont,width=25,bg='#C0E9F3',fg='#000000')
    entry.place(relx=.23,rely=.5)
    done = Button(frame2,font=buttonFont,width=130,height=55,bg='#7874F8',text='Done',borderless=1,command=lambda:word(entry.get()))
    done.place(relx=.8,rely=.50)
    #----This section places the alphabet buttons----#
    #------------------------------------#
    #----main-menu button----------------#
    menuButton(frame2).place(relx=.93,rely=.025)
    #------------------------------------#
    ### Displays the Letter
    #----------------------------------------------------------------------------#  
    
def guesser(buttonFont,frame):
    global random_num
    random_num = random.randint(1,100)
    print(random_num)
    def isNum(num):
        try:
            num = int(num)
            if num == random_num:
                input_text.destroy()
                entry.destroy()
                done.destroy()
                win = Label(window,text='YOU WIN!',font=Font(family="Courier", size='60'),fg='#23E1FF',bg='#0F131E')
                win.place(relx=.1,rely=.4)
                win.config(anchor=CENTER)
            elif num>random_num:
                input_text['text']='Too High'
            else:
                input_text['text']='Too Low'
                global attemptsNum
            attemptsNum+=1
            attempts['text']='Attempts: ' + str(attemptsNum)

        except:
            input_text['text']='Please enter a whole number'
            return False
        
    def guesser_game(num):
        global random
        isNum(num)      
            
    frame3 = Frame(window,bg='#0F131E')
    frame3.pack(side="top",expand=True, fill="both")
    frame.pack_forget()
    #-----------start screen-------------#
    start = Label(frame3,text='Welcome to Number Guesser!',bg='#0F131E',fg='#04F6E8',font=buttonFont)
    start.place(relx=.30,rely=0)
    input_text = Label(frame3,text='Enter a Number (1-100)!',bg='#0F131E',fg='#04F6E8',font=buttonFont)
    input_text.place(relx=.23,rely=.3)
    global attemptsNum
    attemptsNum = 0
    attemptsText = 'Attempts: ' + str(attemptsNum)
    attempts = Label(frame3,text=attemptsText,bg='#0F131E',fg='#04F6E8',font=buttonFont)
    attempts.place(relx=.39,rely=.8)
    entry = Entry(frame3,font=buttonFont,width=25,bg='#C0E9F3',fg='#000000')
    entry.place(relx=.23,rely=.5)
    done = Button(frame3,font=buttonFont,width=130,height=55,bg='#7874F8',text='Done',borderless=1,command=lambda:guesser_game(entry.get()))
    done.place(relx=.8,rely=.50)
     #----main-menu button----------------#
    menuButton(frame3).place(relx=.93,rely=.025)
    #------------------------------------#   
      
      


#### MAIN MENU SCREEN ##### 
def mainMenu(buttonFont):
    frame = Frame(window,bg='#0F131E')
    frame.pack(side="top",expand=True, fill="both")
    g1Button = CircleButton(frame,text='David\nvs\nGoliath',radius=170,borderless=1,focuscolor='',bg='#1CE1B0',activebackground='#A0F5E0',font=buttonFont,command=lambda:pattern(buttonFont,frame))
    g1Button.place(relx=.075)
    g2Button = CircleButton(frame,text='Hangman',radius=170,borderless=1,focuscolor='',bg='#EE1BFF',activebackground='#F676DD',font=buttonFont,command=lambda:hangman(buttonFont,frame))
    g2Button.place(relx=.375)
    g3Button = CircleButton(frame,text='Num Guesser',radius=170,borderless=1,focuscolor='',bg='#F7C601',activebackground='#EFD260',font=buttonFont,command=lambda:guesser(buttonFont,frame))
    g3Button.place(relx=.675)
    exitButton = CircleButton(frame,text='EXIT',radius=170,borderless=1,focuscolor='',bg='#E80033',activebackground='#DC6A83',font=buttonFont,command=window.destroy)
    exitButton.place(rely=.60)
    exitButton.place(relx=.375)

###this deletes a frame with any given frame
def deleteFrame(frame):
    frame.pack_forget()
    mainMenu(buttonFont)

    
    
 ####MAIN METHOD#####       
def main():
    global window 
    window = Tk()
    global buttonFont
    buttonFont = Font(family="Courier", size='50')
    window.title('Game')
    mainMenu(buttonFont)
    window.attributes("-fullscreen", True)
    window.configure(background='#0F131E')
    window.mainloop()
    
if __name__ == "__main__":
    main()




