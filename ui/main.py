try:
    from PySide import QtGui as QtWidgets
    from PySide import QtCore
    
except:
    from PySide2 import QtWidgets,QtCore,QtGui

import maya.OpenMayaUI as omui
import shiboken
from ui.playblast import module
from core import publish

mayaWindowPtr = omui.MQtUtil.mainWindow()
mayaWindow = shiboken.wrapInstance(long(mayaWindowPtr),QtWidgets.QWidget)

class UI(QtWidgets.QWidget):

    def __init__(self):
        QtWidgets.QWidget.__init__(self,mayaWindow)
        
        self.setWindowTitle('Publish Camera')
        
        self.setParent(mayaWindow)
        self.setWindowFlags(QtCore.Qt.Window)
        
        #asset name
        label_name=QtWidgets.QLabel("name")
        self.asset_name=QtWidgets.QLineEdit()
        
        #asset_type
        label_pos=QtWidgets.QLabel("asset_type")
        self.asset_type=QtWidgets.QLineEdit()

        asset_layout = QtWidgets.QHBoxLayout()
        asset_layout.addWidget(self.edit_name)
        asset_layout.addWidget(self.edit_type)

        self.publish_button = QtWidgets.QPushButton("publish")
        self.publish_button.clicked.connect(self.publish)

    def publish(self):

        modeule_options = module.getSelectCam()

        #existing
        publish.publish(
            modeule_options,
            asset_name=self.asset_name.text(),
            asset_type=self.asset_type()
            )

        #should be 
        publish.publish(asset_name=self.asset_name.text(),
            asset_type=self.asset_type()
            )


        
