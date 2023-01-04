import socketserver
import csvReader

processing_times_table = open('processing_times_table.csv')

class MyTCPHandler(socketserver.BaseRequestHandler):
    ''' 
    Class for the TCP Handler based on a simple socketserver
    Inherited from the BaseRequestHandler class.
    '''
    def handle(self):
        self.data = self.request.recv(1024).strip()
        returnedString = str(self.data)
        data = returnedString[2:returnedString.find("</station>")+10]
        wait = csvReader.getWait(data, processing_times_table)
        self.request.sendall(bytes(str(wait)+"\n","utf-8"))
        
if __name__ == "__main__":
    HOST, PORT = "172.20.66.43", 11562
    
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        server.serve_forever()
