import sys
import random
import pygame
import math
from pygame.math import Vector2

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
    blue = (0, 0, 255)
    silver = (192, 192, 192)
    gray = (128, 128, 128)
    red = (255, 0, 0)
    screen = pygame.display.set_mode( (width, height) )
    power = 1
    score = 0
    graze = 0
    size = 25
    lives = 3
    shoot_time = 0
    easy_time = 0
    graze_time = 0
    

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
        #following code works out player movement
        if keys[pygame.K_LEFT]:
            if keys[pygame.K_RIGHT]:
                #holding down left shift will slow down movement
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
            bullet = Bullet(self.rect.centerx, self.rect.bottom)
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

class Simple_Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)   
        self.image = pygame.Surface((30, 30))
        self.image.fill(white)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(int(width / 1.55 - self.rect.width))
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 8)
        self.speedx = random.randrange(-2, 2)
        self.health = 5

    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.top > height + 10 or self.rect.left < -25 or self.rect.right > width/1.55 + 25:
            self.rect.x = random.randrange(int(width / 1.55 - self.rect.width))
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 4)

    def damage(self):
        self.health -= 1
        if self.health < 0:
            self.kill()

    def drop(self):
        if random.randint(0, 100) > 70:
            point = Point(self.rect.centerx, self.rect.bottom)
            all_sprites.add(point)
            points.add(point)
        elif random.randint(0, 100) > 90:
            power = Power(self.rect.centerx, self.rect.bottom)
            all_sprites.add(power)
            powers.add(power)
        
class Easy_Bullet_Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)   
        self.image = pygame.Surface((30, 30))
        self.image.fill(silver)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(int(width / 1.55 - self.rect.width))
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 8)
        self.speedx = random.randrange(-2, 2)
        self.health = 5

    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.top > height + 10 or self.rect.left < -25 or self.rect.right > width/1.55 + 25:
            self.rect.x = random.randrange(int(width / 1.55 - self.rect.width))
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 4)

    def shoot(self):
        easy_bullet = Easy_Bullet(self.rect.centerx, self.rect.bottom)
        all_sprites.add(easy_bullet)
        easy_bullets.add(easy_bullet)

    def damage(self):
        self.health -= 1
        if self.health < 0:
            self.kill()

    def drop(self):
        if random.randint(0, 100) > 70:
            point = Point(self.rect.centerx, self.rect.bottom)
            all_sprites.add(point)
            points.add(point)
        elif random.randint(0, 100) > 90:
            power = Power(self.rect.centerx, self.rect.bottom)
            all_sprites.add(power)
            powers.add(power)

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

class Easy_Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((5, 5))
        self.image.fill(red)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speed = 8
        self.present_x = hitbox.rect.x - self.rect.x
        self.present_y = hitbox.rect.y - self.rect.y
        self.V = pygame.math.Vector2(self.present_x, self.present_y)
        self.V.normalize()
        self.V.scale_to_length(self.speed)

    def update(self):
        self.rect.move_ip(self.V)

        

    

class Point(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((15, 15))
        self.image.fill(black)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = 3
    
    def update(self):
        self.rect.y += self.speedy

        if self.rect.y > height:
            self.kill()

class Power(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((15, 15))
        self.image.fill(blue)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = 3
    
    def update(self):
        self.rect.y += self.speedy

        if self.rect.y > height:
            self.kill()

bullet = pygame.image.load("src/img/heart.png")
bullet = pygame.transform.scale(bullet, (25, 25))

all_sprites = pygame.sprite.Group()
simple_enemies = pygame.sprite.Group()
easy_bullet_enemies = pygame.sprite.Group()
easy_bullets = pygame.sprite.Group()
bullets = pygame.sprite.Group()
points = pygame.sprite.Group()
powers = pygame.sprite.Group()
player = Player()
hitbox = Player_hitbox()
all_sprites.add(player)
all_sprites.add(hitbox)
#spawns in this number of enemies
for n in range(20):
    se = Simple_Enemy()
    all_sprites.add(se)
    simple_enemies.add(se)
for n in range(10):
    ebe = Easy_Bullet_Enemy()
    all_sprites.add(ebe)
    easy_bullet_enemies.add(ebe)

#game starts the main loop
while True:
    #game delays the reading of the code so its not too fast when it runs
    clock.tick(60)

    for event in pygame.event.get():
        #exits game when pygame.quit is called
        if event.type == pygame.QUIT:
            sys.exit()
    
    keys = pygame.key.get_pressed()

    for e in easy_bullet_enemies:
        if easy_time < 15:
            easy_time += 1
        else:
            e.shoot()
            easy_time = 0
    #if the z button is pressed, allows the user to shoot a bullet
    if keys[pygame.K_z]:
        if shoot_time < 3:
            #creates a delay in firing to ensure that a constant stream of bullets is lessened
            shoot_time += 1
        else:
            #after a certain time, player shoots a bullet
            player.shoot()
            shoot_time = 0
    all_sprites.update()
    #checks to see if the bullets and enemies touch, both disappear if they are
    hits = pygame.sprite.groupcollide(simple_enemies, bullets, False, True)
    for hit in hits:
        hit.damage()
        if hit.health < 0:
            #a point item is dropped
            hit.drop()
            #a new enemy is spawned and added to the list of sprites
            se = Simple_Enemy()
            all_sprites.add(se)
            simple_enemies.add(se)
            #score increases for eaach enemy killed
            score += 1   
    hits = pygame.sprite.groupcollide(easy_bullet_enemies, bullets, False, True)
    for hit in hits:
        hit.damage()
        if hit.health < 0:
            #a point item is dropped
            hit.drop()
            #a new enemy is spawned and added to the list of sprites
            ebe = Easy_Bullet_Enemy()
            all_sprites.add(ebe)
            easy_bullet_enemies.add(ebe)
            #score increases for eaach enemy killed
            score += 1   
    #checks to see if player touches a point box, points disappear if they touch
    hits = pygame.sprite.spritecollide(player, points, True)
    for hit in hits:
        #each point box gives 5 points
        score += 5
    hits = pygame.sprite.spritecollide(player, powers, True)
    for hit in hits:
        #each power box gives 1 power
        power += 1
    #checks to see if player hitbox hit an enemy
    hits = pygame.sprite.spritecollide(hitbox, simple_enemies, False)
    if hits:
        if lives != 0:
            #if the player still has lives left, deduct one and continue
            lives -= 1
            print(lives)
        else:
            #if no more lives remain, exit
            pygame.QUIT()
    hits = pygame.sprite.spritecollide(hitbox, easy_bullet_enemies, False)
    if hits:
        if lives != 0:
            lives -= 1
        else:
            pygame.QUIT()
    """hits = pygame.sprite.spritecollide(hitbox, easy_bullets, True)
    if hits:
        if lives != 0:
            lives -= 1
        else:
            pygame.QUIT()"""
    grazing = pygame.sprite.spritecollide(player, simple_enemies, False)
    for grazes in grazing:
        if graze_time < 5:
            graze_time += 1
        else:
            graze += 1
            graze_time = 0

    screen.fill(pink)

    all_sprites.draw(screen)

    #these rectangles set up the window formatting
    pygame.draw.rect(screen, purple, (round(width / 1.55), 0, width - width / 2, height))
    pygame.draw.rect(screen, purple, (0, 0, width, 15))
    pygame.draw.rect(screen, purple, (0, height - 15, width, 20))
    pygame.draw.rect(screen, purple, (0, 0, 30, height))
    #these text update various numbers involved in game display
    font_grazes = pygame.font.SysFont("comicsansms", 20)
    grazes_text = font_grazes.render(f"Grazes: {graze}", True, white)
    font_score = pygame.font.SysFont("comicsansms", 20)
    score_text = font_score.render(f"Score: {score} ", True, white)
    font_power = pygame.font.SysFont("comicsansms", 20)
    power_text = font_power.render(f"Power: {power} ", True, white)
    screen.blit(score_text, (width / 1.5, 10) )
    screen.blit(power_text, (width / 1.5, 80) )
    screen.blit(grazes_text, (width / 1.5, 150) )
    pygame.display.update()

"""Things left to do for next time:
- Add in enemy HP
- Add enemy types (basic bullet shots, advanced bullet shots)
- Add in enemy bullets
- Add in images
- Add in lives"""
