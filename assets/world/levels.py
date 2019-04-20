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

        self.Game_Instance.helpMessage('Press X to activate or deactivate switches', 'Switches')

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
        for asset in self.currentAssets:
            asset.place_forget()
        self.currentAssets = []

    def four(self):

        def bar():
            x = self.Game_Instance.Player_One.Location.copy()[0] + 0.125
            while True:
                if x != self.Game_Instance.Player_One.Location.copy()[0] + 0.125:
                    x = self.Game_Instance.Player_One.Location.copy()[0] + 0.125
                    floor3.place(relx=x, rely=0.0)
                for s in t.positions:
                    if s[0] >= x:
                        t.Star_Items[t.positions.index(s)].config(bg='#222f3e')

        for asset in self.currentAssets:
            asset.place_forget()
        self.currentAssets = []

        floor = Label(self.Game_Frame, width=300, height=300, bg='#222f3e', fg='#222f3e')
        floor.place(relx=.0, rely=.8)

        # floor3 = Label(self.Game_Frame, width=300, height=300, bg='#222f3e', fg='#222f3e')
        # floor3.place(relx=0.175, rely=.0)

        t = Stars(self.Game_Frame)
        Thread(target=t.place).start()

        # Thread(target=bar).start()

        self.currentAssets = [floor, t]

    def rise(self):
        y = .99
        while True:
            self.floor3.place(relx=.0, rely=y)
            y -= 0.00007
            time.sleep(0.005)
            if y < 0:
                break

    def five(self):

        for asset in self.currentAssets:
            asset.place_forget()
        self.currentAssets = []

        floor = Label(self.Game_Frame, width=55, height=300, bg='#141414', fg='#141414')
        floor.place(relx=.0, rely=.8)

        floor2 = Label(self.Game_Frame, width=50, height=300, bg='#141414', fg='#141414')
        floor2.place(relx=.71, rely=.8)

        floor3 = Label(self.Game_Frame, width=18, height=1, bg='#141414', fg='#141414')
        floor3.place(relx=.495, rely=.65)

        floor4 = Label(self.Game_Frame, width=18, height=1, bg='#141414', fg='#141414')
        floor4.place(relx=.29, rely=.5)

        floor5 = Label(self.Game_Frame, width=18, height=1, bg='#141414', fg='#141414')
        floor5.place(relx=.71, rely=.5)

        floor6 = Label(self.Game_Frame, width=18, height=1, bg='#141414', fg='#141414')
        floor6.place(relx=.08, rely=.35)

        self.floor3 = Label(self.Game_Frame, width=300, height=300, bg='#d35400', fg='#d35400')
        self.floor3.place(relx=.0, rely=.99)

        Thread(target=self.rise).start()

        self.Game_Frame.config(bg='#c0392b')
        self.Game_Instance.livesLabelIcon.config(bg='#141414', fg='#FFFFFF')
        self.Game_Instance.timeLabelText.config(bg='#141414', fg='#FFFFFF')
        self.Game_Instance.Player_One.Player_Model.config(bg='#141414')


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
        self.Star_Items = []
        self.Star_Coords = []

    def place(self):
        y = [0.175, 0.2, 0.215, 0.25, 0.275, 0.3, 0.325, 0.35, 0.375]
        for x in range(0, 50):
            self.positions.append([0.025 * x, random.choice(y)])
            if 0.025 * x > 0.35:
                y = [0.05, 0.075, 0.125, 0.15, 0.175, 0.2, 0.215, 0.25, 0.275, 0.3, 0.325, 0.35, 0.375]

        for position in self.positions:
            t = Label(self.Game_Frame, text='●', font=('MS PGothic', 3, 'bold'), bg='#141414', fg='#FFFFFF')
            t.place(relx=position[0], rely=position[1])
            self.Star_Items.append(t)
            time.sleep(0.01)

    def place_forget(self):
        for item in self.Star_Items:
            item.place_forget()

    def get(self):
        return self.Star_Items










