#Criar um menu
print("LI PERSONAL DIAGNÓSTICO")
print("Bem vindo à  LI (Leitura Instrucional)")
print("Sua plataforma de auxílio ao Professor de Educação física")
print("Aqui você receberá os resultados importantes,")
print("que ajudarão a elaborar o plano de treino personalizado.") 
print()
print()
print("PERSONAL DIAGNÓSTICO") 
print()
print()
print("1: Intruções básicas")
print("2: Iniciar Avaliação")
print("3: Referências dos cálculos ")
print("4: Sair")



# Obter a opção do usuário

op = int(input("Digite a opção desejada:"))


while (op != 4):

        if(op == 1):
                print()
                print()
                print()
                print("Olá! Eu sou a LI.")
                print("Vou ajudar a você a organizar, calcular e laudar dados para a construção de um treino de educação física.")
                print("Para usar os meus recursos será necessário algumas ferramentas:")
                print("1 - Fita métrica")
                print("2 - Medidor de pressão arterial")
                print("3 - Medidor de Frenquência cardíaca ou relógio")
                print("4 - Balança de Bioimpedância")
                print()
                print("Bom trabalho!")
                print()
                print()
                









        
        if(op == 2):
                
        #Coleta de dados
                    
                nome = input("Digite Nome:")
                idade = int(input("Digite a idade:"))
                sexo = int(input("Qual o Sexo?  Masculino(1) ou Feminino(2):"))
                print("Nas perguntas a seguir responda:  (1)SIM ou (2)NÃO:")

        #Questionário PARQ-you
                parq1 = int(input("Alguma vez seu médico disse que você possui algum problema cardíaco e recomendou que você só praticasse atividade física sob prescrição médica:"))       
                parq2 = int(input("Você sente dor no tórax quando pratica uma atividade física:"))
                parq3 = int(input("No último mês você sentiu dor torácica quando não estava praticando atividade física:"))
                parq4 = int(input("Você perdeu o equilíbrio em virtude de tonturas ou perdeu a consciência quando estava praticando atividade física:"))
                parq5 = int(input("Você tem algum problema ósseo ou articular que poderia ser agravado com a prática de atividades físicas:"))
                parq6 = int(input("Seu médico já recomendou o uso de medicamentos para controle da sua pressão arterial ou condição cardiovascular:"))
                parq7 = int(input("Você tem conhecimento de alguma outra razão física que o impeça de participar de atividades físicas:"))
                        

                        
                ngv = float(input("Digite o nível de gordura viceral:"))
                idc = float(input("Digite a idade corporal:"))
                mb = float(input("Digite o metabolismo:"))
                pme = float(input("Digite a porcentagem de músculos esqueléticos:"))
                pgc = float(input("Digite a porcentagem de gordura corporal:"))
                fc = float(input("Digite a Frequência Cardiáca:"))
                cc = float(input("Digite a circunferência da cintura:"))
                #cq = float(input("Digite a circunferência do quadril:"))
                #cp = float(input("Digite a circunferência do pescoço:"))
                peso =  float(input("Digite o peso:"))
                altura = float(input("Digite o altura:"))
                papas = float(input("Digite a Pressão arterial (PAS):"))
                papad = float(input("Digite a Pressão arterial (PAD):"))


        #Gênero
                if (sexo==1):
                        gen = str("Masculino")
                if (sexo == 2):
                        gen = str("Feminino")
                

                
        #resultado imc
                imc = float(peso/(altura*altura))
                if (imc < 18.5):
                        rimc = str("Abaixo do peso")
                if (imc >= 18.5 and imc < 25):
                        rimc = str("Normal")
                if (imc >= 25 and imc < 30):
                        rimc = str("Sobrepeso")
                if (imc >= 30):
                        rimc = str("Obeso")
        #Níveis de intensidade FCMáxima
                        
                fcmax = float(207-(0.7*idade))
                leve = float((65*fcmax)/100)
                mode = float((75*fcmax)/100)
                vigo = float((85*fcmax)/100)
                
        #Pressão arterial

                if (papas < 120 and papad < 80):
                    rpa = str("Normal")
                if ((papas >= 120 and papas <= 139) or (papad >= 80 and papad <= 89)):
                    rpa = str("Pré-hipertensão")
                if ((papas >= 140 and papas <= 159) or (papad >= 90 and papad <= 99)):
                    rpa = str("Hipertensão estágio 1")
                if ((papas >= 160 or papad >= 100)):
                    rpa = str("Hipertensão estágio 2")

        # RESULTADO DA GORDURA VICERAL

                if (ngv <= 9):
                    rngv = str("Normal")
                if (ngv >= 10 and ngv <= 14):
                    rngv = str("Alto")
                if (ngv >= 15):
                    rngv = str("Muito Alto")
        #resultado gordura corporal

                print(sexo) 
                if (sexo == 2 and idade >= 20 and idade <= 39 and pgc < 21):
                    rpgc = ("Baixo")
                if (sexo == 2 and idade >= 20 and idade <= 39 and pgc >= 21 and pgc <= 32.9):
                    rpgc = ("Normal")
                if (sexo == 2 and idade >= 20 and idade <= 39 and pgc >= 33 and pgc <= 38.9):
                    rpgc = ("Alto")
                if (sexo == 2 and idade >= 20 and idade <= 39 and pgc >= 39):
                    rpgc = str("Muito Alto")
                if (sexo == 2 and idade  >= 40 and idade <= 59 and pgc < 23):
                    rpgc = str("Baixo")
                if (sexo == 2 and idade  >= 40 and idade <= 59 and pgc >= 23 and pgc <= 33.9):
                    rpgc = str("Normal")
                if (sexo == 2 and idade  >= 40 and idade <= 59 and pgc >= 34 and pgc <= 39.9):
                    rpgc = str("Alto")
                if (sexo == 2 and idade  >= 40 and idade <= 59 and pgc >= 40):
                    rpgc = str("Muito Alto")    
                if (sexo == 2 and idade  >= 60 and idade <= 79 and pgc < 24):
                    rpgc = str("Baixo")
                if (sexo == 2 and idade  >= 60 and idade <= 79 and pgc >= 24 and pgc <= 35.9):
                    rpgc = str("Normal")
                if (sexo == 2 and idade  >= 60 and idade <= 79 and pgc >= 36 and pgc <= 41.9):
                    rpgc = str("Alto") 
                if (sexo == 2 and idade  >= 60 and idade <= 79 and pgc >= 42):
                    rpgc = str("Muito Alto") 
                if (sexo == 1 and idade  >= 20 and idade <= 39 and pgc < 8):
                    rpgc = ("Baixo")
                if (sexo == 1 and idade >= 20 and idade <= 39 and pgc >= 8 and pgc <= 19.9):
                    rpgc = ("Normal")
                if (sexo == 1 and idade  >= 20 and idade <= 39 and pgc >= 20 and pgc <= 24.9):
                    rpgc = ("Alto") 
                if (sexo == 1 and idade  >= 20 and idade <= 39 and pgc >= 25):
                    rpgc = ("Muito Alto")
                if (sexo == 1 and idade  >= 40 and idade <= 59 and pgc < 11):
                    rpgc = ("Baixo")
                if (sexo == 1 and idade  >= 40 and idade <= 59 and pgc >= 11 and pgc <= 21.9):
                    rpgc = ("Normal")
                if (sexo == 1 and idade  >= 40 and idade <= 59 and pgc >= 22 and pgc <= 27.9):
                    rpgc = ("Alto") 
                if (sexo == 1 and idade >= 40 and idade <= 59 and pgc >= 28):
                    rpgc = ("Muito Alto")        
                if (sexo == 1 and idade  >= 60 and idade <= 79 and pgc < 13):
                    rpgc = ("Baixo")
                if (sexo == 1 and idade >= 60 and idade <= 79 and pgc >= 13 and pgc <= 24.9):
                    rpgc = ("Normal")
                if (sexo == 1 and idade >= 60 and idade <= 79 and pgc >= 25 and pgc <= 29.9):
                    rpgc = ("Alto") 
                if (sexo == 1 and idade >= 60 and idade <= 79 and pgc >= 30):
                    rpgc = str("Muito Alto")

        #Resultado músculo esquelético

                if (sexo == 2 and idade >= 18 and idade <= 39 and pme < 24.3):
                    rpme = str("Baixo")
                if (sexo == 2 and idade >= 18 and idade <= 39 and pme >= 24.3 and pme <= 30.3):
                    rpme = str("Normal")
                if (sexo == 2 and idade >= 18 and idade <= 39 and pme >= 30.4 and pme <= 35.3):
                    rpme = str("Alto")
                if (sexo == 2 and idade >= 18 and idade <= 39 and pme >= 35.4):
                    rpme = str("Muito Alto")
                if (sexo == 2 and idade >= 40 and idade <= 59 and pme < 24.1):
                    rpme = str("Baixo")
                if (sexo == 2and idade >= 40 and idade <= 59 and pme >= 24.1 and pme <= 30.1):
                    rpme = str("Normal")
                if (sexo == 2and idade >= 40 and idade <= 59 and pme >= 30.2 and pme <= 35.1):
                    rpme = str("Alto")
                if (sexo == 2 and idade >= 40 and idade <= 59 and pme >= 35.2):
                    rpme = str("Muito Alto")
                if (sexo == 2 and idade >= 60 and idade <= 80 and pme < 23.9):
                    rpme = str("Baixo")
                if (sexo == 2 and idade >= 60 and idade <= 80 and pme >= 23.9 and pme <= 29.9):
                    rpme = str("Normal")
                if (sexo == 2 and idade >= 60 and idade <= 80 and pme >= 30.0 and pme <= 34.9):
                    rpme = str("Alto")
                if (sexo == 2 and idade >= 60 and idade <= 80 and pme >= 35.0):
                    rpme = str("Muito Alto")
                if (sexo == 1 and idade >= 18 and idade <= 39 and pme < 33.3):
                    rpme = str("Baixo")
                if (sexo == 1 and idade >= 18 and idade <= 39 and pme >= 33.3 and pme <= 39.3):
                    rpme = str("Normal")
                if (sexo == 1 and idade >= 18 and idade <= 39 and pme >= 39.4 and pme <= 44.0):
                    rpme = str("Alto")
                if (sexo == 1 and idade >= 18 and idade <= 39 and pme >= 44.1):
                    rpme = str("Muito Alto")
                if (sexo == 1 and idade >= 40 and idade <= 59 and pme < 33.1):
                    rpme = str("Baixo")
                if (sexo == 1 and idade >= 40 and idade <= 59 and pme >= 33.1 and pme <= 39.1):
                    rpme = str("Normal")
                if (sexo == 1 and idade >= 40 and idade <= 9 and pme >= 39.2 and pme <= 43.8):
                    rpme = str("Alto")
                if (sexo == 1 and idade >= 40 and idade <= 9 and pme >= 43.9):
                    rpme = str("Muito Alto")
                if (sexo == 1 and idade >= 60 and idade <= 80 and pme < 32.9):
                    rpme = str("Baixo")
                if (sexo == 11and idade >= 60 and idade <= 80 and pme >= 32.9 and pme <= 38.9):
                    rpme = str("Normal")
                if (sexo == 1 and idade >= 60 and idade <= 80 and pme >= 39.0 and pme <= 43.6):
                    rpme = str("Alto")
                if (sexo ==  1 and idade >= 60 and idade <= 80 and pme >= 43.7):
                    rpme = str("Muito Alto")



        #Resultado Risco de doença relativo ao peso e circunferência da cintura

                if (sexo == 1 and imc < 18,5 and cc <= 102):
                    rdrpcc = str("Sem risco")
                if (sexo == 1 and imc >= 18,5 and imc <= 24,9 and cc <= 102):
                    rdrpcc = str("Sem risco")
                if (sexo == 1 and imc >= 25 and imc <= 29,9 and cc <= 102):
                    rdrpcc = str("Risco aumentado")    
                if (sexo == 1 and imc >= 30 and imc <= 34,9 and cc <= 102):
                    rdrpcc = str("Risco alto")
                if (sexo == 1 and imc >= 35 and imc <= 39,9 and cc <= 102):
                    rdrpcc = str("Risco muito alto")

                if (sexo == 1 and imc < 18,5 and cc > 102):
                    rdrpcc = str("Sem risco")
                if (sexo == 1 and imc >= 18,5 and imc <= 24,9 and cc > 102):
                    rdrpcc = str("Sem risco")
                if (sexo == 1 and imc >= 25 and imc <= 29,9 and cc > 102):
                    rdrpcc = str("Risco alto")    
                if (sexo == 1 and imc >= 30 and imc <= 34,9 and cc > 102):
                    rdrpcc = str("Risco muito alto")
                if (sexo == 1 and imc >= 35 and imc <= 39,9 and cc > 102):
                    rdrpcc = str("Risco muito alto")
                if (sexo == 1 and imc >= 40  and (cc >= 88 or cc < 88)):
                    rdrpcc = str("Risco extremamente alto")

                if (sexo == 2 and imc < 18,5 and cc <= 88):
                    rdrpcc = str("Sem risco")
                if (sexo == 2 and imc >= 18,5 and imc <= 24,9 and cc <= 88):
                    rdrpcc = str("Sem risco")
                if (sexo == 2 and imc >= 25 and imc <= 29,9 and cc <= 88):
                    rdrpcc = str("Risco aumentado")    
                if (sexo == 2 and imc >= 30 and imc <= 34,9 and cc <= 88):
                    rdrpcc = str("Risco alto")
                if (sexo == 2 and imc >= 35 and imc <= 39,9 and cc <= 88):
                    rdrpcc = str("Risco muito alto")

                if (sexo == 2 and imc < 18,5 and cc > 88):
                    rdrpcc = str("Sem risco")
                if (sexo == 2 and imc >= 18,5 and imc <= 24,9 and cc > 88):
                    rdrpcc = str("Sem risco")
                if (sexo == 2 and imc >= 25 and imc <= 29,9 and cc > 88):
                    rdrpcc = str("Risco aumentado")    
                if (sexo == 2 and imc >= 30 and imc <= 34,9 and cc > 88):
                    rdrpcc = str("Risco alto")
                if (sexo == 2 and imc >= 35 and imc <= 39,9 and cc > 88):
                    rdrpcc = str("Risco muito alto")
                if (sexo == 2 and imc >= 40  and (cc >= 88 or cc < 88)):
                    rdrpcc = str("Risco extremamente alto")

                print()
                print()
                print()
        #Diagnóstico
                print("A seguir a LI irá calcular os valores importantes relacionados a seu estado físico")
                input("Pressione ENTER para continuar")
                print()
                print()
                print("LI Diagnóstico")
                print()
                print()
                print("Nome:",nome)
                print("Idade:",idade)
                print("sexo:",gen)
                print("O metabolismo está:",mb)
                print("Sua idade corporal:", idc)
                print("A circunferência da cintura mede (cm):",cc, "/ Classificação:",rdrpcc) 
                print("Frequência Cardíaca:",fc)
                print("Frequência Cardíaca Máxima:",fcmax)
                print("Níveis de Intensidade da Frequência Cardíaca para classificação de atividade:")
                print("Treino leve:",leve, "/ Treino moderado:",mode, "/ Treino vigoroso:",vigo)
                print("Pressão Arterial:",papas,"por",papad , "/  A PA indica:",rpa)
                print("O nível de gordura viceral é:",ngv, "/ O resultado indica que está", rngv)
                print("O percentual de gordura corporal é:",pgc, "/  A classificação de risco é:", rpgc)
                print("O percentual de músculo esquelético é:",pme, "/  A classificação de risco é:",rpme)
                print("IMC:", round(imc,3))
                print("Seu IMC indica:",rimc)
                if ((parq1 == 1) or (parq2 == 1) or (parq3 == 1)or(parq4 == 1)or (parq5 == 1)or (parq6 == 1)or (parq7 == 1)or(rpa == "Hipertensão estágio 1")or(rpa == "Hipertensão estágio 2")): 
                        print("Sua avaliação indicou que você deve procurar uma orientação médica antes de começar qualquer atividade física, risco cardíaco.")
                else:
                        print("Obrigado por usar a LI")
                        print()
                        print()
                        print()
                        
        


        if (op == 3):
                print()
                print()
                print("Referências dos Cálculos:")
                print()
                print()
                print("Índice de Massa Corporal - Organização Mundial de Saúde")
                print("IDADE Corporal - Omron Helthcare")
                print("METABOLISMO BASAL - Omron Helthcare")
                print("Porcentagem de Gordura Corporal - Diretrizes NIH/OMS para IMC")
                print("Porcentagem de Músculo Esquelético - Omron Helthcare")
                print("Nível de Gordura Viceral - Omron Helthcare")
                print("Frequencia Cardíaca Máxima - ACSM 2014")
                print("PARQ YOU - ACSM 2014")
                print()
     
                print()

        
        print(" LI PERSONAL DIAGNÓSTICO")
        print()
        print()
        

        print("1: Intruções básicas")
        print("2: Iniciar Avaliação")
        print("3: Referências dos cálculos ")
        print("4: Sair")
        print()
        print()

        op = int(input("Digite a opção desejada:"))
