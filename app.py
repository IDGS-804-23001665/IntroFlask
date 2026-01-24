from flask import Flask, render_template, request
import math, forms
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.secret_key = 'clave_secreta'
csrf = CSRFProtect()

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

@app.route('/operasBas', methods=['GET', 'POST'])
def operasBas():
    res = None
    if request.method == 'POST':
        n1 = float(request.form.get('num1'))
        n2 = float(request.form.get('num2'))
        
        if request.form.get('operacion') == 'suma':
            res = float(n1) + float(n2)
        if request.form.get('operacion') == 'resta':
            res = float(n1) - float(n2)
        if request.form.get('operacion') == 'multi':
            res = float(n1) * float(n2)
        if request.form.get('operacion') == 'divi':
            res = float(n1) / float(n2)
                
    return render_template('operasBas.html', res=res)

@app.route('/resultado', methods=['GET', 'POST'])
def result():
    n1 = request.form.get('num1')
    n2 = request.form.get('num2')
    return f'<h1>La suma es: {float(n1) + float(n2)}</h1>'

@app.route('/distancia', methods=['GET', 'POST'])
def distancia():
    resultado = None
    if request.method == 'POST':
        x1 = float(request.form.get('x1'))
        y1 = float(request.form.get('y1'))
        x2 = float(request.form.get('x2'))
        y2 = float(request.form.get('y2'))
        
        dist = math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))
        
        resultado = dist
        
    return render_template('distancia.html', resultado=resultado)

@app.route('/alumnos', methods=['GET', 'POST'])
def alumnos():
    mat=0
    nom=''
    ape=''
    correo=''
    alumno_clas = forms.UserForm(request.form)
    if request.method == 'POST' and alumno_clas.validate():
        mat = alumno_clas.matricula.data
        nom = alumno_clas.nombre.data
        ape = alumno_clas.apellido.data
        correo = alumno_clas.correo.data
    return render_template("alumnos.html", form = alumno_clas, mat = mat, nom = nom, ape = ape, correo = correo)

if __name__ == '__main__':
    csrf.init_app(app)
    app.run(debug=True)