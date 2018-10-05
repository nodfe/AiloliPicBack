import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render("view/front/index.html")
        # self.write("Hello,World")

def make_app():
    return tornado.web.Application([
        (r"/",MainHandler)
    ])

if  __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()