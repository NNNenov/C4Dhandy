import c4d, os, sys
from c4d import documents as docs


if __name__ == '__main__':
    doc = docs.GetActiveDocument()
    docPath = doc.GetDocumentPath() 
    docName = doc.GetDocumentName()
    path = os.sep.join([docPath, docName])


    if sys.platform == "darwin" and path.startswith("/Volumes/"): #thanks Antoine Prevot!
        mount = path.split(os.sep)[2]
        server = os.popen("mount | grep " + mount + " | cut -d'@' -f 2 | cut -d'/' -f 1").read().strip()
        if server:
            path = path.replace("/Volumes/", "smb://" + server + "/")

    c4d.CopyStringToClipboard(path)
    print "copied path to clipboard: \n", path
