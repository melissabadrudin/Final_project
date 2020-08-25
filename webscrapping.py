#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 09:44:16 2020

@author: melissabadrudin
"""


#!python
#Imports
import time
import  requests, bs4
#Variaveis
marca=[]
modelo=[]
combustivel=[]
ano=[]
km=[]
potencia=[]
portas=[]
lugares=[]
mudancas=[]
potencia=[]
cilindrada=[]
caixa=[]
ac=[]
condition=[]
precos=[]
#Primeira página. Caso pretenda recomeçar, apenas troque este valor para
#a última página visitada.
pagina=1

pages_file = open('pages.txt','r')
pages_limit=pages_file.readline()

while pagina<=int(pages_limit):
    try:
        destaques=requests.get('https://www.standvirtual.com/carros/?search%5Border%5D=created_at%3Adesc&page='+str(pagina)) #Permite a cada iteração visitar uma página diferente
        anunciosNaoProcessados=bs4.BeautifulSoup(destaques.text,"html.parser")

        print('teste')
        anuncios=anunciosNaoProcessados.findAll('a',"offer-item__photo-link") #Procura qualquer elemento "a" com o nome de classe descrito.
        
        ficheiro=open('precos2.csv','a') #Inicialização do ficheiro csv para guardar os dados
        
        #Para cada link obtido em anuncios, retirar a informação prentendida de cada veículo.
        for i in range(len(anuncios)):
            
            res=requests.get(anuncios[i].get('href'))
            res.raise_for_status()
            paginasoup=bs4.BeautifulSoup(res.text, "html.parser")
            pagina2=paginasoup.findAll("li","offer-params__item")
            string3=paginasoup.findAll("span","offer-price__number")
            for j in range(len(pagina2)):
                string=pagina2[j].getText().replace(" ","")
                string2=[line for line in string.split('\n') if line.strip() !='']
                if string2[0]=='Marca':
                    marca.append(string2[1])
                elif string2[0]=='Modelo':
                    modelo.append(string2[1])
                elif string2[0]=='Combustível':
                    combustivel.append(string2[1])
                elif string2[0]=='Quilómetros':
                    km.append(string2[1].replace('km',''))
                elif string2[0]=='Potência':
                    potencia.append(string2[1])
                elif string2[0]=='Nºdeportas':
                    portas.append(string2[1])
                elif string2[0]=='Lotação':
                    lugares.append(string2[1])
                elif string2[0]=='NúmerodeMudanças':
                    mudancas.append(string2[1])
                elif string2[0]=='AnodeRegisto':
                    ano.append(string2[1])
                elif string2[0]=='Potência':
                    potencia.append(string2[1])
                elif string2[0]=='Cilindrada':
                    cilindrada.append(string2[1].replace('cm3',''))
                elif string2[0]=='TipodeCaixa':
                    caixa.append(string2[1])
                elif string2[0]=='ArCondicionado':
                    ac.append(string2[1])
                elif string2[0]=='Condição':
                    condition.append(string2[1])

            #Limpar a informação de espaços em branco e da indicação da moeda(EUR)
            precos.append(string3[0].getText().replace(" ","").replace('EUR',''))
            
        for j in range(min(len(marca),len(modelo),len(ano),len(precos),len(portas),len(lugares),len(mudancas))):
            ficheiro.write(str(marca[j])+','+str(modelo[j])+','+str(ano[j])+','+str(km[j])+','+str(portas[j])+','+str(lugares[j])+','+str(mudancas[j])+','+str(combustivel[j])+','+str(potencia[j])+','+str(cilindrada[j])+','+str(caixa[j])+','+str(ac[j])+','+str(condition[j])+','+str(precos[j]))
            
        print("Página "+str(pagina)+" concluída com sucesso")
        ficheiro.close()
        marca=[]
        modelo=[]
        combustivel=[]
        ano=[]
        km=[]
        potencia=[]
        portas=[]
        lugares=[]
        mudancas=[]
        precos=[]
        #Passar para a página seguinte.
    except:
        print('error_continue')
    pagina=pagina+1