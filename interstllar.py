import time
import random
import arcade

SCREEN__WIDTH=800
SCREEN_HEIGHT=600


class Startship(arcade.Sprite):
   def __init__(self):
       super().__init__(':resources:images/space_shooter/playerShip1_orange.png')
       self.center_x = SCREEN__WIDTH // 2
       self.center_y = 32
       self.width = 48
       self.height = 48
       self.angle = 0
       self.change_angle = 0
       self.speed = 4
       self.bullet_list = []
       self.score = 10

   def fire(self):
       self.bullet_list.append(Bullet(self))
    


class Enemy:
    def __init__(self):
       super().__init__(':resources:images/space_shooter/playerShip1_blue.png')
       self.center_x = random.randint(0,SCREEN__WIDTH)
       self.center_y = SCREEN_HEIGHT + 2
       self.width = 48
       self.height = 4
       self.speed = 4

    def move(self):
        self.center_y -= self.speed
      
    


class Bullet(arcade.Sprite):
     def __init__(self,host):
       super().__init__(':resources:images/space_shooter/laserRed01.png')
       self.speed = 6
       self.angle = host.angle
       self.center_x = host.center_x
       self.center_y = host.center_y

     def move(self):
        self.center_x += self.speed
        self.center_y += self.speed


class Game(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN__WIDTH , SCREEN_HEIGHT , 'Interstaller Game')
        arcade.set_background_color(arcade.color.NAVY_BLUE)
        self.background_image=arcade.load_texture(':resources:images/backgrounds/stars.png')
        self.me=Startship()
        self.enemy_list = []
        self.start_time = time.time()

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0,0,SCREEN__WIDTH,SCREEN_HEIGHT,self.background_image)
        self.me.draw()
        for enemy in self.enemy_list:
            enemy.draw()

    def on_update(self, delta_time: float):
        self.end_time = time.time()

        if self.end_time - self.start_time >5:
          self.enemy_list.append(Enemy())
          self.start_time = time.time()

        for enemy in self.enemy_list:
            enemy.move()
    


game=Game()
arcade.run()