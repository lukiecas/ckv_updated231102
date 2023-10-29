import pygame
import os
import random
pygame.init()

pygame.display.set_caption("CKV spel")

WIDTH, HEIGHT = 1000, 800
FPS = 60
PLAYER_VEL = 200
LANE_1 = 465
LANE_2 = 530
LANE_3 = 595
LANE_4 = 640
LANE_5 = 695
LANE_6 = 760
window = pygame.display.set_mode((WIDTH, HEIGHT))
bg = pygame.image.load(os.path.join('.','city_background.png')).convert()
enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
ADDENEMY = pygame.USEREVENT + 1

pygame.time.set_timer(ADDENEMY, 1000)

bgX2 = bg.get_width
class Player(pygame.sprite.Sprite):

    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((75, 25))
        #self.surf.fill((0, 0, 0))
        pygame.draw.rect(self.surf, "RED", pygame.Rect(0, 0, 75, 25)) 
        self.rect = self.surf.get_rect()


class Enemy(pygame.sprite.Sprite):

    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.Surface((75, 25))
        self.surf.fill((0, 0, 0))
        lane_decision = random.randint(1, 6)
        if lane_decision == 1:
            lane_number = LANE_1
        elif lane_decision == 2:
            lane_number = LANE_2
        if lane_decision == 3:
            lane_number = LANE_3
        elif lane_decision == 3:
            lane_number = LANE_3
        if lane_decision == 4:
            lane_number = LANE_4
        elif lane_decision == 5:
            lane_number = LANE_5
        if lane_decision == 6:
            lane_number = LANE_6
        
        
        self.rect = self.surf.get_rect(

            center=(

                random.randint(1000 + 20, 1000 + 100),

                lane_number,

            )

        )

        self.speed = random.randint(5, 20)
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()
        


def main(window):
    player = Player()
    enemies = pygame.sprite.Group()

    all_sprites = pygame.sprite.Group()

    all_sprites.add(player)

    player.rect.x = 300
    player.rect.y = LANE_1
    lane_number = 1 
    clock = pygame.time.Clock()
    test_background_X = 0
    test_background_X_2 = test_background_X + 8000
    run = True

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    if lane_number > 1:
                        lane_number = lane_number - 1
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    if lane_number < 6:
                        lane_number = lane_number + 1
            if event.type == ADDENEMY:
                # Create the new enemy and add it to sprite groups
                new_enemy = Enemy()

                enemies.add(new_enemy)

                all_sprites.add(new_enemy)
    
        test_background_X = test_background_X - 20
        test_background_X_2 = test_background_X_2 - 20
        
        window.blit(bg, (test_background_X, 0))
        window.blit(bg, (test_background_X_2, 0))
        window.blit(player.surf, player.rect)
        for entity in all_sprites:
            window.blit(entity.surf, entity.rect)
        if pygame.sprite.spritecollideany(player, enemies):
            player.kill()
            run = False
        
        if lane_number == 1:
            player.rect.y = LANE_1
        if lane_number == 2:
            player.rect.y = LANE_2
        if lane_number == 3:
            player.rect.y = LANE_3
        if lane_number == 4:
            player.rect.y = LANE_4
        if lane_number == 5:
            player.rect.y = LANE_5
        if lane_number == 6:
            player.rect.y = LANE_6
        


        print(test_background_X)
        if test_background_X <= -8000:
            test_background_X = test_background_X_2 + 8000
        if test_background_X_2 <= -8000:
            test_background_X_2 = test_background_X + 8000
        enemies.update()
        
        pygame.display.update()
            
        
    pygame.quit()
    quit()

if __name__ == '__main__':
    main(window)