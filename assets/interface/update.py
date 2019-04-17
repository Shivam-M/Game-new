import os
import time
from configparser import ConfigParser
from threading import Thread
from tkinter import *
from urllib.request import urlretrieve, urlopen
import shutil
import os
import zipfile


class Updater:
    def __init__(self, instance):
        self.Game_Instance = instance
        self.Game_Config = self.Game_Instance.Game_Config
        self.Window = self.Game_Instance.Window

        self.Updater_Config = ConfigParser()
        self.Updater_Config.read('config/updater-config.ini')
        self.currentVersion = open('version.txt', 'r').read()
        self.latestVersion = None

        self.Update_Frame = Frame(self.Window, bg=self.Game_Instance.Colour_Background, height=self.Game_Config['WINDOW']['HEIGHT'], width=self.Game_Config['WINDOW']['WIDTH'])

        self.L_Title = Label(self.Update_Frame, text='UPDATER', font=('Verdana', 30, 'bold'), bg=self.Game_Instance.Colour_Background, fg='#BDC3C7').place(relx=.05, rely=.1)
        self.L_CurrentVersion = Label(self.Update_Frame, text='Current Version', font=('MS PGothic', 13, 'bold'), bg=self.Game_Instance.Colour_Background, fg='#BDC3C7').place(relx=.055, rely=.3)
        self.L_CurrentSize = Label(self.Update_Frame, text='Current Size', font=('MS PGothic', 13, 'bold'), bg=self.Game_Instance.Colour_Background, fg='#BDC3C7').place(relx=.55, rely=.3)

        self.L_LatestVersion = Label(self.Update_Frame, text='Latest Version', font=('MS PGothic', 13, 'bold'), bg=self.Game_Instance.Colour_Background, fg='#BDC3C7').place(relx=.0555, rely=.4)
        self.L_LatestSize = Label(self.Update_Frame, text='Latest Size', font=('MS PGothic', 13, 'bold'), bg=self.Game_Instance.Colour_Background, fg='#BDC3C7').place(relx=.55, rely=.4)

        self.D_CurrentVersion = Label(self.Update_Frame, text='Version 0.20', font=('MS PGothic', 13, 'bold'), bg=self.Game_Instance.Colour_Background, fg='#1abc9c')
        self.D_CurrentVersion.place(relx=.3, rely=.3)
        self.D_CurrentSize = Label(self.Update_Frame, text='Unknown', font=('MS PGothic', 13, 'bold'), bg=self.Game_Instance.Colour_Background, fg='#1abc9c')
        self.D_CurrentSize.place(relx=.8, rely=.3)

        self.D_LatestVersion = Label(self.Update_Frame, text='Unknown', font=('MS PGothic', 13, 'bold'), bg=self.Game_Instance.Colour_Background, fg='#16a085')
        self.D_LatestVersion.place(relx=.3, rely=.4)
        self.D_LatestSize = Label(self.Update_Frame, text='Unknown', font=('MS PGothic', 13, 'bold'), bg=self.Game_Instance.Colour_Background, fg='#16a085').place(relx=.8, rely=.4)

        self.helpfulLabelPrefix = Label(self.Update_Frame, text='Information', fg=self.Game_Config['COLOURS']['BACKGROUND'], font=('MS PGothic', 11, 'bold'), bg='#1abc9c', width=11)
        self.helpfulLabelPrefix.place(relx=.059, rely=.525)
        self.helpfulLabelText = Label(self.Update_Frame, text='Current files and program data will be stored in a backup folder in the directory above.', fg=self.Game_Config['COLOURS']['BACKGROUND'], font=('MS PGothic', 11, 'bold'), bg='#FFFFFF', width=75)
        self.helpfulLabelText.place(relx=.18, rely=.525)

        self.updateText = Label(self.Update_Frame, text='UPDATING GAME', fg='#BDC3C7', bg=self.Game_Config['COLOURS']['BACKGROUND'], font=('MS PGothic', 11, 'bold'))

        self.updatePercentage = Label(self.Update_Frame, text='40%', fg='#BDC3C7', bg=self.Game_Config['COLOURS']['BACKGROUND'], width=5, anchor='e', font=('MS PGothic', 11, 'bold'))

        self.updateBar = Label(self.Update_Frame, text=' ', bg='#BDC3C7', font=('MS PGothic', 3, 'bold'), width=262)
        self.updateFiller = Label(self.Update_Frame, text=' ', bg='#16a085', font=('MS PGothic', 3, 'bold'), width=60)

        self.helpfulLabelText.place(relx=.18, rely=.525)

        self.B_Menu = Button(self.Update_Frame, text='Return to Menu', font=('MS PGothic', 13, 'bold'), bg=self.Game_Instance.Colour_Background, fg='#E74C3C', bd=0, command=lambda: self.hide())
        self.B_Menu.place(relx=.053, rely=.85)
        self.B_Update = Button(self.Update_Frame, text='Check for Updates', font=('MS PGothic', 13, 'bold'), fg=self.Game_Instance.Colour_Background, bg='#16a085', bd=0, width=20, command=lambda: self.check())
        self.B_Update.place(relx=.71, rely=.85)

        self.D_CurrentVersion.config(text=f'Version {self.currentVersion}')

    def check(self):

        self.latestVersion = urlopen(f"https://raw.githubusercontent.com/{self.Updater_Config['CONFIG']['GITHUB']}/master/{self.Updater_Config['CONFIG']['VERSION']}").read().decode()
        self.D_LatestVersion.config(text=f'Version {self.latestVersion}')

        if float(self.currentVersion) < float(self.latestVersion):
            self.helpfulLabelText.config(text='An update is available - click the perform update button to begin.')
            self.B_Update.config(text='Perform Update', command=lambda: self.update())
        else:
            self.B_Update.config(text='Perform Refresh', command=lambda: self.update())
            self.helpfulLabelText.config(text='There are currently no updates available, however a refresh can be forced.')

    def update(self):
        self.B_Update.place_forget()
        self.B_Menu.place_forget()

        self.updateText.place(relx=.0545, rely=.7)
        self.updatePercentage.place(relx=.885, rely=.7)
        self.updateBar.place(relx=.059, rely=.775)
        self.updateFiller.place(relx=.059, rely=.775)

        source = os.getcwd() + '/'
        dest1 = '../test'

        files = os.listdir(source)
        for f in files:
            if f not in (self.Updater_Config['CONFIG']['EXCLUDE']).split(','):
                shutil.move(source + f, dest1)

        urlretrieve(f"https://github.com/{self.Updater_Config['CONFIG']['GITHUB']}/archive/master.zip", "master.zip")

        zip_ref = zipfile.ZipFile('master.zip', 'r')
        zip_ref.extractall(os.getcwd())
        zip_ref.close()

        source = os.getcwd() + '/Game-new-master/'
        dest1 = os.getcwd()
        files = os.listdir(source)

        for f in files:
            if f not in (self.Updater_Config['CONFIG']['EXCLUDE']).split(','):
                shutil.move(source + f, dest1)

        os.rmdir('Game-new-master')
        os.remove('master.zip')

        self.updateFiller.config(width=262)
        self.updatePercentage.config(text='100%')

    def draw(self):
        self.Update_Frame.place(relx=0, rely=0)

    def hide(self):
        self.Update_Frame.place_forget()


