import sys
import random
import pygame
import math
from pygame.math import Vector2

#initializes the program
pygame.init()
pygame.mixer.init()

#load and play background music
pygame.mixer.music.load("src/mus/TOUCH.mp3")
pygame.mixer.music.play(90, 1.5)
pygame.display.set_caption('Start the game!')
#allows the use of the clock to slow down main loop
clock = pygame.time.Clock()
#if statement has no purpose other than being able to store large amounts of variables
if True:
    width, height = 756, 610
    current_key = 0
    white = (255, 255, 255)
    black = (0, 0, 0)
    pink = (186, 9, 115)
    purple = (83, 11, 122)
    blue = (0, 0, 255)
    silver = (192, 192, 192)
    gray = (128, 128, 128)
    red = (255, 0, 0)
    orange = (255,69,0)
    screen = pygame.display.set_mode( (width, height) )
    power = 0
    score = 0
    graze = 0
    size = 25
    lives = 5
    shoot_time = 0
    easy_time = 0
    hard_time = 0
    graze_time = 0
    score_check = 0
    invincibility = 0
    invincibility_timer = 0
    lives_position = round(width / 1.55) + 75
    difficulty_selection = 1
    running = True
    menu = True
    instructions = False
    difficulty = False
    menu_selection = 1
    font_small = pygame.font.SysFont("comicsansms", 15)
    font_medium = pygame.font.SysFont("comicsansms", 20)
    font_large = pygame.font.SysFont("comicsansms", 30)

pygame.display.flip()

class Player(pygame.sprite.Sprite):
    """Creates a player class that can be controlled by the user"""
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
        #following code works out player movement when an arrow key is pressed
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
        #if player goes beyond the border, it sets the position to the border coordinate
        if self.rect.right > width / 1.55 + ((size / 2) - size / 8):
            self.rect.right = width / 1.55 + ((size / 2) - size / 8)
        if self.rect.left < 30 - ((size / 2) - size / 8):
            self.rect.left = 30 - ((size / 2) - size / 8)
        if self.rect.top < 15 - ((size / 2) - size / 8):
            self.rect.top = 15 - ((size / 2) - size / 8)
        if self.rect.bottom > height - 15 + ((size / 2) - size / 8):
            self.rect.bottom = height - 15 + ((size / 2) - size / 8)
        #changes its coordinates based on self.speed
        self.rect.x += self.speedx
        self.rect.y += self.speedy

    
    def shoot(self):
        """Defines what the player does when shooting bullets"""
        #depending on the power level, various bullet classes are called
        if power < 15:
            bullet = Bullet(self.rect.centerx, self.rect.bottom)
            all_sprites.add(bullet)
            bullets.add(bullet)
        elif power < 35:
            bullet = Bullet(self.rect.centerx - 15, self.rect.bottom)
            all_sprites.add(bullet)
            bullets.add(bullet)
            bullet = Bullet(self.rect.centerx + 15, self.rect.bottom)
            all_sprites.add(bullet)
            bullets.add(bullet)
        elif power < 60:
            bullet = Bullet(self.rect.centerx - 18, self.rect.bottom)
            all_sprites.add(bullet)
            bullets.add(bullet)
            bullet = Bullet(self.rect.centerx + 18, self.rect.bottom)
            all_sprites.add(bullet)
            bullets.add(bullet)
            bullet = Bullet(self.rect.centerx - 30, self.rect.bottom)
            all_sprites.add(bullet)
            bullets.add(bullet)
            bullet = Bullet(self.rect.centerx + 30, self.rect.bottom)
            all_sprites.add(bullet)
            bullets.add(bullet)
        elif power > 60:
            bullet = Bullet(self.rect.centerx - 18, self.rect.bottom)
            all_sprites.add(bullet)
            bullets.add(bullet)
            bullet = Bullet(self.rect.centerx + 18, self.rect.bottom)
            all_sprites.add(bullet)
            bullets.add(bullet)
            bullet = Bullet(self.rect.centerx - 30, self.rect.bottom)
            all_sprites.add(bullet)
            bullets.add(bullet)
            bullet = Bullet(self.rect.centerx + 30, self.rect.bottom)
            all_sprites.add(bullet)
            bullets.add(bullet)
            bullet = Bullet(self.rect.centerx - 30, self.rect.bottom + 30)
            all_sprites.add(bullet)
            bullets.add(bullet)
            bullet = Bullet(self.rect.centerx + 30, self.rect.bottom + 30)
            all_sprites.add(bullet)
            bullets.add(bullet)
            bullet = Bullet(self.rect.centerx, self.rect.bottom)
            all_sprites.add(bullet)
            bullets.add(bullet)
    
    def hit(self):
        """Changes the player color to red when invincible after getting hit"""
        self.image.fill(red)

    def normal(self):
        """Changes the player color to black when not invincible after getting hit"""
        self.image.fill(black)

class Player_hitbox(pygame.sprite.Sprite):
    """Hitbox class acts similar to player class, except this class checks for collisions later in the code"""
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
        #moves player hitbox based on what arrow keys are pressed
        if keys[pygame.K_LEFT]:
            if keys[pygame.K_RIGHT]:
                #slows down movement when left shift is pressed
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
        #if hitbox goes beyond the border, the coordinates are set to at the border itself
        if self.rect.right > width / 1.55:
            self.rect.right = width / 1.55
        if self.rect.left < 30:
            self.rect.left = 30
        if self.rect.top < 15:
            self.rect.top = 15
        if self.rect.bottom > height - 15:
            self.rect.bottom = height - 15
        #changes x and y positions based on self.speed
        self.rect.x += self.speedx
        self.rect.y += self.speedy

class Simple_Enemy(pygame.sprite.Sprite):
    """Creates a simple enemy that simply falls from the top at random speeds"""
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)   
        self.image = pygame.Surface((30, 30))
        self.image.fill(red)
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
        """Subtracts health from self when hit by player bullet, disappearing when health = 0"""
        self.health -= 1
        if self.health < 0:
            self.kill()

    def drop(self):
        """Drops a point or power class object based on random chance"""
        if random.randint(0, 100) > 70:
            point = Point(self.rect.centerx, self.rect.bottom)
            all_sprites.add(point)
            points.add(point)
        elif random.randint(0, 100) > 80:
            power = Power(self.rect.centerx, self.rect.bottom)
            all_sprites.add(power)
            powers.add(power)
        
class Hard_Enemy(pygame.sprite.Sprite):
    """Creates an enemy that falls down slowly, and cannot be killed by player"""
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)   
        self.image = pygame.Surface((250, 30))
        self.image.fill(orange)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(int(width / 1.55 - self.rect.width))
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 2)
        self.health = 999999

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > height + 10 or self.rect.left < -25 or self.rect.right > width/1.55 + 25:
            self.rect.x = random.randrange(int(width / 1.55 - self.rect.width))
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 2)

    def damage(self):
        """Subtracts damage from health,and disappears if health = 0"""
        self.health -= 1
        if self.health < 0:
            self.kill()

    def drop(self):
        """Drops a point or power item based on chance"""
        if random.randint(0, 100) > 70:
            point = Point(self.rect.centerx, self.rect.bottom)
            all_sprites.add(point)
            points.add(point)
        elif random.randint(0, 100) > 80:
            power = Power(self.rect.centerx, self.rect.bottom)
            all_sprites.add(power)
            powers.add(power)

class Easy_Bullet_Enemy(pygame.sprite.Sprite):
    """Creates an enemy that uses player position to shoot bullet towards player"""
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)   
        self.image = pygame.Surface((30, 30))
        self.image.fill(purple)
        self.rect = self.image.get_rect()
        self.side = random.randint(0,100)
        self.rect.x = -20 if self.side >= 50 else width / 1.55 - self.rect.width + 20
        self.rect.y = random.randrange(self.rect.height, 35)
        self.speedy = random.randrange(0, 2)
        self.speedx = random.randrange(1, 8) if self.side >= 50 else random.randrange(-8, -1)
        self.health = 5

    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.top > height + 10 or self.rect.left < -25 or self.rect.right > width/1.55 + 25:
            self.rect.x = random.randrange(int(width / 1.55 - self.rect.width))
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 4)

    def shoot(self):
        """Shoots bullets at designated increments by calling an enemy bullet class"""
        global easy_time
        if easy_time < 36:
            easy_time += 1
        else: 
            easy_bullet = Easy_Bullet(self.rect.centerx, self.rect.bottom)
            all_sprites.add(easy_bullet)
            easy_bullets.add(easy_bullet)
            easy_time = 0

    def damage(self):
        """Subtracts health from self, and kills if health = 0"""
        self.health -= 1
        if self.health < 0:
            self.kill()

    def drop(self):
        """Drops point or power item based on luck"""
        if random.randint(0, 100) > 70:
            point = Point(self.rect.centerx, self.rect.bottom)
            all_sprites.add(point)
            points.add(point)
        elif random.randint(0, 100) > 60:
            power = Power(self.rect.centerx, self.rect.bottom)
            all_sprites.add(power)
            powers.add(power)

class Hard_Bullet_Enemy(pygame.sprite.Sprite):
    """Creates an enemy that shoots bullets in a square formation around itself"""
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)   
        self.image = pygame.Surface((30, 30))
        self.image.fill(pink)
        self.rect = self.image.get_rect()
        self.side = random.randint(0,100)
        self.rect.x = random.randrange(int(width / 1.55 - self.rect.width))
        self.rect.y = -30
        self.speedy = 2
        self.health = 30

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > height + 10 or self.rect.left < -25 or self.rect.right > width/1.55 + 25:
            self.rect.x = random.randrange(int(width / 1.55 - self.rect.width))
            self.rect.y = random.randrange(-100, -40)

    def shoot(self):
        """Shoots bullets with a designated cooldown by calling an enemy bullet class"""
        global hard_time
        if hard_time < 70:
            hard_time += 1
        else: 
            hard_bullet = Hard_Bullet(self.rect.left, self.rect.bottom)
            all_sprites.add(hard_bullet)
            hard_bullets.add(hard_bullet)
            hard_bullet = Hard_Bullet(self.rect.centerx, self.rect.bottom)
            all_sprites.add(hard_bullet)
            hard_bullets.add(hard_bullet)
            hard_bullet = Hard_Bullet(self.rect.right, self.rect.bottom)
            all_sprites.add(hard_bullet)
            hard_bullets.add(hard_bullet)
            hard_bullet = Hard_Bullet(self.rect.left, self.rect.centery)
            all_sprites.add(hard_bullet)
            hard_bullets.add(hard_bullet)
            hard_bullet = Hard_Bullet(self.rect.left, self.rect.top)
            all_sprites.add(hard_bullet)
            hard_bullets.add(hard_bullet)
            hard_bullet = Hard_Bullet(self.rect.centerx, self.rect.top)
            all_sprites.add(hard_bullet)
            hard_bullets.add(hard_bullet)
            hard_bullet = Hard_Bullet(self.rect.right, self.rect.top)
            all_sprites.add(hard_bullet)
            hard_bullets.add(hard_bullet)
            hard_bullet = Hard_Bullet(self.rect.right, self.rect.centery)
            all_sprites.add(hard_bullet)
            hard_bullets.add(hard_bullet)
            hard_time = 0

    def damage(self):
        self.health -= 1
        if self.health < 0:
            self.kill()

    def drop(self):
        if random.randint(0, 100) > 70:
            point = Point(self.rect.centerx, self.rect.bottom)
            all_sprites.add(point)
            points.add(point)
        elif random.randint(0, 100) > 60:
            power = Power(self.rect.centerx, self.rect.bottom)
            all_sprites.add(power)
            powers.add(power)

class Bullet(pygame.sprite.Sprite):
    """Creates a bullet for the player to shoot"""
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speed = -10
        self.side = 0
        if self.rect.right < player.rect.left + 1:
            self.side = 1
        elif self.rect.left > player.rect.right + 1:
            self.side = -1
        else:
            self.side = 0
        self.V = pygame.math.Vector2(self.side, 2)
        self.V.normalize()
        self.V.scale_to_length(self.speed)

    def update(self):
        self.rect.move_ip(self.V)

        if self.rect.bottom < 0:
            self.kill()

class Easy_Bullet(pygame.sprite.Sprite):
    """Creates a bullet that enemies use to track player"""
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((5, 5))
        self.image.fill(purple)
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

class Hard_Bullet(pygame.sprite.Sprite):
    """Creates a bullet that shoots out from various points on an enemy class"""
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((5, 5))
        self.image.fill(purple)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.V = (0, 0)
        
        #velocity is set based on position that the bullet is created in relation to the enemy
        if self.rect.centerx < hbe.rect.centerx + 5 and self.rect.centerx > hbe.rect.centerx - 5:
            self.X_vel = 0
        elif self.rect.centerx < hbe.rect.centerx:
            self.X_vel = -3
        elif self.rect.centerx > hbe.rect.centerx:
            self.X_vel = 3
        if self.rect.centery < hbe.rect.centery + 5 and self.rect.centery > hbe.rect.centery - 5:
            self.Y_vel = 0
        elif self.rect.centery < hbe.rect.centery:
            self.Y_vel = -3
        elif self.rect.centery > hbe.rect.centery:
            self.Y_vel = 3
        self.V = (self.X_vel, self.Y_vel)

    def update(self):
        self.rect.move_ip(self.V)       

class Point(pygame.sprite.Sprite):
    """Creates a point item that increases points when collected"""
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
    """Creates a power item that increases power when collected"""
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

#gets the image for the player bullet and scales it down
bullet = pygame.image.load("src/img/heart.png")
bullet = pygame.transform.scale(bullet, (15, 15))

#puts all of the sprites into a sprite group for collisions to work later
all_sprites = pygame.sprite.Group()
simple_enemies = pygame.sprite.Group()
hard_enemies = pygame.sprite.Group()
easy_bullet_enemies = pygame.sprite.Group()
easy_bullets = pygame.sprite.Group()
hard_bullet_enemies = pygame.sprite.Group()
hard_bullets = pygame.sprite.Group()
bullets = pygame.sprite.Group()
points = pygame.sprite.Group()
powers = pygame.sprite.Group()
player = Player()
hitbox = Player_hitbox()
all_sprites.add(player)
all_sprites.add(hitbox)

#begins the menu prompt
while menu:
    clock.tick(60)

    for event in pygame.event.get():
        #exits game when pygame.quit is called
        if event.type == pygame.QUIT:
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if not difficulty:
                    #moves the selected option up if it is not at the highest option
                    if menu_selection != 1:
                        menu_selection -= 1
                else:
                    if difficulty_selection != 1:
                        difficulty_selection -= 1
            if event.key == pygame.K_DOWN:
                #moves the selected option down if it is not at the lowest option
                if not difficulty:
                    if menu_selection != 4:
                        menu_selection += 1
                else:
                    if difficulty_selection != 4:
                        difficulty_selection += 1
            #z is used to select the menu prompts
            if event.key == pygame.K_z:
                if not difficulty:
                    if menu_selection == 1:
                        menu = False
                    if menu_selection == 2:
                        instructions = True
                        difficulty = False
                    if menu_selection == 3:
                        difficulty = True
                        instructions = False
                    if menu_selection == 4:
                        pygame.QUIT()
                else:
                    if difficulty_selection == 1:
                        lives = 10
                        difficulty = False
                    if difficulty_selection == 2:
                        lives = 5
                        difficulty = False
                    if difficulty_selection == 3:
                        lives = 2
                        difficulty = False
                    if difficulty_selection == 4:
                        lives = 0
                        difficulty = False
    
    screen.fill(pink)
    #based on what the variable is, it darkens the selected menu prompt
    if menu_selection == 1:
        start_text = font_medium.render(f"Start", True, black)
        instructions_text = font_medium.render(f"Instructions", True, white)
        difficulty_text = font_medium.render(f"Difficulty", True, white)
        quit_text = font_medium.render("Quit", True, white)
    if menu_selection == 2:
        start_text = font_medium.render(f"Start", True, white)
        instructions_text = font_medium.render(f"Instructions", True, black)
        difficulty_text = font_medium.render(f"Difficulty", True, white)
        quit_text = font_medium.render("Quit", True, white)
    if menu_selection == 3:
        start_text = font_medium.render(f"Start", True, white)
        instructions_text = font_medium.render(f"Instructions", True, white)
        difficulty_text = font_medium.render(f"Difficulty", True, black)
        quit_text = font_medium.render("Quit", True, white)
    if menu_selection == 4:
        start_text = font_medium.render(f"Start", True, white)
        instructions_text = font_medium.render(f"Instructions", True, white)
        difficulty_text = font_medium.render(f"Difficulty", True, white)
        quit_text = font_medium.render("Quit", True, black)

    #if the instructions tab was selected, these text lines display
    if instructions:
        instructions_selected_text = font_medium.render("Move using the arrow keys.", True, white)
        screen.blit(instructions_selected_text, (width / 2.3, 100))
        instructions_selected_text = font_medium.render("Hold shift while moving to slow movements.", True, white)
        screen.blit(instructions_selected_text, (width / 2.3, 125))
        instructions_selected_text = font_medium.render("Press Z to shoot out bullets.", True, white)
        screen.blit(instructions_selected_text, (width / 2.3, 150))
        instructions_selected_text = font_medium.render("Shoot enemies to drop power-ups.", True, white)
        screen.blit(instructions_selected_text, (width / 2.3, 175))
        instructions_selected_text = font_medium.render("Blue power-up increases power.", True, white)
        screen.blit(instructions_selected_text, (width / 2.3, 200))
        instructions_selected_text = font_medium.render("Black power-up increases score.", True, white)
        screen.blit(instructions_selected_text, (width / 2.3, 225))
        instructions_selected_text = font_medium.render("Red enemies move straight down.", True, white)
        screen.blit(instructions_selected_text, (width / 2.3, 250))
        instructions_selected_text = font_medium.render("Orange enemies cannot be defeated.", True, white)
        screen.blit(instructions_selected_text, (width / 2.3, 275))
        instructions_selected_text = font_medium.render("Purple enemies shoot bullets.", True, white)
        screen.blit(instructions_selected_text, (width / 2.3, 300))
        instructions_selected_text = font_medium.render("When hit, you will lose a life.", True, white)
        screen.blit(instructions_selected_text, (width / 2.3, 325))
        instructions_selected_text = font_medium.render("Getting hit grants short invincibility.", True, white)
        screen.blit(instructions_selected_text, (width / 2.3, 350))
        instructions_selected_text = font_medium.render("Touching the enemies with the player", True, white)
        screen.blit(instructions_selected_text, (width / 2.3, 375))
        instructions_selected_text = font_medium.render("without touching the hitbox grants points.", True, white)
        screen.blit(instructions_selected_text, (width / 2.3, 400))
    #if the difficulty tab was selected, these options are displayed
    if difficulty:
        #following code changes tab color and mini description based on what tab is currently selected
        if difficulty_selection == 1:
            easy_text = font_medium.render(f"Easy", True, black)
            screen.blit(easy_text, (width / 2.3, 200) )
            easy_description = font_small.render("Nice and chillin'. 10 lives are given to the player.", True, white)
            screen.blit(easy_description, (width / 2.3, 235) )
            easy_description = font_small.render("A casual player's preferred difficulty.", True, white)
            screen.blit(easy_description, (width / 2.3, 270) )
            medium_text = font_medium.render(f"Normal", True, white)
            screen.blit(medium_text, (width / 2.3, 300) )
            hard_text = font_medium.render(f"Hard", True, white)
            screen.blit(hard_text, (width / 2.3, 400) )
            sanservino_text = font_medium.render("Sanservino", True, white)
            screen.blit(sanservino_text, (width / 2.3, 500) )
            pygame.display.set_caption('I think you can go harder than that...')
        if difficulty_selection == 2:
            easy_text = font_medium.render(f"Easy", True, white)
            screen.blit(easy_text, (width / 2.3, 200) )
            medium_text = font_medium.render(f"Normal", True, black)
            screen.blit(medium_text, (width / 2.3, 300) )
            medium_description = font_small.render("A bit challenging. 5 lives are given to the player.", True, white)
            screen.blit(medium_description, (width / 2.3, 335) )
            medium_description = font_small.render("Intended for most players.", True, white)
            screen.blit(medium_description, (width / 2.3, 370) )
            hard_text = font_medium.render(f"Hard", True, white)
            screen.blit(hard_text, (width / 2.3, 400) )
            sanservino_text = font_medium.render("Sanservino", True, white)
            screen.blit(sanservino_text, (width / 2.3, 500) )
            pygame.display.set_caption('This is not too bad.')
        if difficulty_selection == 3:
            easy_text = font_medium.render(f"Easy", True, white)
            screen.blit(easy_text, (width / 2.3, 200) )
            medium_text = font_medium.render(f"Normal", True, white)
            screen.blit(medium_text, (width / 2.3, 300) )
            hard_text = font_medium.render(f"Hard", True, black)
            screen.blit(hard_text, (width / 2.3, 400) )
            hard_description = font_small.render("Quite difficult. 2 lives are given to the player.", True, white)
            screen.blit(hard_description, (width / 2.3, 435) )
            hard_description = font_small.render("Good for those who like to lose.", True, white)
            screen.blit(hard_description, (width / 2.3, 470) )
            sanservino_text = font_medium.render("Sanservino", True, white)
            screen.blit(sanservino_text, (width / 2.3, 500) )
            pygame.display.set_caption('Feeling confident, huh?')
        if difficulty_selection == 4:
            easy_text = font_medium.render(f"Easy", True, white)
            screen.blit(easy_text, (width / 2.3, 200) )
            medium_text = font_medium.render(f"Normal", True, white)
            screen.blit(medium_text, (width / 2.3, 300) )
            hard_text = font_medium.render(f"Hard", True, white)
            screen.blit(hard_text, (width / 2.3, 400) )
            sanservino_text = font_medium.render("Sanservino", True, black)
            sanservino_description = font_small.render("A brutal campaign with only one life.", True, white)
            screen.blit(sanservino_description, (width / 2.3, 535) )
            sanservino_description = font_small.render("Good for masochists and idiots.", True, white)
            screen.blit(sanservino_description, (width / 2.3, 570) )
            screen.blit(sanservino_text, (width / 2.3, 500) )
            pygame.display.set_caption('All right, clear your desk.')

    screen.blit(start_text, (width / 5, 250) )
    screen.blit(instructions_text, (width / 6, 325) )
    screen.blit(difficulty_text, (width / 7, 400) )
    screen.blit(quit_text, (width / 8, 475))

    pygame.display.flip()

#game starts the main loop
while running:
    #game delays the reading of the code so its not too fast when it runs
    clock.tick(60)

    for event in pygame.event.get():
        #exits game when pygame.quit is called
        if event.type == pygame.QUIT:
            sys.exit()

    #sets the score_check based on the score the player has
    if score_check != 3:
        if score < 150 and score > 50:
            score_check = 2
            pygame.display.set_caption("Let's add a little more.")
    if score_check != 5:
        if score < 300 and score > 150:
            score_check = 4
            pygame.display.set_caption('Too easy?')
    if score_check != 7:
        if score < 450 and score > 300:
            score_check = 6
            pygame.display.set_caption('Release the enemies!')
    if score_check != 9:
        if score < 750 and score > 450:
            score_check = 8
            pygame.display.set_caption("Ooh, let's spice things up a bit.")
    if score_check != 11:
        if score < 1000 and score > 750:
            score_check = 10
            pygame.display.set_caption('Impossible...')
    if score_check != 13:
        if score < 1250 and score > 1000:
            score_check = 12
            pygame.display.set_caption('Now marks the end...')
    
    #sends out various enemies in waves as the player score increases
    if score_check == 0:
        for n in range(10):
            se = Simple_Enemy()
            all_sprites.add(se)
            simple_enemies.add(se)
        score_check = 1
    if score_check == 2:
        for n in range(5):
            se = Simple_Enemy()
            all_sprites.add(se)
            simple_enemies.add(se)
        for n in range(1):
            he = Hard_Enemy()
            all_sprites.add(he)
            hard_enemies.add(he)
        score_check = 3
    if score_check == 4:
        for n in range(5):
            se = Simple_Enemy()
            all_sprites.add(se)
            simple_enemies.add(se)
        for n in range(1):
            ebe = Easy_Bullet_Enemy()
            all_sprites.add(ebe)
            easy_bullet_enemies.add(ebe)
        score_check = 5
    if score_check == 6:
        for n in range(10):
            se = Simple_Enemy()
            all_sprites.add(se)
            simple_enemies.add(se)
        score_check = 7
    if score_check == 8:
        for n in range(5):
            se = Simple_Enemy()
            all_sprites.add(se)
            simple_enemies.add(se)
        for n in range(1):
            hbe = Hard_Bullet_Enemy()
            all_sprites.add(hbe)
            hard_bullet_enemies.add(hbe)
        score_check = 9
    if score_check == 10:
        for n in range(5):
            se = Simple_Enemy()
            all_sprites.add(se)
            simple_enemies.add(se)
        for n in range(1):
            ebe = Easy_Bullet_Enemy()
            all_sprites.add(ebe)
            easy_bullet_enemies.add(ebe)
        score_check = 11
    if score_check == 12:
        for n in range(5):
            se = Simple_Enemy()
            all_sprites.add(se)
            simple_enemies.add(se)
        for n in range(1):
            ebe = Easy_Bullet_Enemy()
            all_sprites.add(ebe)
            easy_bullet_enemies.add(ebe)
        score_check = 13

    keys = pygame.key.get_pressed()
    #causes both bullet enemies to shoot based on how many enemies there are on screen
    for e in hard_bullet_enemies:
        e.shoot()
    for e in easy_bullet_enemies:
        e.shoot()
    #if the z button is pressed, allows the user to shoot a bullet
    if keys[pygame.K_z]:
        if shoot_time < 5:
            #creates a delay in firing to ensure that a constant stream of bullets is lessened
            shoot_time += 1
        else:
            #after a certain time, player shoots a bullet
            player.shoot()
            shoot_time = 0
    all_sprites.update()
    #checks to see if the bullets and red enemies touch
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
    #checks to see if bullets and orange enemies touch
    hits = pygame.sprite.groupcollide(hard_enemies, bullets, False, True)
    for hit in hits:
        hit.damage()
        if hit.health < 0:
            #a point item is dropped
            hit.drop()
            #a new enemy is spawned and added to the list of sprites
            he = Hard_Enemy()
            all_sprites.add(he)
            hard_enemies.add(he)
            #score increases for eaach enemy killed
            score += 1   
    #checks to see if purple enemies and bullets touch
    hits = pygame.sprite.groupcollide(hard_bullet_enemies, bullets, False, True)
    for hit in hits:
        hit.damage()
        if hit.health < 0:
            #a point item is dropped
            hit.drop()
            #a new enemy is spawned and added to the list of sprites
            hbe = Hard_Bullet_Enemy()
            all_sprites.add(hbe)
            hard_bullet_enemies.add(hbe)
            #score increases for eaach enemy killed
            score += 1  
    #checks to see if purple enemies and bullets touch
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
    if invincibility == 0:
        #checks to see if hitbox hit red enemies
        hits = pygame.sprite.spritecollide(hitbox, simple_enemies, False)
        if hits:
            if lives != 0:
                #if the player still has lives left, deduct one and continue
                lives -= 1
                player.hit()
                invincibility_timer = 60
            else:
                #if no more lives remain, exit
                running = False
        #checks to see if hitbox hit purple enemy
        hits = pygame.sprite.spritecollide(hitbox, easy_bullet_enemies, False)
        if hits:
            if lives != 0:
                #if the player still has lives left, deduct one and continue
                lives -= 1
                player.hit()
                invincibility_timer = 60
            else:
                #if no more lives remain, exit
                running = False
        #checks to see if hitbox hit bullets
        hits = pygame.sprite.spritecollide(hitbox, easy_bullets, False)
        if hits:
            if lives != 0:
                #if the player still has lives left, deduct one and continue
                lives -= 1
                player.hit()
                invincibility_timer = 60
            else:
                #if no more lives remain, exit
                running = False
        #checks to see if hitbox hit orange enemy
        hits = pygame.sprite.spritecollide(hitbox, hard_enemies, False)
        if hits:
            if lives != 0:
                #if the player still has lives left, deduct one and continue
                lives -= 1
                player.hit()
                invincibility_timer = 60
            else:
                #if no more lives remain, exit
                running = False
        #checks to see if hitbox hit purple enemy
        hits = pygame.sprite.spritecollide(hitbox, hard_bullet_enemies, False)
        if hits:
            if lives != 0:
                #if the player still has lives left, deduct one and continue
                lives -= 1
                player.hit()
                invincibility_timer = 60
            else:
                #if no more lives remain, exit
                running = False
        #check to see if hitbox hit bullets
        hits = pygame.sprite.spritecollide(hitbox, hard_bullets, False)
        if hits:
            if lives != 0:
                #if the player still has lives left, deduct one and continue
                lives -= 1
                player.hit()
                invincibility_timer = 60
            else:
                #if no more lives remain, exit
                running = False

    #invincibility timer works by creating a time delay from getting hit, to the next time the hit will count, giving the player some invincibility frames
    if invincibility_timer > 0:
        invincibility_timer -= 1
        invincibility = 1
    if invincibility_timer == 0:
        invincibility = 0
        player.normal()
    #checks grazing and sees whether or not the player hits into the various types of enemies
    #graze time cooldown is indicated to ensure that grazes aren't added too quickly
    grazing = pygame.sprite.spritecollide(player, simple_enemies, False)
    for grazes in grazing:
        if graze_time < 10:
            graze_time += 1
        else:
            graze += 1
            graze_time = 0
    grazing = pygame.sprite.spritecollide(player, easy_bullet_enemies, False)
    for grazes in grazing:
        if graze_time < 10:
            graze_time += 1
        else:
            graze += 1
            graze_time = 0
    grazing = pygame.sprite.spritecollide(player, easy_bullets, False)
    for grazes in grazing:
        if graze_time < 10:
            graze_time += 1
        else:
            graze += 1
            graze_time = 0
    grazing = pygame.sprite.spritecollide(player, hard_enemies, False)
    for grazes in grazing:
        if graze_time < 10:
            graze_time += 1
        else:
            graze += 1
            graze_time = 0
    grazing = pygame.sprite.spritecollide(player, hard_bullet_enemies, False)
    for grazes in grazing:
        if graze_time < 10:
            graze_time += 1
        else:
            graze += 1
            graze_time = 0
    grazing = pygame.sprite.spritecollide(player, hard_bullets, False)
    for grazes in grazing:
        if graze_time < 10:
            graze_time += 1
        else:
            graze += 1
            graze_time = 0

    #changes the screen to color silver
    screen.fill(silver)

    #displays the sprites loaded onto groups
    all_sprites.draw(screen)

    #these rectangles set up the window formatting
    pygame.draw.rect(screen, gray, (round(width / 1.55), 0, width - width / 2, height))
    pygame.draw.rect(screen, gray, (0, 0, width, 15))
    pygame.draw.rect(screen, gray, (0, height - 15, width, 20))
    pygame.draw.rect(screen, gray, (0, 0, 30, height))
    
    #repeats code for making a life symbol on the side of the screen, depending on number of lives left
    if lives > 0:
        if lives == 10:
            for n in range(10):
                pygame.draw.rect(screen, red, (lives_position, 235, 5, 5))
                lives_position += 10
            lives_position = round(width / 1.55) + 75
        if lives == 9:
            for n in range(9):
                pygame.draw.rect(screen, red, (lives_position + 5, 235, 5, 5))
                lives_position += 10
            lives_position = round(width / 1.55) + 75
        if lives == 8:
            for n in range(8):
                pygame.draw.rect(screen, red, (lives_position + 5, 235, 5, 5))
                lives_position += 10
            lives_position = round(width / 1.55) + 75
        if lives == 7:
            for n in range(7):
                pygame.draw.rect(screen, red, (lives_position + 5, 235, 5, 5))
                lives_position += 10
            lives_position = round(width / 1.55) + 75
        if lives == 6:
            for n in range(6):
                pygame.draw.rect(screen, red, (lives_position + 5, 235, 5, 5))
                lives_position += 10
            lives_position = round(width / 1.55) + 75
        if lives == 5:
            for n in range(5):
                pygame.draw.rect(screen, red, (lives_position + 5, 235, 5, 5))
                lives_position += 10
            lives_position = round(width / 1.55) + 75
        if lives == 4:
            for n in range(4):
                pygame.draw.rect(screen, red, (lives_position + 5, 235, 5, 5))
                lives_position += 10
            lives_position = round(width / 1.55) + 75
        if lives == 3:
            for n in range(3):
                pygame.draw.rect(screen, red, (lives_position + 5, 235, 5, 5))
                lives_position += 10
            lives_position = round(width / 1.55) + 75
        if lives == 2:
            for n in range(2):
                pygame.draw.rect(screen, red, (lives_position + 5, 235, 5, 5))
                lives_position += 10
            lives_position = round(width / 1.55) + 75
        if lives == 1:
            for n in range(1):
                pygame.draw.rect(screen, red, (lives_position + 5, 235, 5, 5))
                lives_position += 10
            lives_position = round(width / 1.55) + 75
    
    #these text update various numbers involved in game display on right hand side
    lives_text = font_medium.render("Lives: ", True, white)
    grazes_text = font_medium.render(f"Grazes: {graze}", True, white)
    score_text = font_medium.render(f"Score: {score} ", True, white)
    power_text = font_medium.render(f"Power: {power} ", True, white)
    screen.blit(score_text, (width / 1.5, 10) )
    screen.blit(power_text, (width / 1.5, 80) )
    screen.blit(grazes_text, (width / 1.5, 150) )
    screen.blit(lives_text, (width / 1.5, 220))

    pygame.display.update()

#this sections is active once the player runs out of lives
#prints out different stats of the player, and returns a final score based on a calculation
screen.fill(black)
pygame.display.set_caption('Try again next time.')
screen.blit(score_text, (100, 100))
screen.blit(grazes_text, (100, 200))
screen.blit(power_text, (100, 300))
calculation_text = font_medium.render(f"Final score: ({score}) + ({graze} * 5) + ({power})", True, white)
screen.blit(calculation_text, (100, 400))
final_text = font_large.render(f"Final Score: {score + graze * 5 + power}", True, white)
screen.blit(final_text, (100, 550))
pygame.display.update()
#display remains for a few seconds before automatically closing
pygame.time.wait(6500)