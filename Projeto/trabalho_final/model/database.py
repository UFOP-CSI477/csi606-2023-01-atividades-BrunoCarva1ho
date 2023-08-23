import pymysql

class Connection:
    mysql = pymysql.connect(host='localhost',
                        port=3306,
                        user='Bruno',
                        passwd='Passeivoado1',
                        database='final_Web1')
    
#Instancia para execução geral dos comandos SQL no banco
cur = Connection.mysql.cursor()

class Mysql:

    def __init__(self):
        ...
        
    
    def _insertUser(nome, email, estado, cidade, senha):
        cur.execute('INSERT INTO usuarios (email, senha, nome, estado, cidade) VALUES (%s,%s,%s,%s,%s)',(email,senha,nome,estado,cidade))
        cur.connection.commit()
        
    
    def _getUser(email, senha):
        cur.execute('SELECT * FROM usuarios WHERE email=%s AND senha=%s',(email,senha))
        usuario = cur.fetchall()
        
        return usuario
    
    
    def _insertDataDay(id_usuario, qtd_leite, qtd_racao, tempo_gasto, clima, data):
        cur.execute("INSERT INTO dados_leite_diario (id_usuario, quantidade_leite, quantidade_racao, tempo_gasto, clima, data) VALUES (%s,%s,%s,%s,%s,%s)",(id_usuario, qtd_leite, qtd_racao, tempo_gasto, clima, data))
        cur.connection.commit()
        
        
    def _getDataDay(id_usuario):
        cur.execute("SELECT * FROM dados_leite_diario WHERE (id_usuario=%s)",(id_usuario))
        dados = cur.fetchall()
        
        return dados
    
    def _deleteData(id_dados_diarios):
        cur.execute("DELETE  FROM dados_leite_diario WHERE (id_dados_diarios=%s)",(id_dados_diarios))
        cur.connection.commit()
        
    
    def _getTemposLeite(id_usuario):
    
        tempos = []
        
        quente=0
        frio=0
        mediano=0
        
        temposDatabase = Mysql._getDataDay(id_usuario=id_usuario)
        
        for tempo in temposDatabase:
            if(tempo[5] == 'Quente'):
                quente += tempo[2]
                
            elif(tempo[5] == 'Frio'):
                frio += tempo[2]
                
            elif(tempo[5] == 'Mediano'):
                mediano+= tempo[2]
                
        tempos.append(quente)
        tempos.append(frio)
        tempos.append(mediano)
        
        return tempos