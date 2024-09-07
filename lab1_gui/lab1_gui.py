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
        self.axes.set_title('Average Velocity vs. Displacement')
        self.axes.grid(True)
        self.axes.set_xlim(0, 200)
        self.axes.set_ylim(0, 200)
        
        
        self.fig.canvas.mpl_connect('pick_event', self.onpick3)
        
        super(PlotGraph, self).__init__(self.fig)
       
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

        #print(round(mw.line_plot[0].get_data()[1][0],1))
        self.fig.canvas.draw_idle()
  
        
        
        

class MainWindow(widget.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__()

        self.setWindowTitle('Lab 1 - Instantaneous vs. Average Velocity')
        self.setGeometry(1200, 800, 900, 600)    
        self.setLayout(widget.QGridLayout())
        
        self.name_label = widget.QLabel('Leah Leffingwell - PHYS2201')
        
        self.delta_x_label = widget.QLabel('$\delta x$')
        self.t_1_label = widget.QLabel('$t_{1}$')
        self.t_2_label = widget.QLabel('$t_{2}$')
        self.t_3_label = widget.QLabel('$t_{3}$')
        
        self.delta_x_input = widget.QLineEdit()
        self.t_1_input = widget.QLineEdit()
        self.t_2_input = widget.QLineEdit()
        self.t_3_input = widget.QLineEdit()
        
        self.data_array = []
        self.x_array = []
        self.y_array = []
        
        submit_btn = widget.QPushButton('Submit', clicked=lambda: self.f(
                                                                        self.delta_x_input.text(), 
                                                                        self.t_1_input.text(), 
                                                                        self.t_2_input.text(), 
                                                                        self.t_3_input.text(),
                                                                        point='go'
                                                                        )
                                        )
        
        self.table_label = widget.QLabel()
        self.table_label.setVisible(False)
        
        self.graph = PlotGraph(self)
        
        
        self.lobfl_btn = widget.QPushButton('Line of Best Fit (Linear)', clicked=lambda: self.line_of_best_fit(
                                                                                                    self.x_array, 
                                                                                                    self.y_array,
                                                                                                    'linear'))
        
        self.lobfnl_btn = widget.QPushButton('Line of Best Fit (Non-Linear)', clicked=lambda: self.line_of_best_fit(
                                                                                                    self.x_array, 
                                                                                                    self.y_array,
                                                                                                    'nonlinear'))
        
        self.is_clicked = [False, False, False]
        self.extrapolate_btn = widget.QPushButton('Extrapolate', clicked=lambda: self.extrapolate(self.x_array, self.y_array))
        
        self.layout().addWidget(self.name_label,0,0)
        self.layout().addWidget(self.extrapolate_btn, 8, 2,1,1)
        self.layout().addWidget(self.delta_x_label, 1,0)
        self.layout().addWidget(self.delta_x_input, 2, 0)
        self.layout().addWidget(self.t_1_label, 1, 1)
        self.layout().addWidget(self.t_1_input, 2, 1)
        self.layout().addWidget(self.t_2_label, 1, 2)
        self.layout().addWidget(self.t_2_input, 2, 2)
        self.layout().addWidget(self.t_3_label, 1, 3)
        self.layout().addWidget(self.t_3_input, 2, 3)
        self.layout().addWidget(submit_btn, 2, 4)
        self.layout().addWidget(self.table_label, 3, 0, 1, 2)
        self.layout().addWidget(self.graph, 4, 0, 4, 4)
        self.layout().addWidget(self.lobfl_btn, 8, 0, 1,1)
        self.layout().addWidget(self.lobfnl_btn, 8, 1, 1,1)
        
        
        self.show()
        
    def f(self, delta_x, t_1, t_2, t_3, point='bo'):
        #print(delta_x, t_1, t_2, t_3)
        try:
            delta_x = float(delta_x)
            t_1 = float(t_1)
            t_2 = float(t_2)
            t_3 = float(t_3)
            t_av = (t_1+t_2+t_3)/ 3
            v_av = delta_x/t_av
            #self.data_array.append([delta_x,round(v_av,1)])
            #print(self.data_array)
            self.x_array.append(delta_x)
            self.y_array.append(v_av)
            self.graph.axes.plot(delta_x, v_av, point, picker=True)
            #self.graph.axes.annotate(text=f'({delta_x},{round(v_av,1)})', xy=(delta_x+0.5,v_av+0.5))
            self.graph.axes.text(x=delta_x+0.5, y=v_av+0.5, s=f'({delta_x}, {round(v_av, 1)})').set_visible(False)
            self.graph.draw()
            self.graph.flush_events()
            self.delta_x_input.clear()
            self.t_1_input.clear()
            self.t_2_input.clear()
            self.t_3_input.clear()
            print(delta_x, round(v_av,1))
            #print(round(t_av, 4), round(v_av, 1))
            # Outputs the change in position/displacement (delta_x), the average time (t_av), and the average velocity (v_av) of each trial
            # To do (maybe): Render latex in PyQt. Output latex to mpl and convert to pic embed in PyQT? 
            #self.table_label.setText(f'{self.table_label.text()} \n done: delta_x = {delta_x}, t_av = {(round(t_av, 4))}, v_av = {(round(v_av, 1))}')
            #self.table_label.setVisible(True)
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