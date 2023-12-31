from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem
from PyQt5.QtCore import Qt

from setTables import clearTable, calcuateDifferenceOfStatAndCap
from Models.races import *

def updateResistsFromRace(self, race_type: RaceType):
    if self.character:
        self.resistsTable = self.findChild(QTableWidget, 'resistsTable')
        clearTable(self, 'resistsTable')
        for resist, value in race_type.resists.items():
            resist = resist.replace('_resist','').capitalize()
            resistWidget = self.resistsTable.findItems(resist, Qt.MatchFlag.MatchContains)
            valueWidget = QTableWidgetItem(str(value))
            self.resistsTable.setItem(resistWidget[0].row(),1,valueWidget)
            
            resistsCapValue = int(self.resistsTable.item(resistWidget[0].row(),2).text()) + value
            adjustedResistsCapValueWidget = QTableWidgetItem(str(resistsCapValue))
            self.resistsTable.setItem(resistWidget[0].row(),2,adjustedResistsCapValueWidget)       
        calcuateDifferenceOfStatAndCap(self, 'resistsTable')

def calculateNowStats(self):
    if self.character:
        self.statsTable = self.findChild(QTableWidget, 'statsTable')
        clearTable(self, 'statsTable')
        for name, item in self.character.items.items():
            if item is not None:
                for stat, value in item.stats.items():
                    statWidgetRow = (self.statsTable.findItems(stat.capitalize(), Qt.MatchFlag.MatchContains))[0].row()
                    currentValue = int(self.statsTable.item(statWidgetRow, 1).text())
                    valueWidget = QTableWidgetItem(str(value + currentValue))
                    self.statsTable.setItem(statWidgetRow,1,valueWidget)
        calcuateDifferenceOfStatAndCap(self, 'statsTable')
    
def adjustBaseCapFromStatCap(self):
    if self.character:
        pass