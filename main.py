import datetime
import time
from threading import Thread
from tkinter import *
from configparser import ConfigParser
from assets.interface.menu import Menu
from assets.interface.settings import Settings
from assets.world.levels import Levels
from assets.player import Player
from assets.world.physics import Physics
from assets.interface.update import Updater


# TODO: Snow level


class Diamond:
    def __init__(self):
        self.Game_Lives = 3

        self.Game_Config = ConfigParser()
        self.Game_Config.read('config/game.ini')
        self.Game_Page = 1
        self.Game_Level = 1
        self.Game_Seconds = 600

        self.Levels = None
        self.Player_One = None
        self.Physics = None
        self.Game_Switches = []
        self.Live_Strings = ['one', 'two', 'three']
        self.Currently_Animating = False
        self.Mode = False

        self.Colour_Background = self.Game_Config['COLOURS']['BACKGROUND']
        self.Colour_Foreground = self.Game_Config['COLOURS']['FOREGROUND']

        self.Window = Tk()
        self.Window.geometry(f'{self.Game_Config["WINDOW"]["WIDTH"]}x{self.Game_Config["WINDOW"]["HEIGHT"]}+100+100')
        self.Window.config(bg=self.Colour_Background)

        self.UI_Menu = Menu(self)
        self.UI_Settings = Settings(self)
        self.UI_Updater = Updater(self)

        self.UI_Menu.draw()
        # self.UI_Settings.draw()
        # self.UI_Updater.draw()

        self.Game_Frame = Frame(self.Window, bg=self.Game_Config['COLOURS']['BACKGROUND'], height=self.Game_Config['WINDOW']['HEIGHT'], width=self.Game_Config['WINDOW']['WIDTH'])
        self.locationLabel = Label(self.Game_Frame, text='None', bg=self.Game_Config['COLOURS']['BACKGROUND'], font=('MS PGothic', 10, 'bold'), fg='#FFFFFF')
        self.locationLabel.place(relx=.75, rely=.05)
        self.helpfulLabelPrefix = Label(self.Game_Frame, text='Help', fg=self.Game_Config['COLOURS']['BACKGROUND'], font=('MS PGothic', 11, 'bold'), bg='YELLOW', width=5)
        self.helpfulLabelText = Label(self.Game_Frame, text='Placeholder help message.', fg=self.Game_Config['COLOURS']['BACKGROUND'], font=('MS PGothic', 11, 'bold'), bg='#FFFFFF', width=45)
        self.helpfulLabelIcon = Label(self.Game_Frame, text='Switches', fg=self.Game_Config['COLOURS']['BACKGROUND'], font=('MS PGothic', 11, 'bold'), bg='#FFFFFF', width=8)

        self.livesLabelIcon = Label(self.Game_Frame, text='3', fg=self.Game_Config['COLOURS']['BACKGROUND'], font=('MS PGothic', 11, 'bold'), bg='#FFFFFF', width=2)
        self.livesLabelPrefix = Label(self.Game_Frame, text='Lives', fg=self.Game_Config['COLOURS']['BACKGROUND'], font=('MS PGothic', 11, 'bold'), bg='#e74c3c', width=6)
        self.livesLabelText = Label(self.Game_Frame, text='You have three lives remaining', fg=self.Game_Config['COLOURS']['BACKGROUND'], font=('MS PGothic', 11, 'bold'), bg='#FFFFFF', width=40)

        self.timeLabelText = Label(self.Game_Frame, text='10:00', fg=self.Game_Config['COLOURS']['BACKGROUND'], font=('MS PGothic', 11, 'bold'), bg='#FFFFFF', width=6)
        self.timeLabelPrefix = Label(self.Game_Frame, text='Time', fg=self.Game_Config['COLOURS']['BACKGROUND'], font=('MS PGothic', 11, 'bold'), bg='#1abc9c', width=5)

        self.startSingleplayer()

        self.Window.bind('<Tab>', lambda event: self.revealMessage())

        self.Window.mainloop()

    def startSingleplayer(self):
        self.UI_Menu.hide()
        self.Game_Frame.place(relx=0, rely=0)
        self.livesMessage(3)
        self.Player_One = Player(self, self.Game_Frame, '#FFFFFF', 'P1', [0.95, 0.75])
        self.Levels = Levels(self, self.Game_Frame)
        self.Levels.one()
        self.Physics = Physics(self, self.Game_Frame, self.Player_One)
        self.Physics.one()
        Thread(target=self.updateLocation).start()

    def updateLocation(self):
        while True:
            self.locationLabel.config(text=f'{round(self.Player_One.Location[0], 2)}, {round(self.Player_One.Location[1], 2)}')
            time.sleep(0.01)

    def startMultiplayer(self):
        pass

    def helpMessage(self, message, minimal, timeout=3):
        def clearMessage():
            time.sleep(timeout)
            self.helpfulLabelPrefix.place_forget()
            self.helpfulLabelText.place_forget()
            x = 0.25
            y = 0.20
            while True:
                self.helpfulLabelPrefix.place(relx=x, rely=y)
                x += 0.0053
                y -= 0.0067
                time.sleep(0.003)
                if x >= 0.37:
                    print(x, y)
                    break
            x = 0.37
            y = 0.05
            while True:
                self.helpfulLabelIcon.place(relx=x, rely=y)
                x += 0.001
                time.sleep(0.003)
                if x >= 0.426:
                    break
        self.helpfulLabelPrefix.place(relx=.25, rely=.2)
        self.helpfulLabelText.config(text=message)
        self.helpfulLabelText.place(relx=.31, rely=.2)
        Thread(target=clearMessage).start()

    def revealMessage(self):
        def showMessage():
            self.helpfulLabelIcon.place_forget()
            x = 0.37
            y = 0.05
            while True:
                self.helpfulLabelPrefix.place(relx=x, rely=y)
                x -= 0.00538
                y += 0.0068
                time.sleep(0.003)
                if x <= 0.25:
                    print(x, y, '2')
                    break
                self.helpfulLabelText.place(relx=.31, rely=.2)
        if not self.Mode:
            Thread(target=showMessage).start()
        else:
            self.hideMessage()
        self.Mode = not self.Mode

    def hideMessage(self):
        def moveMessage():
            self.helpfulLabelPrefix.place_forget()
            self.helpfulLabelText.place_forget()
            x = 0.25
            y = 0.20
            while True:
                self.helpfulLabelPrefix.place(relx=x, rely=y)
                x += 0.0053
                y -= 0.0067
                time.sleep(0.003)
                if x >= 0.37:
                    print(x, y)
                    break
            x = 0.37
            y = 0.05
            while True:
                self.helpfulLabelIcon.place(relx=x, rely=y)
                x += 0.001
                time.sleep(0.003)
                if x >= 0.426:
                    break
        if not self.Currently_Animating:
            Thread(target=moveMessage).start()


    def livesMessage(self, timeout=3):
        def clearMessage():
            time.sleep(timeout)
            self.livesLabelIcon.place_forget()
            self.livesLabelPrefix.place_forget()
            self.livesLabelText.place_forget()
            x = 0.26
            y = 0.20
            while True:
                self.livesLabelPrefix.place(relx=x, rely=y)
                x -= 0.0053
                y -= 0.0038
                time.sleep(0.003)
                if x <= 0.05:
                    break
            x = 0.1
            y = 0.05
            while True:
                self.livesLabelIcon.config(text=self.Game_Lives)
                self.livesLabelIcon.place(relx=x, rely=y)
                x += 0.001
                time.sleep(0.004)
                if x >= 0.122:
                    break
            time.sleep(0.5)
            x = 0.1
            y = 0.05
            while True:
                self.timeLabelPrefix.place(relx=x, rely=y)
                x += 0.004
                if x >= 0.2:
                    break
                time.sleep(0.004)
            x = 0.2
            y = 0.05
            while True:
                self.timeLabelText.place(relx=x, rely=y)
                x += 0.0015
                if x >= 0.255:
                    break
                time.sleep(0.004)
            Thread(target=self.startCounting).start()

        self.livesLabelPrefix.place(relx=.26, rely=.2)
        self.livesLabelText.config(text=f'You have {self.Live_Strings[self.Game_Lives - 1]} lives remaining')
        self.livesLabelText.place(relx=.33, rely=.2)
        Thread(target=clearMessage).start()

    def startCounting(self):
        while True:
            if self.Game_Seconds == 0:
                break
            self.timeLabelText.config(text=str(datetime.timedelta(seconds=self.Game_Seconds))[2:])
            self.Game_Seconds -= 1
            time.sleep(1)


if __name__ == '__main__':
    Game = Diamond()
