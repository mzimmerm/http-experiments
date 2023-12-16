#!/usr/bin/env python3

import cgi, cgitb # Not used, but will be needed later.
import sys

# see https://docs.python.org/3/library/cgi.html

# Activates exception handler that will display errors in browser
cgitb.enable(display=0, logdir="/burger-protocol/log/")

# To get at submitted form data, use the FieldStorage class.
form = cgi.FieldStorage()

# Get data from query string - normally formed from submitted fields
#   as ?first_name=first&last_name=last etc, but the Protocol handler
#   sends only ?uri=web+burger:burger_data_string
# Use this URL in browsr to test:
#  http://localhost:9091/burger-protocol/cgi-bin/burger-service-cgi.py?uri=MYURI
#  http://localhost:9091/burger-protocol/burger-service.html?uri=MYURI
uri = form.getvalue('uri')

# Print output
print("Content-type: text/html\n\n")
print(f"hello world from burger-service-cgi.py, uri = {uri}!\n")
