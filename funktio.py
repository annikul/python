#funktio 2-lla parametrilla
def funktion_nimi(parametri, toinen_parametri):
    if toinen_parametri == 2:
        return parametri + '-extra-extra'
    else:
        return parametri + '-extra'



#alustetaan muuttujat inputista
parametri = input('Anna parametrin arvo: ')
toinen_parametri = int(input('Anna count arvo: '))

#suoritetaan funktio ja otetaan tulos talteen muuttujaan
funktion_palautus = funktion_nimi(parametri, toinen_parametri) 

#tulostetaan talteen otettu funktion tulos
print(funktion_palautus)


muuttuja = parametri,str(toinen_parametri),"testi"
print(muuttuja)