from app.models.cliente_model import ClienteDbModel
from app import db

def select_all_clientes():
    #clientes = db.session.query(Cliente).all()
    clientesDbModel = ClienteDbModel.query.all()
    return clientesDbModel

def select_cliente_por_id(id):
    #clienteDbModel = ClienteDbModel.query.get(id)
    clienteDbModel = ClienteDbModel.query.filter_by(id=id).first()
    return clienteDbModel

def create_cliente(clienteDbModel):
    db.session.add(clienteDbModel)
    db.session.commit()

def update_cliente(cliente_db_model, cliente_novo):
    cliente_db_model.nome = cliente_novo.nome
    cliente_db_model.email = cliente_novo.email
    cliente_db_model.data_nascimento = cliente_novo.data_nascimento
    cliente_db_model.profissao = cliente_novo.profissao
    cliente_db_model.sexo = cliente_novo.sexo
    db.session.commit()

def delete_cliente(cliente_db_model):
    db.session.delete(cliente_db_model)
    db.session.commit()
