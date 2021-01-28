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

def cadastros(lista):
    enviar = 'False'
    if(lista[0] == 'cc'):
        cliente = Pessoa(lista[1],lista[2])
        if(cadastra_cliente.cadastra(cliente)):
            enviar = 'True'  
    if(lista[0] == 'cf'):
        funcionario = Funcionario(lista[0],lista[1],lista[2],float(lista[3]))
        if(cadastra_funcionario.cadastra(funcionario)):
            enviar = 'True'                                        
    if(lista[0] == 'cp'):
        produto = Produto(lista[0],lista[1],lista[2],float(lista[3]),float(lista[4]))
        if(cadastra_produto.cadastra(produto)):
            enviar = 'True'    
    return enviar


address = 'localhost'
port = 9004
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind((address, port))
sock.listen(10)

con, cliente = sock.accept()
dado = ['start']
with open('cadastro.csv', 'w', newline='') as new_file:
    
    csv_writer = csv.writer(new_file)
    while(dado != []):
        print('passei aqui\n')
        try: 
            data, addr = con.recvfrom(1024)
            dado = ast.literal_eval(data.decode('utf-8'))
            print("passei aqui 0\n")
            if(dado[0] != 'sair'):
                print("Passei aqui 1\n")
                csv_writer.writerow(dado)

                if(dado[0] == 'cc' or dado[0] == 'cf' or dado[0] == 'cp'):
                    enviar = cadastros(dado)
                    con.send(enviar.encode())

                if(dado[0] == 'b'):
                    print("Passei aqui busca 1")
                    existe = cadastra_funcionario.busca(dado[1])
                    print("Passei aqui busca 2")
                    if(existe != None):
                        enviar = 'True'
                        con.send(enviar.encode())
                        
                    else:
                        enviar = 'False'
                        con.send(enviar.encode())
                        
        except ValueError as e:
            print(e)
            sock.close()
            exit()
        except IndexError as e:
            print(e)
            sock.close()
            exit()
        except Exception as e:
            print(e)
            sock.close()
            exit()
    sock.close()
        
            
new_file.close()




