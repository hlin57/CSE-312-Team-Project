import re
import os
from response import generate_response
from config import *
class Router:
    routes = []
    def add_route(route):
        Router.routes.append(route)
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
    def handle_request(self,request, handler):
        self.action(request,handler)

    
def home(request, handler):
    handler.request.sendall(generate_response(b'hello'))
def css(request, handler):
    filename = request.path
    with open(filename,'rb') as css:
        handler.request.sendall(generate_response(css.read(),'text/css; charset=utf-8'))
def java_script(request, handler):
    filename = request.path[request.path.rfind('/')+1:]
    with open(JS + filename,'rb') as js:
        handler.request.sendall(generate_response(js.read(),'text/javascript; charset=utf-8'))

def image(request, handler):
    filename = request.path[request.path.rfind('/')+1:]
    with open(IMAGE + filename,'rb') as image:
        handler.request.sendall(generate_response(image.read(),'image/jpeg'))
def html(request, handler):
    filename = request.path[request.path.rfind('/')+1:]
    print('open:',SRC + filename)
    with open(SRC + filename,'rb') as html:
        handler.request.sendall(generate_response(html.read(),'text/html'))
def signUp(request, handler):
    html(request, handler)
def NotFound(request, handler):
    handler.request.sendall(generate_response(b'content was not found','text/plain','404 Not Found'))


Router.add_route(Route('GET','/.*\.html',signUp))
Router.add_route(Route('GET','/.*\.css',css))
Router.add_route(Route('GET','/.*\.js',java_script))
Router.add_route(Route('GET','/.*\.png',image))
Router.add_route(Route('GET','/.*\.jpg',image))
Router.add_route(Route('GET','/',home))
