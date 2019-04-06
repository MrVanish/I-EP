import pygame
import sys
from flappybird import FlappyBird
from tkinter import *
from ctypes import *
from pymongo import MongoClient

class Menu:

    def getDatabase(self):
        return []
    def safeDatabase(self):
        return True


    def __init__(self, PlayerName):

        self.Player = PlayerName

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

        self.punkts = [
            [pygame.display.get_surface().get_width()/2-50*len("START")/2, 100, "START", (255, 255, 255), (0, 0, 0), 1],
            [pygame.display.get_surface().get_width()/2-50*len("RECORDS")/2, pygame.display.get_surface().get_height()/3 + 100, "RECORDS", (255, 255, 255), (0, 0, 0), 2],
            [pygame.display.get_surface().get_width()/2-50*len("QUIT")/2, pygame.display.get_surface().get_height()/3*2 + 100 , "QUIT", (255, 255, 255), (0, 0, 0), 3]
                        ]

        self.position = 0

        self.background = pygame.transform.scale(pygame.image.load("assets/background.png").convert(),
                                                 ((pygame.display.get_surface()).get_width(),
                                                  (pygame.display.get_surface()).get_height()))
        self.show = True

        self.scoreDB = self.getDatabase()

    def start(self):
        self.show = False
        self.scoreDB.append(FlappyBird().run())
        self.show = True

    def recodr(self):
        print()

    def quit(self):
        sys.exit(0)

    def run(self):
        clock = pygame.time.Clock()
        pygame.font.init()

        while self.show:
            clock.tick(20)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.position == 1 and self.show:
                        self.start()
                    elif self.position == 2 and self.show:
                        self.recodr()
                    elif self.position == 3 and self.show:
                        self.quit()

            self.screen.blit(self.background, (0, 0))

            font = pygame.font.SysFont("Arial", 70)

            mouse = pygame.mouse.get_pos()
            mouseCollision = pygame.Rect(mouse[0], mouse[1], 10, 10)
            startCollision = pygame.Rect(self.punkts[0][0], self.punkts[0][1], 40 * len(self.punkts[0][2]), 100)
            recordsCollision = pygame.Rect(self.punkts[1][0], self.punkts[1][1], 40 * len(self.punkts[1][2]), 100)
            quitCollision = pygame.Rect(self.punkts[2][0], self.punkts[2][1], 40 * len(self.punkts[2][2]), 100)

            if startCollision.colliderect(mouseCollision):
                self.position = 1
            elif recordsCollision.colliderect(mouseCollision):
                self.position = 2
            elif quitCollision.colliderect(mouseCollision):
                self.position = 3
            else:
                self.position = 0

            for i in self.punkts:
                self.screen.blit(font.render(str(i[2]), -1, i[4] if self.punkts.index(i)+1 == self.position else i[3]),((i[0], i[1])))

            self.screen.blit(font.render(str(self.scoreDB), -1, (0, 0, 0)), (0, 100))
            self.screen.blit(font.render(str(self.Player), -1, (0, 0, 0)), (0, 200))

            pygame.display.update()


def start():
    name = entry.get()
    root.destroy()
    Menu(name).run()

root = Tk()
root.title('Name')
root.resizable(False, False)
root.geometry(f"200x50+{int(windll.user32.GetSystemMetrics(0)/2 - 50)}+{int(windll.user32.GetSystemMetrics(1)/2 -50)}")
entry = Entry()
entry.pack()
Button(text='Accept', command=start).pack()
label = Label(height=3)
label.pack()


root.mainloop()
