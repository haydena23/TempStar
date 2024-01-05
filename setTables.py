from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QComboBox
from PyQt5.QtGui import QColor, QBrush

from Models.levels import levels

def initTables(self):
    self.statsTable = self.findChild(QTableWidget, 'statsTable')    
    self.statsCapTable = self.findChild(QTableWidget, 'statsCapTable')        
    self.resistsTable = self.findChild(QTableWidget, 'resistsTable')
    
    setTableItemGeometry(self.statsTable)
    setTableItemGeometry(self.statsCapTable)
    setTableItemGeometry(self.resistsTable)
        
def setTableItemGeometry(table: QTableWidget):
    for row in range(table.rowCount()):
        table.setRowHeight(row,20)
        table.setColumnWidth(0,100)
        table.setColumnWidth(1,20)
        table.setColumnWidth(2,20)
        table.setColumnWidth(3,20)

def setSkillsTable(self):
    self.skillsTable = self.findChild(QTableWidget, 'skillsTable')
    magic_skills = self.character.magic_skills
    melee_skills = self.character.melee_skills
    total_skills = len(magic_skills) + len(melee_skills)
    current_row = 0
    self.skillsTable.setRowCount(total_skills)
    
    for skill, value in {**magic_skills, **melee_skills}.items():
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
        
def clearTable(self, table_name):
    self.tableToClear = self.findChild(QTableWidget, table_name)
    self.level = self.findChild(QComboBox, 'levelComboBox').currentText() 
    default_caps = levels.get(self.level).get(table_name)
    default_keys = list(default_caps.keys())
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