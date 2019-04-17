from tkinter import *


class Settings:
    def __init__(self, instance):
        self.Game_Instance = instance
        self.Game_Config = self.Game_Instance.Game_Config
        self.Window = self.Game_Instance.Window

        self.Settings_Frame = Frame(self.Window, bg=self.Game_Instance.Colour_Background, height=self.Game_Config['WINDOW']['HEIGHT'], width=self.Game_Config['WINDOW']['WIDTH'])

        self.L_Title = Label(self.Settings_Frame, text='SETTINGS', font=('Verdana', 30, 'bold'), bg=self.Game_Instance.Colour_Background, fg='#BDC3C7').place(relx=.05, rely=.1)
        self.L_Connection = Label(self.Settings_Frame, text='Connection Type', font=('MS PGothic', 13, 'bold'), bg=self.Game_Instance.Colour_Background, fg='#BDC3C7').place(relx=.05, rely=.3)
        self.L_Update = Label(self.Settings_Frame, text='Automatic Updates', font=('MS PGothic', 13, 'bold'), bg=self.Game_Instance.Colour_Background, fg='#BDC3C7').place(relx=.05, rely=.4)
        self.L_Position = Label(self.Settings_Frame, text='Show Position', font=('MS PGothic', 13, 'bold'), bg=self.Game_Instance.Colour_Background, fg='#BDC3C7').place(relx=.05, rely=.5)
        self.L_Logging = Label(self.Settings_Frame, text='Event Logging', font=('MS PGothic', 13, 'bold'), bg=self.Game_Instance.Colour_Background, fg='#BDC3C7').place(relx=.05, rely=.6)
        self.L_Help = Label(self.Settings_Frame, text='Help and Tips', font=('MS PGothic', 13, 'bold'), bg=self.Game_Instance.Colour_Background, fg='#BDC3C7').place(relx=.05, rely=.7)

        self.L_Theme = Label(self.Settings_Frame, text='Theme Colour', font=('MS PGothic', 13, 'bold'), bg=self.Game_Instance.Colour_Background, fg='#BDC3C7').place(relx=.55, rely=.3)

        self.S_Connection = Switch(self, [0.35, 0.3], ['C-S', 'P2P'])
        self.S_Update = Switch(self, [0.35, 0.4], ['ALERT', 'ON', 'OFF'])
        self.S_Position = Switch(self, [0.35, 0.5], ['ON', 'OFF'])
        self.S_Logging = Switch(self, [0.35, 0.6], ['ON', 'OFF'])
        self.S_Help = Switch(self, [0.35, 0.7], ['ON', 'OFF'])

        self.S_Theme = Switch(self, [0.85, 0.3], ['DARK', 'LIGHT'])

        self.B_Menu = Button(self.Settings_Frame, text='Change Controls', font=('MS PGothic', 13, 'bold'), bg=self.Game_Instance.Colour_Background, fg='#95a5a6', bd=0, command=lambda: self.changeControls()).place(relx=.625, rely=.85)
        self.B_Menu = Button(self.Settings_Frame, text='Return to Menu', font=('MS PGothic', 13, 'bold'), bg=self.Game_Instance.Colour_Background, fg='#E74C3C', bd=0, command=lambda: self.Settings_Frame.place_forget()).place(relx=.048, rely=.85)
        self.B_Save = Button(self.Settings_Frame, text='Save Settings', font=('MS PGothic', 13, 'bold'), bg=self.Game_Instance.Colour_Background, fg='#2ECC71', bd=0).place(relx=.809, rely=.85)

    def draw(self):
        self.Settings_Frame.place(relx=0, rely=0)

    def hide(self):
        self.Settings_Frame.place_forget()

    def changeControls(self):
        pass


class Switch:
    def __init__(self, instance, position, options=['YES', 'NO']):
        self.Settings_Instance = instance
        self.Window = self.Settings_Instance.Settings_Frame
        self.Switch_Position = position
        self.Switch_Options = options
        self.Switch_Index = 0
        self.Switch_Value = self.Switch_Options[0]
        self.Switch_Button = Button(self.Window, text=self.Switch_Value, font=('MS PGothic', 13, 'bold'), bg='#BDC3C7', fg=self.Settings_Instance.Game_Instance.Colour_Background, command=lambda: self.shuffle(), bd=0, width=7)
        self.Switch_Button.place(relx=self.Switch_Position[0], rely=self.Switch_Position[1])

    def get(self):
        return self.Switch_Value

    def set(self, value):
        self.Switch_Value = value
        self.Switch_Button.config(text=self.Switch_Value)

    def shuffle(self):
        if self.Switch_Index + 1 == len(self.Switch_Options):
            self.Switch_Index = 0
        else:
            self.Switch_Index += 1
        self.Switch_Value = self.Switch_Options[self.Switch_Index]
        self.Switch_Button.config(text=self.Switch_Value)



