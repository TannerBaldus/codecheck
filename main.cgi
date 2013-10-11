#!/usr/bin/python

import cgi, os
import cgitb; cgitb.enable()
import Grader

form = cgi.FieldStorage()

# Get filename.
fileitem = form['filename']
problem = form.getvalue(problem)
studentid = form.getvalue(duckid)
# Test if the file was uploaded
if fileitem.filename:
   # strip leading path from file name to avoid 
   # directory traversal attacks
   fn = studentid+os.path.basename(fileitem.filename)
   open('/tmp/' + fn, 'wb').write(fileitem.file.read())
   studentCode = "/tmp/"+fn
   Checker = Checker(studentid,problem,studentCode)
   message = Checker.message
   details = Checker.diffDetails
   
else:
   message = 'No file was uploaded'
   
print """\
Content-Type: text/html\n
<html>
<body>
   <p>%s</p>
   <p>%s</p>
</body>
</html>
""" % (message,details)