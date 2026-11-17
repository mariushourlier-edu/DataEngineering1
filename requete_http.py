import requests 

class Request:

    def __init__(self, time_out, url):
     if time_out == None:
        self.time_out = 10
     else:
        self.time_out = time_out   
     self.url = url   

    def response(self):
     headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
     response = requests.get(self.url, headers=headers, timeout = self.time_out)