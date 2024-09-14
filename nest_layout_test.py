import PyQt5.QtWidgets as widget
import sys 


class MainWindow(widget.QWidget):
    def __init__(self):
        super().__init__()
        
        
        self.top_layout = widget.QGridLayout()
        self.top_widget = widget.QWidget()
        self.bottom_layout = widget.QFormLayout()
        self.bottom_widget = widget.QWidget()
        self.main_layout = widget.QVBoxLayout()
        #self.main_widget = widget.QWidget()
        
        self.top_label = widget.QLabel('This is the Top Frame Layout')
        self.top_label.setFrameStyle(widget.QFrame.Panel)
        
        self.bottom_label = widget.QLabel('This is the Bottom Layout')
        
        self.top_layout.addWidget(self.top_label)
        self.bottom_layout.addWidget(self.bottom_label)
        
        self.top_widget.setLayout(self.top_layout)
        #self.top_widget.setFrameStyle(widget.QFrame.Panel)
        
        self.main_layout.addWidget(self.top_widget)
        self.main_layout.addLayout(self.bottom_layout)
        self.setLayout(self.main_layout)
        
        self.show()
        

if __name__ == "__main__":

    app = widget.QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
    
"""    queryLabel = w.QLabel(
        w.QApplication.translate("nestedlayouts", "Query:"))
    queryEdit = w.QLineEdit()
    resultView = w.QTableView()
    queryLayout = w.QHBoxLayout()
    queryLayout.addWidget(queryLabel)
    queryLayout.addWidget(queryEdit)
    mainLayout = w.QVBoxLayout()
    mainLayout.addLayout(queryLayout)
    mainLayout.addWidget(resultView)
    window.setLayout(mainLayout)"""
    # Set up the model and configure the view...

