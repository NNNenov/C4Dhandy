#check if the mouse coordinates are in the viewport, and if so, what object(s) are at the x/y location / range
#relevant reading:
# https://developers.maxon.net/docs/Cinema4DPythonSDK/html/modules/c4d.utils/ViewportSelect/index.html#ViewportSelect.PickObject
# https://developers.maxon.net/docs/Cinema4DPythonSDK/html/modules/c4d.gui/EditorWindow/index.html?highlight=screen2local#EditorWindow.Local2Screen

import c4d
from c4d import gui, utils
#Welcome to the world of Python

state = c4d.BaseContainer()


bd = doc.GetActiveBaseDraw()
win = bd.GetEditorWindow()

frame = bd.GetFrame()
left = frame["cl"]
right = frame["cr"]
top = frame["ct"]
bottom = frame["cb"]

width = right - left + 1
height = bottom - top +1

ViewportSelect = utils.ViewportSelect()


def main():
    while gui.GetInputState(c4d.BFM_INPUT_MOUSE, c4d.BFM_INPUT_MOUSELEFT, state):
        if state.GetInt32(c4d.BFM_INPUT_VALUE)==0:
            break

    ix = state.GetInt32(c4d.BFM_INPUT_X)
    iy = state.GetInt32(c4d.BFM_INPUT_Y)
    
    gx, gy = win.Global2Local()
    print(" win.Global2Local() %s , %s") % (gx, gy)
    print(" MOUSE %s , %s") % (ix, iy)
    print("left %s r %s t %s b %s") % (left, right, top, bottom)
    print("calc %s , %s") % (ix+gx,iy+gy)
    
    x = ix+gx
    y = iy+gy
    
    if (0 <= x <= right and 0 <= y <= bottom):
        print (ViewportSelect.PickObject(bd, doc, x, y, 2, 3) )
    else:
        print "out of bounds"
if __name__=='__main__':
    main()
