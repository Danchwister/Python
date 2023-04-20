import sqlite3

class CRUDExample:

    def __init__(self):
        self.conn = sqlite3.connect('example.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, email TEXT)')

    def create(self, name, email):
        self.cursor.execute('INSERT INTO users (name, email) VALUES (?, ?)', (name, email))
        self.conn.commit()
        print('Usuário criado com sucesso!')

    def read(self, id):
        self.cursor.execute('SELECT * FROM users WHERE id = ?', (id,))
        user = self.cursor.fetchone()
        if user:
            print(f'ID: {user[0]}')
            print(f'Nome: {user[1]}')
            print(f'E-mail: {user[2]}')
        else:
            print('Usuário não encontrado!')

    def update(self, id, name, email):
        self.cursor.execute('UPDATE users SET name = ?, email = ? WHERE id = ?', (name, email, id))
        rows_affected = self.cursor.rowcount
        self.conn.commit()
        if rows_affected > 0:
            print('Usuário atualizado com sucesso!')
        else:
            print('Usuário não encontrado!')

    def delete(self, id):
        self.cursor.execute('DELETE FROM users WHERE id = ?', (id,))
        rows_affected = self.cursor.rowcount
        self.conn.commit()
        if rows_affected > 0:
            print('Usuário deletado com sucesso!')
        else:
            print('Usuário não encontrado!')

    def __del__(self):
        self.cursor.close()
        self.conn.close()

# exemplo de uso
crud = CRUDExample()

# criar um novo usuário
crud.create('João Silva', 'joao@example.com')

# ler um usuário
crud.read(1)

# atualizar um usuário
crud.update(1, 'João da Silva', 'joao.silva@example.com')

# deletar um usuário
crud.delete(1)