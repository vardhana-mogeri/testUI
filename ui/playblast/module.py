import maya.cmds as cmds

def getSelectCam():
    list_selected = cmds.ls(sl=True,type='camera',r=True,dag=True,long=True)
    selected_cam = cmds.listRelatives(list_selected,p=True,fullPath=True)
    return selected_cam