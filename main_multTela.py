import sys
import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog,QMessageBox
from PyQt5.QtCore import QCoreApplication 

from tela_inicial import Tela_inicial
from tela_cadastro_funcionario import Tela_cadastro_funcionario
from tela_cadastro_cliente import Tela_cadastro_cliente

from pessoa import Pessoa, Cadastra_pessoa



class Ui_main(QtWidgets.QWidget):
	def setupUi(self, Main):
		Main.setObjectName('Main')
		Main.resize(640, 480)
	
		self.QtStack = QtWidgets.QStackedLayout()

		self.stack0 = QtWidgets.QMainWindow()
		self.stack1 = QtWidgets.QMainWindow()
		self.stack2 = QtWidgets.QMainWindow()

		self.tela_inicial = Tela_inicial()
		self.tela_inicial.setupUi(self.stack0)

		self.tela_cadastro_funcionario = Tela_cadastro_funcionario()
		self.tela_cadastro_funcionario.setupUi(self.stack1)
		
		self.tela_cadastro_cliente = Tela_cadastro_cliente()
		self.tela_cadastro_cliente.setupUi(self.stack2)
		
		

		self.QtStack.addWidget(self.stack0)
		self.QtStack.addWidget(self.stack1)
		self.QtStack.addWidget(self.stack2)

class Main(QMainWindow, Ui_main):
	def __init__(self, parent=None):
		super(Main, self).__init__(parent)
		self.setupUi(self)

		self.cadastra_pessoa = Cadastra_pessoa()

		# Interação tela inicial
		self.tela_inicial.pushButton.clicked.connect(lambda: self.QtStack.setCurrentIndex(1))
		self.tela_inicial.pushButton_2.clicked.connect(lambda: self.QtStack.setCurrentIndex(2))
		self.tela_inicial.pushButton_3.clicked.connect(QtCore.QCoreApplication.instance().quit)

		# Interação tela cadastra funcionario
		self.tela_cadastro_funcionario.pushButton_2.clicked.connect(lambda: self.QtStack.setCurrentIndex(0))



	# 	self.tela_cadastro.pushButton.clicked.connect(self.btnCadastra)
	# 	self.tela_cadastro.pushButton_2.clicked.connect(lambda: self.QtStack.setCurrentIndex(0))

	# 	self.tela_busca.pushButton.clicked.connect(self.btnBusca)
	# 	self.tela_busca.pushButton_2.clicked.connect(lambda: self.QtStack.setCurrentIndex(0))

	# def abrirTelaCadastro(self):
	# 	self.QtStack.setCurrentIndex(1)

	# def abrirTelaBusca(self):
	# 	if(self.cadastro.lista_pessoas != []):
	# 		self.QtStack.setCurrentIndex(2)
	# 	else:
	# 		QMessageBox.information(None, 'Busca', 'Não existem pessoas cadastradas')

	# def btnCadastra(self):
	# 	nome = self.tela_cadastro.lineEdit.text()
	# 	cpf = self.tela_cadastro.lineEdit_2.text()
	# 	end = self.tela_cadastro.lineEdit_3.text()
	# 	nasc = self.tela_cadastro.lineEdit_4.text()

	# 	if(not(nome == '' or cpf == '' or end == '' or nasc == '')):
	# 		pessoa = Pessoa(nome, cpf, end, nasc);

	# 		if(self.cadastro.cadastra(pessoa)):
	# 			QMessageBox.information(None, 'Cadastro', 'Cadastro realizado com sucesso')
	# 			self.tela_cadastro.lineEdit.setText('')
	# 			self.tela_cadastro.lineEdit_2.setText('')
	# 			self.tela_cadastro.lineEdit_3.setText('')
	# 			self.tela_cadastro.lineEdit_4.setText('')
	# 		else:
	# 			QMessageBox.information(None, 'Cadastro', 'CPF informado já cadastrado')
       
	# 	else:
	# 		QMessageBox.information(None, 'Cadastro', 'Informe todos os dados')
		
	# def btnBusca(self):
	# 	cpf = self.tela_busca.lineEdit.text()

	# 	if(cpf != ''):
	# 		pessoa = self.cadastro.busca(cpf)
			
	# 		if(pessoa != None):

	# 			self.tela_busca.lineEdit.setText('')
	# 			self.tela_busca.lineEdit_2.setText(pessoa.nome)
	# 			self.tela_busca.lineEdit_3.setText(pessoa.cpf)
	# 			self.tela_busca.lineEdit_4.setText(pessoa.endereco)
	# 			self.tela_busca.lineEdit_5.setText(pessoa.data_nasc)

	# 		else:
 #  				QMessageBox.information(None, 'Busca', 'Dados não encotrado')
	# 	else:
 # 			QMessageBox.information(None, 'Busca', 'Preencha o campo para buscar')
            



if __name__ == "__main__":
    app = QApplication(sys.argv)
    show_main = Main()
    sys.exit(app.exec_())
