from tkinter import *

top = Tk()
playList = []

def results():
   print(playlist)



def exportList():
    with open('test.txt', 'w') as f:
        for item in playlist:
            f.write("%s\n" % item)

def clearWindow():
    for widgets in top.winfo_children():
        widgets.destroy()

def mainMenu():
    clearWindow()
    LMain = Label(top, text = "Block 5 GUI Projects")
    LMain.grid(column = 2, row = 1)
    
    B1Main = Button(text = "Week 1", bg = "white", command = week1)
    B1Main.grid(column = 2, row = 2)
    
    B2Main = Button(text = "Week 2", bg = "white", command = week2)
    B2Main.grid(column = 2, row = 3)
    
    B3Main = Button(text = "Week 3", bg = "white")
    B3Main.grid(column = 2, row = 4)

def week1():
    def addToList():
        newItem = E1.get()
        playList.append(newItem)
        E1.delete(0, END)
    
    clearWindow()
    #This is a Label widget
    L1 = Label(top, text = "Playlist Maker")
    L1.grid(column = 0, row = 1)

    #This is a Entry widget
    E1 = Entry(top, bd = 5)
    E1.grid(column = 0, row = 2)

    #This is a Button widget
    B1 = Button(text = "    Print Playlist    ", bg = "#c6edee", command = results)
    B1.grid(column = 0, row = 3)

    B2 = Button(text = " + ", bg = "#feebe5", command = addToList)
    B2.grid(column = 1, row = 2)

    B3 = Button(text = "Export List", bg = "white", command = exportList)
    B3.grid(column = 0, row = 4)
    
    Bclear = Buutton(text = " mainMenu ", bg = "white", command = mainMenu)
    Bclear.grid(colunm = 3, row = 1)

def week2():
    clearWindow()
    L1W2 = Lable(top, text = "Dice Roller Program")
    L1W2.grid(column = 0, row = 1)
    
    L2W2 = Lable(top, text = "How many sides?")
    L2W2.grid(column = 0, row = 2)
    
    L3W2 = Lable(top, text = "How many rolls?")
    L3W2.grid(column = 2, row = 2)
    
    E1W2 = Entry(top, bd = 5)
    E1W2.grid(column = 0, row = 3)
    
    E2W2 = Entry(top, bd = 5)
    E2W2.grid(column = 2, row = 3)
    
    B1W2 = Button(text = "Roll", bg = "Yellow")
    B1W2.grid(column = 2, row = 4)

    #to add: roll function and exit button

if __name__ == "__main__":
    mainMenu()
    top.mainloop()
