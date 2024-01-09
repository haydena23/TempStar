from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QComboBox, QCheckBox, QLabel
from PyQt5.QtCore import Qt

from setTables import clearTable, calculateDifferenceOfStatAndCap
from Models.races import RaceType
from Models.mappings import equip_weapon_map, table_names, race_type_mapping, realm_rank_map

from Models.levels import levels

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
        calculateDifferenceOfStatAndCap(self, 'resistsTable')
        
def calculateNowStats(self):
    if self.character:
        equipWeapons = self.findChild(QComboBox, 'equippedWeaponsComboBox')
        weaponsNotAllowed = equip_weapon_map.get(equipWeapons.currentText())
        for table in table_names:
            self.tableWidget = self.findChild(QTableWidget, table)
            clearTable(self, table)
            for name, item in self.character.currentItems.items():
                if item is not None:
                    if item.slot in weaponsNotAllowed:
                        pass
                    else:

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
        skillsTable = self.findChild(QTableWidget, 'resistsTable')
        skillsTable.resizeColumnToContents(2)
        for table in table_names:
            calculateDifferenceOfStatAndCap(self, table)
        checkTOADisplay(self)
        totalUtility = 0
        for slot, item in self.character.currentItems.items():
            if item is not None:
                if slot not in weaponsNotAllowed:
                    totalUtility += item.total_utility
        self.findChild(QLabel, 'totalUtilityValue').setText(f"( {totalUtility} )")
    
def adjustBaseCapFromStatCap(self):
    if self.character:
        self.level = self.findChild(QComboBox, 'levelComboBox').currentText()
        self.statsTable = self.findChild(QTableWidget, 'statsTable')
        self.statsCapTable = self.findChild(QTableWidget, 'statsCapTable')
        self.default = levels.get(self.level).get('statsCapTable')
        for row in range(self.statsCapTable.rowCount()):
            capWidgetValue = int(self.statsCapTable.item(row, 1).text())
            cap = ((list(self.default.items()))[row])[1]
            if capWidgetValue > cap:
                capWidgetValue = cap
            currentStatCapValue = int(self.statsTable.item(row,2).text())
            newValueWidget = QTableWidgetItem(str(currentStatCapValue + capWidgetValue))
            self.statsTable.setItem(row, 2, newValueWidget)

def adjustSkillsFromRealmRank(self, realm_rank):
    if self.character:
        self.skillsTable = self.findChild(QTableWidget, 'skillsTable')
        currentRace = race_type_mapping.get(self.findChild(QComboBox, 'raceComboBox').currentText())
        updateResistsFromRace(self, currentRace)
        for row in range(self.skillsTable.rowCount()):
            currentStat = int(self.skillsTable.item(row, 1).text())
            currentStatCap = int(self.skillsTable.item(row, 2).text())
            correctedSkillWidget = QTableWidgetItem(str(currentStat + (realm_rank - 1)))
            correctedSkillCapWidget = QTableWidgetItem(str(currentStatCap + (realm_rank - 1)))
            self.skillsTable.setItem(row, 1, correctedSkillWidget)
            self.skillsTable.setItem(row, 2, correctedSkillCapWidget)
        calculateDifferenceOfStatAndCap(self, 'skillsTable')
def autoUpdateRealmRank(self):
    currentRealmRank = realm_rank_map.get(self.findChild(QComboBox, 'realmRankComboBox').currentText())
    adjustSkillsFromRealmRank(self, currentRealmRank)
    
def checkTOADisplay(self):
    bonusesTable = self.findChild(QTableWidget, 'bonusesTable')
    allBonusesCheck = self.findChild(QCheckBox, 'checkBox').isChecked()
    if allBonusesCheck:
        for i in range(bonusesTable.rowCount()):
            bonusesTable.setRowHidden(i, False)
    else:
        for i in range(bonusesTable.rowCount()):
            if int(bonusesTable.item(i,1).text()) == 0:
                bonusesTable.setRowHidden(i, True)
            else:
                bonusesTable.setRowHidden(i, False)
    bonusesTable.resizeColumnToContents(0)