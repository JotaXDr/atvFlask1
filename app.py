from flask import Flask,render_template,request,redirect

app = Flask(__name__)
class cadpokemon:
    def __init__(self,numero,nome,tipo,altura,peso):
        self.numero = numero
        self.nome = nome
        self.tipo = tipo
        self.altura = altura
        self.peso = peso

lista = []

@app.route('/jogador')
def jogadores():
    return render_template("Jogadores.html",Titulo = "Jogadores Cadastrados", ListaPokemons = lista)

@app.route('/')
def inicio():
    return 'Começando'

@app.route('/cadastro')
def cadastro():
    return render_template("Cadastro.html",Titulo = "Cadastro jogadores")

@app.route('/criar', methods= ['POST'])
def criar():
        numero = request.form['numero']
        nome = request.form['nome']
        tipo = request.form.getlist('tipo')
        altura = request.form['altura']
        peso = request.form['peso']
        obj = cadpokemon(numero,nome,tipo,altura,peso)
        lista.append(obj)
        return redirect('/jogador')

@app.route('/excluir/<numeropkm>', methods = ['GET','DELETE'])
def excluir(numeropkm):
    for i, pkm in enumerate(lista):
        if pkm.numero == numeropkm:
            lista.pop(i)
            break
    return redirect('/pokemon')


@app.route('/editar/<numeropkm>', methods = ['GET'])
def editar(numeropkm):
    for i, pkm in enumerate(lista):
         if pkm.numero == numeropkm:
             return render_template("Editar.html", pokemon=pkm, Titulo = "Editar")



@app.route('/alterar/<numeropkm>', methods = ['PUT', 'POST'])
def alterar(numeropkm):
   numero = request.form['numero']
   for pkm in lista:
       if pkm.numero == numero:
           pkm.nome = request.form['nome']
           pkm.tipo = request.form('tipo')
           pkm.altura = request.form['altura']
           pkm.peso = request.form['peso']
       return redirect('/pokemon')


if __name__ == '__main__':
    app.run()
