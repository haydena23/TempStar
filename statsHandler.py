from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem
from PyQt5.QtCore import Qt

from setTables import clearTable, calcuateDifferenceOfStatAndCap
from Models.races import *
from Models.mappings import table_names, stat_cap_default_caps

def updateResistsFromRace(self, race_type: RaceType):
    if self.character:
        self.resistsTable = self.findChild(QTableWidget, 'resistsTable')
        calculateNowStats(self)
        for resist, value in race_type.resists.items():
            resist = resist.replace('_resist','').capitalize()
            resistWidget = self.resistsTable.findItems(resist, Qt.MatchFlag.MatchContains)
            currentValue = int(self.resistsTable.item(resistWidget[0].row(), 1).text())
            valueWidget = QTableWidgetItem(str(value + currentValue))
            self.resistsTable.setItem(resistWidget[0].row(),1,valueWidget)
            
            resistsCapValue = int(self.resistsTable.item(resistWidget[0].row(),2).text()) + value
            adjustedResistsCapValueWidget = QTableWidgetItem(str(resistsCapValue))
            self.resistsTable.setItem(resistWidget[0].row(),2,adjustedResistsCapValueWidget)       
        calcuateDifferenceOfStatAndCap(self, 'resistsTable')
        
def calculateNowStats(self):
    if self.character:
        for table in table_names:
            self.tableWidget = self.findChild(QTableWidget, table)
            clearTable(self, table)
            for name, item in self.character.items.items():
                if item is not None:
                    for stat, value in item.stats.items():
                        if '_' in stat:
                            stat = ' '.join(word.capitalize() for word in stat.split('_'))
                        else:
                            stat = stat.capitalize()
                        try:
                            statWidgetRow = (self.tableWidget.findItems(stat, Qt.MatchFlag.MatchExactly))[0].row()
                            currentValue = int(self.tableWidget.item(statWidgetRow, 1).text())
                            valueWidget = QTableWidgetItem(str(value + currentValue))
                            self.tableWidget.setItem(statWidgetRow,1,valueWidget)
                        except:
                            pass
        adjustBaseCapFromStatCap(self)
        for table in table_names:
            calcuateDifferenceOfStatAndCap(self, table)
    
def adjustBaseCapFromStatCap(self):
    if self.character:
        stat_caps = stat_cap_default_caps
        self.statsTable = self.findChild(QTableWidget, 'statsTable')
        self.statsCapTable = self.findChild(QTableWidget, 'statsCapTable')
        for row in range(self.statsCapTable.rowCount()):
            capWidgetValue = int(self.statsCapTable.item(row, 1).text())
            cap = ((list(stat_caps.items()))[row])[1]
            if capWidgetValue > cap:
                capWidgetValue = cap
            currentStatCapValue = int(self.statsTable.item(row,2).text())
            newValueWidget = QTableWidgetItem(str(currentStatCapValue + capWidgetValue))
            self.statsTable.setItem(row, 2, newValueWidget)
        # calcuateDifferenceOfStatAndCap(self, 'statsTable')

def adjustStatsFromMythirian(self):
    if self.character:
        pass