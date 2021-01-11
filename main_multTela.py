import sys

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox

from cadastra_pessoa import *
from tela_cadastro_cliente import Tela_cadastro_cliente
from tela_cadastro_funcionario import Tela_cadastro_funcionario
from tela_cadastro_produto import Tela_cadastro_produto
from tela_inicial import Tela_inicial
from tela_primeiro_acesso import Tela_primeiro_acesso
from tela_login_funcionario import Tela_login_func
from tela_op_funcionario import Tela_op_funcionario
from tela_tipo_cadastro import Tela_tipo_cadastro
from tela_listagens import Tela_listagens
from tela_tipo_exclusao import Tela_tipo_exclusao
from tela_listDados import Tela_listDados
from produtos import *

class Ui_main(QtWidgets.QWidget):
	def setupUi(self, Main):
		Main.setObjectName('Main')
		Main.resize(640, 480)
	
		self.QtStack = QtWidgets.QStackedLayout()

		self.stack0 = QtWidgets.QMainWindow()
		self.stack1 = QtWidgets.QMainWindow()
		self.stack2 = QtWidgets.QMainWindow()
		self.stack3 = QtWidgets.QMainWindow()
		self.stack4 = QtWidgets.QMainWindow()
		self.stack5 = QtWidgets.QMainWindow()
		self.stack6 = QtWidgets.QMainWindow()
		self.stack7 = QtWidgets.QMainWindow()
		self.stack8 = QtWidgets.QMainWindow()
		self.stack9 = QtWidgets.QMainWindow()
		self.stack10 = QtWidgets.QMainWindow()

		self.primeiro_acesso = Tela_primeiro_acesso()
		self.primeiro_acesso.setupUi(self.stack0)

		self.tela_inicial = Tela_inicial()
		self.tela_inicial.setupUi(self.stack1)

		self.tela_login_func = Tela_login_func()
		self.tela_login_func.setupUi(self.stack2)

		self.tela_op_funcionario = Tela_op_funcionario()
		self.tela_op_funcionario.setupUi(self.stack3)

		self.tela_tipo_cadastro = Tela_tipo_cadastro()
		self.tela_tipo_cadastro.setupUi(self.stack4)

		self.tela_tipo_exclusao = Tela_tipo_exclusao()
		self.tela_tipo_exclusao.setupUi(self.stack5)

		self.tela_listagens = Tela_listagens()
		self.tela_listagens.setupUi(self.stack6)

		self.tela_cadastro_funcionario = Tela_cadastro_funcionario()
		self.tela_cadastro_funcionario.setupUi(self.stack7)
		
		self.tela_cadastro_cliente = Tela_cadastro_cliente()
		self.tela_cadastro_cliente.setupUi(self.stack8)

		self.tela_cadastro_produto = Tela_cadastro_produto()
		self.tela_cadastro_produto.setupUi(self.stack9)

		self.tela_listDados = Tela_listDados()
		self.tela_listDados.setupUi(self.stack10)

		self.QtStack.addWidget(self.stack0)#tela primeiro acesso
		self.QtStack.addWidget(self.stack1)#tela inicial
		self.QtStack.addWidget(self.stack2)#tela de login
		self.QtStack.addWidget(self.stack3)#tela de opções para o funcionario
		self.QtStack.addWidget(self.stack4)#tela para tipos de cadastro
		self.QtStack.addWidget(self.stack5)#tela para opções de exclusão
		self.QtStack.addWidget(self.stack6)#tela para opções de listagens
		self.QtStack.addWidget(self.stack7)#tela para cadastro de funcionários
		self.QtStack.addWidget(self.stack8)#tela para cadastro de clientes
		self.QtStack.addWidget(self.stack9)#tela para cadastro de clientes
		self.QtStack.addWidget(self.stack10)#tela para listar dados


class Main(QMainWindow, Ui_main):
	def __init__(self, parent=None):
		super(Main, self).__init__(parent)
		self.setupUi(self)

		# cadastro de cliete
		self.cadastra_cliente = Cadastra_pessoa()

		# cadastro de funcionario
		self.cadastra_funcionario = Cadastra_funcionario()

		# cadastro de produto
		self.cadastra_produto = Cadastra_produto()

		#Interação tela primeiro acesso
		self.primeiro_acesso.pushButton.clicked.connect(self.primeiro_cadastro)
		self.primeiro_acesso.pushButton_2.clicked.connect(QtCore.QCoreApplication.instance().quit)
		
		# Interação tela inicial
		self.tela_inicial.pushButton.clicked.connect(lambda: self.QtStack.setCurrentIndex(2))
		self.tela_inicial.pushButton_3.clicked.connect(QtCore.QCoreApplication.instance().quit)

		#Interação tela login funcionario
		self.tela_login_func.pushButton.clicked.connect(self.btnLoginFunc)
		self.tela_login_func.pushButton_2.clicked.connect(lambda: self.QtStack.setCurrentIndex(1))
		
		#Interação tela de opções para o Funcionario
		self.tela_op_funcionario.pushButton.clicked.connect(lambda: self.QtStack.setCurrentIndex(4))#tipos de cadastro
		self.tela_op_funcionario.pushButton_2.clicked.connect(lambda: self.QtStack.setCurrentIndex(5))#tipos de exclusao
		self.tela_op_funcionario.pushButton_3.clicked.connect(lambda: self.QtStack.setCurrentIndex(6))#tipos de listagem
		self.tela_op_funcionario.pushButton_4.clicked.connect(lambda: self.QtStack.setCurrentIndex(1))#voltar para login

		#Interação tela tipos de cadastro
		self.tela_tipo_cadastro.pushButton.clicked.connect(lambda: self.QtStack.setCurrentIndex(7))#cadastro de funcionarios
		self.tela_tipo_cadastro.pushButton_2.clicked.connect(lambda: self.QtStack.setCurrentIndex(8))#cadastro de clientes
		self.tela_tipo_cadastro.pushButton_3.clicked.connect(lambda: self.QtStack.setCurrentIndex(9))#cadastro de clientes
		self.tela_tipo_cadastro.pushButton_4.clicked.connect(lambda: self.QtStack.setCurrentIndex(3))#voltar para tela de opções para funcionarios

		#Interação tela tipos de exclusao
		self.tela_tipo_exclusao.pushButton_4.clicked.connect(lambda: self.QtStack.setCurrentIndex(3))

		#Interação tela tipos de listagens		
		self.tela_listagens.pushButton.clicked.connect(self.btnListFunc)	
		self.tela_listagens.pushButton_2.clicked.connect(self.btnListCli)
		self.tela_listagens.pushButton_3.clicked.connect(self.btnListProd)		
		self.tela_listagens.pushButton_4.clicked.connect(lambda: self.QtStack.setCurrentIndex(3))

		# Interação tela cadastra funcionario
		self.tela_cadastro_funcionario.pushButton.clicked.connect(self.btnCadastra_func)
		self.tela_cadastro_funcionario.pushButton_2.clicked.connect(lambda: self.QtStack.setCurrentIndex(4))

		# Interação tela cadastra cliente
		self.tela_cadastro_cliente.pushButton.clicked.connect(self.btnCadastra_cliente)
		self.tela_cadastro_cliente.pushButton_2.clicked.connect(lambda: self.QtStack.setCurrentIndex(4))

		# Interação tela cadastra produto
		self.tela_cadastro_produto.pushButton.clicked.connect(self.btnCadastra_produto)
		self.tela_cadastro_produto.pushButton_2.clicked.connect(lambda: self.QtStack.setCurrentIndex(4))

		# Interação listar dados
		self.tela_listDados.pushButton.clicked.connect(self.clear_area)


	def primeiro_cadastro(self):
		nome = self.primeiro_acesso.lineEdit.text()
		cpf = self.primeiro_acesso.lineEdit_2.text()
		salario = self.primeiro_acesso.lineEdit_3.text()

		if(not(nome == '' or cpf == '' or salario == '')):
			funcionario = Funcionario(nome, cpf, salario)

			if(self.cadastra_funcionario.cadastra(funcionario)):
				QMessageBox.information(None, 'Cadastro', 'Cadastro realizado com sucesso!')
				self.QtStack.setCurrentIndex(1)
			else:
				QMessageBox.information(None, 'Cadastro', 'CPF informado já cadastrado')

		else:
			QMessageBox.information(None, 'Cadastro', 'Informe todos os dados')

	def btnLoginFunc(self):
		cpf = self.tela_login_func.lineEdit.text()

		if(not(cpf == '')):
			exite = self.cadastra_funcionario.busca(cpf)

			# tela funcionario
			if(exite != None):
				self.QtStack.setCurrentIndex(3)
				self.tela_login_func.lineEdit.setText('')
			else:
				QMessageBox.information(None, 'Login', 'Cpf não encotrado')
				self.tela_login_func.lineEdit.setText('')

		else:
			QMessageBox.information(None, 'Login', 'Informe seu cpf')
			self.tela_login_func.lineEdit.setText('')


	def btnCadastra_func(self):
		nome = self.tela_cadastro_funcionario.lineEdit.text()
		cpf = self.tela_cadastro_funcionario.lineEdit_2.text()
		salario = self.tela_cadastro_funcionario.lineEdit_3.text()
		
		if(not(nome == '' or cpf == '' or salario == '')):
			funcionario = Funcionario(nome, cpf, salario)

			if(self.cadastra_funcionario.cadastra(funcionario)):
				QMessageBox.information(None, 'Cadastro', 'Cadastro realizado com sucesso')
				self.tela_cadastro_funcionario.lineEdit.setText('')
				self.tela_cadastro_funcionario.lineEdit_2.setText('')
				self.tela_cadastro_funcionario.lineEdit_3.setText('')
			else:
				QMessageBox.information(None, 'Cadastro', 'CPF informado já cadastrado')
		else:
			QMessageBox.information(None, 'Cadastro', 'Informe todos os dados')
	

	def btnCadastra_cliente(self):
		nome = self.tela_cadastro_cliente.lineEdit.text()
		cpf = self.tela_cadastro_cliente.lineEdit_2.text()
		
		if(not(nome == '' or cpf == '')):
			cliente = Pessoa(nome, cpf)

			if(self.cadastra_cliente.cadastra(cliente)):
				QMessageBox.information(None, 'Cadastro', 'Cadastro realizado com sucesso')
				self.tela_cadastro_cliente.lineEdit.setText('')
				self.tela_cadastro_cliente.lineEdit_2.setText('')
			else:
				QMessageBox.information(None, 'Cadastro', 'CPF informado já cadastrado')
		else:
			QMessageBox.information(None, 'Cadastro', 'Informe todos os dados')
	
	def btnCadastra_produto(self):
		codigo = self.tela_cadastro_produto.lineEdit.text()
		nome = self.tela_cadastro_produto.lineEdit_2.text()
		valor = self.tela_cadastro_produto.lineEdit_3.text()
		quantidade = self.tela_cadastro_produto.lineEdit_4.text()

		if(not(codigo == '' or nome == '' or valor == '' or quantidade == '')):
			produto = Produto(codigo, nome, valor, quantidade)
			
			if(self.cadastra_produto.cadastra(produto)):
				QMessageBox.information(None, 'Cadastro', 'Produto cadastrado com sucesso!')
				self.tela_cadastro_produto.lineEdit.setText('')
				self.tela_cadastro_produto.lineEdit_2.setText('')
				self.tela_cadastro_produto.lineEdit_3.setText('')
				self.tela_cadastro_produto.lineEdit_4.setText('')
			else:
				QMessageBox.information(None, 'Cadastro', 'Codigo informado já cadastrado!')
		else:
			QMessageBox.information(None, 'Cadastro', 'Informe todos os dados')

	def btnListFunc(self):
		self.QtStack.setCurrentIndex(10)

		for qtd, func in  enumerate(self.cadastra_funcionario.lista_pessoas):
			info = "Funcionario: {}\nNome: {}\nCPF: {}\nSalario: {}\n".format(qtd+1, func.nome, func.cpf, func.salario)
			self.tela_listDados.listWidget.addItem(info)

	def btnListCli(self):

		if(self.cadastra_cliente.lista_pessoas != []):
			self.QtStack.setCurrentIndex(10)

			for qtd, cli in  enumerate(self.cadastra_cliente.lista_pessoas):
				info = "Clinte: {}\nNome: {}\nCPF: {}\n".format(qtd+1, cli.nome, cli.cpf)
				self.tela_listDados.listWidget.addItem(info)

		else:
			QMessageBox.information(None, 'Listar', 'Não existem clientes cadastrados')
			self.QtStack.setCurrentIndex(6)

	def btnListProd(self):

		if(self.cadastra_produto.lista_produtos != []):
			self.QtStack.setCurrentIndex(10)

			for qtd, prod in  enumerate(self.cadastra_produto.lista_produtos):
				info = "Produto: {}\nCódigo:\nNome: {}\nValor:\nQuantidade: {}\n" \
				.format(qtd+1, prod.codigo, prod.nome, prod.valor, prod.quantidade)
				self.tela_listDados.listWidget.addItem(info)

		else:
			QMessageBox.information(None, 'Listar', 'Não existem produtos cadastrados')
			self.QtStack.setCurrentIndex(6)
	
	def clear_area(self):
		self.tela_listDados.listWidget.clear()
		self.QtStack.setCurrentIndex(6)

		

if __name__ == "__main__":
    app = QApplication(sys.argv)
    show_main = Main()
    sys.exit(app.exec_())
