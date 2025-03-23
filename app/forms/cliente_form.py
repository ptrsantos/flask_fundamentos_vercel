from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField
#from wtforms.fields.html5 import EmailField
from wtforms import DateField
from wtforms.fields.simple import EmailField
from wtforms.validators import DataRequired, Email

class ClienteForm(FlaskForm):

    nome = StringField("nome", validators=[DataRequired()])
    email = EmailField("email", validators=[Email(), DataRequired()])
    #data_nascimento = DateField("data_nascimento", validators=[DataRequired()], format="%d %m %Y")
    #data_nascimento = DateField('Data de Nascimento', format=['%d/%m/%Y'], validators=[DataRequired()])
    data_nascimento = DateField('Data de Nascimento', format='%Y-%m-%d')
    #data_nascimento = DateField('Data de Nascimento', validators=[DataRequired()])
    profissao = StringField("profissao", validators=[DataRequired()])
    sexo = SelectField("sexo", validators=[DataRequired()], choices=[("M", "Masculino"), ("F", "Feminino"), ("N", "Nenhuma das opções")])