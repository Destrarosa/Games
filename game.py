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
jump_count = 15
bg_m = pygame.mixer.Sound('music/mz.mp3')
bg_m.play()
zombe_timer = pygame.USEREVENT + 1
pygame.time.set_timer(zombe_timer, 5500)

label = pygame.font.Font('Fonts/PlaypenSans-ExtraBold.ttf',100)
lose_label = label.render('You loose!', False, (60, 171, 199))
restart_label = label.render('New game', False, (60, 171, 199))
restart_label_rect = restart_label.get_rect(topleft=(500,500))
bullet = pygame.image.load('images/luk.png').convert_alpha()
bullets = []
bullets_left = 5
gameplay = True
running = True
while running:


    # screen.blit(text_surface, (450, 100))
    screen.blit(background, (bg_x,0))
    screen.blit(background,(bg_x+1440,0))


    if gameplay:
        player_sq = player[0].get_rect(topleft=(player_x,player_y))

        if zombe_list_in_game:
            for (i,el) in enumerate(zombe_list_in_game):
                screen.blit(zombe, el)
                el.x -= 10
                if el.x < -10:
                    zombe_list_in_game.pop(i)

                if player_sq.colliderect(el):
                    gameplay = False

        screen.blit(player[player_count], (player_x, player_y))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            screen.blit(player[player_count], (player_x, player_y))
        if keys[pygame.K_LEFT] and player_x > 50:
            player_x -= player_speed
        elif keys[pygame.K_RIGHT] and player_x < 1200:
            player_x += player_speed

        if not is_jamp:
            if keys[pygame.K_SPACE]:
                is_jamp = True
        else:
            if jump_count >=-15:
                if jump_count>0:
                    player_y -= (jump_count**2)/2
                else:
                    player_y += (jump_count**2)/2
                jump_count -=1
            else:
                is_jamp = False
                jump_count = 15
        if player_count == 14:
            player_count = 0
        else:
            player_count +=1

        bg_x -= 2
        if bg_x == -1440:
            bg_x = 0

        if bullets:
            for (i,el) in enumerate(bullets):
                screen.blit(bullet, (el.x, el.y))
                el.x += 4
                if el.x > 1440:
                    bullets.pop(i)
                if zombe_list_in_game:
                    for(index, zombe_el) in enumerate(zombe_list_in_game):
                        if el.colliderect(zombe_el):
                            zombe_list_in_game.pop(index)
                            bullets.pop(i)
    else:
        screen.fill((23, 20, 46))
        screen.blit(lose_label, (500,300))
        screen.blit(restart_label, (restart_label_rect))
        mouse = pygame.mouse.get_pos()
        if restart_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            gameplay=True
            player_x = 100
            zombe_list_in_game.clear()
            bullets.clear()
            bullets_left = 5


    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        if event.type == zombe_timer:
            zombe_list_in_game.append(zombe.get_rect(topleft= (1450,680)))
        if gameplay and event.type == pygame.KEYUP and event.key == pygame.K_b and bullets_left>0:
            bullets.append(bullet.get_rect(topleft=(player_x+130, player_y+250)))
            bullets_left -=1
    clock.tick(21)