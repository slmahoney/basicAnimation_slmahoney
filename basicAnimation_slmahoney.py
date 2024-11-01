#sabrina mahoney
#basic animation
#duck run game

def main():

    import pygame
    pygame.init()


    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Duck run!")


    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background_image = pygame.image.load("voodoo_cactus_underwater.png").convert()
    
    duck = pygame.image.load("duck.png")
    duck = duck.convert()
    duck = duck.convert_alpha()
    duck = pygame.transform.scale(duck, (100,100))
    
    duck_x = 0
    duck_y = 200
    

        
    clock = pygame.time.Clock()
    keepGoing = True


    while keepGoing:

        
        clock.tick(30)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
        
        duck_x +=5
        if duck_x > screen.get_width():
            duck_x = 0
            
        duck_y += 5
        if duck_y > screen.get_height():
            duck_y = 0


        screen.blit(background_image, (0, 0))
        screen.blit(duck, (duck_x, duck_y))
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()