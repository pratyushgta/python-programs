"""
 * This file contains server-side code implementing methods for simple calculator operations
 * DC-E4
 *
 * @author Pratyush Kumar (github.com/pratyushgta)
"""
import xmlrpc.server


class MyServer:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b


# create instance of SimpleXMLRPCServer class listening on localhost, port 6363
server = xmlrpc.server.SimpleXMLRPCServer(("localhost", 6363))
# registers instance of MyServer, so it can access methods of MyServer
server.register_instance(MyServer())
server.serve_forever()
