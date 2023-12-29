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