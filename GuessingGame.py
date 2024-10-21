# The Program is a GUI based guessing game that allows the user to guess a random 
#number inserted by the user and it indicates if the user input is correct, too big or too small
# Nkosi Zachariah
# 10 March 2023


import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import random
    
class Game(QWidget): # MyWidget inherits from QWidget
    
    def __init__(self, parent=None): # parent defines parent widget
        QWidget.__init__(self, parent) # super class constructor
        self.setGeometry(250, 250, 250, 250) # Setting the Location and size of the main widget
        self.setWindowTitle('Guessing Game')
        self.grids()
         
    def close_button(self):
        #quits the game
        self.close()
        
    def new_game_clicked(self):
        
        #Restarts the game when the user presses the new game button and displays the number of attempts a user has
        
        self.guess1_Label.setText('Guess 1')    
        self.guess2_Label.setText('Guess 2')   
        self.guess3_Label.setText('Guess 3')
        
        self.user_first_guess.setText('')
        self.user_sec_guess.setText('')
        self.user_third_guess.setText('')
        
        self.result1.setText('')        
        self.result2.setText('')     
        self.result3.setText('')     
        #new random number
        self.number = random.randint(1,10)
        
    def text(self):
        #holds the guess number entered by the user
        self.edit.text()
     
    def clicked(self):
        
        #Responsible for the change of the color and picture change on the game
        
        if self.color_combo.currentText() == 'red':     #red background
            self.setAutoFillBackground(True)
            bg_color = self.palette()
            bg_color.setColor(self.backgroundRole(), Qt.red)
            self.setPalette(bg_color)
        else:
            self.setAutoFillBackground(True)    #blue background
            bg_color = self.palette()
            bg_color.setColor(self.backgroundRole(), Qt.blue)
            self.setPalette(bg_color)
        
        if self.picture_combo.currentText() == 'mickey':    #mickey picture widget
            self.picture_.setPixmap(QPixmap('mickey.gif'))
        else:
            self.picture.setPixmap(QPixmap('pluto.gif'))    #pluto picture widget
                  
    def guesses(self):
        
        #Shows the guess number, number guessed and whether it is correct or not then allows the user to attempt again if incorrect
        
        while True:
            if self.guess1_Label.text() == 'Guess 1' :
                self.guess1_Label.setText('Guess 1:')
                if int(self.edit.text()) == self.number:
                    self.user_first_guess.setText(self.edit.text())
                    self.result1.setText('Correct!')
                elif int(self.edit.text()) < self.number:
                    self.user_first_guess.setText(self.edit.text())
                    self.result1.setText('Too small')
                else:
                    self.user_first_guess.setText(self.edit.text())
                    self.result1.setText('Too big')
                break
            
            elif self.guess2_Label.text() == 'Guess 2':
                self.guess2_Label.setText('Guess 2:')
                if int(self.edit.text()) == self.number:
                    self.user_sec_guess.setText(self.edit.text())
                    self.result2.setText('Correct!')
                elif int(self.edit.text()) < self.number:
                    self.user_sec_guess.setText(self.edit.text())
                    self.result2.setText('Too small')
                else:
                    self.user_sec_guess.setText(self.edit.text())
                    self.result2.setText('Too big')
                break
            
            elif self.guess3_Label.text() == 'Guess 3':
                self.guess3_Label.setText('Guess 3:') 
                if int(self.edit.text()) == self.number:
                    self.user_third_guess.setText(self.edit.text())
                    self.result3.setText('Correct!')
                elif int(self.edit.text()) < self.number:
                    self.user_third_guess.setText(self.edit.text())
                    self.result3.setText('Too small')   
                else:
                    self.user_third_guess.setText(self.edit.text())
                    self.result3.setText('Too big') 
                break            
            break    
        
    def grids(self):
        
        #Adds all the widgets into the window in a grid format
        
        grid = QGridLayout()#creates grid layout
        
        #creates an initial background color
        self.setAutoFillBackground(True)
        bg_color = self.palette()
        bg_color.setColor(self.backgroundRole(), Qt.red)
        self.setPalette(bg_color)
        
        #creates an initial display image
        self.picture = QLabel(self)
        pixmap = QPixmap('mickey.gif')
        self.picture.setPixmap(pixmap)
        self.resize(pixmap.width(),pixmap.height())
        grid.addWidget(self.picture, 0,0,15,1)
        
        #guess displays
        guess = QLabel('Guesses:')
        guess.setFont(QFont('Bold',15,2))
        grid.addWidget(guess, 0,1)
        
        #shows the number of attempts/guesses a user has
        self.guess1_Label = QLabel('Guess 1')
        self.guess2_Label = QLabel('Guess 2')
        self.guess3_Label = QLabel('Guess 3')
        grid.addWidget(self.guess1_Label,1,1)
        grid.addWidget(self.guess2_Label,2,1)
        grid.addWidget(self.guess3_Label,3,1)   
        
        self.user_first_guess = QLabel('')
        self.user_sec_guess = QLabel('')
        self.user_third_guess = QLabel('')
        grid.addWidget(self.user_first_guess,1,2)
        grid.addWidget(self.user_sec_guess,2,2)
        grid.addWidget(self.user_third_guess,3,2)
        
        self.result1 = QLabel('')
        self.result2 = QLabel('')
        self.result3 = QLabel('')
        grid.addWidget(self.result1, 1,3)
        grid.addWidget(self.result2, 2,3)
        grid.addWidget(self.result3, 3,3)
        
        #user edit entry
        self.edit = QLineEdit(self)
        grid.addWidget(self.edit,4,2)        
        
        #random number
        self.number = random.randint(1,10)
        
        self.guess_button = QPushButton('Guess')
        self.guess_button.clicked.connect(self.text)                                        
        self.guess_button.clicked.connect(self.guesses)                                        
        grid.addWidget(self.guess_button, 4,3)        
        
        #Interface controls
        inter = QLabel('Interface:') 
        inter.setFont(QFont('Bold',15,2))#heading formatting
        grid.addWidget(inter, 7,1)        
        
        pic = QLabel('Picture:')
        color = QLabel('Colour:')
        grid.addWidget(pic, 8,1)
        grid.addWidget(color, 9,1)        
        
        self.closer = QPushButton('Close')
        self.closer.clicked.connect(self.close_button)                                     
        grid.addWidget(self.closer, 10, 1)         
        
        self.change = QPushButton('Change')
        grid.addWidget(self.change, 9,3)        
        self.change.clicked.connect(self.clicked)    
        
        self.new = QPushButton('New Game')
        self.new.clicked.connect(self.new_game_clicked)   
        grid.addWidget(self.new, 10,2)
        
        self.color_combo = QComboBox()
        self.color_combo.addItem('red')
        self.color_combo.addItem('blue')      
        grid.addWidget(self.color_combo,9,2)
        
        self.picture_combo = QComboBox()
        self.picture_combo.addItem('mickey')
        self.picture_combo.addItem('pluto')
        grid.addWidget(self.picture_combo,8,2)
      
        self.setLayout(grid)
    
if __name__ == '__main__':
    try:
        app = QApplication(sys.argv)
        window = Game() # create MyWidget object
        window.show()
        sys.exit(app.exec_())
    except:
        pass