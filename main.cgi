#!/usr/bin/python

import cgi, os
import cgitb; cgitb.enable()
import Grader
import Validate

form = cgi.FieldStorage()

# Get filename.
fileitem = form['filename'] 
problem = form.getvalue('problem')
studentid = form.getvalue('duckid')
# Test if the file was uploaded

validator = Validate.validator()
message = []
details =[]

if fileitem.filename:
   # strip leading path from file name to avoid 
   # directory traversal attacks
   fn = studentid+os.path.basename(fileitem.filename)
   if validator.checkFile(fn): ## check to make sure file contains .py
      if validator.checkID(studentid): ##check to makesure that duckid is int he class
         open('/tmp/' + fn, 'wb').write(fileitem.file.read())
         studentCode = "/tmp/"+fn
         C = Grader.Checker(studentid,problem,studentCode) ##initalize checker class
         C.check() # check the student code
         message = C.message
         details = C.diffDetails
         
      else:
         message.append("That is not a valid duckid") ## if not valid ID let the student know
   else:
      message.append("That isn't a python file.") ## if its not a python file the the student know
   
else:
   message.append('No file was uploaded') ## if there wasn't a file uploaded let them know
   
print 'Content-Type: text/html\n'
print '<html>'
print '<body>'
print(problem)
for line in message:
   print '<p>'+line+'</p>'

if details:
   for line in details:
      print '<p>'+line+'</p>'

print '</body>'
print '</html>'
