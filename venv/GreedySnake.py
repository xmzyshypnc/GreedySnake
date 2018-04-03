# !/usr/bin python
#coding=utf-8

import pygame as pg
from pygame.locals import *
from sys import exit

class GreedySnake(object):
    background_file_path = "background.jpg"
    #mouse_file_path = "white.png"
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
           print item
    def Snake(self):
        while True:
            for event in pg.event.get():
                if event.type == QUIT:
                    exit()
                #事件处理
            #画界面
            self.screen.blit(self.background,(0,0))
            #添加文字
            tanchishe = self.title_font.render(u"贪吃蛇",True,(128,0,128))
            kaishiyouxi = self.my_font.render(u"开始游戏",True,(0,0,255))
            zuigaojilu = self.my_font.render(u"最高记录",True,(0,0,255))
            youxishuoming = self.my_font.render(u"游戏说明",True,(0,0,255))
            self.screen.blit(tanchishe,(120,120))
            self.screen.blit(kaishiyouxi,(640,360))
            self.screen.blit(zuigaojilu,(640,440))
            self.screen.blit(youxishuoming,(640,520))
            pg.display.update()
gs = GreedySnake()
gs.get_fonts()
gs.Snake()

