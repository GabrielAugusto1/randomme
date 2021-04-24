import sqlite3 

def createdb():
    connection = sqlite3.connect('projetoip2.db')
    cursor = connection.cursor()
    #tabela professor, disciplina, aluno e turma
    cursor.execute('CREATE TABLE IF NOT EXISTS dadosprof (nome TEXT, cpf INTEGER NOT NULL, depto TEXT')
    cursor.execute('CREATE TABLE IF NOT EXISTS dadosdisc (codigod TEXT NOT NULL, nome TEXT NOT NULL')
    cursor.execute('CREATE TABLE IF NOT EXISTS dadosaluno (cpf INTEGER NOT NULL, nome TEXT NOT NULL')
    cursor.execute('CREATE TABLE IF NOT EXISTS dadosturma (codigot TEXT, periodo TEXT, codigod TEXT, cpfp INTEGER, cpfa INTEGER')
    connection.close()




class Pessoa:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

class Professor(Pessoa):
    def __init__(self, nome, cpf, depto):
        Pessoa.__init__(nome, cpf)
        self.depto = depto
    
    def profCREATE():
        try:
            connection = sqlite3.connect('projetoip2.db')
            self.cursor = self.connection.cursor()
            #SOLICITANDO DADOS
            nome = input('Nome: ')
            cpf = input('Cpf: ')
            depto = input('Departamento: ')
            #JOGANDO NA TABELA
            self.cursor.execute('INSERT INTO dadosprof (nome, cpf, depto) VALUES (?, ?, ?)', (nome, cpf, depto))
            self.connection.commit()
            self.connection.close()
            print("Professor cadastrado com sucesso!!!")
        except:
            print('Ocorreu um erro não esperado!!')
            self.connection.close()

            


    def profREAD():
        try:
            self.connection = sqlite3.connect('projetoip2.db')
            self.cursor = self.connection.cursor()
            readcpf = input('Digite o cpf do professor: ')
            self.cursor.execute('SELECT * FROM projetoip2 WHERE cpf = %d'(readcpf))
            data = self.cursor.fetchone()
            print('Nome: ', data[0])
            print('Cpf: ', data[1])
            print('Departamento: ', data[2])
            self.connect.close()
        except:
            print('Ocorreu um erro não esperado!!')
            self.connection.close()

    def profUPDATE():
        self.connection = sqlite3.connect('projetoip2.db')
        self.cursor = self.connection.cursor()
        readcpf = input('Digite o cpf do professor: ')
        self.cursor.execute('UPDATE dadosprof')
        pass

    def profDELETE():
        pass

class Disciplina:
    def __init__(self, codigod, nome):
        self.codigod = codigod
        self.nome = nome

    def disciplinaCREATE():
        pass

    def disciplinaREAD():
        pass

    def disciplinaUPDATE():
        pass

    def disciplinaDELETE():
        pass

class Aluno(Pessoa):
    def __init__(self, nome, cpf):
        Pessoa.__init__(nome, cpf)
        
    def alunoCREATE():
        connection = sqlite3.connect('projetoip2.db')
        cursor = connection.cursor()
        #SOLICITANDO DADOS
        nome = input('Nome: ')
        cpf = input('Cpf: ')
        #JOGANDO NA TABELA
        cursor.execute('INSERT INTO projetoip2 (nome, cpf,  VALUES (?, ?)', (nome, cpf))
        connection.commit()
        connection.close()
        print("Professor adicionado com sucesso!!!")

    def alunoREAD():
        pass

    def alunoUPDATE():
        pass

    def alunoDELETE():
        pass

class Turma:
    def __init__(self, codigot, periodo, codigod, cpf, cpf):
        self.codigot = codigot
        self.periodo = periodo
        self.codigod = codigod
        self.pessoa.Professor = cpfa
        self.cpfp = cpfp

    def disciplinaCREATE():
        pass

    def disciplinaREAD():
        pass

    def disciplinaUPDATE():
        pass

    def disciplinaDELETE():
        pass
