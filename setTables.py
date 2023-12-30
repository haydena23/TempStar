from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem

def initTables(self):
    self.statsTable = self.findChild(QTableWidget, 'statsTable')
    for row in range(self.statsTable.rowCount()):
        self.statsTable.setRowHeight(row,20)
        self.statsTable.setColumnWidth(0,100)
        self.statsTable.setColumnWidth(1,20)
        self.statsTable.setColumnWidth(2,20)
        self.statsTable.setColumnWidth(3,20)
        
    self.statsCapTable = self.findChild(QTableWidget, 'statsCapTable')
    for row in range(self.statsCapTable.rowCount()):
        self.statsCapTable.setRowHeight(row,20)
        self.statsCapTable.setColumnWidth(0,100)
        self.statsCapTable.setColumnWidth(1,20)
        self.statsCapTable.setColumnWidth(2,20)
        self.statsCapTable.setColumnWidth(3,20)
        
    self.resistsTable = self.findChild(QTableWidget, 'resistsTable')
    for row in range(self.resistsTable.rowCount()):
        self.resistsTable.setRowHeight(row,20)
        self.resistsTable.setColumnWidth(0,100)
        self.resistsTable.setColumnWidth(1,20)
        self.resistsTable.setColumnWidth(2,20)
        self.resistsTable.setColumnWidth(3,20)
        
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
        
        current_row += 1
    
    for row in range(self.statsCapTable.rowCount()):
        self.skillsTable.setRowHeight(row,20)
        self.skillsTable.setColumnWidth(0,120)
        self.skillsTable.setColumnWidth(1,20)
        self.skillsTable.setColumnWidth(2,20)
        self.skillsTable.setColumnWidth(3,20)
        
def clearTable(self, table_name):
    self.tableToClear = self.findChild(QTableWidget, table_name)
    for row in range(self.tableToClear.rowCount()):
        self.tableToClear.setItem(row, 1, QTableWidgetItem("0"))
        self.tableToClear.setItem(row, 2, QTableWidgetItem("26"))
        self.tableToClear.setItem(row, 3, QTableWidgetItem("-26"))
        
def calcuateDifferenceOfStatAndCap(self, table_name):
    self.table = self.findChild(QTableWidget, table_name)
    for row in range(self.table.rowCount()):
        self.currentValue = int(self.table.item(row, 1).text())
        self.cap = int(self.table.item(row, 2).text())
        difference = self.currentValue - self.cap
        self.table.setItem(row, 3, QTableWidgetItem(str(difference)))