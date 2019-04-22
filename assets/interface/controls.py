from tkinter import *
from tkinter.ttk import Combobox


class Controls:
    def __init__(self, instance):
        self.Game_Instance = instance
        self.Game_Config = self.Game_Instance.Game_Config
        self.Window = self.Game_Instance.Window

        self.Controls_Frame = Frame(self.Window, bg=self.Game_Instance.Colour_Background, height=self.Game_Config['WINDOW']['HEIGHT'], width=self.Game_Config['WINDOW']['WIDTH'])

        self.L_Title = Label(self.Controls_Frame, text='CONTROLS', font=('Verdana', 30, 'bold'), bg=self.Game_Instance.Colour_Background, fg='#BDC3C7').place(relx=.05, rely=.1)
        self.L_Action = Label(self.Controls_Frame, text='Game Action', font=('MS PGothic', 13, 'bold'), bg=self.Game_Instance.Colour_Background, fg='#BDC3C7').place(relx=.3, rely=.3)
        self.L_Bind = Label(self.Controls_Frame, text='Key Bind', font=('MS PGothic', 13, 'bold'), bg=self.Game_Instance.Colour_Background, fg='#BDC3C7').place(relx=.6, rely=.3)
        self.L_Notification = Label(self.Controls_Frame, text='Example Notification', font=('MS PGothic', 13, 'bold'), bg=self.Game_Instance.Colour_Background, fg='#BDC3C7')
        self.L_Notification.place(relx=.05, rely=.7)

        self.C_Action = Combobox(self.Controls_Frame, width=27, font=('MS PGothic', 12, 'bold'), values=['Left', 'Right', 'Jump', 'Interact', 'Hints'], state='readonly')
        self.C_Action.place(relx=.301, rely=.38)

        self.E_Bind = Entry(self.Controls_Frame, width=8, font=('MS PGothic', 12, 'bold'))
        self.E_Bind.place(relx=.602, rely=.382)

        self.C_Action.bind('<<ComboboxSelected>>', lambda event: self.updateKey())

        self.B_Bind = Button(self.Controls_Frame, text='Bind Button', font=('MS PGothic', 13, 'bold'), fg=self.Game_Instance.Colour_Background, bg='#f39c12', bd=0, command=lambda: self.saveBind()).place(relx=.565, rely=.475)
        self.B_Menu = Button(self.Controls_Frame, text='Return to Settings', font=('MS PGothic', 13, 'bold'), bg=self.Game_Instance.Colour_Background, fg='#E74C3C', bd=0, command=lambda: self.Controls_Frame.place_forget()).place(relx=.048, rely=.85)
        self.B_Save = Button(self.Controls_Frame, text='Save Settings', font=('MS PGothic', 13, 'bold'), bg=self.Game_Instance.Colour_Background, fg='#2ECC71', bd=0, command=lambda: self.saveControls()).place(relx=.809, rely=.85)

    def draw(self):
        self.Controls_Frame.place(relx=0, rely=0)

    def hide(self):
        self.Controls_Frame.place_forget()

    def updateKey(self):
        bindedButton = self.Game_Config['CONTROLS'][self.C_Action.get()]
        self.E_Bind.delete(0, END)
        self.E_Bind.insert(INSERT, bindedButton.upper())

    def saveBind(self):
        self.Game_Config.set('CONTROLS', self.C_Action.get(), self.E_Bind.get())
        self.L_Notification.config(text=f'Successfully binded the action \'{self.C_Action.get()}\' to the key \'{self.E_Bind.get().upper()}\'')

    def saveControls(self):
        with open('config/game.ini', 'w') as configfile:
            self.Game_Config.write(configfile)
        self.L_Notification.config(text='Successfully saved all new key binds to the config file.')

