dark_mode_style = """
    QMenuBar, QMenu {
        background-color: #2b2f38;
        color: #9da5b4;
    }
    QMenuBar::item:selected , QMenu::item:selected {
        background-color: #313438;
    }
    QMainWindow {
        background-color: #2b2f38; /* Dark background color */
        color: #abb2bf; /* Light text color */
    }
    QLabel, QGroupBox {
        color: #abb2bf;
    }
    QTabWidget::pane {
        background-color: #494d52;
    }
    QTabBar::tab {
        background-color: #21252b;
        color: #9da5b4;
    }
    QTabBar::tab:selected {
        background-color: #2b2f38;
        color: #9da5b4;
    }
    QTableWidget, QTableWidget::Section {
        background-color: #585a5c;
    }
"""

    # QLabel, QPushButton, QLineEdit, QTableWidget, QComboBox {
    #     background-color: #454545; /* Darker elements */
    #     color: #ffffff;
    #     border: 1px solid #767676;
    # # }