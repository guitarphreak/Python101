import maya.cmds as cmds
 
cmds.upAxis( axis='y', rotateView=True )
cmds.currentUnit( linear='cm' )
cmds.currentUnit( time='ntsc' )
 
def createMenu(*args):
    mi = cmds.window('MayaWindow', menuArray=True, query=True)
    for m in mi:
        if m == 'RDojo_Menu':
            cmds.deleteUI('RDojo_Menu', menu=True)
 
    cmds.menu('RDojo_Menu', label='RDMenu', tearOff=True, parent='MayaWindow')
 
createMenu()