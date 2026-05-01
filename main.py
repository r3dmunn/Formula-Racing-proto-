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
        if self.rect.x >= 880:
            self.rect.x = 870
        elif self.rect.x <= 360:
            self.rect.x = 370
        #TODO; Fijarse si la hitbox se mueve al mismo tiempo que el Rect
    def draw(self):
        screen.blit(self.img,self.image_Rect)
    def sound(self):
        self.soundcar.set_volume(0.25)
        self.soundcar.play(loops=-1)

class debry():
    def __init__(self):
        self.img = pygame.image.load("wooden-log-yes.png").convert_alpha()
        self.rect = pygame.Rect(540,0,20,50)
        self.image_Rect = self.img.get_rect(center=(540,0))
        self.hitbox = self.image_Rect.center
        self.sp = 18
    def draw(self):
        screen.blit(self.img,self.image_Rect)
    def movement(self):
        self.rect.y += self.sp*dt
        self.rect = self.image_Rect
    def reposition(self):
        while self.rect.y >= 720:
            self.rect.y = 0
        
player_inst = player()        
debry_inst = debry()
debry_inst2 = debry()
debry_inst3 = debry()

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
        pygame.draw.rect(screen,(255,255,255),(640,i,20,20))
        pygame.draw.rect(screen,(255,0,0),(890,i,20,20))
        i += 72
    

        
    player_inst.draw()
    player_inst.movement()
    player_inst.sound()
    
    debry_inst.draw()
    debry_inst.movement()
    debry_inst.reposition()
    
    debry_inst2.rect.x= 740
    debry_inst2.sp = 22
    debry_inst2.draw()
    debry_inst2.movement()
    debry_inst2.reposition()
    
    debry_inst3.rect.x = 620
    debry_inst3.sp= 15
    debry_inst3.draw()
    debry_inst3.movement()
    debry_inst3.reposition()
    
    pygame.display.flip()
    dt = clock.tick(60)/100
    