from character import Character
from class_types import *
from race_types import *
from mappings import *
from PyQt5.QtWidgets import QTableWidgetItem, QTableWidget, QComboBox
from setTables import initTables, setSkillsTable

def new_character_change(self, class_type: ClassType):
    self.character = Character("New Character", class_type, 1, 1, 1)
    reset_ui_for_new_character(self)

def create_new_character_on_open(self):
    initTables(self)
    self.character = Character("New Character", Armsman, 1, 1, 1)
    reset_ui_for_new_character(self)
    
        
def reset_ui_for_new_character(self):
    update_stats_table(self)
    update_resists_table(self)
    update_stats_cap_table(self)
    setSkillsTable(self)
    setAllowedClassesComboBox(self)

def update_stats_table(self):
    if self.character:
        for stat_type, row in stats_row_mapping.items():
            stat_value = self.character.stats.get(stat_type, 0)
            self.tableWidget = self.findChild(QTableWidget,'statsTable')
            value_item = QTableWidgetItem(str(stat_value))
            self.tableWidget.setItem(row, 1, value_item)
    
def update_stats_cap_table(self):
    if self.character:
        for stat_cap_type, row in stats_cap_mapping.items():
            stat_cap_value = self.character.stat_caps.get(stat_cap_type, 0)
            self.tableWidget = self.findChild(QTableWidget,'statsCapTable')
            value_item = QTableWidgetItem(str(stat_cap_value))
            self.tableWidget.setItem(row, 1, value_item)
                    
def update_resists_table(self):
    if self.character:
        for resist_type, row in resists_row_mapping.items():
            resist_value = self.character.resists.get(resist_type, 0)
            self.tableWidget = self.findChild(QTableWidget,'resistsTable')
            value_item = QTableWidgetItem(str(resist_value))
            self.tableWidget.setItem(row, 1, value_item)

def setAllowedClassesComboBox(self):
    if self.character:
        self.raceComboBox = self.findChild(QComboBox,'raceComboBox')
        self.raceComboBox.clear()
        for race in self.character.allowed_races:
            self.raceComboBox.addItem(str(race.name))
        self.raceComboBox.model().sort(0)
        self.raceComboBox.setCurrentIndex(0)