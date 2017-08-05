import c4d

#This script allows you to quickly and easily rotate the currently selected object(s(local axis)) in 90 degree steps, 
#by holding 1, 2 or 3 (X,Y,Z axis) then pressing the assigned hotkey.

#Reccomend use as a hotkey for workflow efficiency.

#For example, lets assume the script shortcut is mapped to the ` key
#to rotate 90 degrees along the X axis, hold down 1 then press `
#you can pick your own modifier keys to use instead of 1,2,3 by modifying the code, check the code below in def Main()

def checkPressed(k):
    # Check any one key
    bc = c4d.BaseContainer()
    if c4d.gui.GetInputState(c4d.BFM_INPUT_KEYBOARD, k ,bc):
        if bc[c4d.BFM_INPUT_VALUE] == 1:
            return True
        else:
            return False

def rotat(obj, r):
    
    newMatrix = obj.GetMl()
    
    doc.StartUndo()
    doc.AddUndo(c4d.UNDOTYPE_HIERARCHY_PSR, obj)
    
    if r is "x":
        newMatrix *= c4d.utils.MatrixRotX(c4d.utils.Rad(90)) 
    elif r is "y":
        newMatrix *= c4d.utils.MatrixRotY(c4d.utils.Rad(90)) 
    elif r is "z":
        newMatrix *= c4d.utils.MatrixRotZ(c4d.utils.Rad(90)) 
        
    obj.SetMl(newMatrix)
        
    doc.EndUndo()

def main():

  #obj = doc.GetActiveObject()
  objs = doc.GetActiveObjects(0)
  
  if len(objs) == 0:
        pass

  for obj in objs:
      if checkPressed(ord('1')):
        rotat(obj, "x")
    	
      elif checkPressed(ord('2')):
        rotat(obj, "y")
    	
      elif checkPressed(ord('3')):
        rotat(obj, "z")
    
  c4d.EventAdd()
  
if __name__=='__main__':
  main()
