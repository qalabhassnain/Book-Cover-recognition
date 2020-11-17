import PyPDF2 as pypdf
def findInDict(needle, haystack):
    for key in haystack.keys():
        try:
            value=haystack[key]
        except:
            continue
        if key==needle:
            return value
        if isinstance(value,dict):
            x=findInDict(needle,value)
            if x is not None:
                return x
pdfobject=open('doc06082920200117125740.pdf','rb')
pdf=pypdf.PdfFileReader(pdfobject)
xfa=findInDict('/XFA',pdf.resolvedObjects)
xml=xfa[7].getObject().getData()