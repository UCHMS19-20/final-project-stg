import sys
import random
import pygame

#initializes the program
pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()
#if statement has no purpose other than being able to store large amounts of variables
if True:
    width = 756
    height = 610
    current_key = 0
    white = (255, 255, 255)
    black = (0, 0, 0)
    pink = (186, 9, 115)
    purple = (83, 11, 122)
    screen = pygame.display.set_mode( (width, height) )
    power = 1
    score = 0
    grazes = 0
    size = 25
    font_grazes = pygame.font.SysFont("comicsansms", 20)
    grazes_text = font_grazes.render(f"Grazes: {grazes}", True, white)
    font_score = pygame.font.SysFont("comicsansms", 20)
    score_text = font_score.render(f"Score: {score} ", True, white)
    font_power = pygame.font.SysFont("comicsansms", 20)
    power_text = font_power.render(f"Power: {power} ", True, white)

pygame.display.flip()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((size, size))
        self.image.fill(black)
        self.rect = self.image.get_rect()
        self.rect.centerx = 261
        self.rect.bottom = height - 25
        self.speedx = 0
        self.speedy = 0
        self.speed = 5

    def update(self):
        self.speedx = 0
        self.speedy = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            if keys[pygame.K_RIGHT]:
                if keys[pygame.K_LSHIFT]:
                    self.speedx = -self.speed
                else:
                    self.speedx = -self.speed / 2 
            else:
                if keys[pygame.K_LSHIFT]:
                    self.speedx = -self.speed / 2
                else:
                    self.speedx = -self.speed
                    
        if keys[pygame.K_RIGHT]:
            if keys[pygame.K_LSHIFT]:
                self.speedx = self.speed / 2
            else:
                self.speedx = self.speed        
        if keys[pygame.K_UP]:
            if keys[pygame.K_LSHIFT]:
                self.speedy = -self.speed / 2
            else:
                self.speedy = -self.speed
                
        if keys[pygame.K_DOWN]:
            if keys[pygame.K_LSHIFT]:
                self.speedy = self.speed / 2
            else:
                self.speedy = self.speed
        if self.rect.right > width / 1.55 + ((size / 2) - size / 8):
            self.rect.right = width / 1.55 + ((size / 2) - size / 8)
        if self.rect.left < 30 - ((size / 2) - size / 8):
            self.rect.left = 30 - ((size / 2) - size / 8)
        if self.rect.top < 15 - ((size / 2) - size / 8):
            self.rect.top = 15 - ((size / 2) - size / 8)
        if self.rect.bottom > height - 15 + ((size / 2) - size / 8):
            self.rect.bottom = height - 15 + ((size / 2) - size / 8)
        self.rect.x += self.speedx
        self.rect.y += self.speedy

    def shoot(self):
        if power < 15:
            bullet = Bullet(self.rect.centerx, self.rect.top)
            all_sprites.add(bullet)
            bullets.add(bullet)

class Player_hitbox(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((size / 4, size / 4))
        self.image.fill(white)
        self.rect = self.image.get_rect()
        self.rect.centerx = 261
        self.rect.bottom = height - 35
        self.speedx = 0
        self.speedy = 0
        self.speed = 5

    def update(self):
        self.speedx = 0
        self.speedy = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            if keys[pygame.K_RIGHT]:
                if keys[pygame.K_LSHIFT]:
                    self.speedx = -self.speed
                else:
                    self.speedx = -self.speed / 2 
            else:
                if keys[pygame.K_LSHIFT]:
                    self.speedx = -self.speed / 2
                else:
                    self.speedx = -self.speed
                    
        if keys[pygame.K_RIGHT]:
            if keys[pygame.K_LSHIFT]:
                self.speedx = self.speed / 2
            else:
                self.speedx = self.speed        
        if keys[pygame.K_UP]:
            if keys[pygame.K_LSHIFT]:
                self.speedy = -self.speed / 2
            else:
                self.speedy = -self.speed
                
        if keys[pygame.K_DOWN]:
            if keys[pygame.K_LSHIFT]:
                self.speedy = self.speed / 2
            else:
                self.speedy = self.speed
        if self.rect.right > width / 1.55:
            self.rect.right = width / 1.55
        if self.rect.left < 30:
            self.rect.left = 30
        if self.rect.top < 15:
            self.rect.top = 15
        if self.rect.bottom > height - 15:
            self.rect.bottom = height - 15
        self.rect.x += self.speedx
        self.rect.y += self.speedy

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)   
        self.image = pygame.Surface((10, 10))
        self.image.fill(white)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(int(width / 1.55 - self.rect.width))
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 8)

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > height + 10 or self.rect.left < -25 or self.rect.right > width/1.55 + 25:
            self.rect.x = random.randrange(int(width / 1.55 - self.rect.width))
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 4)

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy

        if self.rect.bottom < 0:
            self.kill()

bullet = pygame.image.load("src/img/heart.png")
bullet = pygame.transform.scale(bullet, (35, 35))

all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
bullets = pygame.sprite.Group()
player = Player()
hitbox = Player_hitbox()
all_sprites.add(player)
all_sprites.add(hitbox)
for n in range(20):
    e = Enemy()
    all_sprites.add(e)
    enemies.add(e)

#game starts the main loop
while True:
    #game delays the reading of the code so its not too fast when it runs
    clock.tick(60)

    for event in pygame.event.get():
        #exits game when pygame.quit is called
        if event.type == pygame.QUIT:
            sys.exit()
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_z]:
        player.shoot()
    all_sprites.update()
    hits = pygame.sprite.groupcollide(enemies, bullets, True, True)
    for hit in hits:
        e = Enemy()
        all_sprites.add(e)
        enemies.add(e)
    hits = pygame.sprite.spritecollide(hitbox, enemies, False)
    if hits:
        pygame.QUIT()
    grazing = pygame.sprite.spritecollide(player, enemies, False)
    if grazing:
        grazes += 1

    screen.fill(pink)

    all_sprites.draw(screen)

    pygame.draw.rect(screen, purple, (round(width / 1.55), 0, width - width / 2, height))
    pygame.draw.rect(screen, purple, (0, 0, width, 15))
    pygame.draw.rect(screen, purple, (0, height - 15, width, 20))
    pygame.draw.rect(screen, purple, (0, 0, 30, height))
    screen.blit(score_text, (width / 1.5, 10) )
    screen.blit(power_text, (width / 1.5, 80) )
    screen.blit(grazes_text, (width / 1.5, 150) )
    pygame.display.update()

"""Things left to do for next:
- Fix grazing
- Add in score and power points
- Add in images"""
