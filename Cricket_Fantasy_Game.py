# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_code.ui'
#'M O T CODE'
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!

from calculate_points import player_points
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from OpenTeam import Ui_Dialog as Open   # importing open window dialogbox
from NewTeam import Ui_Dialog as New     # importing new window dialogbox
from Evaluate import Ui_evaluate_team as Eva  # importing evaluate window dialogbox

import sqlite3
fant=sqlite3.connect('Fantasy.db')  # connecting to database file(fandatabase.db)
fantcurs=fant.cursor()


class Ui_MainWindow(object):
    def __init__(self):
        self.newDialog = QtWidgets.QMainWindow()
        self.new_screen = New()
        self.new_screen.setupUi(self.newDialog)

        self.EvaluateWindow = QtWidgets.QMainWindow()
        self.eval_screen = Eva()
        self.eval_screen.setupUi(self.EvaluateWindow)

        self.openDialog = QtWidgets.QMainWindow()
        self.open_screen = Open()
        self.open_screen.setupUi(self.openDialog)

      # FILE OPENING MENU
    def file_open(self):
        self.open_screen.setupUi(self.openDialog)
        self.openDialog.show()
        self.open_screen.openbtn.clicked.connect(self.openteam)

    # EVALUATE TEAM MENU
    def file_evaluate(self):
        self.eval_screen.setupUi(self.EvaluateWindow)
        self.EvaluateWindow.show()

    def setupUi(self, MainWindow):

        # INITIALISING POINTS AND COUNTS
        self.avail_points = 1000
        self.used_points = 0
        self.totalcount = 0
        self.batsmencount = 0
        self.bowlerscount = 0
        self.alrdscount = 0
        self.wicketerscount = 0
        # INITIALIZING LISTS
        self.a = []  # bowler names list
        self.b = []  #  batsman nameslist
        self.c = []   # allrounder names list
        self.d = []  #wicketer names list
        self.list1 = []    # selectedplayer's list
    
   
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(556, 523)
        MainWindow.setStyleSheet("background-color: rgb(213, 205, 208);")
        self.central_w = QtWidgets.QWidget(MainWindow)
        self.central_w.setObjectName("central_w")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.central_w)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_3.addItem(spacerItem)
        self.frame = QtWidgets.QFrame(self.central_w)
        self.frame.setStyleSheet("background-color: rgb(172, 139, 182);\n"
"font: 75 10pt \"Georgia\";\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setContentsMargins(-1, 5, -1, 24)
        self.gridLayout.setObjectName("gridLayout")
        self.BAT = QtWidgets.QLabel(self.frame)
        self.BAT.setStyleSheet("color: rgb(0, 170, 255);")
        self.BAT.setObjectName("BAT")
        self.gridLayout.addWidget(self.BAT, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.WK = QtWidgets.QLabel(self.frame)
        self.WK.setStyleSheet("color: rgb(0, 170, 255);")
        self.WK.setObjectName("WK")
        self.gridLayout.addWidget(self.WK, 1, 7, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 2, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 1, 4, 1, 1)
        self.ARL = QtWidgets.QLabel(self.frame)
        self.ARL.setStyleSheet("color: rgb(0, 170, 255);")
        self.ARL.setObjectName("ARL")
        self.gridLayout.addWidget(self.ARL, 1, 5, 1, 1)
        self.BOWL = QtWidgets.QLabel(self.frame)
        self.BOWL.setStyleSheet("color: rgb(0, 170, 255);")
        self.BOWL.setObjectName("BOWL")
        self.gridLayout.addWidget(self.BOWL, 1, 3, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.frame)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 1, 6, 1, 1)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setStyleSheet("\n"
"font: Bold 9pt \"Georgia\";")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.verticalLayout_3.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.central_w)
        self.frame_2.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
"border-color: rgb(255, 255, 255);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_2.setLineWidth(0)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setContentsMargins(46, 8, 23, 5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        self.label_6.setStyleSheet("font: 75 9pt \"MS Shell Dlg 2\";")
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        self.points_available = QtWidgets.QLabel(self.frame_2)
        self.points_available.setStyleSheet("color: rgb(85, 170, 255);")
        self.points_available.setObjectName("points_available")
        self.horizontalLayout.addWidget(self.points_available)
        self.label_7 = QtWidgets.QLabel(self.frame_2)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout.addWidget(self.label_7, 0, QtCore.Qt.AlignRight)
        self.points_used = QtWidgets.QLabel(self.frame_2)
        self.points_used.setStyleSheet("color: rgb(85, 170, 255);")
        self.points_used.setObjectName("points_used")
        self.horizontalLayout.addWidget(self.points_used, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_3.addWidget(self.frame_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem1 = QtWidgets.QSpacerItem(13, 345, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.frame_3 = QtWidgets.QFrame(self.central_w)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setStyleSheet("border-color: rgb(15, 15, 15);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_3.setLineWidth(2)
        self.frame_3.setMidLineWidth(1)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout.setContentsMargins(19, -1, 19, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_5 = QtWidgets.QFrame(self.frame_3)
        self.frame_5.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
        self.frame_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        
        self.bat_rb = QtWidgets.QRadioButton(self.frame_5) # bat_rb
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bat_rb.sizePolicy().hasHeightForWidth())
        self.bat_rb.setSizePolicy(sizePolicy)
        self.bat_rb.setEnabled(False)
        self.bat_rb.setTabletTracking(False)
        self.bat_rb.setAcceptDrops(False)
        self.bat_rb.setObjectName("bat_rb")
        self.horizontalLayout_2.addWidget(self.bat_rb)
        
        self.bow_rb = QtWidgets.QRadioButton(self.frame_5)#bat_rb
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        self.bow_rb.setEnabled(False)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bow_rb.sizePolicy().hasHeightForWidth())
        self.bow_rb.setSizePolicy(sizePolicy)
        self.bow_rb.setObjectName("bow_rb")
        
        self.horizontalLayout_2.addWidget(self.bow_rb)
        self.ar_rb = QtWidgets.QRadioButton(self.frame_5)#ar_rb
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ar_rb.sizePolicy().hasHeightForWidth())
        self.ar_rb.setSizePolicy(sizePolicy)
        self.ar_rb.setEnabled(False)
        self.ar_rb.setObjectName("ar_rb")
        self.horizontalLayout_2.addWidget(self.ar_rb)

        
        self.wk_rb = QtWidgets.QRadioButton(self.frame_5)#wk_rb
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        self.wk_rb.setEnabled(False)
        sizePolicy.setHeightForWidth(self.wk_rb.sizePolicy().hasHeightForWidth())
        self.wk_rb.setSizePolicy(sizePolicy)
        self.wk_rb.setObjectName("wk_rb")
        self.horizontalLayout_2.addWidget(self.wk_rb)
        
        self.verticalLayout.addWidget(self.frame_5) #available_players
        self.av_player = QtWidgets.QListWidget(self.frame_3)
        self.av_player.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.av_player.setObjectName("av_player")
        self.verticalLayout.addWidget(self.av_player)
        
        self.horizontalLayout_4.addWidget(self.frame_3)
        spacerItem2 = QtWidgets.QSpacerItem(13, 345, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.label_9 = QtWidgets.QLabel(self.central_w)
        self.label_9.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.label_9.setLineWidth(-10)
        self.label_9.setMidLineWidth(-10)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_4.addWidget(self.label_9)
        spacerItem3 = QtWidgets.QSpacerItem(13, 345, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.frame_4 = QtWidgets.QFrame(self.central_w)
        self.frame_4.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_4.setLineWidth(2)
        self.frame_4.setMidLineWidth(1)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setContentsMargins(18, 9, 14, -1)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_6 = QtWidgets.QFrame(self.frame_4)
        self.frame_6.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
        self.frame_6.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_8 = QtWidgets.QLabel(self.frame_6)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_3.addWidget(self.label_8, 0, QtCore.Qt.AlignHCenter)
        self.team_name = QtWidgets.QLabel(self.frame_6)
        self.team_name.setStyleSheet("color: rgb(85, 170, 255);")
        self.team_name.setObjectName("team_name")
        self.horizontalLayout_3.addWidget(self.team_name)
        
        self.verticalLayout_2.addWidget(self.frame_6) #select_players
        self.sel_player = QtWidgets.QListWidget(self.frame_4)
        self.sel_player.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.sel_player.setObjectName("sel_player")
        self.verticalLayout_2.addWidget(self.sel_player)
        self.horizontalLayout_4.addWidget(self.frame_4)
        spacerItem4 = QtWidgets.QSpacerItem(13, 345, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        MainWindow.setCentralWidget(self.central_w)

        
        self.menubar = QtWidgets.QMenuBar(MainWindow) #Menubar
        self.menubar.setGeometry(QtCore.QRect(0, 0, 556, 21))
        self.menubar.setObjectName("menubar")
        
        
        self.menuManage_Teams = QtWidgets.QMenu(self.menubar)
        self.menuManage_Teams.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.menuManage_Teams.setStyleSheet("color: rgb(0, 170, 255);")
        self.menuManage_Teams.setStyleSheet("background-color: rgb(232, 232, 232);")
        self.menuManage_Teams.setStyleSheet("selection-background-color: rgb(0, 170, 255);\n""\n""")
        self.menuManage_Teams.setObjectName("menuManage_Teams")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.new_t = QtWidgets.QAction(MainWindow)#new window
        self.new_t.setIconText("NEW Team")
        self.new_t.setShortcut("Ctrl+N")
        self.new_t.setShortcutContext(QtCore.Qt.WindowShortcut)
        self.new_t.setVisible(True)
        self.new_t.setShortcutVisibleInContextMenu(True)
        self.new_t.setObjectName("new_t")
        
        self.open_t = QtWidgets.QAction(MainWindow)#open team
        self.open_t.setObjectName("open_t")
        
        self.save_t = QtWidgets.QAction(MainWindow)#save team
        self.save_t.setObjectName("save_t")
        
        self.evaluate_t = QtWidgets.QAction(MainWindow)#EVALUATETEAM
        self.evaluate_t.setObjectName("evaluate_t")
        
        self.actionQuit = QtWidgets.QAction(MainWindow)# Quitwindow
        self.actionQuit.setObjectName("actionQuit") 
        self.actionQuit.triggered.connect(self.quit)
        
        self.menuManage_Teams.addAction(self.new_t)
        self.menuManage_Teams.addAction(self.open_t)
        self.menuManage_Teams.addAction(self.save_t)
        self.menuManage_Teams.addAction(self.evaluate_t)
        self.menuManage_Teams.addAction(self.actionQuit)
        self.menubar.addAction(self.menuManage_Teams.menuAction())

        #Action triggered
        self.new_t.triggered.connect(self.file_new)
        self.open_t.triggered.connect(self.file_open)
        self.save_t.triggered.connect(self.file_save)
        self.evaluate_t.triggered.connect(self.file_evaluate)
        self.actionQuit.triggered.connect(self.quit)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        # DOUBLE CLICK
        self.av_player.itemDoubleClicked.connect(self.removelist1)
        self.sel_player.itemDoubleClicked.connect(self.removelist2)

        # -----stats of player
        self.stats = {}

        self.new_screen.savename.clicked.connect(self.namechange)

        # RADIOBUTTONS  CLICK
        self.bat_rb.clicked.connect(self.load_names)
        self.wk_rb.clicked.connect(self.load_names)
        self.bow_rb.clicked.connect(self.load_names)
        self.ar_rb.clicked.connect(self.load_names)
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.BAT.setText(_translate("MainWindow", "##"))
        self.label_2.setText(_translate("MainWindow", "Batsman (BAT)"))
        self.WK.setText(_translate("MainWindow", "##"))
        self.label_4.setText(_translate("MainWindow", "Bowlers (BOW)"))
        self.label_10.setText(_translate("MainWindow", "AllRounders (AR) "))
        self.ARL.setText(_translate("MainWindow", "##"))
        self.BOWL.setText(_translate("MainWindow", "##"))
        self.label_12.setText(_translate("MainWindow", "Wicket-Keeper (WK)"))
        self.label.setText(_translate("MainWindow", "Your Selection"))
        self.label_6.setText(_translate("MainWindow", "Points Availables"))
        self.points_available.setText(_translate("MainWindow", "####"))
        self.label_7.setText(_translate("MainWindow", "Points Used"))
        self.points_used.setText(_translate("MainWindow", "####"))
        self.bat_rb.setText(_translate("MainWindow", "BAT"))
        self.bow_rb.setText(_translate("MainWindow", "BOW"))
        self.ar_rb.setText(_translate("MainWindow", "AR"))
        self.wk_rb.setText(_translate("MainWindow", "WK"))
        self.label_9.setText(_translate("MainWindow", ">"))
        self.label_8.setText(_translate("MainWindow", "Team Name  :"))
        self.team_name.setText(_translate("MainWindow", "Displayed Here"))
        self.menuManage_Teams.setTitle(_translate("MainWindow", "Manage Teams"))
        self.new_t.setText(_translate("MainWindow", "NEW Team"))
        self.new_t.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.open_t.setText(_translate("MainWindow", "OPEN Team"))
        self.open_t.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.save_t.setText(_translate("MainWindow", "SAVE Team"))
        self.save_t.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.evaluate_t.setText(_translate("MainWindow", "EVALUATE Team"))
        self.evaluate_t.setShortcut(_translate("MainWindow", "Ctrl+E"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
     # NEW FILE MENU
    def file_new(self):
        self.newDialog.show()

    def namechange(self):
        teamname = self.new_screen.team_name.text()
        fantcurs.execute("SELECT DISTINCT Name FROM Teams")
        l = fantcurs.fetchall()
        for i in l:
            if i[0] == teamname:
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText("Team with same name already exists!!\nPlease choose Another Name")
                msg.setWindowTitle("Invalid Team Name")
                msg.exec_()
                return 0
        if len(teamname) == 0:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("You cannot leave the field blank!!!")
            msg.setWindowTitle("Invalid Team Name")
            msg.exec_()
            return 0
        elif teamname.isnumeric():
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("Please enter a valid teamname\n(Name must contain atleast one character)!!")
            msg.setWindowTitle("Invalid Team Name")
            msg.exec_()
            return 0
        else:
            self.reset()
            self.tname = self.new_screen.team_name.text()
            self.team_name.setText(str('    '+self.tname))
            self.newDialog.close()

    #TO RESET ALL COUNTS AND LITS
    def reset(self):
        self.enablebuttons()
        self.load_names()
        self.used_points = 0
        self.alrdscount = 0
        self.wicketerscount = 0
        self.batsmencount = 0
        self.bowlerscount = 0
        self.totalcount = 0
        self.avail_points = 1000
        self.points_available.setText(str(self.avail_points))
        self.points_used.setText(str(self.used_points))
        self.BOWL.setText(str(self.bowlerscount))
        self.BAT.setText(str(self.batsmencount))
        self.ARL.setText(str(self.alrdscount))
        self.WK.setText(str(self.wicketerscount))
        self.list1.clear()
        self.load_names()

        self.sel_player.clear()


        #SAVE TEAM MENU
    def file_save(self):
        if not self.error():  #IF THERE IS AN ERROR
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setInformativeText('Insufficient Players or Points!!')
            msg.setWindowTitle("Fantasy Cricket")
            msg.exec_()
        elif self.error():  # IF NO ERROR
            try:
                fantcurs.execute("SELECT DISTINCT Name FROM Teams;")
                x = fantcurs.fetchall()
                for i in x:
                    if self.team_name.text() == i[0]:   # CHECKING IF THE TEAMNAME ALREADY EXISTS
                        print('Data already Exists')
                        fantcurs.execute("DELETE  FROM Teams WHERE Name='" + self.team_name.text() + "';") #DELETING TO UPDATE TEAM
            except:
                print('error')
            for i in range(self.sel_player.count()):
                # print('----addding--')
                # print('teamnane: ',self.team_name.text())
                # print('playername: ',self.list1[i])
                # print('points: ', player_points[self.list1[i]])
                try:
                    fantcurs.execute("INSERT INTO Teams (Name,Players,Value) VALUES (?,?,?)",
                                     (self.team_name.text(), self.list1[i], player_points[self.list1[i]]))

                    # self.file_evaluate()
                except:
                    print('Error in Operation!')
            fant.commit()
        else:
            print('---Error in Operation')


    # QUITING METHOD
    def quit(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setInformativeText('Thank you')
        msg.setWindowTitle("Fantasy Cricket")
        msg.exec_()
        # print('exit')
        sys.exit()

   #ON RADIOBUTTONS CLICKED
    def load_names(self):
        Batsman = 'BAT'
        WicketKeeper = 'WK'
        Allrounder = 'AR'
        Bowler = 'BWL'
        sql1 = "SELECT Player,Value from Stats WHERE ctg = '" + Batsman + "';"
        sql2 = "SELECT Player,Value from Stats WHERE ctg = '" + WicketKeeper + "';"
        sql3 = "SELECT Player,Value from Stats WHERE ctg ='" + Allrounder + "';"
        sql4 = "SELECT Player,Value from Stats WHERE ctg = '" + Bowler + "';"

        fantcurs.execute(sql1)
        x = fantcurs.fetchall()
        fantcurs.execute(sql4)
        y = fantcurs.fetchall()
        fantcurs.execute(sql3)
        z = fantcurs.fetchall()
        fantcurs.execute(sql2)
        w = fantcurs.fetchall()

        batsmen = []
        bowlers = []
        allrounders = []
        wcktkeepers = []

        for k in x:
            batsmen.append(k[0])
            self.b.append(k[0])
            self.stats[k[0]] = k[1]
        for k in y:
            bowlers.append(k[0])
            self.stats[k[0]] = k[1]
            self.a.append(k[0])
        for k in w:
            wcktkeepers.append(k[0])
            self.stats[k[0]] = k[1]
            self.d.append(k[0])
        for k in z:
            allrounders.append(k[0])
            self.stats[k[0]] = k[1]
            self.c.append(k[0])
        for i in self.list1:
            if i in allrounders:
                allrounders.remove(i)
            elif i in batsmen:
                batsmen.remove(i)
            elif i in bowlers:
                bowlers.remove(i)
            elif i in wcktkeepers:
                wcktkeepers.remove(i)

        if self.bat_rb.isChecked() == True:
            self.av_player.clear()
            for i in range(len(batsmen)):
                item = QtWidgets.QListWidgetItem(batsmen[i])
                font = QtGui.QFont()
                font.setBold(True)
                font.setWeight(75)
                item.setFont(font)
                self.av_player.addItem(item)
        elif self.bow_rb.isChecked() == True:
            self.av_player.clear()
            for i in range(len(bowlers)):
                item = QtWidgets.QListWidgetItem(bowlers[i])
                font = QtGui.QFont()
                font.setBold(True)
                font.setWeight(75)
                item.setFont(font)
                self.av_player.addItem(item)
        elif self.ar_rb.isChecked() == True:
            self.av_player.clear()
            for i in range(len(allrounders)):
                item = QtWidgets.QListWidgetItem(allrounders[i])
                font = QtGui.QFont()
                font.setBold(True)
                font.setWeight(75)
                item.setFont(font)
                self.av_player.addItem(item)

        elif self.wk_rb.isChecked() == True:
            self.av_player.clear()
            for i in range(len(wcktkeepers)):
                item = QtWidgets.QListWidgetItem(wcktkeepers[i])
                font = QtGui.QFont()
                font.setBold(True)
                font.setWeight(75)
                item.setFont(font)
                self.av_player.addItem(item)

    def removelist1(self, item):   # REMOVE FROM AVAILABLE PLAYERS AND ADD TO SELECTED PLAYERS
        self.conditions_1(item.text())
        self.av_player.takeItem(self.av_player.row(item))
        self.sel_player.addItem(item.text())
        self.totalcount = self.sel_player.count()
        self.list1.append(item.text())
        self.error()

    def conditions_1(self, cat):   # Adding and Deducting respective points from points_calculator.py
        self.avail_points -= self.stats[cat]
        self.used_points += self.stats[cat]
        if cat in self.a:
            self.bowlerscount += 1
        elif cat in self.d:
            self.wicketerscount += 1
        elif cat in self.c:
            self.alrdscount += 1
        elif cat in self.b:
            self.batsmencount += 1

        self.points_available.setText(str(self.avail_points))
        self.points_used.setText(str(self.used_points))
        self.BOWL.setText(str(self.bowlerscount))
        self.BAT.setText(str(self.batsmencount))
        self.ARL.setText(str(self.alrdscount))
        self.WK.setText(str(self.wicketerscount))

    def conditions_2(self, cat):   # Adding and Deducting respective poinrs from points_calculator.py
        self.avail_points += self.stats[cat]
        self.used_points -= self.stats[cat]
        if cat in self.a:
            self.bowlerscount -= 1
        elif cat in self.d:
            self.wicketerscount -= 1
        elif cat in self.c:
            self.alrdscount -= 1
        elif cat in self.b:
            self.batsmencount -= 1

        self.points_available.setText(str(self.avail_points))
        self.points_used.setText(str(self.used_points))
        self.BOWL.setText(str(self.bowlerscount))
        self.BAT.setText(str(self.batsmencount))
        self.ARL.setText(str(self.alrdscount))
        self.WK.setText(str(self.wicketerscount))

    def removelist2(self, item):   # REMOVE FROM SELECTED PLAYERS AND ADD TO AVAIALBLE PLAYERS
        self.sel_player.takeItem(self.sel_player.row(item))
        self.av_player.addItem(item.text())
        self.list1.remove(item.text())
        # self.error()
        self.totalcount = self.sel_player.count()
        self.conditions_2(item.text())

    def openteam(self):  #upon open team selected
        self.reset()
        teamname = self.open_screen.open_cb.currentText()
        self.team_name.setText(teamname)
        self.enablebuttons()
        fantcurs.execute("SELECT Players from Teams WHERE Name= '" + teamname + "';")
        x=fantcurs.fetchall()
        score=[]
        for i in x:
            fantcurs.execute("SELECT Value from Stats WHERE Player='"+i[0]+"';")
            y=fantcurs.fetchone()
            score.append(y[0])
        # print(score)
        sum=0
        for i in score:
            sum+=i
        self.sel_player.clear()
        self.load_names()
        for i in x:
            self.sel_player.addItem(i[0])
            self.list1.append(i[0])
            self.conditions_1(i[0])
        self.used_points = sum
        self.avail_points = 1000 - sum
        self.points_available.setText(str(self.avail_points))
        self.points_used.setText(str(self.used_points))
        self.openDialog.close()

    def enablebuttons(self):
        self.bat_rb.setEnabled(True)
        self.bow_rb.setEnabled(True)
        self.ar_rb.setEnabled(True)
        self.wk_rb.setEnabled(True)
        
    def disablebuttons(self):
        self.bat_rb.setEnabled(False)
        self.bow_rb.setEnabled(False)
        self.ar_rb.setEnabled(False)
        self.wk_rb.setEnabled(False)
        

    def error(self):
        msg = QMessageBox()
        if self.wicketerscount > 1:
            msg.setIcon(QMessageBox.Critical)
            # msg.setText("Error")
            msg.setInformativeText('Only 1 Wicket-Keeper is allowed!')
            msg.setWindowTitle("Error")
            msg.exec_()
            return 0
        elif self.totalcount > 11:
            msg.setIcon(QMessageBox.Critical)
            msg.setInformativeText('More than 11 players not allowed!')
            msg.setWindowTitle("Selection Error")
            msg.exec_()
            return 0
        elif self.totalcount < 11 :
            return 0
        elif self.wicketerscount < 1:
            return 0
        elif self.avail_points <= -1:
            msg.setIcon(QMessageBox.Critical)
            msg.setInformativeText('Not enough Points, Please Reselect!')
            msg.setWindowTitle("Selection Cricket")
            msg.exec_()
            return 0

        return 1



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
