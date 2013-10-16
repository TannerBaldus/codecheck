#!/usr/bin/python

import cgi, os
import cgitb; cgitb.enable()
import Grader

form = cgi.FieldStorage()

# Get filename.
fileitem = form['filename']
problem = form.getvalue('problem')
studentid = form.getvalue('duckid')
# Test if the file was uploaded
if fileitem.filename:
   # strip leading path from file name to avoid 
   # directory traversal attacks
   fn = studentid+os.path.basename(fileitem.filename)
   message = []
   details =[]
   if ".py" not in fn:
       message.append("That's not a python file")

   else:
      open('/tmp/' + fn, 'wb').write(fileitem.file.read())
      studentCode = "/tmp/"+fn
      C = Grader.Checker(studentid,problem,studentCode)
      C.check()
      message.append(str(fn))
      message[0] = str(fn)
      details = C.diffDetails
   
else:
   message = 'No file was uploaded'
   
print 'Content-Type: text/html\n'
print '<html>'
print '<body>'

for line in message:
   print '<p>'+line+'</p>'
if details:
   for line in details:
      print '<p>'+line+'</p>'

print '</body>'
print '</html>'
