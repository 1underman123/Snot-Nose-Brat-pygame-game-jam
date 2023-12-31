import pygame
from classes import Player, Platform, Lever, Door


def level(level_dict, goal, screen, background, background_rect, timer, elapsed_time):
    screen.blit(background,background_rect)
    goal.draw(screen)
    for groups, group in level_dict.items():
        if groups == "Platform Group":
            group.draw(screen)
        elif groups == "Lever Group":
            for lever in group:
                lever.draw(screen)
        else:
            for door in group:
                door.draw(screen)

def title_screen(screen, font):
    screen.fill('Black')
    screen.blit(font.render("Snots and", False, (255, 255, 255)), (10,0))
    screen.blit(font.render("Spooks:", False, (255, 255, 255)), (10,10))
    screen.blit(font.render("Escape of", False, (255, 255, 255)), (10,20))
    screen.blit(font.render("the Snot", False, (255, 255, 255)), (10,30))
    screen.blit(font.render("Nose Brat", False, (255, 255, 255)), (10,40))
    screen.blit(font.render("Press Enter", False, (255, 0, 0)), (6,50))

def game_over(screen, font, total_time):
    screen.fill('Black')
    screen.blit(font.render("You have", False, (255, 0, 0)), (0,0))
    screen.blit(font.render("been caught", False, (255, 0, 0)), (0,10))
    screen.blit(font.render("...", False, (255, 0, 0)), (0,20))
    screen.blit(font.render("Press Enter", False, (255, 255, 255)), (0,30))
    screen.blit(font.render("time:{:.2f}".format(total_time/60), False, (255,255,255)), (0,40))

def win(screen, font, total_time):
    screen.fill('Black')
    screen.blit(font.render("You Escaped!", False, (255, 238, 131)), (5,0))
    screen.blit(font.render("Press Enter", False, (255, 0, 0)), (6,15))
    screen.blit(font.render("to try again", False, (255, 0, 0)), (4,25))
    screen.blit(font.render("time:{:.2f}".format(total_time/60), False, (255,255,255)), (10,40))

def fading(screen, fade_color, duration):
    fade_surface = pygame.Surface((screen.get_width(), screen.get_height()))
    fade_surface.fill(fade_color)
    for alpha in range(0, 256):
        fade_surface.set_alpha(alpha)
        screen.blit(fade_surface, (0, 0))
        pygame.display.update()
        pygame.time.delay(duration//60)



#five_platform = pygame.image.load('graphics/platforms/5-platform.png').convert_alpha()
#floor = pygame.image.load('graphics/platforms/floor.png').convert_alpha()
#wall = pygame.image.load('graphics/platforms/wall.png').convert_alpha()
#platforms = [Platform(floor, 0, 52),Platform(five_platform, screen.get_width()/2, (screen.get_height()/2)+3), Platform(wall, -1, 0), Platform(wall, 80, 0)]
#platforms_group = pygame.sprite.Group()
#platforms_group.add(platforms)
## background
#background = pygame.image.load('graphics/background.png').convert_alpha()
#background_rect = background.get_rect(topleft = (0,2))
## make levers & group them
#levers = [Lever("dark blue", 10, 52), Lever("yellow", 25, 52)]
#lever_group = pygame.sprite.Group()
#lever_group.add(levers)
#
#
#
#
#
#        screen.blit(background,background_rect)
#        platforms_group.draw(screen)
#        brat.draws(screen)
#        for lever in lever_group:
#            lever.draw(screen)
#        for door in door_group:
#            door.draw(screen)
#        
#        
#
#        
#
#        # update the screen
#        pygame.display.flip()