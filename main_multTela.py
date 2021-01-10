import sys

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox

from cadastra_pessoa import *
from tela_cadastro_cliente import Tela_cadastro_cliente
from tela_cadastro_funcionario import Tela_cadastro_funcionario
from tela_inicial import Tela_inicial
from tela_primeiro_acesso import Tela_primeiro_acesso
from tela_login_funcionario import Tela_login_func

class Ui_main(QtWidgets.QWidget):
	def setupUi(self, Main):
		Main.setObjectName('Main')
		Main.resize(640, 480)
	
		self.QtStack = QtWidgets.QStackedLayout()

		self.stack0 = QtWidgets.QMainWindow()
		self.stack1 = QtWidgets.QMainWindow()
		self.stack2 = QtWidgets.QMainWindow()
		# self.stack3 = QtWidgets.QMainWindow()

		self.primeiro_acesso = Tela_primeiro_acesso()
		self.primeiro_acesso.setupUi(self.stack0)

		self.tela_inicial = Tela_inicial()
		self.tela_inicial.setupUi(self.stack1)

		self.tela_login_func = Tela_login_func()
		self.tela_login_func.setupUi(self.stack2)

		# self.tela_cadastro_funcionario = Tela_cadastro_funcionario()
		# self.tela_cadastro_funcionario.setupUi(self.stack2)
		#
		# self.tela_cadastro_cliente = Tela_cadastro_cliente()
		# self.tela_cadastro_cliente.setupUi(self.stack3)


		self.QtStack.addWidget(self.stack0)
		self.QtStack.addWidget(self.stack1)
		self.QtStack.addWidget(self.stack2)

class Main(QMainWindow, Ui_main):
	def __init__(self, parent=None):
		super(Main, self).__init__(parent)
		self.setupUi(self)

		# cadastro de cliete
		self.cadastra_cliente = Cadastra_pessoa()

		# cadastro de funcionario
		self.cadastra_funcionario = Cadastra_funcionario()

		#Interação tela primeiro acesso
		self.primeiro_acesso.pushButton.clicked.connect(self.primeiro_cadastro)
		self.primeiro_acesso.pushButton_2.clicked.connect(QtCore.QCoreApplication.instance().quit)
		
		# Interação tela inicial
		self.tela_inicial.pushButton.clicked.connect(lambda: self.QtStack.setCurrentIndex(2))
		self.tela_inicial.pushButton_3.clicked.connect(QtCore.QCoreApplication.instance().quit)

		#Interação tela login funcionario
		self.tela_login_func.pushButton.clicked.connect(self.btnLoginFunc)
		self.tela_login_func.pushButton_2.clicked.connect(lambda: self.QtStack.setCurrentIndex(1))

		# Interação tela cadastra funcionario
		# self.tela_cadastro_funcionario.pushButton.clicked.connect(self.btnCadastra_func)
		# self.tela_cadastro_funcionario.pushButton_2.clicked.connect(lambda: self.QtStack.setCurrentIndex(0))

		# Interação tela cadastra cliente
		#self.tela_cadastro_cliente.pushButton.clicked.connect(self.btnCadastra_cliente)
		#self.tela_cadastro_cliente.pushButton_2.clicked.connect(lambda: self.QtStack.setCurrentIndex(0))


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
				pass
			else:
				QMessageBox.information(None, 'Login', 'Cpf não encotrado')

		else:
			QMessageBox.information(None, 'Login', 'Informe seu cpf')


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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    show_main = Main()
    sys.exit(app.exec_())
