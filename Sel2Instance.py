import c4d

def main():
    doc = c4d.documents.GetActiveDocument() 
    selected = doc.GetActiveObjects(0)
    
    if len(selected) > 0: 
        for ob in reversed(selected):
            op = c4d.BaseObject(c4d.Oinstance)
            op[c4d.INSTANCEOBJECT_LINK] = ob
            op.InsertBefore(doc.GetFirstObject())
            op.SetName("%s instance" % ob.GetName()) #change the name of the new instance to the name of the original object + " instance"
            
            print "made %s instance" % ob.GetName() 
            
    c4d.EventAdd() 
    
if __name__ == "__main__":
    main()
