from flask import Flask, render_template, request

app = Flask(__name__)
app.secret_key = 'clave_secreta'

@app.route('/')
def index():
    title = "IDGS804 - Intro Flask"
    listado = ["Juan", "Ana", "Pedro", "Luisa"]
    return render_template('index.html', title=title, listado=listado)

@app.route('/saludo1')
def saludo1():
    return render_template('saludo1.html')

@app.route('/saludo2')
def saludo2():
    return render_template('saludo2.html')

@app.route('/hola') 
def func():
    return "Hola mundo -- hola"

@app.route('/user/<string:user>')
def user(user):
    return f'Hola, {user}'

@app.route('/numer/<int:n>')
def numero(n):
    return f'<h1>Numero: {n}</h1>'

@app.route('/username/<int:id>/<string:username>')
def username(id, username):
    return f'<h1>Hola, {username} Tu id es: {id}</h1>'

@app.route('/suma/<float:n1>/<float:n2>')
def suma(n1,n2):
    return f"<h1>La suma es: {n1 + n2}</h1>"

@app.route('/default/')
@app.route('/default/<string:param>')
def func2(param="Daniel"):
    return f'<h1>Hola, {param}</h1>'

@app.route('/operaciones')
def operaciones():
    return '''
            <form>
                <label for="name">Name: </label>
                    <input type="text" id="name" name="name" required>
                </br>
                <laber for="name">a paterno: </label>
                    <input type="text" id="name" name="name" required>
                </br>
                <input type="submit" value="Submit">
            </form>
            '''

@app.route('/operasBas')
def operasBas():
    return render_template('operasBas.html')

@app.route('/resultado', methods=['GET', 'POST'])
def result():
    n1 = request.form.get('num1')
    n2 = request.form.get('num2')
    return f'<h1>La suma es: {float(n1) + float(n2)}</h1>'

if __name__ == '__main__':
    app.run(debug=True)