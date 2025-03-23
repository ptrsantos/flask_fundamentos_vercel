from app import app
from flask import render_template
from app.forms.cliente_form import ClienteForm
from app import db
from app.models.cliente_model import ClienteDbModel
from app.entidades.cliente import Cliente
from flask import redirect, url_for
from flask import request
from app.services import cliente_service

@app.route("/", methods=["GET"])
def index():
    return redirect(url_for("listar_clientes"))

@app.route("/cadastrar_cliente", methods=["GET", "POST"])
def cadastrar_cliente():
    form = ClienteForm()
    if form.validate_on_submit():
        nome = form.nome.data
        email = form.email.data
        data_nascimento = form.data_nascimento.data
        profissao = form.profissao.data
        sexo = form.sexo.data
        print(f"Nome: {nome}\nEmail: {email}\nData de Nascimento: {data_nascimento}\nProfissão: {profissao}\nSexo: {sexo}")
        clienteDbModel = ClienteDbModel(nome=nome, email=email, data_nascimento=data_nascimento, profissao=profissao, sexo=sexo)    
        try:
            cliente_service.create_cliente(clienteDbModel)
            return redirect(url_for("listar_clientes"))
        except Exception as e:
            print(f"Não foi possível cadastrar o cliente. Erro: {e}")
    else:
        print("Formulário inválido")
    return render_template("clientes/cadastro_cliente.html", form=form)

@app.route("/listar_clientes")
def listar_clientes():
    clientes = cliente_service.select_all_clientes()
    return render_template("clientes/lista_clientes.html", clientes=clientes)


# @app.route("/detalhe_cliente", methods=["GET"])
# def detalhe_cliente():
#     id = request.args.get("id")
#     clienteDbModel = ClienteDbModel.query.get(id)
#     return render_template("clientes/detalhe_cliente.html", cliente=clienteDbModel)

@app.route("/detalhe_cliente/<int:id>", methods=["GET"])
def detalhe_cliente(id):
    clienteDbModel = cliente_service.select_cliente_por_id(id)
    return render_template("clientes/detalhe_cliente.html", cliente=clienteDbModel)


@app.route("/editar_cliente/<int:id>", methods=["GET", "POST"])
def editar_cliente(id):
    clienteDbModel = cliente_service.select_cliente_por_id(id)
    form = ClienteForm(obj=clienteDbModel)
    form.sexo.data = clienteDbModel.sexo
    if form.validate_on_submit():
        nome = form.nome.data,
        email = form.email.data,
        data_nascimento = form.data_nascimento.data,
        profissao = form.profissao.data,
        sexo = form.sexo.data
        cliente = Cliente(nome=nome, data_nascimento=data_nascimento, email=email, profissao=profissao, sexo=sexo)
        try:
            cliente_service.update_cliente(clienteDbModel, cliente)
            return redirect(url_for("listar_clientes"))
        except Exception as e:
            print(f"Não foi possível editar o cliente. Erro: {e}")
    return render_template("clientes/cadastro_cliente.html", form=form)

@app.route("/excluir_cliente/<int:id>", methods=["GET", "POST"])
def excluir_cliente(id):
    clienteDbModel = cliente_service.select_cliente_por_id(id)
    if request.method == "POST":
        try:
            cliente_service.delete_cliente(clienteDbModel)
            return redirect(url_for("listar_clientes"))
        except Exception as e:
            print(f"Não foi possível excluir o cliente. Erro: {e}")
    return render_template("clientes/excluir_cliente.html", cliente=clienteDbModel)