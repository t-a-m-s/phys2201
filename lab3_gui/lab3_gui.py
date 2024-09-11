import sys
from PyQt5 import QtCore
import PyQt5.QtWidgets as widget
import matplotlib 
import matplotlib.pyplot as plt
matplotlib.use('QT5Agg')

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as agg 
from matplotlib.figure import Figure as Fig
import numpy as np

from matplotlib.lines import Line2D



class PlotGraph(agg):
    
    def __init__(self, x_lim = 10, y_lim = 10, x_label = 'X Label', 
                 y_label = 'Y Label', graph_title = 'Graph Title', *args, **kwargs):
        self.fig = Fig(figsize=(200,100), dpi=100)
        self.axes = self.fig.add_subplot(111)
        self.axes.grid(True)
        self.axes.set_title(graph_title)
        print(x_lim, y_lim)
        self.axes.set_xlim(0, x_lim)
        self.axes.set_ylim(0, y_lim)
        self.axes.set_xlabel(x_label)
        self.axes.set_ylabel(y_label)
        # Click to see data coords
        self.fig.canvas.mpl_connect('pick_event', self.onpick3) 
        
        super(PlotGraph, self).__init__(self.fig)
        
    # Not keep? 
    def set_graph_config(self, ):
        self.axes.set_title('Lab 3 - Placeholder')
        self.axes.set_xlim(0, 8)
        self.axes.set_ylim(0, 12)
        self.axes.set_xlabel('x-axis - Placeholder')
        self.axes.set_ylabel('y-axis - Placeholder')
        
       
    # Why points not changing colour how I want -> Deleted data point colour change for now
    # (FIXED) But now text visibility is not working ugh
    def onpick3(self, event):
        point = event.artist
        x = point.get_xdata().item()
        y = round(point.get_ydata().item(),1)
        
        for txt in self.axes.texts:
            txt.set_visible(False)
            txt_x,txt_y = txt.get_position()
            
            if x == txt_x-0.5:
                print(x)
                txt.set_visible(True)

        self.fig.canvas.draw_idle()
  

class MainWindow(widget.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__()
        # Define initUI() function
        #self.initUI()

        self.setWindowTitle('Lab 2 - Picket Fence Free Fall')
        self.setGeometry(1200, 800, 900, 600)    
        self.setLayout(widget.QGridLayout())
        
        self.name_label = widget.QLabel('Leah Leffingwell - PHYS2201')
        
        self.data_array = []
        self.x_array = []
        self.y_array = []
        
        submit_btn = widget.QPushButton('Submit', clicked=lambda: self.f())
        
        # graph_title
        self.graph_title_label = widget.QLabel('Graph Title')
        self.graph_title_input = widget.QLineEdit()
        
        # x_lim, y_lim
        self.x_lim_label = widget.QLabel('x lim')
        self.x_lim_input = widget.QLineEdit()
        self.y_lim_label = widget.QLabel('y lim')
        self.y_lim_input = widget.QLineEdit()
        
        # x_label, y_label
        self.x_label_label = widget.QLabel('x label')
        self.x_label_input = widget.QLineEdit()
        self.y_label_label = widget.QLabel('y label')
        self.y_label_input = widget.QLineEdit()
        
        # is_grid
        self.is_grid_btn = widget.QCheckBox('Grid')
        
        self.plot_graph_btn = widget.QPushButton('Create Graph', clicked=lambda: self.plot_graph(
                                                                                                graph_title=self.graph_title_input.text(),
                                                                                                x_lim=int(self.x_lim_input.text()),
                                                                                                y_lim=int(self.y_lim_input.text()),
                                                                                                x_label=self.x_label_input.text(),
                                                                                                y_label=self.y_label_input.text(),
                                                                                                is_grid=self.is_grid_btn.checkState()
                                                                                                ))
    
        self.graph_widgets = [
            self.graph_title_label,
            self.graph_title_input,
            self.x_lim_label,
            self.x_lim_input,
            self.y_lim_label,
            self.y_lim_input,
            self.x_label_label,
            self.x_label_input,
            self.y_label_label,
            self.y_label_input,
            self.is_grid_btn,
            self.plot_graph_btn
            ]

        self.edit_graph_btn = widget.QPushButton('Edit Graph', clicked=lambda: self.edit_graph())
        self.edit_graph_btn.setVisible(False)
    
        # x,y limits, x,y labels, graph title
        self.graph = PlotGraph() #x_lim = x, y_lim = y, x_label = 'X Label', y_label = 'Y Label', graph_title = 'Graph Title
        self.graph.setVisible(False)
        
        self.is_clicked = [] # Add False for each QPushButton widget to check if is_clicked

        # Add Lab 3 Widgets Below
        
        self.placeholder_label = widget.QLabel('This is a Placeholder for the Lab 3 parameters required to plot')
        
        # See nested and stacked layouts
        # Also try tabs to combine all lab programs into one app
        # Don't change rowspan on widgets. Doesn't fix graph being nudged up and down
        self.layout().addWidget(self.name_label,0,0, 1, 1)

        self.layout().addWidget(submit_btn, 2, 7)
        self.layout().addWidget(self.plot_graph_btn, 10, 7)
        self.layout().addWidget(self.edit_graph_btn, 10, 7)
        
        self.layout().addWidget(self.graph_title_label, 9, 0)
        self.layout().addWidget(self.graph_title_input, 10, 0 )
        
        self.layout().addWidget(self.x_label_label, 9, 1)
        self.layout().addWidget(self.x_label_input, 10, 1)
        
        self.layout().addWidget(self.y_label_label, 9, 2)
        self.layout().addWidget(self.y_label_input, 10, 2)
        
        self.layout().addWidget(self.x_lim_label, 9, 3)
        self.layout().addWidget(self.x_lim_input, 10, 3)
        
        self.layout().addWidget(self.y_lim_label, 9, 4)
        self.layout().addWidget(self.y_lim_input, 10, 4)
        
        self.layout().addWidget(self.is_grid_btn, 10, 5)
        
        self.layout().addWidget(self.graph, 4, 0, 4, 8)
        
        
        # Add Lab 3 Widgets to Layout Below
        self.layout().addWidget(self.placeholder_label, 2, 0, 1,7)
        
        self.show()
        
    def f(self):
        try:
            print('Clicked submit button')
        except:
            pass
        
    def plot_graph(self, is_grid = True, graph_title = 'Graph Title - Placeholder', x_lim = 10, y_lim = 10, x_label = 'x-axis - Placeholder', y_label = 'y-axis - Placeholder'):
        try:
            self.graph.axes.grid(is_grid)
            self.graph.axes.set_title(graph_title)
            self.graph.axes.set_xlim(0, x_lim)
            self.graph.axes.set_ylim(0, y_lim)
            self.graph.axes.set_xlabel(x_label)
            self.graph.axes.set_ylabel(y_label)
            self.graph.setVisible(True)
            self.edit_graph_btn.setVisible(True)
            
            for widget in self.graph_widgets:
                widget.setVisible(False)
            
        except:
            pass
        
    def edit_graph(self):
        #self.graph.setVisible(False)
        self.edit_graph_btn.setVisible(False)
        self.plot_graph_btn.setText('Update Graph')
        for widget in self.graph_widgets:
                widget.setVisible(True)
        
        
        
def main():
    app = widget.QApplication([])
    mw = MainWindow()

    #Test Dataset (Self produced)



    sys.exit(app.exec_())

if __name__ == '__main__':
    main()