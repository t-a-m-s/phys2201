import sys
import PyQt5.QtWidgets as widget
import PyQt5 as qt

if __name__ == '__main__':
    app = widget.QApplication([])
    window = widget.QWidget()
    
    wid = widget.QPushButton('wid')
    wid.setLayoutDirection(qt.QtCore.Qt.RightToLeft)
    wid.setMaximumSize(50,30)
    jet = widget.QCheckBox('jet')
    jet.setLayoutDirection(qt.QtCore.Qt.RightToLeft)
    
    but = widget.QLabel('button')
    but.setAlignment(qt.QtCore.Qt.AlignHCenter)
    but.setFrameStyle(widget.QFrame.Panel)
    but.setLayout(widget.QGridLayout())
    but.layout().addWidget(wid, 1,0)
    but.layout().addWidget(jet,2,1)
    window.setLayout(widget.QVBoxLayout())
    
    window.layout().addWidget(but)
    
    window.show()
    sys.exit(app.exec())