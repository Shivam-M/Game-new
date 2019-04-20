import time
from threading import Thread


class Physics:
    def __init__(self, instance, frame, player):
        self.Game_Instance = instance
        self.Game_Frame = frame
        self.Player = player
        self.physicsLevel = 0
        self.Unlocked = None

    def one(self):
        def physics():
            while self.physicsLevel == 1:
                if 0.7 > self.Player.Location[0] > 0.5:
                    self.Player.Location[1] += 0.002
                elif self.Player.Location[0] > 1.0:
                    self.Player.Location = [0.05, 0.15]
                    self.Game_Instance.Levels.two()
                    self.two()
                else:
                    if self.Player.Location[1] <= 0.74:
                        self.Player.Location[1] += 0.002
                if self.Player.Location[1] > 1.0:
                    self.Game_Instance.Game_Lives -= 1
                    self.Game_Instance.livesMessage()
                    self.Player.Location = [0.05, 0.75]
                time.sleep(0.002)
        self.physicsLevel = 1
        Thread(target=physics).start()

    def two(self):
        self.Unlocked = False

        def physics():
            while self.physicsLevel == 2:
                if 0.36 > self.Player.Location[0] > 0.31:
                    self.Player.Location[1] += 0.002
                elif 0.5 > self.Player.Location[0] > 0.36:
                    if 0.39 < self.Player.Location[1] < 0.66:
                        self.Player.Location[1] += 0.002
                    elif self.Player.Location[1] < 0.38:
                        self.Player.Location[1] += 0.002
                    elif self.Player.Location[1] > 0.67:
                        self.Player.Location[1] += 0.002
                elif 0.58 > self.Player.Location[0] > 0.5:
                    self.Player.Location[1] += 0.002
                elif 0.73 > self.Player.Location[0] > 0.58:
                    if self.Player.Location[1] < 0.53:
                        self.Player.Location[1] += 0.002
                    elif self.Player.Location[1] > 0.54:
                        self.Player.Location[1] += 0.002
                elif 0.78 > self.Player.Location[0] > 0.73:
                    self.Player.Location[1] += 0.002
                elif 0.99 > self.Player.Location[0] >= 0.85:
                    if not self.Unlocked:
                        self.Player.Location[0] = 0.85
                    if self.Player.Location[1] <= 0.74:
                        self.Player.Location[1] += 0.002
                elif self.Player.Location[0] >= 0.99:
                    self.four()
                    self.Game_Instance.Levels.four()
                else:
                    if self.Player.Location[1] <= 0.74:
                        self.Player.Location[1] += 0.002
                if self.Player.Location[1] > 1.0:
                    self.Game_Instance.Game_Lives -= 1
                    self.Game_Instance.livesMessage()
                    self.Game_Instance.Levels.one()
                    self.one()
                    self.Player.Location = [0.05, 0.75]
                a = True
                for switch in self.Game_Instance.Game_Switches:
                    if not switch.Status:
                        a = False
                if a:
                    self.Game_Instance.Levels.barrier.place_forget()
                    self.Unlocked = True
                time.sleep(0.002)
        self.physicsLevel = 2
        Thread(target=physics).start()

    def three(self):
        self.Player.Location = [0.05, 0.75]
        self.Player.Velocity2[0] = -0.000001

        def physics():
            pass

        self.physicsLevel = 3
        Thread(target=physics).start()

    def four(self):
        self.Player.Location = [0.05, 0.75]

        def physics():
            while self.physicsLevel == 4:
                if self.Player.Location[0] > 0.99:
                    self.five()
                    self.Game_Instance.Levels.five()
                else:
                    if self.Player.Location[1] <= 0.74:
                        self.Player.Location[1] += 0.002
                time.sleep(0.002)
        self.physicsLevel = 4
        Thread(target=physics).start()

    def five(self):
        self.Player.Location = [0.05, 0.75]

        def physics():
            while self.physicsLevel == 5:
                if 0.42 >= self.Player.Location[0] > 0.29:
                    if self.Player.Location[1] < 0.45:
                        self.Player.Location[1] += 0.002
                    elif self.Player.Location[1] > 0.455:
                        if self.Player.Location[1] <= 0.74:
                            self.Player.Location[1] += 0.002
                elif 0.21 > self.Player.Location[0] > 0.07:
                    if self.Player.Location[1] < 0.3:
                        self.Player.Location[1] += 0.002
                    elif self.Player.Location[1] > 0.355:
                        if self.Player.Location[1] <= 0.74:
                            self.Player.Location[1] += 0.002

                elif 0.48 > self.Player.Location[0] > 0.42:
                    self.Player.Location[1] += 0.002
                elif 0.63 >= self.Player.Location[0] > 0.48:
                    if self.Player.Location[1] < 0.6:
                        self.Player.Location[1] += 0.002
                    elif self.Player.Location[1] > 0.65:
                        self.Player.Location[1] += 0.002
                    # self.Player.Location[1] += 0.002
                elif 0.7 >= self.Player.Location[0] > 0.63:
                    self.Player.Location[1] += 0.002
                elif 0.85 >= self.Player.Location[0] > 0.7:
                    if self.Player.Location[1] < 0.45:
                        self.Player.Location[1] += 0.002
                    elif self.Player.Location[1] > 0.455:
                        if self.Player.Location[1] <= 0.74:
                            self.Player.Location[1] += 0.002
                else:
                    if self.Player.Location[1] <= 0.74:
                        self.Player.Location[1] += 0.002
                time.sleep(0.002)

        self.physicsLevel = 5
        Thread(target=physics).start()
