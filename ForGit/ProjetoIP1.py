#CRUD nome, cpf e departamento de PROFESSOR
#CRUD código e nome da DISCIPLINA
#CRUD nome e cpf do ALUNO
#CRUD código da turma, período, código da disciplina, cpf professor e cpf aluno (TURMA)

professorgeral = []
disciplinageral = []
alunogeral = []
turmageral = []


#PROFESSOR__________________________________________________________________________
#PROFESSOR CREATE:
def professorCREATE(tudoprofessor):
    professorgeral.append(tudoprofessor)
    print("Professor adicionado com sucesso!!!\n")
#PROFESSOR READ:
def professorREAD(cpf):
    pesquisa = False
    for i in range(len(professorgeral)):
        if cpf in professorgeral[i]:
            pesquisa = True
            print("Nome: %s"%professorgeral[i][0])
            print("CPF: %s"%professorgeral[i][1])
            print("Departamento: %s\n"%professorgeral[i][2])
            break
    if pesquisa == False:
        print("Professor não encontrado!!!\n")
#PROFESSOR UPDATE:
def professorUPDATE(cpf):
    pesquisa = False
    for i in range(len(professorgeral)):
        if cpf in professorgeral[i]:
            pesquisa = True
            print("\nEscolha o que deseja atualizar:\n")
            print("(1) Nome\n(2)Cpf\n(3)Departamento\n")
            escolha = int(input("Opção escolhida: "))
            if escolha == 1:
                nome = input("Digite o novo nome a ser inserido: \n")
                professorgeral[i][0] = nome
                print("Nome atualizado com sucesso!!!\n")
            elif escolha == 2:
                cpf1 = input("Digite o novo cpf a ser inserido: \n")
                professorgeral[i][1] = cpf1
                print("Cpf atualizado com sucesso!!!\n")
            elif escolha == 3:
                departamento = input("Digite o novo departamento a ser inserido: \n")
                professorgeral[i][2] = departamento
                print("Departamento atualizado com sucesso!!!\n")
            else:
                print("Opção invalida... Tente novamente!\n")
            break
    if pesquisa == False:
        print("Professor não encontrado!!!\n")
#PROFESSOR REMOVE:
def professorREMOVE(cpf):
    pesquisa = False
    for i in range(len(professorgeral)):
        if cpf in professorgeral[i]:
            pesquisa = True
            del professorgeral[i]
            print("Professor deletado com sucesso!!!\n")
            break
    if pesquisa == False:
        print("Professor não encontrado!!!\n")



#DISCIPLINA__________________________________________________________________________
#DISCIPLINA CREATE:
def disciplinaCREATE(tudodisciplina):
    disciplinageral.append(tudodisciplina)
    print("Disciplina adicionada com sucesso!!!\n")

#DISCIPLINA READ:
def disciplinaREAD(codigo):
    pesquisa = False
    for i in range(len(disciplinageral)):
        if codigo in disciplinageral[i]:
            pesquisa = True
            print("Código da disciplina: %s"%disciplinageral[i][0])
            print("Nome da disciplina: %s"%disciplinageral[i][1])
            break
    if pesquisa == False:
        print("Disciplina não encontrada!!!\n")
#DISCIPLINA UPDATE:
def disciplinaUPDATE(codigo):
    pesquisa = False
    for i in range(len(disciplinageral)):
        if codigo in disciplinageral[i]:
            pesquisa = True
            print("\nEscolha o que deseja atualizar:\n")
            print("(1)Código da disciplina\n(2)Nome da disciplina\n")
            escolha = int(input("Opção escolhida: "))
            if escolha == 1:
                codigo1 = input("Digite o novo Código da disciplina a ser inserido: \n")
                disciplinageral[i][0] = codigo1
                print("Código da disciplina atualizado com sucesso!!!\n")
            elif escolha == 2:
                nome = input("Digite o novo nome a ser inserido: \n")
                disciplinageral[i][1] = nome
                print("Nome atualizado com sucesso!!!\n")
            else:
                print("Opção invalida... Tente novamente!\n")
            break
    if pesquisa == False:
        print("Disciplina não encontrada!!!\n")
#DISCIPLINA REMOVE:
def disciplinaREMOVE(codigo):
    pesquisa = False
    for i in range(len(disciplinageral)):
        if codigo in disciplinageral[i]:
            pesquisa = True
            del disciplinageral[i]
            print("Professor deletado com sucesso!!!\n")
            break
    if pesquisa == False:
        print("Professor não encontrado!!!\n")

#ALUNO__________________________________________________________________________
#ALUNO CREATE:
def alunoCREATE(tudoaluno):
    alunogeral.append(tudoaluno)
    print("Aluno adicionado com sucesso!!!\n")
#ALUNO READ:
def alunoREAD(b):
    pesquisa = False
    for i in range(len(alunogeral)):
        if b in alunogeral[i]:
            pesquisa = True
            print("Cpf: %s"%alunogeral[i][0])
            print("Nome: %s"%alunogeral[i][1])
            break
    if pesquisa == False:
        print("Aluno não encontrado!!!\n")
#ALUNO UPDATE:
def alunoUPDATE(cpf):
    pesquisa = False
    for i in range(len(alunogeral)):
        if cpf in alunogeral[i]:
            pesquisa = True
            print("\nEscolha o que deseja atualizar:\n")
            print("(1)Cpf\n(2)Nome\n")
            escolha = int(input("Opção escolhida: "))
            if escolha == 1:
                cpf1 = input("Digite o novo Cpf a ser inserido: \n")
                alunogeral[i][0] = cpf1
                print("Cpf atualizado com sucesso!!!\n")
            elif escolha == 2:
                nome = input("Digite o novo nome a ser inserido: \n")
                alunogeral[i][1] = nome
                print("Nome atualizado com sucesso!!!\n")
            else:
                print("Opção invalida... Tente novamente!\n")
            break
    if pesquisa == False:
        print("Aluno não encontrado!!!\n")
#ALUNO REMOVE:
def alunoREMOVE(cpf):
    pesquisa = False
    for i in range(len(alunogeral)):
        if cpf in alunogeral[i]:
            pesquisa = True
            del alunogeral[i]
            print("Aluno deletado com sucesso!!!\n")
            break
    if pesquisa == False:
        print("Aluno não encontrado!!!\n")
#TURMA__________________________________________________________________________
#TURMA CREATE:
def turmaCREATE(tudoturma):
    turmageral.append(tudoturma)
    print("Turma criada com sucesso!!!\n")
#TURMA READ:
def turmaREAD(codigoturma):
    pesquisa = False
    for i in range(len(turmageral)):
        if codigoturma in turmageral[i][0]:
            pesquisa = True
            print("Código da turma: %s"%(turmageral[i][0]))
            print("Período: %s"%(turmageral[i][1]))
            print("Código da Disciplina: %s" % (turmageral[i][2]))
            print("Cpf do(s) professor(es): ")
            for x in range(len(turmageral[i][3])):
                print(turmageral[i][3][x])
            print("Cpf do(s) aluno(s): ")
            for y in range(len(turmageral[i][4])):
                print(turmageral[i][4][y])
            break
    if pesquisa == False:
        print("Turma não encontrada!!!\n")
#TURMA UPDATE:
def turmaUPDATE(codigoturma):
    pesquisa = False
    for i in range(len(turmageral)):
        if codigoturma in turmageral[i]:
            pesquisa = True
            print("\nEscolha o que deseja atualizar:\n")
            print("(1)Código da turma\n(2)Período\n(3)Código da Disciplina\n(4)Cpf do(s) professor(es)\n(5)Cpf do(s) aluno(s)\n")
            escolha = int(input("Opção escolhida: "))
            if escolha == 1:
                codigo = input("Digite o novo Código da turma a ser inserido: \n")
                turmageral[i][0] = codigo
                print("Código da turma atualizado com sucesso!!!\n")
            elif escolha == 2:
                periodo = input("Digite o novo Período a ser inserido: \n")
                alunogeral[i][1] = periodo
                print("Período atualizado com sucesso!!!\n")
            elif escolha == 3:
                codigo1 = input("Digite o novo Código da Disciplina a ser inserido: \n")
                alunogeral[i][2] = codigo1
                print("Código da Disciplina atualizado com sucesso!!!\n")
            elif escolha == 4:
                cpfdosprofessores = []
                while True:
                    cpf = input("Digite o(s) novo(s) cpf(s) a ser(em) insedo(s): (*Para sair, digite 0)\n")
                    if cpf == 0:
                        break
                    cpfdosprofessores.append(cpf)
                turmageral[i][3].append(cpfdosprofessores)
                print("Cpf do(s) professor(es) atualizado com sucesso!!!\n")
            elif escolha == 5:
                cpfdosalunos = []
                while True:
                    cpf1 = input("Digite o(s) novo(s) cpf(s) a ser(em) insedo(s): (*Para sair, digite 0)\n")
                    if cpf1 == 0:
                        break
                    cpfdosalunos.append(cpf1)
                turmageral[i][4].append(cpfdosalunos)
                print("Cpf do(s) aluno(s) atualizado com sucesso!!!\n")
            else:
                print("Opção invalida... Tente novamente!\n")
            break
    if pesquisa == False:
        print("Turma não encontrada!!!\n")
#TURMA REMOVE:
def turmaREMOVE(codigoturma):
    pesquisa = False
    for i in range(len(turmageral)):
        if codigoturma in turmageral[i]:
            pesquisa = True
            del turmageral[i]
            print("Turma deletada com sucesso!!!\n")
            break
    if pesquisa == False:
        print("Turma não encontrado!!!\n")

#ATA DE EXERCÍCIO:
def ataexercicio(ata):
    x = False
    a = 1
    for i in range(len(disciplinageral)):
        if ata in disciplinageral[i][0]:
            x = True
            print("________________________________Ata de exercício_________________________________")
            print("Data:___/____/______|____________________________________________________________")
            print("Código da disciplina: %s"%(disciplinageral[i][0]))
            print("Nome da disciplina: %s"%(disciplinageral[i][1]))
    for o in range(len(turmageral)):
        if ata in turmageral[o][2]:
            print("Código da turma: %s" % (turmageral[i][0]))
            print("Período: %s" % (turmageral[i][1]))
            for z in range(len(turmageral[i][3])):
                c = turmageral[i][3][z]
                for v in range(len(professorgeral)):
                    if c in professorgeral[v][1]:
                        print("Professor: %s"%(professorgeral[v][0]))
            print("\n\n")
            print("   CPF:                     Nome do Aluno:                    Assinatura:   \n")
            for b in range(len(turmageral[i][4])):
                n = turmageral[i][4][b]
                for m in range(len(alunogeral)):
                    l = str(a)
                    if n in alunogeral[m][0]:
                        print(l + "    %s              %s"%(alunogeral[m][0], alunogeral[m][1]))
                        a += 1
            print("\n\n\n_________________________________________________________________________________")
            break
    if x == False:
        print("\nDisciplina não encontrada!!!")



#COMEÇANDO O LOOP INFINITO DO MENU__________________________________________________________________________
while True:
    print("_____________________________________________________________________________________________________")
    print("____________________________________SISTEMA DE CONTROLE ACADÊMICO____________________________________")
    print("_____________________________________________________________________________________________________\n\n\n")
    print("Digite a opção desejada:\n")
    print("(1)CRUD Professores\n(2)CRUD Disciplinas\n(3)CRUD Alunos\n(4)CRUD Turmas\n(5)Ata de exercício\n")
    escolha = int(input("Opção escolhida: \n"))
    if escolha == 1: #CRUDPROFESSOR
        print("O que deseja fazer?\n(1)Criar Professor\n(2)Consultar Professor\n(3)Atualizar Professor\n(4)Deletar Professor")
        escolha1 = int(input("Opção escolhida: \n"))
        if escolha1 == 1:
            tudoprofessor = []
            nome = input("Nome do professor: ")
            tudoprofessor.append(nome)
            cpf = input("Cpf do professor: ")
            tudoprofessor.append(cpf)
            depto = input("Departamento do professor: ")
            tudoprofessor.append(depto)
            professorCREATE(tudoprofessor)

        elif escolha1 == 2:
            cpf = input("Digite o cpf do professor que deseja consultar: \n")
            professorREAD(cpf)
        elif escolha1 == 3:
            cpf = input(("Digite o cpf do professor que deseja atualizar: \n"))
            professorUPDATE(cpf)
        elif escolha1 == 4:
            cpf = input("Digite o cpf do professor que deseja deletar: \n")
            professorREMOVE(cpf)
        else:
            print("Opção invalida... Tente novamente!\n")

    if escolha == 2: #CRUD DISCIPLINA
        print("O que deseja fazer?\n(1)Criar Disciplina\n(2)Consultar Disciplina\n(3)Atualizar Disciplina\n(4)Deletar Disciplina")
        escolha2 = int(input("Opção escolhida: \n"))
        if escolha2 == 1:
            tudodisciplina = []
            codigo = input("Código da disciplina: ")
            nomedisciplina = input("Nome da disciplina: ")
            tudodisciplina.append(codigo)
            tudodisciplina.append(nomedisciplina)
            disciplinaCREATE(tudodisciplina)
        elif escolha2 == 2:
            codigo = input("Digite o código da disciplina que deseja consultar: \n")
            disciplinaREAD(codigo)
        elif escolha2 == 3:
            codigo = input(("Digite o código da disciplina que deseja atualizar: \n"))
            disciplinaUPDATE(codigo)
        elif escolha2 == 4:
            codigo = input("Digite o código da disciplina que deseja deletar: \n")
            disciplinaREMOVE(codigo)
        else:
            print("Opção invalida... Tente novamente!\n")

    if escolha == 3: #CRUD ALUNO
        print("O que deseja fazer?\n(1)Criar Aluno\n(2)Consultar Aluno\n(3)Atualizar Aluno\n(4)Deletar Aluno")
        escolha3 = int(input("Opção escolhida: \n"))
        if escolha3 == 1:
            tudoaluno = []
            cpf = input("Cpf do aluno: ")
            nomealuno = input("Nome do aluno: ")
            tudoaluno.append(cpf)
            tudoaluno.append(nomealuno)
            alunoCREATE(tudoaluno)
        elif escolha3 == 2:
            cpf = input("Digite o cpf do aluno que deseja consultar: \n")
            alunoREAD(cpf)
        elif escolha3 == 3:
            cpf = input(("Digite o cpf do aluno que deseja atualizar: \n"))
            alunoUPDATE(cpf)
        elif escolha3 == 4:
            cpf = input("Digite o cpf do aluno que deseja deletar: \n")
            alunoREMOVE(cpf)
        else:
            print("Opção invalida... Tente novamente!\n")

    if escolha == 4: #CRUD TURMA
        print("O que deseja fazer?\n(1)Criar Turma\n(2)Consultar Turma\n(3)Atualizar Turma\n(4)Deletar Turma")
        escolha4 = int(input("Opção escolhida: \n"))
        if escolha4 == 1:
            tudoturma = []
            cpfaluno = []
            cpfprof = []
            codigoturma = input("Código da turma: ")
            tudoturma.append(codigoturma)
            periodoturma = input("Período da turma: ")
            tudoturma.append(periodoturma)
            codigodisc = input("Código da disciplina: ")
            tudoturma.append(codigodisc)

            turmaCREATE(tudoturma)
            while True:
                cpf = input("Cpf do professor(para sair, digite 0): \n")
                if cpf == "0":
                    break
                else:
                    cpfprof.append(cpf)
            tudoturma.append(cpfprof)
            while True:
                cpf1 = input("Cpf do aluno(para sair, digite 0) \n")
                if cpf1 == "0":
                    break
                else:
                    cpfaluno.append(cpf1)
            tudoturma.append(cpfaluno)
            turmaCREATE(tudoturma)

        elif escolha4 == 2:
            codigoturma = input("Digite o código da turma que deseja consultar: \n")
            turmaREAD(codigoturma)
        elif escolha4 == 3:
            codigoturma = input(("Digite o código da turma que deseja atualizar: \n"))
            turmaUPDATE(codigoturma)
        elif escolha4 == 4:
            codigoturma = input("Digite o código da turma que deseja deletar: \n")
            turmaREMOVE(codigoturma)
        else:
            print("Opção invalida... Tente novamente!\n")

    if escolha == 5:
        ata = input("Digite o código da disciplina para gerar a ata:\n")
        ataexercicio(ata)
