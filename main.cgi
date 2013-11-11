#!/usr/bin/python

import cgi, os
import cgitb; cgitb.enable()
import Grader
import Validator

form = cgi.FieldStorage()

# Get filename.
fileitem = form['filename']
problem = form.getvalue('problem')
studentid = form.getvalue('duckid')
# Test if the file was uploaded

validator = validator()

if fileitem.filename:
   # strip leading path from file name to avoid 
   # directory traversal attacks
   fn = studentid+os.path.basename(fileitem.filename)
         details = C.diffDetails
         
      else:
         details = C.diffDetails
         
      else:
   if validator.checkFile(fn):
      if validator.checkID(studentid):
         open('/tmp/' + fn, 'wb').write(fileitem.file.read())
         studentCode = "/tmp/"+fn
         C = Grader.Checker(studentid,problem,studentCode)
         C.check()
         message = C.message
         details = C.diffDetails
         
      else:
         message = "That is not a valid duckid"

   else:
      message = "That isn't a python file."
   
else:
   message = 'No file was uploaded'
   
print 'Content-Type: text/html\n'
print '<html>'
print '<body>'

for line in message:
   print '<p>'+line+'</p>'

for line in details:
   print '<p>'+line+'</p>'

print '</body>'
print '</html>'