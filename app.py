from flask import Flask, request
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)

csrf = CSRFProtect(app)

@app.route("/")
def pagina_inicial():
    return "Hello World"

@app.route("/soma")
def soma_valores():
    num1 = request.args.get('num1', default = 1, type = int)
    num2 = request.args.get('num2', default = 1, type = int)
    soma = num1 + num2
    return f'Sua soma de {num1}+{num2}={str(soma)}'

if __name__ == '__main__':
    app.run()


