import pygame
import random

pygame.init()

window_width = 1200
window_height = 900
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Money Catcher")

white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)

font = pygame.font.SysFont(None, 30)

background_image = pygame.image.load("background_scifi2.png").convert()
game_over_background = pygame.image.load("goa_text_background.png").convert()
money_image = pygame.image.load("chick.png").convert_alpha()
money_image = pygame.transform.scale(money_image, (100, 200))
jail_image = pygame.image.load("matrix_final.png").convert_alpha()
jail_image = pygame.transform.scale(jail_image, (200, 100))
player_image = pygame.image.load("wtate.png").convert_alpha()
player_image = pygame.transform.scale(player_image, (150, 150))

pygame.mixer.init() 
pygame.mixer.music.load("theme.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.5)
game_over_sound = pygame.mixer.Sound("game_over.mp3")
catch_money_sound = pygame.mixer.Sound("perfect.mp3")

clock = pygame.time.Clock()

player_x = 400
player_y = 750
player_speed = 10
money_list = []
jail_list = []
score = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < window_width - player_image.get_width():
        player_x += player_speed

    if random.randint(1, 100) == 1:
        money_list.append(pygame.Rect(random.randint(0, window_width - money_image.get_width()), -money_image.get_height(), money_image.get_width(), money_image.get_height()))
    if random.randint(1, 200) == 1:
        jail_list.append(pygame.Rect(random.randint(0, window_width - jail_image.get_width()), -jail_image.get_height(), jail_image.get_width(), jail_image.get_height()))

    for money in money_list[:]:  
        money.move_ip(0, 5)
        if money.y > window_height: 
            money_list.remove(money)
    for jail in jail_list[:]:
        jail.move_ip(0, 5)
        if jail.y > window_height:  
            jail_list.remove(jail)

    
    for money in money_list[:]:
        if money.colliderect(pygame.Rect(player_x, player_y, player_image.get_width(), player_image.get_height())):
            score += 1
            money_list.remove(money)
            catch_money_sound.stop()
            catch_money_sound.play()

    for jail in jail_list[:]:
        if jail.colliderect(pygame.Rect(player_x, player_y, player_image.get_width(), player_image.get_height())):
            game_over_sound.play()
            pygame.mixer.music.stop()  
            running = False

    
    window.blit(background_image, (0, 0))
    for money in money_list:
        window.blit(money_image, money)
    for jail in jail_list:
        window.blit(jail_image, jail)
    window.blit(font.render("Score: " + str(score), True, black), (10, 10))
    window.blit(player_image, (player_x, player_y))
    pygame.display.update()

    
    clock.tick(60)


window.blit(game_over_background, (0, 0))
game_over_text = font.render("The matrix got top G. now it's time for Nika Keshelava to rise up and enslave people", True, red)
game_over_rect = game_over_text.get_rect(center=(window_width // 2, window_height // 2 - 150))
window.blit(game_over_text, game_over_rect)

score_text = font.render("Chicks caught in bed: " + str(score), True, white)
score_rect = score_text.get_rect(center=(window_width // 2, window_height // 2 + 115))
window.blit(score_text, score_rect)

pygame.display.update()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()