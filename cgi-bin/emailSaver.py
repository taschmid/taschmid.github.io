#!/usr/bin/env python
 
import cgi, cgitb 
 
form = cgi.FieldStorage() 
 
firstName = form.getvalue('firstName') 
lastName = form.getvalue('lastName') 
email = form.getvalue('email')