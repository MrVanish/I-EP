import pygame
import sys
import random
import time
import pymongo

class FlappyBird:
    def __init__(self):


        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.bird = pygame.Rect( 55, 40, 40, 40)

        self.background = pygame.transform.scale(pygame.image.load("assets/background.png").convert(),
                                                 ((pygame.display.get_surface()).get_width(), (pygame.display.get_surface()).get_height()))
        self.birdSprites = [pygame.image.load("assets/1.png").convert_alpha(),
                            pygame.image.load("assets/2.png").convert_alpha(),
                            pygame.image.load("assets/dead.png"),
                            pygame.image.load("assets/0.png").convert_alpha()]
        self.wallUp = pygame.image.load("assets/bottom.png").convert_alpha()
        self.wallDown = pygame.image.load("assets/top.png").convert_alpha()

        self.widthScreen = pygame.display.get_surface().get_width()
        self.heightScreen = pygame.display.get_surface().get_height()

        self.gap = [random.randint(120, 200) for i in range(5)]
        self.wallx = [self.widthScreen + i * self.widthScreen / 4 for i in range(5)]
        self.offset = [random.randint(-120, 120) for i in range(5)]

        self.birdY = 350
        self.jump = 0
        self.jumpSpeed = 10
        self.gravity = 5
        self.dead = False
        self.animation = True
        self.sprite = 0
        self.counter = 0


    def updateWalls(self):

        for i in range(5):
            if self.wallx[i] < -self.widthScreen / 4:
                self.wallx[i] = self.widthScreen
                self.gap[i] = random.randint(120, 200)
                self.offset[i] = random.randint(-120, 200)
                self.counter += 1
            self.wallx[i] -= 10

        font = pygame.font.SysFont("Arial", 70)

        self.screen.blit(font.render(str(self.wallx), -1, (0, 0, 0)), (0, 100))
        self.screen.blit(font.render(str(self.gap), -1, (0, 0, 0)), (0, 200))
        self.screen.blit(font.render(str(self.offset), -1, (0, 0, 0)), (0, 300))


    def birdUpdate(self):
        if self.jump:
            self.jumpSpeed -= 1
            self.birdY -= self.jumpSpeed
            self.jump -= 1
        else:
            self.birdY += self.gravity
            self.gravity += 0.2
        self.bird[1] = self.birdY
        for i in range(5):

            upRect = pygame.Rect(self.wallx[i],self.heightScreen/2 + self.gap[i] - self.offset[i] + 10, self.wallUp.get_width() - 10, self.wallUp.get_height())
            downRect = pygame.Rect(self.wallx[i], 0 - self.gap[i] - self.offset[i] - 10, self.wallDown.get_width() - 10, self.wallDown.get_height())

            if upRect.colliderect(self.bird):
                self.dead = True
                break
            if downRect.colliderect(self.bird):
                self.dead = True
                break

        if not 0 < self.bird[1] < self.heightScreen:
            self.dead = True

    def run(self):
        clock = pygame.time.Clock()
        pygame.font.init()

        while not self.dead:
            clock.tick(10)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN and not self.dead:
                    self.jump = 20
                    self.gravity = 5
                    self.jumpSpeed = 10

            self.screen.blit(self.background, (0, 0))

            for i in range(5):

                self.screen.blit(self.wallUp, (self.wallx[i], 360 + self.gap[i] - self.offset[i]))
                self.screen.blit(self.wallDown, (self.wallx[i], 0 - self.gap[i] - self.offset[i]))

            font = pygame.font.SysFont("Arial", 70)
            self.screen.blit(font.render(str(self.counter), -1, (255, 255, 255)), ((pygame.display.get_surface()).get_width() / 2 - 35, 50))

            if self.dead:
                self.sprite = 2
            elif self.jump:
                self.sprite = 1

            self.screen.blit(self.birdSprites[self.sprite], (70, self.birdY))


            if not self.dead and self.animation:
                self.sprite = 0
                self.animation = False
            elif not self.dead and not self.animation:
                self.sprite = 3
                self.animation = True

            self.updateWalls()
            self.birdUpdate()

            pygame.display.update()

        font = pygame.font.SysFont("Arial", 200)
        self.screen.blit(font.render('Your score : ' + str(self.counter), -1, (0, 0, 0)), (100, self.heightScreen/2-100))
        pygame.display.update()
        time.sleep(2)
        return self.counter
