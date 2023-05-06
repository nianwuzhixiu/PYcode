import shelve
shelFile=shelve.open('mydata')
cat=['tom','jerry','candy']
shelFile['cat']=cat
shelFile.close()
