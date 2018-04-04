# !/usr/bin python
#coding=utf-8

from __future__ import print_function
from __future__ import print_function
from __future__ import print_function
import pygame as pg
from pygame.locals import *
from sys import exit
from Button import Button
import random
import time

class GreedySnake(object):
    background_file_path = "background.jpg"
    #mouse_file_path = "white.png"
    #最小单位为5像素
    unit = 5
    def __init__(self):
        #创建一个窗口以及初始化背景等
        pg.init()
        #创建一个窗体
        self.screen = pg.display.set_mode((1080,720),0,32)
        pg.display.set_caption("贪吃蛇")
        #设置默认字体
        self.my_font = pg.font.Font("simsun.ttf",45)
        self.title_font = pg.font.Font("simsun.ttf",100)
        #加载图片
        #self.background = pg.image.load(GreedySnake.background_file_path).convert()
        #self.mouse_cursor = pg.image.load(GreedySnake.mouse_file_path).convert_alpha()
        #画出主界面
        self.background = pg.image.load(self.background_file_path).convert_alpha()
    def get_fonts(self):
       for item in  pg.font.get_fonts():
           print(item)

    def InitGame(self):
        #初始化游戏界面
        #初始化被吃的块
        self.food_pos_x = random.randint(0,1079)
        self.food_pos_y = random.randint(0,719)
        self.current_rank = pg.Rect(self.food_pos_x,self.food_pos_y,10,10)
        pg.draw.rect(self.screen,(255,255,255),self.current_rank)
        #初始化虫子
        self.worm_pos_x,self.worm_pos_y,self.worm_last_pos_x,self.worm_last_pos_y = 0,0,0,0
        self.worm = pg.Rect(self.worm_pos_x,self.worm_pos_y,10,10)
        pg.draw.rect(self.screen,(255,255,255),self.worm)
        #初始化时钟对象
        self.clock = pg.time.Clock()
        #初始化速度
        self.speed = 10
        #初始化吃没吃到
        self.is_eaten = False
        pg.display.update()

    def GenerateFood(self):
        while 1:
            self.food_pos_x = random.randint(0, 1079)
            self.food_pos_y = random.randint(0, 719)
            self.current_rank.move(self.food_pos_x, self.food_pos_y)
            if self.worm.contains(self.current_rank):
                # print("233")
                # 如果虫子包含了食物就重新寻找位置
                continue
            else:
                break
        self.is_eaten = False

    def HandleKey(self,key_type,passed_distance):
        move_dis = 0
        while move_dis < passed_distance:
            move_dis += GreedySnake.unit
            self.worm_pos_y += move_dis
            self.worm_last_pos_x = self.worm_pos_x
            self.worm_last_pos_y = self.worm_pos_y
            if self.worm_pos_y > 720:
                self.worm_pos_y -= 720
            self.worm.move_ip(self.worm_pos_x, self.worm_pos_y)
            # 画图
            self.screen.fill(0, 0, 0)
            pg.draw.rect(self.screen, (255, 255, 255), self.worm)
            pg.display.update()
            if self.worm_pos_x == self.food_pos_x and self.worm_last_pos_y < self.food_pos_y and self.worm_pos_y > self.food_pos_y:
                self.is_eaten = True
                self.GenerateFood()
            else:
                self.is_eaten = False

    def Snake(self):
        # 添加文字
        tanchishe = self.title_font.render(u"贪吃蛇", True, (128, 0, 128))
        kaishiyouxi = self.my_font.render(u"开始游戏", True, (0, 0, 255))
        zuigaojilu = self.my_font.render(u"最高记录", True, (0, 0, 255))
        youxishuoming = self.my_font.render(u"游戏说明", True, (0, 0, 255))
        # 创建按钮
        start_button = Button(640, 360, 820, 410)
        record_button = Button(640, 440, 820, 485)
        introduction_button = Button(640, 520, 820, 560)
        while True:
            # 画界面
            self.screen.blit(self.background, (0, 0))
            #添加文字
            self.screen.blit(tanchishe, (120, 120))
            self.screen.blit(kaishiyouxi, (640, 360))
            self.screen.blit(zuigaojilu, (640, 440))
            self.screen.blit(youxishuoming, (640, 520))
            pg.display.update()
            for event in pg.event.get():
                if event.type == QUIT:
                    exit()
                #事件处理
                elif event.type == MOUSEBUTTONDOWN:
                # 检测是否有点击
                    if pg.mouse.get_pressed()[0]:
                        # 获取鼠标位置
                        self.cursor_x, self.cursor_y = pg.mouse.get_pos()
                        #print kaishiyouxi.get_rect()
                        #print self.cursor_x, self.cursor_y
                        if start_button.judge(self.cursor_x,self.cursor_y):
                            #开始游戏
                            self.screen.fill((0,0,0))
                            self.screen.blit(self.background, (0, 0))
                            pg.display.update()
                            #随机初始化界面
                            self.InitGame()
                            while True:
                                for event in pg.event.get():
                                    if event.type == QUIT:
                                        exit()
                                    if event.type == KEYDOWN:
                                        if event.key in (K_UP,K_DOWN,K_LEFT,K_RIGHT):

                                            passed_time = self.clock.tick() / 1000
                                            passed_distance = passed_time * self.speed
                                            #print(passed_time)

                                        if event.key == K_UP:
                                            #向上
                                            self.worm_pos_y -= passed_distance
                                            #处理之前先判断有没有吃到食物
                                            if self.worm_pos_x == self.food_pos_x and self.worm_last_pos_y > self.food_pos_y and self.worm_pos_y < self.food_pos_y:
                                                #吃到
                                                self.is_eaten = True
                                            else:
                                                self.is_eaten = False
                                            if self.worm_pos_y < 0:
                                            #超过了最上方
                                                self.worm_pos_y = 720 + self.worm_pos_y

                                        elif event.key == K_DOWN:
                                            #向下
                                            #print 1
                                            self.HandleKey("DOWN",passed_distance)


                                            #print(self.worm_pos_x)
                                            #print(self.worm_pos_y)
                                        elif event.key == K_LEFT:
                                            #向左
                                            if self.worm_pos_y == self.food_pos_y and self.worm_last_pos_x > self.food_pos_x and self.worm_pos_x < self.food_pos_x:
                                                self.is_eaten = True
                                            else:
                                                self.is_eaten = False

                                            self.worm_pos_x -= passed_distance
                                            if self.worm_pos_x < 0:
                                                # 超过了最左边
                                                self.worm_pos_x = 1080 + self.worm_pos_x

                                        elif event.key == K_RIGHT:
                                            # 向右
                                            if self.worm_pos_y == self.food_pos_y and self.worm_last_pos_x < self.food_pos_x and self.worm_pos_x > self.food_pos_x:
                                                self.is_eaten = True
                                            else:
                                                self.is_eaten = False
                                            self.worm_pos_x += passed_distance
                                            if self.worm_pos_x > 1080:
                                                # 超过了最左边
                                                self.worm_pos_x -= 1080
                                        #判断能否吃到
                                        if self.is_eaten is True:
                                            #$合并成一个
                                            self.worm.union(self.current_rank)


                                        else:
                                            pass
                                    #print("纵坐标是"+str(self.worm_pos_y))
                                    self.screen.blit(self.background, (0, 0))
                                    self.worm.move_ip(self.worm_pos_x, self.worm_pos_y)
                                    pg.draw.rect(self.screen,(255,255,255),self.worm)
                                    pg.draw.rect(self.screen,(255,255,255),self.current_rank)
                                    pg.display.update()


                                #pg.display.update()
                                #pass


                        elif record_button.judge(self.cursor_x,self.cursor_y):
                            #查看记录
                            pass
                        elif introduction_button.judge(self.cursor_x,self.cursor_y):
                            #查看说明
                            pass
                        else:
                            pass

gs = GreedySnake()
#gs.get_fonts()
gs.Snake()

