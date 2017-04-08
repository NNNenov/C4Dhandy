import c4d

op = c4d.documents.GetActiveDocument() 

def main():
    c4d.gui.ActiveObjectManager_SetObject(c4d.ACTIVEOBJECTMODE_SHADER, op, c4d.ACTIVEOBJECTMANAGER_SETOBJECTS_OPEN)
    
    #ACTIVEOBJECTMODE_OBJECT	Object mode.
    #ACTIVEOBJECTMODE_TAG	Tag mode.
    #ACTIVEOBJECTMODE_MATERIAL	Material mode.
    #ACTIVEOBJECTMODE_SHADER	Shader mode.
    #ACTIVEOBJECTMODE_NODE	Node mode.
    #ACTIVEOBJECTMODE_TIMELINE	Time-line mode.
    #ACTIVEOBJECTMODE_FCURVE	F-curve mode.
    #ACTIVEOBJECTMODE_BITMAPINFO	BodyPaint bitmap info mode.
    #ACTIVEOBJECTMODE_TOOL	Tool mode.
    #ACTIVEOBJECTMODE_VIEW	View mode.
    #ACTIVEOBJECTMODE_INFOTAB	Info tab.
    #ACTIVEOBJECTMODE_CAMERA	Editor camera mode.
    #ACTIVEOBJECTMODE_RENDERDATA	Render data mode.
    #ACTIVEOBJECTMODE_DOCUMENT	Document settings mode.
    #ACTIVEOBJECTMODE_MODELING	Modeling mode.

if __name__=='__main__':
    main()

#thanks to gr4ph0s via http://plugincafe.com/forum/forum_posts.asp?TID=13525
