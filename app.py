# - API - É um lugar para disponibilizar recursos e/ou funcionalidades.
# 1. Objetivo - Criar um api que disponibiliza consulta criação edição e exclusão de livros
# 2. Url Base - localhost
# 3. EndPoints
#     localhost/livros (get)
#     localhost/livros (post)
#     localhost/livros/id (get)
#     localhost/livros/id (put)
#     localhost/livros/id (delete)
# 4. Quais recursos


from flask import Flask, jsonify, request

app = Flask(__name__)
 
livros = [
    {
        'id': 1,
        'titulo': 'O Senhor dos aneis - a Sociedade do Anel',
        'autor': 'J.R.R Tolkien'
        
    },
    {
        'id': 2,
        'titulo': 'Harry Potter e a Pedra Filosofal',
        'autor': 'J.R Howling'
        
    },    
    {
        'id': 3,
        'titulo': 'James Clear',
        'autor': 'Hábitos Atômicos'
        
    }
]

#incluir novo livro

@app.route('/livros', methods=['POST'])

def incluir_novo():
    novo_livro = request.get_json()
    livros.append(novo_livro)

#consultar(todos)

@app.route('/livros',methods=['GET'])
def obter_livros():
    return jsonify(livros)

#consultar(id)

@app.route('/livros/<int:id>',methods=['GET'])

def obter_livro_por_id(id):
    for livro in livros:
      if livro.get('id') == id:
       return jsonify(livro)

#editar
@app.route('/livros/<int:id>', methods=['PUT'])

def editar_livro_por_id(id):
    livro_alterado = request.get_json()
    for indice,livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])
#excluir
@app.route('/livros/<int:id>', methods=['DELETE'])

def excluir_livros(id):
    for indice, livro, in enumerate(livros):
        if livros.get('id') == id:
            del livros[indice]
            
            return jsonify(livros)


app.run(port=5000,host='localhost',debug=True)