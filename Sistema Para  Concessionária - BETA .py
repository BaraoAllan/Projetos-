print('                 CONCESSIONÁRIA') #(nome)#               ')

print('------------------MENU PRINCIPAL-----------------')
listacarros = []

def cadastrarcarro(codigo):

 print('Você selecionou a opção de Cadastrar carro')

 print('O código da carro é: {:0>3}'.format(codigo))

 nome = input('Entre com o nome da carro:')

 tipo = input('Entre com o tipo da carro:')

 # TIPOS DE CARROS :
 # Hatchs;
 # Sedans;
 # SUVs;
 # Picapes;
 # Utilitários

 valor = float(input('Entre com o valor R$ do carro:'))

#Insira valor inteiro, sem virgula e pontos

 dicionariocarro = {'codigo'   : codigo,

                        'nome' : nome,

                        'tipo': tipo,

                        'valor': valor}

 listacarros.append(dicionariocarro.copy())

def consultarcarros():

 while True:

   try:

     print('Você Selecionou a Opção de Consultar carros')

     opConsultar = int(input('Entre com a opção desejada\n1- Consultar Todas os carros\n2- Consultar carros por Código\n3- Consultar carros por tipo\n4- Retornar\n-->'))

     if opConsultar == 1:

       print('-' * 20)

       for carros in listacarros:

           for key, value in carros.items():

             print('{} : {}'.format(key,value))

           print('-' * 20)

     elif opConsultar == 2:

       print('Você Selecionou a Opção carros por Código')

       entrada = int(input('Digite o Código: '))

       print('-' * 20)

       for carros in listacarros:

         if(carros['codigo'] == entrada):

           for key, value in carros.items():

             print('{} : {}'.format(key,value))

           print('-' * 20)

     elif opConsultar == 3:

       print('Você Selecionou a Opção carros por tipo')

       entrada = input('Digite o tipo: ')

       print('-' * 20)

       for carros in listacarros:

         if(carros['tipo'] == entrada):

           for key, value in carros.items():

             print('{} : {}'.format(key,value))

           print('-' * 20)

     elif opConsultar == 4:

       break

     else:

       print('Você insiriu valores incorretors')

       continue

   except ValueError:

     print('Você insiriu valores que não existem...')

     continue

def removercarro():

   print('Você Selecionou o Remover carros')

   entrada = int(input('Digite o Código da carros que irá remover: '))

   for carros in listacarros:

     if(carros['codigo'] == entrada):

       listacarros.remove(carros)

   else:

     print('Você removeu o código.')



registrocarros = 0

while True:

   try:

     opcao = int(input('Digite a opção desejada:\n1- Cadastrar carros\n2- Consultar carros\n3- Remover carros\n4- Sair\n-->'))


     if opcao == 1:

       registrocarros = registrocarros + 1

       cadastrarcarro(registrocarros)

     elif opcao == 2:

       consultarcarros()

     elif opcao == 3:

       removercarro()

     elif opcao == 4:

       print('Programa finalizado')

       break

     else:

       print('Digite somente uma das opções do MENU')

       continue

   except ValueError:

       print('Numeros invalidos...')



#FEITO POR BaraoAllan