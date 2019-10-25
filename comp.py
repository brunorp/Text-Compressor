#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import string

arg1 = sys.argv[1]
arq = sys.argv[2]

if arg1 == '-c':
    cont = 0
    contaPalavra = 0
    palavras = []
    dicio = {}
    p = 0
    arquivo_desc = open(arq, 'r')
    arquivo_desc = arquivo_desc.read();


    conteudo_arquivo = arquivo_desc.split()
    tira_ponto = ''.join([c for c in arquivo_desc if c
                            not in string.punctuation])
    x = tira_ponto.split()

    for palavra in x:
        if palavra not in palavras and len(palavra) > 3:
            palavras.append(palavra)
            dicio[p] = {'palavra': palavra, 'comp': 2}
            p += 1

    numB = len(palavras)
    numA = 0
    arquivo_comp = open('arquivo_comp.txt', 'wb')

    if len(palavras) > 255:
        numA = len(palavras) / 256
        numB = len(palavras) % 256
        arquivo_comp.write('%c%c' % (chr(numA), chr(numB)))
    else:
        arquivo_comp.write('%c%c' % (chr(numA), chr(numB)))

    for i in range(len(palavras)):
        arquivo_comp.write('%s,' % palavras[i])

    contaPalavraA = 0
    contaPalavraB = 0

    for i in range(len(palavras)):
        if len(palavras[i]) > 3:
            if dicio[i]['palavra'] in x:
                if contaPalavraB > 255:
                    contaPalavraA = contaPalavraB / 256
                    contaPalavraB = contaPalavraB % 256
                    dicio[i]['comp'] = '%c%c%c ' % (chr(255),
                            chr(contaPalavraA), chr(contaPalavraB))
                    contaPalavraB += 1
                else:
                    dicio[i]['comp'] = '%c%c%c ' % (chr(255),
                            chr(contaPalavraA), chr(contaPalavraB))
                    contaPalavraB += 1

    for palavra in conteudo_arquivo:
        if palavra[-1] in string.punctuation:
            if len(palavra[0:-1]) > 3:
                for i in range(len(dicio)):
                    if palavra[0:-1] in dicio[i]['palavra']:
                        arquivo_comp.write('%s%c ' % (dicio[i]['comp'],
                                palavra[-1]))
            else:
                arquivo_comp.write('%s' % palavra)
        else:
            if len(palavra) > 3:
                for i in range(len(dicio)):
                    if palavra in dicio[i]['palavra']:
                        arquivo_comp.write(dicio[i]['comp'])
            else:
                arquivo_comp.write('%s ' % palavra)

    arquivo_comp.close()
elif arg1 == '-d':
	
	arq_comp = open(arq, 'rb')
	arq_comp = arq_comp.read();
	palavras = {}
	comprimido = []
	contaPalavraA = 0
	contaPalavraB = 0
	arquivo_desc = open('arquivo_desc.txt', 'w')

	print(ord(arq_comp[1]))
	soma = (ord(arq_comp[0])*256) + ord(arq_comp[1])		
	conteudo_arquivo = arq_comp[2:].split(',', soma)
	conteudo_comprimido = conteudo_arquivo[-1]

	for i in range(soma):
		if contaPalavraB > 255:
			contaPalavraA = contaPalavraB / 256
			contaPalavraB = contaPalavraB % 256
			palavras[i] = {'palavra': conteudo_arquivo[i],
							'comp': '%c%c%c' % (chr(255),
							chr(contaPalavraA), chr(contaPalavraB))}
			contaPalavraB += 1
		else:
			palavras[i] = {'palavra': conteudo_arquivo[i],
							'comp': '%c%c%c' % (chr(255),
							chr(contaPalavraA), chr(contaPalavraB))}
			contaPalavraB += 1
		
	print(palavras[16]);
	print(palavras[38]);
	print(palavras)
 
    #Substitui todos códigos ASCII pelas palavras certas e adiciona espaços.
	for i in range(len(palavras)):
		if(palavras[i]['comp'] in conteudo_comprimido):
			conteudo_comprimido = conteudo_comprimido.replace(palavras[i]['comp'], " " +palavras[i]['palavra'] + " ")
			conteudo_comprimido = conteudo_comprimido.replace('  ',' ')
	conteudo_comprimido_list = list(conteudo_comprimido) #Transforma o conteúdo comprimido em um array de caracteres

	#Tira o espaço de antes dos pontos.
	for i in range(len(conteudo_comprimido_list)):
		if conteudo_comprimido_list[i] in string.punctuation:
			conteudo_comprimido_list[i-1] = "";

	arquivo_desc.write("".join(conteudo_comprimido_list).strip())
