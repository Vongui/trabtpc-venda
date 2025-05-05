from flask import Flask, render_template, request, redirect, url_for, flash, json
from controller.controller_cliente import ControllerCliente
from model.cliente import Cliente
from controller.controller_venda import ControllerVenda
from model.venda import Venda
from controller.controller_produto import ControllerProduto
from model.produto import Produto
from controller.controller_item_venda import ControllerItemVenda
from model.item_venda import ItemVenda
import os

controller_cliente = ControllerCliente()
controller_produto = ControllerProduto()
controle_venda = ControllerVenda()
controle_itemvenda = ControllerItemVenda()

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", titulo="Página Inicial")

#Cliente
@app.route("/listar-clientes")
def listar_clientes():
    clientes = controller_cliente.listarTodosRegistros(Cliente())
    return render_template("clientes/listar.html", titulo="Lista de Clientes", lista=clientes)

@app.route("/cadastrar-cliente", methods=["GET", "POST"])
def cadastrar_cliente():
    if request.method == "POST":
        cliente = Cliente()
        cliente.nome = request.form["nome"]
        cliente.endereco = request.form["endereco"]
        controller_cliente.incluir_cliente(cliente)
        return redirect(url_for("listar_clientes"))

    return render_template("clientes/cadastrar.html", titulo="Cadastro de Clientes")

@app.route("/remover-cliente/<int:id>")
def remover_aluno(id):
    cliente = Cliente()
    cliente.codcliente = id
    controller_cliente.excluir_cliente(cliente)
    return redirect(url_for("listar_clientes"))

#Produtos
@app.route("/listar-produtos")
def listar_produtos():
    produtos = controller_produto.listarTodosRegistros(Produto())
    return render_template("produtos/listar.html", titulo="Lista de Produtos", lista=produtos)

@app.route("/cadastrar-produto", methods=["GET", "POST"])
def cadastrar_produto():
    if request.method == "POST":
        produto = Produto()
        produto.descricao = request.form["descricao"]
        produto.preco = request.form["preco"]
        controller_produto.incluir_produto(produto)
        return redirect(url_for("listar_produtos"))
    return render_template("produtos/cadastrar.html", titulo="Cadastro de Produtos")

@app.route("/remover-produto/<int:id>")
def remover_produto(id):
    produto = Produto()
    produto.codproduto = id
    controller_produto.excluir_produto(produto)
    return redirect(url_for("listar_produtos"))

# #Venda
@app.route("/listar-vendas")
def listar_vendas():
    venda = controle_venda.listarTodosRegistros(Venda())
    produtos = controller_produto.listarTodosRegistros(Produto())
    clientes = controller_cliente.listarTodosRegistros(Cliente())
    return render_template("vendas/listar.html", titulo="Lista de Vendas", lista=venda, lista_produtos=produtos, lista_clientes=clientes)
@app.route("/cadastrar-vendas")
def cadastrar_vendas():
    clientes = controller_cliente.listarTodosRegistros(Cliente())
    produtos_obj = controller_produto.listarTodosRegistros(Produto())
    produtos = [
        {
            "codproduto": p.codproduto,
            "descricao": p.descricao,
            "preco": p.preco
        }
        for p in produtos_obj
    ]

    return render_template("vendas/cadastrar.html", clientes=clientes, produtos=produtos)

from flask import request, redirect

@app.route("/salvar-venda", methods=["POST"])
def salvar_venda():
    dados = request.form
    venda = Venda()
    venda.data = dados["data"]
    venda.codcliente = int(dados["codcliente"])
    venda.valor_total = float(dados["valor_total"])

    controle_venda.incluir(venda)

    ultima_venda = controle_venda.buscarUltimoRegistro(Venda(), "codvenda")

    itens = json.loads(dados["itens"])
    for item in itens:
        item_venda = ItemVenda()
        item_venda.codvenda = ultima_venda
        item_venda.codproduto = item["codproduto"]
        item_venda.qtde = item["qtde"]
        item_venda.valor = item["valor"]
        controle_itemvenda.incluir(item_venda)

    return redirect("/listar-vendas")


@app.route("/detalhes-venda/<int:codvenda>")
def detalhes_venda(codvenda):
    venda_aux = Venda()
    venda_aux.codvenda = codvenda
    venda = controle_venda.pesquisaCodigo(venda_aux)

    itens = controle_itemvenda.listarItensPorVenda(codvenda)
    produtos = controller_produto.listarTodosRegistros(Produto())
    clientes = controller_cliente.listarTodosRegistros(Cliente())
    return render_template("vendas/detalhes.html", venda=venda, itens=itens, produtos=produtos, lista_clientes=clientes)



if __name__ == "__main__":
    app.run(debug=True)