from wtforms import Form, StringField, PasswordField, EmailField, BooleanField, IntegerField, validators, RadioField, SubmitField

class UserForm(Form):
    matricula = IntegerField("Matricula",[
        validators.DataRequired(message = "El campo es requerido")
    ])
    nombre = StringField("Nombre",[
        validators.DataRequired(message = "El campo es requerido")
    ])
    apellido = StringField("Apellido",[
        validators.DataRequired(message = "El campo es requerido")
    ])
    correo = EmailField("Correo",[
        validators.Email(message = "Ingrese correo valido")
    ])
    

class CinepolisForm(Form):
    nombre = StringField('Nombre', [
        validators.DataRequired(message='El nombre es requerido')
    ])
    cant_compradores = IntegerField('Cantidad Compradores', [
        validators.DataRequired(message='El campo es requerido'),
        validators.NumberRange(min=1, message='Debe haber al menos 1 comprador')
    ])
    cant_boletas = IntegerField('Cantidad de Boletas', [
        validators.DataRequired(message='El campo es requerido'),
        validators.NumberRange(min=1, message='Mínimo 1 boleta')
    ])
    tarjeta = RadioField('Tarjeta Cineco', choices=[('si', 'Sí'), ('no', 'No')], default='no')
