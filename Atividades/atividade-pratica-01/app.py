from flask import Flask, render_template, redirect, request, session, url_for
from flask_bootstrap import Bootstrap
from models.BD import mysql

app = Flask(__name__)
Bootstrap(app)
app.secret_key = 'asdjn4239dasdm2354HTGSDF4564'


#REDIRECIONAMENTO PÓS TENTATIVA DE LOGIN
@app.route("/index.html")
def index():
    username = ''
    if 'username' in session:
        username = session['username']
        return render_template("index.html",username=username)
    
    return render_template("/login.html")


#LOGOUT
@app.route('/logout')
def logout():
    session.pop('username',None)
    return redirect(url_for('login'))

#LOGIN
@app.route("/login", methods= ['POST','GET'])
def login():
    logado = None
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        
        with mysql.cursor() as cur:
            cur.execute("SELECT * FROM usuarios WHERE email=%s AND senha=%s",(email,senha))
            logado = cur.fetchall()
            
            if logado:
                session['username']= logado
                return redirect(url_for('index'))
            else:
                return render_template('/login.html', mensagem='Usuário ou senha inválidos')

    return render_template('/login.html')



#CADASTRAR USUÁRIO
@app.route("/cadastrar-usuario", methods=['POST','GET'])
def cadastrar_usuario():
    
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']
        
        with mysql.cursor() as cur:
            cur.execute("INSERT INTO usuarios (nome,email,senha) VALUES(%s,%s,%s)",(nome,email,senha))
            cur.connection.commit()
            
        return redirect("/login")
        
    return render_template('/cadastrar.html')



#CADASTRAR ENDEREÇO
@app.route("/cadastrar-endereco", methods=['POST','GET'])
def cadastrar_endereco():
    
    if 'username' in session:
        username = session['username']
        
        if request.method == 'POST':
            rua = request.form['rua']
            numero = request.form['numero']
            bairro = request.form['bairro']
            telefone = request.form['telefone']
            usuario_id = username[0][0]
            
            with mysql.cursor() as cur:
                cur.execute('INSERT INTO enderecos (usuario_id,rua,numero,bairro,telefone) VALUES (%s,%s,%s,%s,%s)',(usuario_id,rua,numero,bairro,telefone))
                cur.connection.commit()
                
            return render_template("/index.html",username=username)
        
        return render_template("/cadastrarEndereco.html", username=username)
    
    else:
        return redirect(url_for('login'))
    

#EDITAR ENDEREÇO
@app.route("/editar-endereco/<int:id>", methods=['GET','POST'])
def editar_endereco(id):
    
    if 'username' in session:
        username = session['username']
        
        if request.method == 'POST':
            rua = request.form['rua']
            numero = request.form['numero']
            bairro = request.form['bairro']
            telefone = request.form['telefone']
            
            with mysql.cursor() as cur:
                cur.execute("UPDATE enderecos SET rua=%s, numero=%s, bairro=%s, telefone=%s WHERE id=%s",(rua,numero,bairro,telefone,id))
                cur.connection.commit()
                
            return render_template("/index.html",username=username)
        
        return render_template("editarEndereco.html", id=id, username=username)
    
    return render_template("editarEndereco.html", id=id)
        
    

#EXIBIR ENDEREÇOS
@app.route("/meus-enderecos", methods=['GET'])
def meus_enderecos():
    
    if 'username' in session:
        username = session['username']
        id = username[0][0]
        
        with mysql.cursor() as cur:
            cur.execute("SELECT * FROM enderecos WHERE usuario_id=%s ", id)
            enderecos = cur.fetchall()
            
            return render_template('/enderecos.html', enderecos=enderecos, username=username)


if __name__ == '__main__':
    app.run(debug=True)