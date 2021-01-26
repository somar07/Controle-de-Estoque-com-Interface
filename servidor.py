import socket
import csv
import ast
import pickle
from cadastra_produtos import *
from cadastra_pessoa import *

#Objeto para cadastro de produtos, clientes e funcionarios
cadastra_produto = Cadastra_produto()
cadastra_cliente = Cadastra_pessoa()
cadastra_funcionario = Cadastra_funcionario()



address = 'localhost'
port = 8003
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind((address, port))
sock.listen(10)

con, cliente = sock.accept()

with open('cadastro.csv', 'w', newline='') as new_file:
    csv_writer = csv.writer(new_file)
    data, addr = con.recvfrom(1024)

    while True:
        try:
            if(data):
                csv_writer.writerow(ast.literal_eval(data.decode('utf-8')))
            
            
                with open('cadastro.csv','r') as file:
                    file_csv = file.readlines()

                    for line in file_csv:
                        if(line.startswith('cc')):
                            listaDados = line.split(',')
                            cliente = Pessoa(listaDados[0],listaDados[1])
                            cadastra_cliente.cadastra(cliente)
                            print('Cliente Cadastrado!')
                            
                        elif(line.startswith('cf')):
                            listaDados = line.split(',')
                            funcionario = Funcionario(listaDados[0],listaDados[1],listaDados[2],float(listaDados[3]))
                            cadastra_funcionario.cadastra(funcionario)
                            print('Funcionario Cadastrado!')

                        elif(line.startswith('cp')):
                            listaDados = line.split(',')
                            produto = Produto(listaDados[0],listaDados[1],listaDados[2],float(listaDados[3]),float(listaDados[4]))
                            if(cadastra_produto.cadastra(produto)):
                                enviar = 'True'
                                con.send(enviar.encode())
                            else:
                                enviar = 'False'
                                con.send(enviar.encode())

                        else:
                            print('Nada por aqui...')
            print(cadastra_produto.lista_produtos)
        except:
            exit()
            
        

sock.close()
