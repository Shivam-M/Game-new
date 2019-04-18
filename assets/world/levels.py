import random
import time
from threading import Thread
from tkinter import *


class Levels:
    def __init__(self, instance, frame):
        self.Game_Instance = instance
        self.Game_Frame = frame

        self.currentAssets = []

    def one(self):
        # self.Game_Instance.Physics.one()
        for asset in self.currentAssets:
            asset.place_forget()
        self.currentAssets = []
        self.Game_Instance.Game_Switches = []

        floor = Label(self.Game_Frame, width=65, height=300, bg='#FFFFFF', fg='#FFFFFF')
        floor.place(relx=.0, rely=.8)

        floor2 = Label(self.Game_Frame, width=65, height=300, bg='#FFFFFF', fg='#FFFFFF')
        floor2.place(relx=.7, rely=.8)

        self.currentAssets.extend([floor, floor2])

    def two(self):
        # self.Game_Instance.Physics.two()
        for asset in self.currentAssets:
            asset.place_forget()
        self.currentAssets = []

        floor = Label(self.Game_Frame, width=40, height=300, bg='#FFFFFF', fg='#FFFFFF')
        floor.place(relx=.0, rely=.8)

        floor2 = Label(self.Game_Frame, width=17, height=1, bg='#FFFFFF', fg='#FFFFFF')
        floor2.place(relx=.375, rely=.725)

        floor3 = Label(self.Game_Frame, width=17, height=1, bg='#FFFFFF', fg='#FFFFFF')
        floor3.place(relx=.6, rely=.6)

        floor4 = Label(self.Game_Frame, width=17, height=1, bg='#FFFFFF', fg='#FFFFFF')
        floor4.place(relx=.375, rely=.45)

        floor5 = Label(self.Game_Frame, width=40, height=300, bg='#FFFFFF', fg='#FFFFFF')
        floor5.place(relx=.8, rely=.8)

        self.barrier = Label(self.Game_Frame, width=50, height=100, bg='#FFFFFF', fg='#FFFFFF')
        self.barrier.place(relx=.875, rely=.0)

        Test = Switch(self.Game_Frame, 'Test', [0.665, 0.55])
        Test2 = Switch(self.Game_Frame, 'Test', [0.44, 0.40])
        self.Game_Instance.Game_Switches.extend([Test, Test2])
        self.currentAssets = [floor, floor2, floor3, floor4, floor5, Test, Test2]

    def three(self):
        pass

    def four(self):
        floor = Label(self.Game_Frame, width=65, height=300, bg='#222f3e', fg='#222f3e')
        floor.place(relx=.0, rely=.8)

        floor2 = Label(self.Game_Frame, width=65, height=300, bg='#222f3e', fg='#222f3e')
        floor2.place(relx=.7, rely=.8)

        t = Star(self.Game_Frame)
        Thread(target=t.place).start()


class Switch:
    def __init__(self, frame, tag, location):
        self.Tag = tag
        self.Game_Frame = frame
        self.Location = location
        self.Status = False

        self.Switch_Item = Label(self.Game_Frame, font=('MS PGothic', 1, ''), height=3, bg='#bdc3c7', fg='#bdc3c7')
        self.Switch_Item.place(relx=self.Location[0], rely=self.Location[1])

    def get(self):
        return self.Switch_Item

    def toggle(self):
        if self.Status:
            self.Switch_Item.config(bg='#bdc3c7', fg='#bdc3c7')
        else:
            self.Switch_Item.config(bg='#2ecc71', fg='#2ecc71')
        self.Status = not self.Status

    def place_forget(self):
        self.Switch_Item.place_forget()


class Stars:
    def __init__(self, frame):
        self.Game_Frame = frame
        self.positions = []

    def place(self):
        y = [0.1, 0.15, 0.2, 0.125, 0.175, 0.05, 0.215, 0.25, 0.275, 0.3, 0.325, 0.35, 0.375]
        for x in range(0, 50):
            self.positions.append([0.025 * x, random.choice(y)])

        for position in self.positions:
            t = Label(self.Game_Frame, text='●', font=('MS PGothic', 3, 'bold'), bg='#141414', fg='#FFFFFF')
            t.place(relx=position[0], rely=position[1])
            time.sleep(0.01)










