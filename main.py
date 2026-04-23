import pygame


pygame.init()
pygame.mixer.init()
running, dt = True,0
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
class player:
    def __init__(self):
        self.img = pygame.image.load("mercedes_8bit.png").convert_alpha()
        self.rect = pygame.Rect(640,360,20,50)
        self.image_Rect = self.img.get_rect(center=(640,360))
        self.hitbox = self.image_Rect.center
        self.sp = 35
        self.startup = pygame.mixer.Sound("8bit_car_startup.wav")
        self.soundcar = pygame.mixer.Sound("8bit_car_engine.wav")
    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.rect.y -= self.sp*dt
        if keys[pygame.K_s]:
            self.rect.y += self.sp*dt
        if keys[pygame.K_d]:
            self.rect.x += self.sp*dt
        if keys[pygame.K_a]:
            self.rect.x -= self.sp*dt
        self.rect = self.image_Rect
        #TODO; Fijarse si la hitbox se mueve al mismo tiempo que el Rect
    def draw(self):
        screen.blit(self.img,self.image_Rect)
    def sound(self):

        self.soundcar.play(loops=-1)
        
player_inst = player()        

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill("grey") #TODO; Cambiar el color
    pygame.draw.rect(screen,(0,0,0),(360,0,550,1280))
    pygame.draw.rect(screen,(255,255,255),(360,-50,550,1280),20)
    i=0
    for _ in range(13):
        pygame.draw.rect(screen,(255,0,0),(360,i,20,20))
        pygame.draw.rect(screen,(255,0,0),(890,i,20,20))
        i += 72    
    player_inst.draw()
    player_inst.movement()
    player_inst.sound()
    
    pygame.display.flip()
    dt = clock.tick(60)/100