import matplotlib.pyplot as plt
from flask import Flask,render_template, redirect, request, session
from flask_bootstrap import Bootstrap
from model.database import Mysql
import model.graficos as graf

#Inicialização da aplicação Flask
app = Flask(__name__)
Bootstrap(app)
app.secret_key = 'senha'


#Instancia única das funcionalidades do banco de dados('Singleton')
instance = Mysql


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['POST','GET'])
def login():
    
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        
        usuario = instance._getUser(email= email, senha= senha)
        
        
        if(usuario != ()):
            
            id = usuario[0][0]
            dados_diarios = instance._getDataDay(id)
            
            graf.grafico_dia(id)
            graf.grafico_tempos(id)

            
            return render_template('home_page.html', nome_usuario= usuario[0][3], id_usuario= id, dados_diarios= dados_diarios)
    
    return redirect('/')



@app.route('/home-page/<usuario>/<int:id>', methods=['POST',"GET"])
def home_page(usuario, id):
    graf.grafico_dia(id)
    graf.grafico_tempos(id)
    dados_diarios = instance._getDataDay(id) 
    
    return render_template('home_page.html', nome_usuario=usuario, id_usuario= id, dados_diarios= dados_diarios)



@app.route('/register-data/<usuario>/<int:id>', methods=['POST','GET'])
def register_data(usuario, id):
    
    if request.method == 'POST':
        
        qtd_leite = request.form['qtd_leite']
        qtd_racao = request.form['qtd_racao']
        tempo_gasto = request.form['tempo_gasto']
        clima = request.form['clima']
        data = request.form['data']
        
        instance._insertDataDay(id_usuario= id, qtd_leite= qtd_leite, qtd_racao= qtd_racao, tempo_gasto= tempo_gasto, clima= clima, data= data)
        dados_diarios = instance._getDataDay(id) 
        graf.grafico_dia(id)
        graf.grafico_tempos(id)

        return render_template("/home_page.html", nome_usuario=usuario, id_usuario=id,dados_diarios=dados_diarios)

    return render_template("/register_day.html", nome_usuario=usuario, id_usuario= id)



@app.route('/register-user', methods=['POST','GET'])
def register_page():
    
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        estado = request.form['estado']
        cidade = request.form['cidade']
        senha = request.form['senha']
            
        instance._insertUser(nome= nome, email= email,estado= estado,cidade= cidade,senha= senha)
        
        return redirect('/')
        
    return render_template('register_page.html')


@app.route('/delete-data/<id_dados_diarios>/<usuario>/<int:id>')
def delete_data(id_dados_diarios, usuario, id):
    id_data = int(id_dados_diarios)
    
    instance._deleteData(id_data)
    dados_diarios = instance._getDataDay(id)
    graf.grafico_tempos(id)
    graf.grafico_dia(id)
    
    return render_template("home_page.html", nome_usuario=usuario, id_usuario=id, dados_diarios=dados_diarios)


if __name__ == '__main__':
    app.run(debug=True)
