import pygame
import math

def multiply_matrice_vector(m, v):
    return [m[0][0]*v[0]+m[0][1]*v[1], m[1][0]*v[0]+m[1][1]*v[1]]

def sheer(v, angle):
    m1 = [[1, -math.tan(angle/2)], [0, 1]]
    m2 = [[1, 0], [math.sin(angle), 1]]
    new_v = multiply_matrice_vector(m1, v)
    new_v = [round(num) for num in new_v]
    new_v = multiply_matrice_vector(m2, new_v)
    new_v = [round(num) for num in new_v]
    new_v = multiply_matrice_vector(m1, new_v)
    new_v = [round(num) for num in new_v]
    return new_v


def draw_image(screen, image_pixels, angle, center):
    print(center)
    offset_x, offset_y = int(center[0]) - int(len(image_pixels[0])/2), int(center[1]) - int(len(image_pixels)/2)
    offset_x, offset_y = 0, 0
    for row in range(len(image_pixels)):
        for col in range(len(image_pixels[0])):

            pixel_loc = row - int(len(image_pixels)/2), col-int(len(image_pixels[0])/2)
            new_pixel_loc = sheer(pixel_loc, angle)
            new_pixel_loc = new_pixel_loc[0] + center[1], new_pixel_loc[1] + center[0]
            screen.set_at(new_pixel_loc, screen.unmap_rgb(image_pixels[row][col]))


def main():
    pygame.init()

    # Set up the drawing window
    infoObject = pygame.display.Info()
    screen_h, screen_w = int(infoObject.current_w*0.9), int(infoObject.current_h*0.9)
    screen = pygame.display.set_mode((screen_h, screen_w))

    # Fill the background with white
    screen.fill((255, 255, 255))
    image = pygame.image.load('images/Sandkingdom.jpg')
    image_pixels = pygame.PixelArray(image)
    center = int(screen_w/2), int(screen_h/2)
    # Main loop
    running = True
    angle = math.pi/2 * 150/180

    while running:

        # Look at every event in the queue
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.time.delay(1)
        pygame.display.update()
        screen.fill((255, 255, 255))
        draw_image(screen, image_pixels, angle, center)
        angle += 0.1

    # Done! Time to quit.
    pygame.quit()

if __name__ == '__main__':
    main()