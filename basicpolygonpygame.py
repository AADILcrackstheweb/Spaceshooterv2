import pygame as pyg
import sys  
#Sprite class   
class Sprite(pyg.sprite.Sprite):  
    def __init__(self, pos):  
        pyg.sprite.Sprite.__init__(self)  
        self.image = pyg.Surface([20, 20])  
        self.image.fill((255, 0, 255))  
        self.rect = self.image.get_rect()  
        self.rect.center = pos  
def main():  
    pyg.init()  
    clock = pyg.time.Clock()  
    fps = 50  
    bg = [0, 0, 0]  
    size =[300, 300]  
    screen = pyg.display.set_mode(size)  
    player = Sprite([40, 50])  
    # Define keys for player movement  
    player.move = [pyg.K_LEFT, pyg.K_RIGHT, pyg.K_UP, pyg.K_DOWN]  
    player.vx = 5  
    player.vy = 5  
  
    wall = Sprite([100, 60])  
  
    wall_group = pyg.sprite.Group()  
    wall_group.add(wall)  
  
    player_group = pyg.sprite.Group()  
    player_group.add(player)  
  
    while True:  
        for event in pyg.event.get():  
            if event.type == pyg.QUIT:  
                return False  
        key = pyg.key.get_pressed()  
        for i in range(2):  
            if key[player.move[i]]:  
                player.rect.x += player.vx * [-1, 1][i]  
  
        for i in range(2):  
            if key[player.move[2:4][i]]:  
                player.rect.y += player.vy * [-1, 1][i]  
        screen.fill(bg)  
        # first parameter takes a single sprite  
        # second parameter takes sprite groups  
        # third parameter is a kill command if true  
        hit = pyg.sprite.spritecollide(player, wall_group, True)  
        if hit:  
        # if collision is detected call a function to destroy  
            # rect  
            player.image.fill((255, 255, 255))  
        player_group.draw(screen)  
        wall_group.draw(screen)  
        pyg.display.update()  
        clock.tick(fps)  //fps indicates frmes per second
    pyg.quit()  
    sys.exit  
if __name__ == '__main__':  
