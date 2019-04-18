from tkinter import *
from threading import Thread
from time import sleep


class Player:
    def __init__(self, instance, frame, colour, tag, location):
        self.Game_Instance = instance
        self.Game_Frame = frame
        self.Colour = colour
        self.Tag = tag
        self.Location = location
        self.Velocity = [0.0, 0.0]
        self.Velocity2 = [0.0, 0.0]
        self.Left, self.Right = False, False

        self.cooldownJump = False

        self.Player_Model = Label(self.Game_Frame, width=2, height=1, bg=self.Colour)
        self.Player_Model.place(relx=location[0], rely=location[1])

        Thread(target=self.update).start()
        # Thread(target=self.gravity).start()

        self.Game_Instance.Window.bind(f'<{self.Game_Instance.Game_Config["CONTROLS"]["JUMP"].title()}>', lambda event: self.up())
        self.Game_Instance.Window.bind(f'<{self.Game_Instance.Game_Config["CONTROLS"]["RIGHT"].title()}>', lambda event: self.right())
        self.Game_Instance.Window.bind(f'<{self.Game_Instance.Game_Config["CONTROLS"]["LEFT"].title()}>', lambda event: self.left())
        self.Game_Instance.Window.bind(f'<KeyRelease-{self.Game_Instance.Game_Config["CONTROLS"]["LEFT"].title()}>', lambda event: self.releaseL())
        self.Game_Instance.Window.bind(f'<KeyRelease-{self.Game_Instance.Game_Config["CONTROLS"]["RIGHT"].title()}>', lambda event: self.releaseR())
        self.Game_Instance.Window.bind(f'<{self.Game_Instance.Game_Config["CONTROLS"]["INTERACT"].lower()}>', lambda event: self.switch())
        self.Game_Instance.Window.bind(f'<{self.Game_Instance.Game_Config["CONTROLS"]["INTERACT"].title()}>', lambda event: self.switch())

        try:
            self.Game_Instance.Window.bind(f'<{self.Game_Instance.Game_Config["CONTROLS"]["RIGHT"].lower()}>', lambda event: self.right())
            self.Game_Instance.Window.bind(f'<{self.Game_Instance.Game_Config["CONTROLS"]["LEFT"].lower()}>', lambda event: self.left())
            self.Game_Instance.Window.bind(f'<KeyRelease-{self.Game_Instance.Game_Config["CONTROLS"]["LEFT"].lower()}>', lambda event: self.releaseL())
            self.Game_Instance.Window.bind(f'<KeyRelease-{self.Game_Instance.Game_Config["CONTROLS"]["RIGHT"].lower()}>', lambda event: self.releaseR())
            self.Game_Instance.Window.bind(f'<{self.Game_Instance.Game_Config["CONTROLS"]["JUMP"].lower()}>', lambda event: self.up())
        except:
            pass

    def up(self):
        Thread(target=self.jump).start()

    def right(self):
        self.Velocity[0] = +0.00001
        self.Right = True

    def left(self):
        self.Velocity[0] = -0.00001
        self.Left = True

    def releaseL(self):
        self.Left = False
        if not self.Right:
            self.Velocity[0] = 0.0

    def releaseR(self):
        self.Right = False
        if not self.Left:
            self.Velocity[0] = 0.0

    def jump(self):
        if self.isStill():
            self.cooldownJump = True
            self.Velocity[1] = -0.00007
            if self.Right:
                self.Velocity[0] = +0.00002
            elif self.Left:
                self.Velocity[0] = -0.00002
            sleep(0.125)
            sleep(0.125)
            if self.Right:
                self.Velocity[0] = +0.00001
            elif self.Left:
                self.Velocity[0] = -0.00001
            self.Velocity[1] = 0
            sleep(0.31)
            self.cooldownJump = False

    def isStill(self):
        LocNow = self.Location.copy()
        sleep(0.01)
        LocThen = self.Location.copy()
        if LocNow[1] != LocThen[1]:
            return False
        return True

    def update(self):
        while True:
            self.Location[1] += self.Velocity[1]
            self.Location[0] += self.Velocity[0]
            self.Location[1] += self.Velocity2[1]
            self.Location[0] += self.Velocity2[0]
            self.Player_Model.place(relx=self.Location[0], rely=self.Location[1])

    def gravity(self):
        while True:
            self.Velocity[1] += 0.05

    def switch(self):
        for switch in self.Game_Instance.Game_Switches:
            if abs(switch.Location[0] - self.Location[0]) <= 0.025:
                if abs(switch.Location[1] - self.Location[1]) <= 0.025:
                    switch.toggle()




