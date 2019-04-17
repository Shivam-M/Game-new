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

        self.Levels = None
        self.Player_One = None
        self.Physics = None
        self.Game_Switches = []

        self.Colour_Background = self.Game_Config['COLOURS']['BACKGROUND']
        self.Colour_Foreground = self.Game_Config['COLOURS']['FOREGROUND']

        self.Window = Tk()
        self.Window.geometry(f'{self.Game_Config["WINDOW"]["WIDTH"]}x{self.Game_Config["WINDOW"]["HEIGHT"]}')
        self.Window.config(bg=self.Colour_Background)

        self.UI_Menu = Menu(self)
        self.UI_Settings = Settings(self)
        self.UI_Updater = Updater(self)

        self.UI_Menu.draw()
        # self.UI_Settings.draw()
        self.UI_Updater.draw()

        self.Game_Frame = Frame(self.Window, bg=self.Game_Config['COLOURS']['BACKGROUND'], height=self.Game_Config['WINDOW']['HEIGHT'], width=self.Game_Config['WINDOW']['WIDTH'])
        self.locationLabel = Label(self.Game_Frame, text='None', bg=self.Game_Config['COLOURS']['BACKGROUND'], font=('MS PGothic', 10, 'bold'), fg='#FFFFFF')
        self.locationLabel.place(relx=.05, rely=.05)
        self.helpfulLabelPrefix = Label(self.Game_Frame, text='Help', fg=self.Game_Config['COLOURS']['BACKGROUND'], font=('MS PGothic', 11, 'bold'), bg='YELLOW', width=5)
        self.helpfulLabelPrefix.place(relx=.25, rely=.2)
        self.helpfulLabelText = Label(self.Game_Frame, text='Press X to activate or deactivate switches', fg=self.Game_Config['COLOURS']['BACKGROUND'], font=('MS PGothic', 11, 'bold'), bg='#FFFFFF', width=45)
        self.helpfulLabelText.place(relx=.31, rely=.2)

        self.livesLabelPrefix = Label(self.Game_Frame, text='Lives', fg=self.Game_Config['COLOURS']['BACKGROUND'], font=('MS PGothic', 11, 'bold'), bg='#e74c3c', width=6)
        # self.livesLabelPrefix.place(relx=.26, rely=.2)
        self.livesLabelText = Label(self.Game_Frame, text='You have three lives remaining', fg=self.Game_Config['COLOURS']['BACKGROUND'], font=('MS PGothic', 11, 'bold'), bg='#FFFFFF', width=40)
        # self.livesLabelText.place(relx=.33, rely=.2)
        # self.startSingleplayer()

        self.Window.mainloop()

    def startSingleplayer(self):
        self.UI_Menu.hide()
        self.Game_Frame.place(relx=0, rely=0)
        self.Player_One = Player(self, self.Game_Frame, '#FFFFFF', 'P1', [0.05, 0.75])
        self.Levels = Levels(self, self.Game_Frame)
        self.Levels.two()
        self.Physics = Physics(self, self.Game_Frame, self.Player_One)
        self.Physics.two()
        Thread(target=self.updateLocation).start()

    def updateLocation(self):
        while True:
            self.locationLabel.config(text=f'{round(self.Player_One.Location[0], 2)}, {round(self.Player_One.Location[1], 2)}')
            time.sleep(0.01)

    def startMultiplayer(self):
        pass




if __name__ == '__main__':
    Game = Diamond()
