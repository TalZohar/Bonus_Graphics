import pygame

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

    # Draw a solid blue circle in the center
    draw_circle(screen, [300,250], 60, (0,0,0))
    # Flip the display
    pygame.display.flip()
    # Main loop
    running = True
    while running:
        # Look at every event in the queue
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


    # Done! Time to quit.
    pygame.quit()

if __name__ == '__main__':
    main()