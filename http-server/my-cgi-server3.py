# Section is an generalization for later.
# PORT = 8080
# 
# try:
#     PORT = os.environ['NEWSPEAK_PORT']
# except:
#     PORT = 8080
#     print "NEWSPEAK_PORT not was not set, setting serving port to default ", PORT
# For now, just copied server.py here and changed the port

import http.server
import socketserver

PORT = 9091
# DIRECTORY = "webIDE"
# DIRECTORY = "" # when Handler super used, this shows contents of my top level / directory

# Simple vs CGI is the only difference
class Handler(http.server.CGIHTTPRequestHandler):
    cgi_directories = ['/burger-protocol/cgi-bin', '/general/cgi-bin']
    #pass
    #def __init__(self, *args, **kwargs):
    #    super().__init__(*args, directory=DIRECTORY, **kwargs)

# Handler.extensions_map['.wasm'] = 'application/wasm'

# with socketserver.TCPServer(("", PORT), Handler) as httpd:
with http.server.HTTPServer(("", PORT), Handler) as httpd:
    # print ("Python3: servable/my-serve3.sh using servable/my-cgi-server3.py serving at port", PORT, " in directory ", DIRECTORY)
    print ("Python3: servable/my-serve3.sh using http-experiments/my-cgi-server3.py serving at port", PORT)
    httpd.serve_forever()
