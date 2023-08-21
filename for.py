
import sys
planos_info=("10 reais 2gb com validade de 1 semana \n 20 reais 4 gb com 15 dias de validade para usar com whatsapp 120min de chamadas durante os 15 dias\n 30 reais 10gb mensais para gastar como quiser e ligar para todas as operadores utilizando bônus de 8h por dia e sms ilimitados + whatsapp ilimitado incluindo video chamadas! não perca essa promoção dos sonhos ")
number=-1
# start do bloco de autoatendimento
while number != 0: 
    number = int (input (" selecione uma atividade. \n [1] para recarregar o celular \n [2] para ver os planos disponiveis \n [3] para mudar o plano\n[4] para falar com um humano! \n [0] para sair \n "))
    #inicio da função
    if number != 1 and number != 2 and number != 3 and number != 0 and number != 4:
        print ("não entendi. tente novamente!")
        #inicio do bloco de recarga
    elif number == 1:
        recarga = -1
        while recarga  !=9:
            recarga= int (input("selecione um valor \n [1] R$ 10,00 \n [2] R$ 20,00 \n [3] R$ 30,00 \n [0] para encerrar o atendimento\n [9] para voltar ao menu anterior\n " ))
            if recarga ==1:
                print(" e... realizado a recarga de 10,00 com sucesso!")
                break
            elif recarga==2:
                print("e... realizado a recarga de 20,00 com sucesso!")
                break
            elif recarga==3:
                print("e... realizado a recarga de 30,00!")
                break
            elif recarga==0:
                print("finalizando atendimento!")
                sys.exit()
            else:
                print ("não entendi tente novamente")
    #start dos blocos de informações
    elif number == 2:
        print (planos_info)
        #inicio do bloco de mudança de planos
    elif number == 3:
        plano=1
        while plano !=0:
            plano=int(input ("seu plano atual é o plano básico de 10 reais\n [9] para ver os planos disponiveis\n [2] para o plano de 20 reais \n [3] para o plano de 30 reais\n [0] para sair\n" ) )
            if plano == 9:
                print(planos_info)
            elif plano ==2:
                print("realizada a mudança de plano para o intermediario o valor também foi atualizado!\n faça uma recarga de R$20,00 e comece aproveitar o seu plano")
                break
            elif plano == 3:
                print("realizada a mudança de plano para o avançado e atualizamos o valor da cobrança, recarregue 30 reais e comece a utilizar seu plano mensal! ")
                break
            else:
                print ("não entendi tente novamente")
                
    elif number == 4:
        print("me perdoe por ser incapaz de resolver seu problema! estou passando para um de nossos atendentes e encerrando este canal...")
        sys.exit
        
print("obrigado por usar nosso sistema de auto atendimento! volte sempre que precisar.")
        