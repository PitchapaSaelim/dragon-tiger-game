from tkinter import *
from tkinter import messagebox
#I learn how to use tkinter from https://likegeeks.com/python-gui-examples-tkinter-tutorial/
from random import random
from PIL import Image, ImageTk
#Dowload PIL to open image >>> open cmd >>> pip install pillow
#I learn how to use PIL from https://python3.wannaphong.com/2014/11/image-processing-python.html

class Dragon_Tiger:  
    def __init__(self):
        self.gui = Tk()
        self.__user_chips = 10000
        self.__passConfirm = FALSE
        self.__passChoose = FALSE

        self.gui.geometry("800x600")
        self.gui.title("Dragon Tiger")
        self.gui.iconbitmap(r'img/cards1.ico')

        self.__img = Image.open("img/back_card.png")
        self.__img = self.__img.resize((int(self.__img.width * .2), int(self.__img.height * .2)))
        photo = ImageTk.PhotoImage(self.__img)

        self.__lbl = Label(image=photo)
        self.__lbl2 = Label(image=photo)
        self.__lbl.place(relx = 0.3, rely = 0.3, anchor = CENTER)
        self.__lbl2.place(relx = 0.75, rely = 0.3, anchor = CENTER)

        bets = Label(text="BET  : ")
        self.__input_bet = Entry(self.gui)
        bets.place(relx = 0.4, rely = 0.8, anchor = CENTER)
        self.__input_bet.place(relx = 0.5, rely = 0.8, anchor = CENTER)

        self.open = Button( self.gui, text="OPEN CARD", bg='black', fg='white', command=self.open_card)
        self.open.place(relx = 0.1, rely = 0.6, anchor = CENTER)
        self.dragon = Button( self.gui, text="DRAGON", bg='red', fg='white', command=self.choose_dragon)
        self.dragon.place(relx = 0.3, rely = 0.6, anchor = CENTER)
        self.tiger = Button( self.gui, text="TIGER", bg='blue', fg='white', command=self.choose_tiger)
        self.tiger.place(relx = 0.75, rely = 0.6, anchor = CENTER)
        self.tiger = Button(self.gui, text="DRAW", bg='green', fg='white', command=self.choose_draw)
        self.tiger.place(relx=0.53, rely=0.45, anchor=CENTER)
        self.check = Button(self.gui, text="CONFIRM", bg='gray', fg='white', command=self.confirm)
        self.check.place(relx=0.5, rely=0.9, anchor=CENTER)
        self.check = Button(self.gui, text="EXIT", bg='gray', fg='white', command=self.exit)
        self.check.place(relx=0.95, rely=0.95, anchor=CENTER)

        self.__chip = Label(text=f"Chips  : {self.__user_chips}")
        self.__chip.place(relx=0.05, rely=0.05, anchor=CENTER)
        self.gui.mainloop() 
    
    @property
    def user_chips(self):
        return self.__user_chips
    
    @user_chips.setter
    def user_chips(self,user_chips):
        self.__user_chips = user_chips
    
    @property
    def passConfirm(self):
        return self.__passConfirm
    
    @passConfirm.setter
    def passConfirm(self,passConfirm):
        self.__passConfirm = passConfirm
    
    @property
    def passChoose(self):
        return self.__passChoose
    
    @passChoose.setter
    def passChoose(self,passChoose):
        self.__passChoose = passChoose
    
    @property
    def img(self):
        return self.__img
    
    @img.setter
    def img(self,img):
        self.__img = img

    @property
    def lbl(self):
        return self.__lbl
    
    @lbl.setter
    def lbl(self,lbl):
        self.__lbl = lbl
    
    @property
    def lbl2(self):
        return self.__lbl2
    
    @lbl2.setter
    def lbl2(self,lbl2):
        self.__lbl2 = lbl2
    
    @property
    def input_bet(self):
        return self.__input_bet
    
    @input_bet.setter
    def input_bet(self,input_bet):
        self.__input_bet = input_bet

    def display(self):
        if self.__choose == 0:
            self.txt = Label(text="Dragon", bg="lightgreen")
            self.txt.place(relx=0.5, rely=0.7, anchor=CENTER)
            self.__passChoose = TRUE
        elif self.__choose == 1:
            self.txt = Label(text="  Tiger  ", bg="lightgreen")
            self.txt.place(relx=0.5, rely=0.7, anchor=CENTER)
            self.__passChoose = TRUE
        elif self.__choose == 2:
            self.txt = Label(text="  Draw  ", bg="lightgreen")
            self.txt.place(relx=0.5, rely=0.7, anchor=CENTER)
            self.__passChoose = TRUE
        else:
            self.txt = Label(text="Select", bg="lightgreen")
            self.txt.place(relx=0.5, rely=0.7, anchor=CENTER)


    def choose_dragon(self):
        self.__choose = 0
        self.display()
        
    def choose_tiger(self):
        self.__choose = 1
        self.display()

    def choose_draw(self):
        self.__choose = 2
        self.display()

    def confirm(self):
        self.__val = self.__input_bet.get()
        if (not(self.__val.isdigit())):
            messagebox.showerror("Error", "Not Integer Number")
        elif(not(self.__choose==1 or self.__choose==2 or self.__choose==0)):
            messagebox.showerror("Error", "Please Choose dragon OR tiger OR draw")
        else:
            try:
                if (int(self.__val)>self.__user_chips or int(self.__val)<=0):
                    messagebox.showerror("Sorry", "You have lost all your chips.")
                else:
                    messagebox.showinfo("Success", "Bet Successful")
                    self.__passConfirm=TRUE
            except ValueError:
                messagebox.showerror("Error", "Error message")

    def open_card(self):
        from random import randint
        if(self.__passConfirm == TRUE and self.__passChoose == TRUE):
            Dragon = randint(1,13)
            Tiger = randint(1,13)

            opDragon = randint(1,4)
            opTiger = randint(1,4)

            self.imgDra = Image.open("img/cards/"+str(Dragon)+"_"+str(opDragon)+".PNG")
            self.photoDra = ImageTk.PhotoImage(self.imgDra)
            self.imgTi = Image.open("img/cards/"+str(Tiger)+"_"+str(opTiger)+".PNG")
            self.photoTi = ImageTk.PhotoImage(self.imgTi)
            self.__lbl = Label(image=self.photoDra)
            self.__lbl1 = Label(image=self.photoTi)
            self.__lbl.place(relx=0.3, rely=0.3, anchor=CENTER)
            self.__lbl1.place(relx=0.75, rely=0.3, anchor=CENTER)

            win = 99
            if(Dragon<Tiger):
                win = 1
            elif (Dragon>Tiger):
                win = 0
            elif (Dragon==Tiger):
                win = 2

            if (self.__choose==win):
                if(win!=2):
                    self.__val = int(self.__val) * 1
                else:
                    self.__val = int(self.__val) * 7
                self.__user_chips = self.__user_chips + int(self.__val)
                messagebox.showinfo("You Win", " + "+str(self.__val)+" Chips")
            else:
                if (win != 2):
                    self.__user_chips = self.__user_chips - int(self.__val)
                    messagebox.showinfo("You Lose", " - " + str(self.__val) + " Chips")
                else:
                    self.__user_chips = self.__user_chips - (int(self.__val)/2)
                    messagebox.showinfo("You Lose", " - " + str((int(self.__val)/2)) + " Chips")


            self.__chip1 = Label(text=f"Chips   :  {self.__user_chips}  ")
            self.__chip1.place(relx=0.05, rely=0.05, anchor=CENTER)
            self.__passChoose = FALSE
            self.__passConfirm = FALSE
            self.__choose = 99
            self.display()

        else:
            messagebox.showerror("Error", "Betting  Unsuccessful")

    def exit(self):
        self.gui.destroy()

