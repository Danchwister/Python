import mysql.connector

#Logar no Banco de Dados
conexao = mysql.connector.connect(
    host= "localhost",
    user= "root",
    password= "rootxc",
    database= "youtubepython",
)
cursor = conexao.cursor()
#Conectado ao BD
# 4 Métodos: CRUD
# Editando o banco, tem que usar o conexao.commit()
comando = 






cursor.close()
conexao.close()
