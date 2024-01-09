from Models.character import Character
from Models.classes import *
from Models.races import *
from Models.mappings import *
from PyQt5.QtWidgets import QTableWidgetItem, QTableWidget, QComboBox
from setTables import initTables, setSkillsTable, calculateDifferenceOfStatAndCap, setBonusesTable

def new_character_change(self, class_type: ClassType):
    self.character = Character("New Character", class_type, 1, 1, 1, None, self.character.vault)
    reset_ui_for_new_character(self)

def create_new_character_on_open(self):
    initTables(self)
    self.character = Character("New Character", Armsman, 1, 1, 1)
    reset_ui_for_new_character(self)
     
def reset_ui_for_new_character(self):
    set_initial_table(self, 'statsTable', stats_row_mapping, self.character.base_stats)
    set_initial_table(self, 'statsCapTable', stats_cap_mapping, self.character.stat_caps)
    set_initial_table(self, 'resistsTable', resists_row_mapping, self.character.resists)
    setSkillsTable(self)
    setBonusesTable(self)
    setAllowedClassesComboBox(self)
    setRealmRank(self)

def set_initial_table(self, table_name, mapping, stats):
    if self.character:
        for stat_type, row in mapping.items():
            stat_value = stats.get(stat_type, 0)
            self.tableWidget = self.findChild(QTableWidget,table_name)
            value_item = QTableWidgetItem(str(stat_value))
            self.tableWidget.setItem(row, 1, value_item)
            calculateDifferenceOfStatAndCap(self, table_name)

def setAllowedClassesComboBox(self):
    if self.character:
        self.raceComboBox = self.findChild(QComboBox,'raceComboBox')
        self.raceComboBox.clear()
        for race in self.character.allowed_races:
            self.raceComboBox.addItem(str(race.name))
        self.raceComboBox.model().sort(0)
        self.raceComboBox.setCurrentIndex(0)

def setRealmRank(self):
    if self.character:
        self.realmRankComboBox = self.findChild(QComboBox, 'realmRankComboBox')
        self.realmRankComboBox.setCurrentIndex(0)