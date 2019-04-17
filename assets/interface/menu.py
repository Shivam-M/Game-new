from tkinter import *


class Menu:
    def __init__(self, instance):
        self.Game_Instance = instance
        self.Game_Config = self.Game_Instance.Game_Config
        self.Window = self.Game_Instance.Window

        self.Menu_Frame = Frame(self.Window, bg=self.Game_Instance.Colour_Background, height=self.Game_Config['WINDOW']['HEIGHT'], width=self.Game_Config['WINDOW']['WIDTH'])

        self.L_Title = Label(self.Menu_Frame, text='DIAMOND', font=('Verdana', 30, 'bold'), bg=self.Game_Instance.Colour_Background, fg='#BDC3C7').place(relx=.05, rely=.1)
        self.L_Single = Button(self.Menu_Frame, text='Singleplayer', font=('MS PGothic', 13, 'bold'), bg=self.Game_Instance.Colour_Background, fg='#BDC3C7', bd=0, command=lambda: self.Game_Instance.startSingleplayer()).place(relx=.05, rely=.3)
        self.L_Multi = Button(self.Menu_Frame, text='Multiplayer', font=('MS PGothic', 13, 'bold'), bg=self.Game_Instance.Colour_Background, fg='#BDC3C7', bd=0, command=lambda: self.Game_Instance.startMultiplayer()).place(relx=.05, rely=.385)
        self.L_Options = Button(self.Menu_Frame, text='Settings', font=('MS PGothic', 13, 'bold'), bg=self.Game_Instance.Colour_Background, fg='#BDC3C7', bd=0, command=lambda: self.Game_Instance.UI_Settings.draw()).place(relx=.05, rely=.470)
        self.L_Test = Button(self.Menu_Frame, text='Developer', font=('MS PGothic', 13, 'bold'), bg=self.Game_Instance.Colour_Background, fg='#BDC3C7', bd=0).place(relx=.05, rely=.555)
        self.L_Update = Button(self.Menu_Frame, text='Update Game', font=('MS PGothic', 13, 'bold'), bg=self.Game_Instance.Colour_Background, fg='#BDC3C7', bd=0).place(relx=.05, rely=.640)
        self.L_Exit = Button(self.Menu_Frame, text='Close Game', font=('MS PGothic', 13, 'bold'), bg=self.Game_Instance.Colour_Background, fg='#E74C3C', bd=0, command=lambda: self.Game_Instance.Window.destroy()).place(relx=.05, rely=.8)

        self.L_Leaderboard = Label(self.Menu_Frame, text='Leaderboard', font=('MS PGothic', 13, 'bold'), bg=self.Game_Instance.Colour_Background, fg='#BDC3C7', bd=0).place(relx=.45, rely=.3)
        self.T_Names = Text(self.Menu_Frame, font=('MS PGothic', 13, 'bold'), bg=self.Game_Instance.Colour_Background, fg='#BDC3C7', width=15, height=10).place(relx=.45, rely=.375)
        self.T_Scores = Text(self.Menu_Frame, font=('MS PGothic', 13, 'bold'), bg=self.Game_Instance.Colour_Background, fg='#BDC3C7', width=15, height=10).place(relx=.775, rely=.375)

    def draw(self):
        self.Menu_Frame.place(relx=0, rely=0)

    def hide(self):
        self.Menu_Frame.place_forget()
