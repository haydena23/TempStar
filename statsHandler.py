from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem
from PyQt5.QtCore import Qt

from setTables import clearTable, calcuateDifferenceOfStatAndCap
from Models.race_types import *

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