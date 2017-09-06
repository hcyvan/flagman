from kernel.app import app

from  routes import api


@app.route('/', endpoint='chengyihang')
def hello_world():
    return 'Hello, World!'


class Foo:
    def test(self):
        return 'test...'

def test2():
    return 'test2'


if __name__ == '__main__':
    print(app.root_path)
    app.run()
