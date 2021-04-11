from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)
app.config["testcase"] = []


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/app', methods=['get', 'post'])
def hello_app():
    return 'hello, app'


@app.route('/abc/<int:tmp>', methods=['get', 'post'])
def hello(tmp):
    print(request.data)
    print(request.json)
    print(tmp)
    return 'hello'


class TestCaseServer(Resource):
    def get(self):
        if "id" in request.args:
            # 从用例库中找对应的用例
            for i in app.config["testcase"]:
                # 返回用例
                if i["id"] == request.args["id"]:
                    print(i)
                    return i
        else:
            return app.config["testcase"]

    def post(self):
        """
        每条testcase 要有id, description, steps
        :return:
        """
        print(request.json)
        if 'id' not in request.json:
            return {"result": "error", "error code": "404", "errmessage": "need testcase id"}
        app.config["testcase"].append(request.json)
        return {"error": "ok", "erroer code": "0"}


api.add_resource(TestCaseServer, '/testcase')


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")