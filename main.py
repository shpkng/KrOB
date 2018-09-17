'''
File: main.py
Project: KrOB
File Created: Wednesday, 5th September 2018 12:49:27 am
Author: shpkng (shpkng@gmail.com)
Organization: Communication University of China
License: GPL
-----
Last Modified: Thursday, 6th September 2018 5:46:14 am
Modified By: shpkng (shpkng@gmail.com)
-----
Valar Morghulis.
'''
import crawler
import os
import re
import requests as req
from PyQt5 import QtWidgets, uic
import PyQt5.sip
import ctypes
try:
    temp1=ctypes.windll.LoadLibrary( 'DLL\\Qt5Core.dll' )
    temp2=ctypes.windll.LoadLibrary( 'DLL\\Qt5Gui.dll' )
    temp3=ctypes.windll.LoadLibrary( 'DLL\\Qt5Widgets.dll' )
    temp4=ctypes.windll.LoadLibrary( 'DLL\\msvcp140.dll' )
    temp5=ctypes.windll.LoadLibrary( 'DLL\\Qt5PrintSupport.dll' )
except:
    pass
app = QtWidgets.QApplication([])
ui = uic.loadUi("main.ui")

path = '' #客户端位置   165行
gameNo = 0

def getFolder():
    pass

def display():
    c.getInfo()
    for x in range(len(c.athletes['GameNo'])):
        ui.table.addItem(QtWidgets.QListWidgetItem(\
        (c.athletes['Athlete'][1][x].text+' @ '+c.athletes['Athlete'][0][x].text).ljust(48,' ')+\
        #c.athletes['Summoner'][x].text.ljust(16,' ')+\
        c.athletes['Champion'][x].text.ljust(16,' ')))

def setGameNo():
    global gameNo
    gameNo = c.athletes['GameNo'][ui.table.currentRow()][2:-1]

def getBat(n,path):
    print(n)
    print(re.search(r'@s.+',req.get("http://www.op.gg/match/new/batch/id=%d" % int(n)).content.decode('utf8','ignore')).group(0))
    with open((path[:-4]+'Game/OPGG.bat'),'w+',encoding='utf8') as f:
        f.write(re.search(r'@s.+',req.get("http://www.op.gg/match/new/batch/id=%d" % int(n)).content.decode('ansi','ignore')).group(0))
        f.close()

def startOB():
    if ui.path.text() == '' or not os.path.exists(ui.path.text()[:-4]+'Game/League of Legends.exe'):
        msg = QtWidgets.QMessageBox.critical(None,'Oops','请检查填入的地址')
    else:
        getBat(gameNo,ui.path.text())
        os.chdir(ui.path.text()[:-4]+'Game')
        os.system(ui.path.text()[:-4]+'Game\OPGG.bat')

#I:\腾讯游戏\英雄联盟\TCLS

c = crawler.crawler()
ui.table.clicked.connect(setGameNo)
ui.startButton.clicked.connect(startOB)
ui.flushButton.clicked.connect(display)
ui.show()
app.exec()
