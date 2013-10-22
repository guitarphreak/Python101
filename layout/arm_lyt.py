import maya.cmds as mc

result = mc.promptDialog(title='Create Locators', text='1', message='Enter the Number of Locators:', button=['OK', 'Cancel'], defaultButton='OK', cancelButton='Cancel', dismissString='Cancel')

if result=='OK':
    numLocators = int(mc.promptDialog(query=True, text=True))
    i = 0
    while (i<numLocators):
        i += 1
        mc.spaceLocator(position=(0,0,0), name='locatorDelDemonio%d' %i)
        
else:
    print 'Script cancelled by user'

if int(mc.promptDialog(query=True, text=True))<1:
    print 'Is not possible to create less than one locator!'