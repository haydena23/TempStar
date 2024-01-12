"""
def setMaxImbue(self, level):
    imbueCapacityLabel = self.findChild(QLabel, 'imbueCapacityLabel')
    maxOverchargeLabel = self.findChild(QLabel, 'maxOverchargeLabel')
    capacity = imbue_caps[level]
    maxOverchargeLabel.setText(str(capacity))
    imbueCapacityLabel.setText(str(capacity - 5.5))

def initSCArchTypes(self):
    for i in range(1, 5):
        self.findChild(QComboBox, f'statCategory{i}').clear()
        for index, category in enumerate(alb_arch_maps):
            self.findChild(QComboBox, f'statCategory{i}').insertItem(index, category)

def setArchtypes(self, box):
    archBox = box.objectName()[-1]
    currentArchtype = box.currentText()
    statBox = self.findChild(QComboBox, f'statCombo{archBox}')
    statBox.clear()
    currentRealm = self.character.class_type.realm
    for index, stat in enumerate(arch_map[currentRealm][currentArchtype]):
        statBox.insertItem(index, stat.replace("_"," ").title())
        
    valueBox = self.findChild(QComboBox, f'statValue{archBox}')
    valueBox.clear()
    values = list(stat_values_by_level[currentArchtype])
    values.sort()
    for value in values:
        valueBox.addItem(str(value))
    autoUpdateRealmRank(self)
    
def onSCStatComboBoxChanged(self, box):
    currentItem = self.findChild(QListWidget, 'scItemsListWidget').currentItem().text()
    currentSlot = self.findChild(QComboBox, 'scCurrentSlot').currentText()
    if currentItem == "<Empty Slot>":
        pass
    else:
        vaultCopy = None
        
        for index, item in enumerate(self.character.vault[currentSlot]):
            if item.name == currentItem:
                vaultCopy = item
                
        statToSet = {}
        comboboxes = [self.scStatComboBox1, self.scStatComboBox2, self.scStatComboBox3, self.scStatComboBox4]
        for index, box in enumerate(comboboxes):
            if box.currentText() != '<Empty>':
                statToSet[box.currentText().lower().replace(" ","_")] = int(self.findChild(QComboBox, f'statValue{box.objectName()[-1]}').currentText())
        vaultCopy.setStats(statToSet)
        setImbueLabels(self, calculateTotalImbueCost(self))
        autoUpdateRealmRank(self)
        
def updateAfterValueChange(self):
    currentItem = self.findChild(QListWidget, 'scItemsListWidget').currentItem().text()
    currentSlot = self.findChild(QComboBox, 'scCurrentSlot').currentText()
    vaultCopy = None
        
    for index, item in enumerate(self.character.vault[currentSlot]):
        if item.name == currentItem:
            vaultCopy = item
                
    statToSet = {}
    comboboxes = [self.scStatComboBox1, self.scStatComboBox2, self.scStatComboBox3, self.scStatComboBox4]
    for index, box in enumerate(comboboxes):
        if box.currentText() != '<Empty>':
            statToSet[box.currentText().lower().replace(" ","_")] = int(self.findChild(QComboBox, f'statValue{box.objectName()[-1]}').currentText())
    vaultCopy.setStats(statToSet)
    setImbueLabels(self, calculateTotalImbueCost(self))
    autoUpdateRealmRank(self)
    
def setImbueLabels(self, costs):
    # Default cost if a key is missing
    default_cost = 0.0

    # Define label-cost pairs
    label_cost_pairs = [
        ('gemImbue1', float(costs.get('comboBox1', default_cost))),
        ('gemImbue2', float(costs.get('comboBox2', default_cost))),
        ('gemImbue3', float(costs.get('comboBox3', default_cost))),
        ('gemImbue4', float(costs.get('comboBox4', default_cost))),
        ('totalCostImbue', float(costs.get('totalCost', default_cost))),
        ('gemHighest', float(max(costs.get('comboBox1', default_cost), costs.get('comboBox2', default_cost), costs.get('comboBox3', default_cost), costs.get('comboBox4', default_cost))))
    ]
    for label_name, cost in label_cost_pairs:
        label = self.findChild(QLabel, label_name)
        if label:
            label.setText(str(cost))
    
    total_cost = costs.get('totalCost', 0.0)
    max_overcharge_value = float(self.maxOverchargeLabel.text())

    if total_cost < max_overcharge_value:
        color = "#24b5c2"  # Blue
    elif total_cost == max_overcharge_value:
        color = "#5ad662"  # Green
    else:
        color = "red"

    total_cost_label = self.findChild(QLabel, 'totalCostImbue')
    if total_cost_label:
        total_cost_label.setStyleSheet(f"color: {color};")
        
"""