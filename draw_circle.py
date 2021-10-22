import pygame
import math

def draw_circle(screen, center, radius, color):
    x = 0
    y = radius
    offset_x, offset_y = center
    err = 5/4 - radius

    while x <= y:
        screen.set_at((x + offset_x, y + offset_y), color)
        screen.set_at((-x + offset_x, y + offset_y), color)
        screen.set_at((x + offset_x, -y + offset_y), color)
        screen.set_at((-x + offset_x, -y + offset_y), color)
        screen.set_at((y + offset_x, x + offset_y), color)
        screen.set_at((y + offset_x, -x + offset_y), color)
        screen.set_at((-y + offset_x, x + offset_y), color)
        screen.set_at((-y + offset_x, -x + offset_y), color)
        x += 1
        if err < 0:
            err = err + 2*x+1
        else:
            y -= 1
            err = err + 2*x - 2*y + 1





def main():
    pygame.init()

    # Set up the drawing window
    screen = pygame.display.set_mode([500, 500])

    # Fill the background with white
    screen.fill((255, 255, 255))


    # Main loop
    running = True
    x = 0
    while running:

        # Look at every event in the queue
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        mouse_x, mouse_y = pygame.mouse.get_pos()
        dist = int(math.sqrt((mouse_x-x)**2 + (mouse_y-250)**2))
        screen.fill((255, 255, 255))
        draw_circle(screen, [x, 250], dist, (0, 0, 0))
        pygame.display.flip()

        x += 1
        if x == 500:
            x = 0
        pygame.time.delay(5)

    # Done! Time to quit.
    pygame.quit()

if __name__ == '__main__':
    main()