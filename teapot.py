class ESPTeapot:
    def __init__(self, url):
        self.url = url
        self.status = 'ready'
        self.temp = 0

    def start(self, temp):
        # code = request.get(self.url+'/start', params={'temp': temp}).status_code
        code = 200
        if code == 200:
            self.status = 'Starting'
        else:
            self.status = 'Error'
            print("connection error")
        return self.status, self.temp

    def get_status(self):
        # self.status, self.temp = request.get(self.url+'/status').text.split()
        self.status, self.temp = 'In Process', 80
        return self.status, self.temp

    def stop(self):
        # code = request.get(self.url+'/stop').status_code
        code = 200
        if code == 200:
            self.status = 'Stopped'
        return self.status, self.temp

    def check_connection(self):
        pass
