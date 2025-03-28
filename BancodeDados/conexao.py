import sqlite3

conexao = sqlite3.connect('banco')
cursor = conexao.cursor()


#cursor.execute('CREATE TABLE usuarios(id INT, nome VARCHAR(100), endereco VARCHAR(100), email VARCHAR(100));')
#cursor.execute('CREATE TABLE produtos(id INT, nome VARCHAR(100), endereco VARCHAR(100), email VARCHAR(100));')
#cursor.execute('CREATE TABLE gerentes(id INT, nome VARCHAR(100), endereco VARCHAR(100), email VARCHAR(100));')
#cursor.execute('DROP TABLE produtos'),


#cursor.execute('ALTER TABLE clientes RENAME TO usuario');

# cursor.execute('ALTER TABLE usuario ADD COLUMN telefoni INT');

#cursor.execute('ALTER TABLE usuario RENAME COLUMN telefoni TO telefone ');


#cursor.execute('INSERT INTO usuario (id, nome, endereco, email, telefone) VALUES (1, "Isadora", "França", "isa@gmail.com", 123456)')
# cursor.execute('INSERT INTO usuario (id, nome, endereco, email, telefone) VALUES (2, "Maria", "Salvador", "isa@gmail.com", 123456)')
# cursor.execute('INSERT INTO usuario (id, nome, endereco, email, telefone) VALUES (3, "José", "Curitiba", "isa@gmail.com", 123456)')
#cursor.execute('INSERT INTO gerentes (id, nome, endereco, email) VALUES (8, "Cyntia", "Inglaterra", "cy@gmail.com")')
#cursor.execute('DELETE FROM usuario where id=1')
#cursor.execute('UPDATE usuario SET endereco = "Minas Gerais" WHERE id = "3"')


# dados = cursor.execute("SELECT nome, telefone FROM usuario WHERE id > 2")
# for usuario in dados:
#     print(usuario)

# dados = cursor.execute("SELECT * FROM usuario")
# for usuario in dados:
#     print(usuario) 

#ORDEM BY E DESC
# dados = cursor.execute('SELECT * FROM usuario ORDER BY nome DESC')
# for usuario in dados:
#     print(usuario) 

# LIMIT E DISTINCT

# dados = cursor.execute('SELECT DISTINCT * FROM usuario LIMIT 3')
# for usuario in dados:
#     print(usuario) 

# # GROUPY BY E HAVING
# dados = cursor.execute('SELECT nome FROM usuario GROUP BY nome HAVING id>3')
# for usuario in dados:
#     print(usuario) 

# JOIN'S
# INNER JOIN - 
# dados = cursor.execute('SELECT * FROM usuario INNER JOIN gerentes ON usuario.id = gerentes.id')
# for usuario in dados:
#     print(usuario)    

# # JOIN - LEFT JOIN - ESQUERDA
# dados = cursor.execute('SELECT * FROM usuario LEFT JOIN gerentes ON usuario.nome = gerentes.nome')
# for usuario in dados:
#     print(usuario) 


# JOIN - RIGHT JOIN - DIREITO
# dados = cursor.execute('SELECT * FROM usuario RIGHT JOIN gerentes ON usuario.nome = gerentes.nome')
# for usuario in dados:
#     print(usuario)


# # JOIN - FULL JOIN 
# dados = cursor.execute('SELECT * FROM usuario FULL JOIN gerentes ON usuario.nome = gerentes.nome')
# for usuario in dados:
#     print(usuario)

# SUB CONSULTAS 
dados = cursor.execute('SELECT * FROM usuario WHERE nome IN (SELECT nome FROM gerentes) ')
for usuario in dados:
    print(usuario)



   





conexao.commit()
conexao.close