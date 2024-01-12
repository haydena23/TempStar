from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QComboBox
from PyQt5.QtGui import QColor, QBrush
from PyQt5.QtCore import Qt

from Models.levels import levels
from Models.mappings import mythical_base_map

def initTables(self):
    self.statsTable = self.findChild(QTableWidget, 'statsTable')    
    self.statsCapTable = self.findChild(QTableWidget, 'statsCapTable')        
    self.resistsTable = self.findChild(QTableWidget, 'resistsTable')
    self.bonusesTable = self.findChild(QTableWidget, 'bonusesTable')
    
    setTableItemGeometry(self.statsTable)
    setTableItemGeometry(self.statsCapTable)
    setTableItemGeometry(self.resistsTable)
    setTableItemGeometry(self.bonusesTable)
        
def setTableItemGeometry(table: QTableWidget):
    for row in range(table.rowCount()):
        table.setRowHeight(row,20)
        table.setColumnWidth(0,200)
        table.setColumnWidth(1,20)
        table.setColumnWidth(2,20)
        table.setColumnWidth(3,20)
    table.resizeColumnsToContents()

def setSkillsTable(self):
    self.skillsTable = self.findChild(QTableWidget, 'skillsTable')
    skills = self.character.skills
    magic_skills = self.character.magic_skills
    melee_skills = self.character.melee_skills
    dual_wield_skills = self.character.dual_wield_skills
    archery_skills = self.character.archery_skills
    total_skills = len(skills) + len(magic_skills) + len(melee_skills) + len(dual_wield_skills) + len(archery_skills)
    current_row = 0
    self.skillsTable.setRowCount(total_skills)
    
    for skill, value in {**magic_skills, **melee_skills, **dual_wield_skills, **archery_skills, **skills}.items():
        skill_item = QTableWidgetItem(str(skill))
        value_item = QTableWidgetItem(str(value))
        
        self.skillsTable.setItem(current_row, 0, skill_item)
        self.skillsTable.setItem(current_row, 1, value_item)
        self.skillsTable.setItem(current_row, 2, QTableWidgetItem("11"))
        
        current_row += 1
    calculateDifferenceOfStatAndCap(self, 'skillsTable')
    
    for row in range(self.statsCapTable.rowCount()):
        self.skillsTable.setRowHeight(row,20)
        self.skillsTable.setColumnWidth(0,120)
        self.skillsTable.setColumnWidth(1,20)
        self.skillsTable.setColumnWidth(2,20)
        self.skillsTable.setColumnWidth(3,20)
    self.skillsTable.resizeColumnToContents(0)
        
def setBonusesTable(self):
    self.bonusesTable = self.findChild(QTableWidget, 'bonusesTable')
    self.bonusesTable.setRowCount(0)
    level = self.findChild(QComboBox, 'levelComboBox').currentText()
    for i, (bonus_name, bonus_value) in enumerate(self.character.toa_bonuses.items()):
        self.bonusesTable.insertRow(i)
        formatted_name = bonus_name.replace('_', ' ').title()
        self.bonusesTable.setItem(i, 0, QTableWidgetItem(formatted_name))
        self.bonusesTable.setItem(i, 1, QTableWidgetItem(str(bonus_value)))
        third_column_value = levels.get(level).get('bonusesTable').get(bonus_name, 0)
        self.bonusesTable.setItem(i, 2, QTableWidgetItem(str(third_column_value)))
        self.bonusesTable.setRowHidden(i, True)
    calculateDifferenceOfStatAndCap(self, 'bonusesTable')
    
def clearTable(self, table_name):
    self.tableToClear = self.findChild(QTableWidget, table_name)
    self.level = self.findChild(QComboBox, 'levelComboBox').currentText() 
    self.resistanceHardCap = levels.get(self.level).get(table_name)
    baseStats = self.character.base_stats.copy()
    resistStats = self.character.resists.copy()
    default_caps = levels.get(self.level).get(table_name).copy()
    default_keys = list(default_caps.keys())
    adjustStatsFromMythirian(self, default_caps, self.resistanceHardCap, table_name, baseStats, resistStats)
    for row in range(self.tableToClear.rowCount()):
        self.tableToClear.setItem(row, 1, QTableWidgetItem("0"))
        self.tableToClear.setItem(row, 2, QTableWidgetItem(f"{default_caps[default_keys[row]]}"))
        
def calculateDifferenceOfStatAndCap(self, table_name):
    self.table = self.findChild(QTableWidget, table_name)
    for row in range(self.table.rowCount()):
        self.currentValue = int(self.table.item(row, 1).text())
        self.cap = int(self.table.item(row, 2).text())
        difference = self.currentValue - self.cap
        self.table.setItem(row, 3, QTableWidgetItem(str(difference)))
        setColorBasedOnDifference(self, self.table, row, difference)
        
def setColorBasedOnDifference(self, table, row, difference):
    for column_index in range(table.columnCount()):
        item = table.item(row, column_index)
        match difference:
            case _ if difference < 0:
                item.setForeground(QBrush(QColor('#24b5c2')))
            case 0:
                item.setForeground(QBrush(QColor('#5ad662')))
            case _ if difference > 0:
                item.setForeground(QBrush(QColor('red')))
                
def adjustStatsFromMythirian(self, capsDict, realCaps, table_name, baseStats, resistsStats):
    currentLevel = int(self.findChild(QComboBox, 'levelComboBox').currentText())
    if self.character:
        try:
            myth = self.character.currentItems['Mythirian'].stats
            if myth is not None:
                if self.character.currentItems['Mythirian'].bonus_level <= currentLevel:
                    for mythical_key, base_keys in mythical_base_map.items():
                        if mythical_key in myth:
                            for bonus in mythical_base_map[mythical_key]:
                                if bonus in capsDict:
                                    capsDict[bonus] = realCaps[bonus] + myth[mythical_key]
                                    if table_name == 'statsTable':
                                        baseStats[bonus] = myth[mythical_key]
                                    if table_name == 'resistsTable':
                                        resistsStats[bonus] = myth[mythical_key]
                                    
        except Exception as e:
            pass
            # print(f"Error in adjustStatsFromMythirian: {e}")
            