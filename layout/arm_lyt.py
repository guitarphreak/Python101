import maya.cmds as mc

result = mc.promptDialog(title='Create Locators', text='1', message='Enter the Number of Locators:', button=['OK', 'Cancel'], defaultButton='OK', cancelButton='Cancel', dismissString='Cancel')

if result=='OK':
    numLocators = int(mc.promptDialog(query=True, text=True))
    i = 0
    while (i<numLocators):
        i += 1
        mc.spaceLocator(p=(0,0,0), n='locatorDelDemonio%d' %i)
        
else:
    print 'Script cancelled by user'
    return

if int(numLocators = int(mc.promptDialog(query=True, text=True)))<1:
    print 'Is not possible to create less than one locator!'
    return