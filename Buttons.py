class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)

    def draw(self, x):
        #draw button on the screen
        x.blit(self.image,(self.rect.x, self.rect.y))

