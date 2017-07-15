import c4d

#script to select first and last point of selected splines

def main():

    doc = c4d.documents.GetActiveDocument() #set context (this document)
    selo = doc.GetActiveObjects(0) #selo is now an array of the currently selected objects in the object manager
    
    if len(selo) > 0: #if we have one or more selected objects in the scene, proceed:
        
        for o in selo: #loop through selected objects
    
                select_points = o.GetPointS() #create a BaseSelect "object" (get a selection going)
                
                pc = len(o.GetAllPoints()) #how many points are there? (get all the points, get the length of the array)

                select_points.Select(0) #add point index 0 to the selection
                
                select_points.Select(pc-1) #add the last point to the selection (-1 )
        

c4d.EventAdd()
    
if __name__ == "__main__":
    main()
