'''
File: crawler.py
Project: KrOB
File Created: Wednesday, 5th September 2018 12:54:29 am
Author: shpkng (shpkng@gmail.com)
Organization: Communication University of China
License: GPL
-----
Last Modified: Thursday, 6th September 2018 4:25:55 am
Modified By: shpkng (shpkng@gmail.com)
-----
Valar Morghulis.
'''

import requests as req
import linecache
from bs4 import BeautifulSoup as bs
import re


class crawler:
    text = '213'
    athletes = {}

    def getInfo(self):
        r = req.get("http://www.op.gg/spectate/pro/")
        b= bs(r.content,'html.parser')
        self.athletes['Champion']=b.select('.ChampionName')
        self.athletes['Summoner']=b.select('.SummonerName')
        self.athletes['Athlete']=[b.select('.TeamName'),b.select('.Extra')]
        self.athletes['GameNo']=re.findall(r'e\([0-9]+\)',r.text)

    def getBat(self,n,path):
        with open((path+'/OPGG.bat'),'w') as f:
            f.write(re.search(r'@s.+',req.get("http://www.op.gg/match/new/batch/id=%d" % int(n)).content.decode('ansi','ignore')).group(0))