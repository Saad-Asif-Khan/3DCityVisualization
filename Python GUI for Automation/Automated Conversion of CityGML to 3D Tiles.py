"""
******************************************************
****Python GUI for Automation of 3D model creation****
****             2018-19                          ****
******************************************************

@ This code contains Python GUI that can be used for 
automatic conversion of CityGML models to Cesium 3D Tiles.
"""

from PyQt5 import QtCore, QtGui, QtWidgets
import os, sys, csv
import urllib3
from bs4 import BeautifulSoup as BS

class Ui_Dialog(QtWidgets.QMainWindow):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(978, 370)
        
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(360, 18, 143, 24))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(380, 58, 20, 291))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(120, 58, 806, 24))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.radio_download = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(9)
        self.radio_download.setFont(font)
        self.radio_download.setObjectName("radio_download")
        self.horizontalLayout_7.addWidget(self.radio_download)
        spacerItem = QtWidgets.QSpacerItem(400, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem)
        self.radio_ = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(9)
        self.radio_.setFont(font)
        self.radio_.setObjectName("radio_")
        self.horizontalLayout_7.addWidget(self.radio_)
        self.layoutWidget1 = QtWidgets.QWidget(Dialog)
        self.layoutWidget1.setGeometry(QtCore.QRect(400, 110, 561, 239))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.srcText = QtWidgets.QLineEdit(self.layoutWidget1)
        self.srcText.setMaximumSize(QtCore.QSize(410, 25))
        self.srcText.setObjectName("srcText")
        self.horizontalLayout_2.addWidget(self.srcText)
        self.srcData = QtWidgets.QPushButton(self.layoutWidget1)
        self.srcData.setEnabled(True)
        self.srcData.setMaximumSize(QtCore.QSize(40, 25))
        font = QtGui.QFont()
        font.setFamily("Serif")
        self.srcData.setFont(font)
        self.srcData.setObjectName("srcData")
        self.horizontalLayout_2.addWidget(self.srcData)
        self.gridLayout_3.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.convert = QtWidgets.QPushButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(9)
        self.convert.setFont(font)
        self.convert.setObjectName("convert")
        self.horizontalLayout_4.addWidget(self.convert)
        self.cancel = QtWidgets.QPushButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(9)
        self.cancel.setFont(font)
        self.cancel.setObjectName("cancel")
        self.horizontalLayout_4.addWidget(self.cancel)
        self.gridLayout_3.addLayout(self.horizontalLayout_4, 4, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        spacerItem3 = QtWidgets.QSpacerItem(35, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.DestText = QtWidgets.QLineEdit(self.layoutWidget1)
        self.DestText.setMaximumSize(QtCore.QSize(410, 25))
        self.DestText.setObjectName("DestText")
        self.horizontalLayout_3.addWidget(self.DestText)
        self.destData = QtWidgets.QPushButton(self.layoutWidget1)
        self.destData.setEnabled(True)
        self.destData.setMaximumSize(QtCore.QSize(40, 25))
        font = QtGui.QFont()
        font.setFamily("Serif")
        self.destData.setFont(font)
        self.destData.setObjectName("destData")
        self.horizontalLayout_3.addWidget(self.destData)
        self.gridLayout_3.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 0, 2, 1, 1)
        self.skipfactor = QtWidgets.QLineEdit(self.layoutWidget1)
        self.skipfactor.setMaximumSize(QtCore.QSize(410, 25))
        self.skipfactor.setObjectName("skipfactor")
        self.gridLayout_2.addWidget(self.skipfactor, 1, 2, 1, 1)
        self.listoption = QtWidgets.QListWidget(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        self.listoption.setFont(font)
        self.listoption.setObjectName("listoption")
        item = QtWidgets.QListWidgetItem()
        self.listoption.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listoption.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listoption.addItem(item)
        self.gridLayout_2.addWidget(self.listoption, 0, 0, 3, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 3, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 0, 1, 1, 1)
        self.fmeModel_text = QtWidgets.QLineEdit(self.layoutWidget1)
        self.fmeModel_text.setMaximumSize(QtCore.QSize(410, 25))
        self.fmeModel_text.setObjectName("fmeModel_text")
        self.gridLayout.addWidget(self.fmeModel_text, 0, 2, 1, 1)
        self.fmeModel = QtWidgets.QPushButton(self.layoutWidget1)
        self.fmeModel.setEnabled(True)
        self.fmeModel.setMaximumSize(QtCore.QSize(40, 25))
        font = QtGui.QFont()
        font.setFamily("Serif")
        self.fmeModel.setFont(font)
        self.fmeModel.setObjectName("fmeModel")
        self.gridLayout.addWidget(self.fmeModel, 0, 3, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(12, 111, 371, 241))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_6 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(9)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_5.addWidget(self.label_6)
        self.download_folder = QtWidgets.QLineEdit(self.widget)
        self.download_folder.setMaximumSize(QtCore.QSize(207, 25))
        self.download_folder.setObjectName("download_folder")
        self.horizontalLayout_5.addWidget(self.download_folder)
        self.browsedownload = QtWidgets.QPushButton(self.widget)
        self.browsedownload.setMaximumSize(QtCore.QSize(40, 25))
        self.browsedownload.setObjectName("browsedownload")
        self.horizontalLayout_5.addWidget(self.browsedownload)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_7 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(9)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_8.addWidget(self.label_7)
        self.download_folder_2 = QtWidgets.QLineEdit(self.widget)
        self.download_folder_2.setMaximumSize(QtCore.QSize(410, 25))
        self.download_folder_2.setObjectName("download_folder_2")
        self.horizontalLayout_8.addWidget(self.download_folder_2)
        self.browsedownload_2 = QtWidgets.QPushButton(self.widget)
        self.browsedownload_2.setMaximumSize(QtCore.QSize(40, 25))
        self.browsedownload_2.setObjectName("browsedownload_2")
        self.horizontalLayout_8.addWidget(self.browsedownload_2)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.textBrowser = QtWidgets.QTextBrowser(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy)
        self.textBrowser.setMinimumSize(QtCore.QSize(300, 120))
        self.textBrowser.setMaximumSize(QtCore.QSize(500, 120))
        self.textBrowser.setMouseTracking(False)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem5)
        self.download = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(9)
        self.download.setFont(font)
        self.download.setObjectName("download")
        self.horizontalLayout_6.addWidget(self.download)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.textBrowser.raise_()
        self.layoutWidget.raise_()
        self.layoutWidget.raise_()
        self.layoutWidget.raise_()
        self.label_4.raise_()
        self.line.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.fmeModel, self.radio_download)
        Dialog.setTabOrder(self.radio_download, self.browsedownload)
        Dialog.setTabOrder(self.browsedownload, self.destData)
        Dialog.setTabOrder(self.destData, self.srcData)
        Dialog.setTabOrder(self.srcData, self.radio_)
        Dialog.setTabOrder(self.radio_, self.cancel)

        ## choose download and conversion option
        self.radio_.setChecked(True)
        self.radio_download.toggled.connect(lambda:self.btnstate(self.radio_download))
        self.radio_.toggled.connect(lambda:self.btnstate(self.radio_))   

        ## Here call different buttons
        self.fmeModel.clicked.connect(self.fmebrowse)
        self.srcData.clicked.connect(self.srcbrowse)
        self.destData.clicked.connect(self.destbrowse)
        self.browsedownload_2.clicked.connect(self.downloadbrowse)
        self.browsedownload.clicked.connect(self.download_htm_browse)
        self.download.clicked.connect(self.download_button)
        self.convert.clicked.connect(self.get3Dtiles)
        
        

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Conversion Tool CityGML to 3D Tiles"))
        self.label_4.setText(_translate("Dialog", "Conversion Tool"))
        self.radio_download.setText(_translate("Dialog", "Download"))
        self.radio_.setText(_translate("Dialog", "Conversion"))
        self.label_2.setText(_translate("Dialog", "Source Data:"))
        self.srcData.setText(_translate("Dialog", "..."))
        self.convert.setText(_translate("Dialog", "Convert"))
        self.cancel.setText(_translate("Dialog", "Cancel"))
        self.label_3.setText(_translate("Dialog", "Dest Data:"))
        self.destData.setText(_translate("Dialog", "..."))
        self.label_5.setText(_translate("Dialog", "Enter Skip Factor:"))
        self.listoption.setToolTip(_translate("Dialog", "<html><head/><body><p><span style=\" color:#00007f;\">right click check what\'s this?</span></p></body></html>"))
        self.listoption.setWhatsThis(_translate("Dialog", "<html><head/><body><p>Select-</p><p>&lt;All&gt; for processing all CityGML\'s individually.</p><p>&lt;States&gt; for processing CityGML\'s State-wise</p><p>&lt;Cluster&gt; for processing in certain number that you specify in Skip factor.</p></body></html>"))
        __sortingEnabled = self.listoption.isSortingEnabled()
        self.listoption.setSortingEnabled(False)
        item = self.listoption.item(0)
        item.setText(_translate("Dialog", "All"))
        item = self.listoption.item(1)
        item.setText(_translate("Dialog", "State"))
        item = self.listoption.item(2)
        item.setText(_translate("Dialog", "Cluster {State-wise}"))
        self.listoption.setSortingEnabled(__sortingEnabled)
        self.label.setText(_translate("Dialog", "FME Model:"))
        self.fmeModel.setText(_translate("Dialog", "..."))
        self.label_6.setText(_translate("Dialog", "Html File(s)"))
        self.browsedownload.setText(_translate("Dialog", "..."))
        self.label_7.setText(_translate("Dialog", "Download Folder"))
        self.browsedownload_2.setText(_translate("Dialog", "..."))
        self.download.setText(_translate("Dialog", "Download"))
    def btnstate(self,b):
        if b.text()=="Download":  
            if b.isChecked()==True:
                self.download_folder.setEnabled(True)
                self.download_folder_2.setEnabled(True)
                self.textBrowser.setEnabled(True)
                self.download.setEnabled(True)
                self.browsedownload.setEnabled(True)
                self.browsedownload_2.setEnabled(True)
               
                
            else:
                self.download_folder.setDisabled(True)
                self.download_folder_2.setDisabled(True)
                self.textBrowser.setDisabled(True)
                self.download.setDisabled(True)
                self.browsedownload.setDisabled(True)
                self.browsedownload_2.setDisabled(True)
                
        if b.text()=="Conversion":
            if b.isChecked() == True:
                self.fmeModel_text.setEnabled(True)
                self.srcText.setEnabled(True)
                self.DestText.setEnabled(True)
                self.fmeModel.setEnabled(True)
                self.srcData.setEnabled(True)
                self.destData.setEnabled(True)
                self.listoption.setEnabled(True)
                self.skipfactor.setEnabled(True)
                self.convert.setEnabled(True)
                self.cancel.setEnabled(True)
                
            else:
                self.fmeModel_text.setDisabled(True)
                self.srcText.setDisabled(True)
                self.DestText.setDisabled(True)
                self.fmeModel.setDisabled(True)
                self.srcData.setDisabled(True)
                self.destData.setDisabled(True)
                self.listoption.setDisabled(True)
                self.skipfactor.setDisabled(True)
                self.convert.setDisabled(True)
                self.cancel.setDisabled(True)
                
    ##****** Conversion Code*********##
    def conversion(self,model,src,dest):
            model = '"'+model.replace("\\","\\\\")+'"'
            print(model)
            print(src)
            print(dest)
            cmd = "fme"+" "+model+" --SourceDataset_CITYGML "+src+" --DestDataset_CESIUM3DTILES "+" "+dest
            print(cmd)
            os.system(cmd)
                        
    def createstring(self,folds,files,new_dest):
        tempsrc =''
        prefix = root_src+"\\"+folds
        for gml in files:
            if(gml[-4:]=='.zip'):
                tempname = prefix+"\\"+gml
                tempsrc=tempsrc+"\" \""+tempname
        src = '"""""'+tempsrc[3:]+'"""""'
        src = src.replace("\\","\\\\")
        src = src.replace('" "','"" ""')
        new_dest = '"'+new_dest.replace("\\","\\\\")+'"'
        self.conversion(fmemodel,src,new_dest)
        
    def skip_factor(self,root_src,n):
        subfolds = os.listdir(root_src)
        for folds in subfolds:
            total_files = os.listdir(root_src+"\\"+folds)
            total_n = len(total_files)
            start=0
            run_len = n
            counter = 0                                                             
            while start<total_n:
                new_dest = root_dest+"\\"+folds+str(counter)
                if not os.path.exists(new_dest):
                        os.mkdir(new_dest)
                if(run_len<=total_n):
                    print("Processing :",(run_len-start)," files.")                      
                    self.createstring(folds,total_files[start:run_len],new_dest)
                if(run_len>total_n):
                    print("Processing: ",(total_n-start)," files")
                    self.createstring(folds,total_files[start:total_n],new_dest)
                start = start+n
                run_len = run_len+n
                counter = counter+1
                
    def runstates(self,root_src,root_dest):
        print("runstates")
        subfolds = os.listdir(root_src)
        counter = 0
        for folds in subfolds:
            new_dest = root_dest+"\\"+folds+str(counter)
            if not os.path.exists(new_dest):
                    os.mkdir(new_dest)
            files = os.listdir(root_src+"\\"+folds)
            self.createstring(folds,files,new_dest)
            counter = counter+1
                    
    def runall(self,root_src,root_dest):
        subfolds = os.listdir(root_src)
        counter=0
        for folds in subfolds:
            files = os.listdir(root_src+"\\"+folds)
            for gml in files:
                new_dest = root_dest+"\\"+folds+gml[-4:]+str(counter)
                if not os.path.exists(new_dest):
                    os.mkdir(new_dest)
                    if (gml[-4:]=='.zip'):
                        file = '""'+root_src+"\\"+folds+"\\"+gml+'""'
                        self.conversion(fmemodel,file,new_dest)
                    counter = counter+1                 
                    print(counter)
                    
      ##*******Conversion code Ends*****##
                    
    def download_htm_browse(self):
        global rootfolder
        rootfolder = QtWidgets.QFileDialog.getExistingDirectory(self,'Select HTML Download Directory')
        self.download_folder.setText(rootfolder)
    def downloadbrowse(self):
        global dir_path1
        dir_path1 = QtWidgets.QFileDialog.getExistingDirectory(self,'Select Download Directory')
        self.download_folder_2.setText(dir_path1)
        
##*********Download Automate*******##
    def download_button(self):
        global filename
        list_folds = os.listdir(rootfolder)
        for filename in list_folds:
            htm_file = rootfolder+"/"+str(filename)
            base_name = filename.split('.')[0]
            dir_path = dir_path1+"\\"+filename.split('.')[0]+"\\"
            if not os.path.exists(dir_path):
                os.mkdir(dir_path)      
            htm = open(htm_file,'r')
            pars = BS(htm,'html.parser')
            ##print(pars.prettify())
            a_tags = pars.find_all('a')
            for links in a_tags:
                self.downloadfunc(links.get('href'),dir_path)
    def downloadfunc(self,url,dir_path):
        ##getting name from url;
        parts_url = str(url).split('/') 
        base_filename = parts_url[(len(parts_url)-1)]
        print(dir_path)
        print(base_filename)
        ##Download only Zip file
        typ = base_filename.split('.')
        file_type = typ[1]
        if(file_type =='zip'):
            ## from here, download of files with base names will be done...
            down_url = url
            http = urllib3.PoolManager()
            web_file = http.request('GET', down_url)
            file_name = dir_path+base_filename
            if not os.path.exists(file_name):
                local_file = open(file_name,'wb')
                local_file.write(web_file.data)
                web_file.close()
                local_file.close()
                a=''
                a +="Downloaded: "+base_filename+" in Folder"+filename
                self.textBrowser.setPlainText('a')
 
    def fmebrowse(self):
        global fmemodel
        fmemodel, _ = QtWidgets.QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", ""," Files (*.fmw);;All Files (*)")
        self.fmeModel_text.setText(fmemodel)
        return fmemodel
    def srcbrowse(self):
        global root_src
        root_src = QtWidgets.QFileDialog.getExistingDirectory(self,'Select Directory')
        self.srcText.setText(root_src)
    def destbrowse(self):
        global root_dest
        root_dest = QtWidgets.QFileDialog.getExistingDirectory(self,'Select Destination Directory')
        self.DestText.setText(root_dest)

    def get3Dtiles(self):
            skip= self.listoption.currentItem().text()
            print("check skip",type(skip))
            if(skip=='All'):
                self.runall(root_src,root_dest)             
            if(skip=="State"):
                self.runstates(root_src,root_dest)
            if(skip=="Cluster {State-wise}"):
                n = int(self.skipfactor.text())
                print("N",n)
                self.skip_factor(root_src,n)
                    

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

