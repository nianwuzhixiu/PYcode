import pprint
cats=[{'name':'tom','age':'17'},{'name':'jerry','age':'15'}]
fileObj=open('myCat.py','w')
fileObj.write('cat = '+pprint.pformat(cats)+'\n')
fileObj.close()
