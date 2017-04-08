import c4d

op = c4d.documents.GetActiveDocument() #op needs to be relative to mode you are trying to set, e.g:
#    #obj
#    obj = op
#    c4d.gui.ActiveObjectManager_SetObject(c4d.ACTIVEOBJECTMODE_OBJECT, obj, c4d.ACTIVEOBJECTMANAGER_SETOBJECTS_OPEN)
#    
#    #tag
#    tag = op.GetTags()[0]
#    c4d.gui.ActiveObjectManager_SetObject(c4d.ACTIVEOBJECTMODE_TAG, tag, c4d.ACTIVEOBJECTMANAGER_SETOBJECTS_OPEN)
#    
#    #mat
#    mat = doc.GetActiveMaterial()
#    c4d.gui.ActiveObjectManager_SetObject(c4d.ACTIVEOBJECTMODE_MATERIAL, mat, c4d.ACTIVEOBJECTMANAGER_SETOBJECTS_OPEN)
#
#    #shader
#    sha = mat.GetFirstShader()
#    c4d.gui.ActiveObjectManager_SetObject(c4d.ACTIVEOBJECTMODE_SHADER, sha, c4d.ACTIVEOBJECTMANAGER_SETOBJECTS_OPEN)
#    
#    #tool
#    tool = c4d.plugins.FindPlugin(doc.GetAction(), c4d.PLUGINTYPE_TOOL)
#    c4d.gui.ActiveObjectManager_SetObject(c4d.ACTIVEOBJECTMODE_TOOL, tool, c4d.ACTIVEOBJECTMANAGER_SETOBJECTS_OPEN)

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
