import maya.cmds as cmds
import sys
import json
import tempfile

def createLocators(*args):
    lctr_dictionary = {}
    my_list = (['lctr_l_arm1',[0.0,0.0,0.0]],['lctr_l_arm2',[1.0,0.0,-1.0]],['lctr_l_wrist',[2.0,0.0,0.0]],['lctr_l_armEnd',[3.0,0.0,1.0]])
    #Check for valid amount of locators (not null).
    #if (cmds.textField('numLocators', query=True, text=True) == ''):
        #print 'No locators created. Please enter the amount of locators required.'
        #return
    #If amount of locators is not null, convert it to a number.
    lctr_dictionary['names'] = [my_list[each][0] for each in range(len(my_list))]
    lctr_dictionary['position'] = [my_list[each][1] for each in range(len(my_list))]
    varLocators = 4#int(cmds.textField('numLocators', query=True, text=True))
    sel = cmds.radioButtonGrp('radioGroup', query=True, select=True)
    #Check for valid x,y,z tuple.        
    xPos = 0.0#cmds.textField('xValue', query=True, text=True)
    yPos = 0.0#cmds.textField('yValue', query=True, text=True)
    zPos = 0.0#cmds.textField('zValue', query=True, text=True)
    #print sel
    #Check if positioning Linear is selected.
    if sel == 1:
        #print 'linear'
        for i in range(0, varLocators):
            cmds.spaceLocator(position=(lctr_dictionary['position'][i][0], lctr_dictionary['position'][i][1], lctr_dictionary['position'][i][2]), name='lctr_%d' %(i+1))
            i += 1
        return lctr_dictionary
    #Check if positioning Relative is selected.            
    elif sel == 2:
        #print 'relative'
        for i in range(0, varLocators):
            cmds.spaceLocator(position=(lctr_dictionary['position'][i][0], lctr_dictionary['position'][i][1], lctr_dictionary['position'][i][2]), relative=True, name='lctr_%d' %(i+1))
            i += 1
        return lctr_dictionary
    #Check if positioning Absolute is selected.
    elif sel == 3:
        #print 'absolute'
        for i in range(0, varLocators):
            cmds.spaceLocator(position=(lctr_dictionary['position'][i][0], lctr_dictionary['position'][i][1], lctr_dictionary['position'][i][2]), absolute=True, name='lctr_%d' %(i+1))
            i += 1
        return lctr_dictionary
    #Check for a valid positioning method.
    elif sel == 0:
        print 'Please choose one of the positioning methods'
        return 0

#Save Json method
def saveJsonFile(*args):
    #Check to see if there is any data to save
    if data == 0:
        print 'Dictionary is empty'
        return
    else:
        fileName = 'C:/Users/andres/Documents/GitHub/Python101/data/locator_info.json'
        with open(fileName, 'w') as outfile:
            json.dump(data, outfile)

        file.close(outfile)
        print 'json created'
        return

#Load Json file method
def loadJsonFile():
    
    fileName = 'C:/Users/andres/Documents/GitHub/Python101/data/locator_info.json'
    #Check to see if the file exists
    try:
        with open(fileName, 'r') as infile:
            data2=(open(infile.name, 'r').read())
            info = json.loads(data2)
            return info
    except IOError:
        print 'File does not exist'
        return 0

#Deletes the window upon pressing the Cancel button.
def deleteWindow(*args):
    cmds.deleteUI('locatorUI')

#If the UI window already exists delete it to create a new one.
if cmds.window('locatorUI', exists=True):
	cmds.deleteUI('locatorUI')

data = 0	
window = cmds.window('locatorUI', title = 'Locator Creator', width=240, height=300, mnb=False, mxb=False, sizeable=False)
#General layout for the window
mainLayout = cmds.columnLayout(rowSpacing=10, columnWidth=240, columnAlign='center')
cmds.separator(width=245, height=20, parent = mainLayout)

#Enter the number of locators needed
#scndLayout = cmds.rowLayout(numberOfColumns=2, columnWidth2=(100,60), parent = mainLayout)
#cmds.text(label='Number of Locators:', parent = scndLayout)
#cmds.textField('numLocators', width=40, height=20, parent = scndLayout)

#Enter the desired positioning of the locators
thirdLayout = cmds.rowLayout(numberOfColumns=3, columnWidth3=(45,80,80), parent = mainLayout)
cmds.text(label='Position:', parent = thirdLayout)
cmds.radioButtonGrp('radioGroup', numberOfRadioButtons=3, columnWidth3=(50,65,40), labelArray3=['Linear','Relative','Absolute'], parent = thirdLayout)

#Enter the x,y,z coordinates to create the locators
#fourthLayout = cmds.rowLayout(numberOfColumns=6, columnWidth6=(20,40,20,40,20,40), parent = mainLayout)
#cmds.text(label='X', align='right', parent = fourthLayout)
#cmds.textField('xValue', width=30, height=20, parent = fourthLayout, text='0')
#cmds.text(label='Y', align='right', parent = fourthLayout)
#cmds.textField('yValue', width=30, height=20, parent = fourthLayout, text='0')
#cmds.text(label='Z', align='right', parent = fourthLayout)
#cmds.textField('zValue', width=30, height=20, parent = fourthLayout, text='0')

#Create/Cancel buttons
fifthLayout = cmds.rowLayout(numberOfColumns=4, columnWidth4=(56,56,56,56), columnAlign4=('center','center','center','center'), parent = mainLayout)
cmds.button(label='Create', width=60, command="data=createLocators()", parent = fifthLayout)
cmds.button(label='Save Json', width=60, command="saveJsonFile(data)", parent = fifthLayout)
cmds.button(label='Load Json', width=60, command="data=loadJsonFile()", parent = fifthLayout)
cmds.button(label='Cancel', width=60, parent = fifthLayout, command=deleteWindow)
cmds.separator(width=245, height=15, parent = mainLayout)
cmds.showWindow(window)