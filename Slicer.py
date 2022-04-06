import pygame

pygame.display.set_mode((300,360), pygame.HIDDEN)

def slice_images(x,y,imgs):
    num_of_imgs = len(imgs)
    IMGS = []
    for img in imgs:
        IMG = pygame.image.load(img).convert_alpha()
        IMG = pygame.transform.scale(IMG, (x//num_of_imgs,y))
        IMG = pygame.PixelArray(IMG)
        IMGS.append(IMG)

    RESULT = pygame.Surface((x,y))
    RESULT = pygame.PixelArray(RESULT)

    for i in range(x//num_of_imgs):
        for j in range(y):
            for k in range(num_of_imgs):
                RESULT[i*num_of_imgs+k][j]= IMGS[k][i][j]

    RESULT = pygame.PixelArray.make_surface(RESULT)
    return RESULT

def slice_images_with_color(x,y,imgs,color):
    num_of_imgs = len(imgs)
    x = x*num_of_imgs
    y = y*num_of_imgs
    IMGS = []
    for img in imgs:
        IMG1 = pygame.image.load(img).convert_alpha()
        IMG1 = pygame.transform.scale(IMG1, (x//num_of_imgs//2,y))
        IMG1 = pygame.PixelArray(IMG1)
        IMGS.append(IMG1)

    RESULT = pygame.Surface((x,y))
    RESULT.fill(color)
    RESULT = pygame.PixelArray(RESULT)

    for i in range(x//num_of_imgs//2):
        for j in range(y):
            for k in range(num_of_imgs):
                RESULT[i*num_of_imgs*2+k*2][j]= IMGS[k][i][j]

    RESULT = pygame.PixelArray.make_surface(RESULT)
    return RESULT


