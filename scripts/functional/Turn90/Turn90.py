import c4d

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

  obj=doc.GetActiveObject()
  
  if obj is None:
        pass
		
  if checkPressed(ord('1')):
    rotat(obj, "x")
	
  elif checkPressed(ord('2')):
    rotat(obj, "y")
	
  elif checkPressed(ord('3')):
    rotat(obj, "z")
    
  c4d.EventAdd()
  
if __name__=='__main__':
  main()
