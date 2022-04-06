import re
class Router:
    def __init__(self):
        self.routes = []
    def add_route(self,route):
        self.routes.append(route)
    def handle_request(self, request, handler):
        for route in self.routes:
            if route.is_request_match(request):
                route.handle_request(request, handler)
                return
        # return 404



class Route:
    def __init__(self, method, path, action):
        self.method = method
        self.path = path
        self.action = action
    def is_request_match(self, request):
        return request.method == self.method and re.search('^'+self.path,request.path)