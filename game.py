import pygame
clock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((1440,900))
pygame.display.set_caption("Marianna wants to game")
icon = pygame.image.load('images/icon.png')
pygame.display.set_icon(icon)



# myfont = pygame.font.Font('fonts/PlaypenSans-ExtraBold.ttf',80)
# text_surface = myfont.render('Marianna', True, (70, 55, 171))

background = pygame.image.load('images/fonz.jpg').convert()
zombe = pygame.image.load('images/zombi.png').convert_alpha()
zombe_x = 1500
zombe_list_in_game = []

player = [
    pygame.image.load('images/pers1r.png').convert_alpha(),
    pygame.image.load('images/pers2.png').convert_alpha(),
    pygame.image.load('images/pers3.png').convert_alpha(),
    pygame.image.load('images/pers4.png').convert_alpha(),
    pygame.image.load('images/pers5.png').convert_alpha(),
    pygame.image.load('images/pers6.png').convert_alpha(),
    pygame.image.load('images/pers7.png').convert_alpha(),
    pygame.image.load('images/pers8.png').convert_alpha(),
    pygame.image.load('images/pers9.png').convert_alpha(),
    pygame.image.load('images/pers10.png').convert_alpha(),
    pygame.image.load('images/pers11.png').convert_alpha(),
    pygame.image.load('images/pers12.png').convert_alpha(),
    pygame.image.load('images/pers13.png').convert_alpha(),
    pygame.image.load('images/pers15.png').convert_alpha(),
    pygame.image.load('images/pers16.png').convert_alpha(),
     ]
player_count = 0
bg_x = 0
player_speed = 10
player_x = 100
player_y = 450
is_jamp = False
jump_count = 12
bg_m = pygame.mixer.Sound('music/mz.mp3')
bg_m.play()
zombe_timer = pygame.USEREVENT + 1
pygame.time.set_timer(zombe_timer, 2500)

running = True
while running:


    # screen.blit(text_surface, (450, 100))
    screen.blit(background, (bg_x,0))
    screen.blit(background,(bg_x+1440,0))

    player_sq = player[0].get_rect(topleft=(player_x,player_y))
    zombe_sq = zombe.get_rect(topleft=(zombe_x,650))

    if zombe_list_in_game:
        for el in zombe_list_in_game:
            screen.blit(zombe, el)
            el.x -= 20

            if player_sq.colliderect(zombe_sq):
                print("You lose")

    screen.blit(player[player_count], (player_x, player_y))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 50:
        player_x -= player_speed
    elif keys[pygame.K_RIGHT] and player_x < 1200:
        player_x += player_speed

    if not is_jamp:
        if keys[pygame.K_SPACE]:
            is_jamp = True
    else:
        if jump_count >=-12:
            if jump_count>0:
                player_y -= (jump_count**2)/2
            else:
                player_y += (jump_count**2)/2
            jump_count -=1
        else:
            is_jamp = False
            jump_count = 12
    if player_count == 14:
        player_count = 0
    else:
        player_count +=1

    bg_x -= 2
    if bg_x == -1440:
        bg_x = 0


    zombe_x -= 30
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        if event.type == zombe_timer:
            zombe_list_in_game.append(zombe.get_rect(topleft= (1500,670)))
    clock.tick(20)