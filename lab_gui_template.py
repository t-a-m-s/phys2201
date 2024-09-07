import sys
import PyQt5.QtWidgets as widget
import matplotlib 
matplotlib.use('QT5Agg')

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as agg 
from matplotlib.figure import Figure as Fig
import numpy as np

from matplotlib.lines import Line2D

import lab1

# I am regretting not documenting anything


class PlotGraph(agg):
    
    def __init__(self, *args, **kwargs):
        self.fig = Fig(figsize=(200,100), dpi=100)
        self.axes = self.fig.add_subplot(111)
        self.axes.set_title('Lab GUI Template')
        self.axes.grid(True)
        self.axes.set_xlim(0, 200)
        self.axes.set_ylim(0, 200)
        
        
        self.fig.canvas.mpl_connect('pick_event', self.onpick3)
        
        super(PlotGraph, self).__init__(self.fig)


class MainWindow(widget.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__()

        self.setWindowTitle('Lab GUI Template')
        self.setGeometry(1200, 800, 900, 600)    
        self.setLayout(widget.QGridLayout())
        
        self.name_label = widget.QLabel('Leah Leffingwell - PHYS2201')

        self.graph = PlotGraph(self)

        """
            This template is designed to work using the CLI and very little interaction with the GUI. 
            Connect a backend database like Sqlite3 to handle data for graph plotting.

        
        """


        self.layout().addWidget(self.name_label, 0, 0, 1, 1)
        self.layout().addWidget(self.graph, 4,0,4,4)

        self.show()
        
    def f(self, x = np.random.rand(50), y = np.random.rand(50), point='bo'):
        area = 30*np.random.rand(50)**2
        colors = np.random.rand(50)
        try:
            
            self.graph.axes.scatter(x,y, s=area, c=colors, alpha=0.5)
            self.graph.draw()
            self.graph.flush_events()
        except:
            pass
        
        
    def line_of_best_fit(self, x, y, linetype):
        #print(self.is_clicked)
        self.x_val = np.array((x[0],x[-1]))
        self.y_val = np.array((round(y[0],1),round(y[-1],1)))
        slope, intercept = np.polyfit(np.log(self.x_val), np.log(self.x_val), 1)
        print(slope)
        b = 0.1345*np.array(x)+ 90.50
        
        match linetype:
            case 'linear':
                if self.is_clicked[0] == False:
                    #print(self.is_clicked)
                    self.is_clicked[0] = True
                    self.lobf_l = self.graph.axes.plot(np.array(x),b, color='k')
                    #self.graph.axes.plot(self.graph.axes.plot(x, y),np.unique(self.x_val), np.poly1d(np.polyfit(self.x_val, self.y_val, 1))(np.unique(self.y_val)), color='black')
                    self.graph.draw()
                    self.graph.flush_events() 
                    #self.lobf_btn.setStyleSheet('background-color:lightgrey')
                elif self.is_clicked[0] == True: 
                    #print(self.is_clicked)
                    self.is_clicked[0] = False
                    self.lobf_l[0].remove()
                    #print(self.lobf, self.lobf[0])
                    self.graph.draw()
                    self.graph.flush_events() 
                #print(self.lobf)
            case 'nonlinear':
                if self.is_clicked[1] == False:
                    #print(self.is_clicked)
                    self.is_clicked[1] = True
                    self.lobf_nl = self.graph.axes.plot(np.unique(x), 
                                                    np.poly1d(np.polyfit(x, y, 1))(np.unique(y)), color='red')    
                    self.graph.draw()
                    self.graph.flush_events() 
                    #self.lobf_btn.setStyleSheet('background-color:lightgrey')
                elif self.is_clicked[1] == True: 
                    #print(self.is_clicked)
                    self.is_clicked[1] = False
                    self.lobf_nl[0].remove()
                    #print(self.lobf, self.lobf[0])
                    self.graph.draw()
                    self.graph.flush_events() 
                #print(self.lobf)
                
            
            
    def extrapolate(self, x, y):
        b = 0.1345*(np.array((0.1,10.0)))+ 90.50
        if self.is_clicked[2] == False:
            self.is_clicked[2] = True
            self.extrapolate_line = self.graph.axes.plot(np.array((0.1,10.0)),b, 'red')

        else:
            self.is_clicked[2] = False
            self.extrapolate_line[0].remove()
        
        self.graph.draw()
        self.graph.flush_events()


app = widget.QApplication([])
mw = MainWindow()

#Test Dataset (Self produced)
for row in lab1.rows:
    mw.f(row[0], row[1], row[2], row[3])


sys.exit(app.exec_())