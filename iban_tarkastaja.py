from stdnum import iban as kukuu

def main():
    tilinumero = input('Anna IBAN-tilinumero: ')
    on_oikea_iban = kukuu.is_valid(tilinumero)
    if on_oikea_iban:
        print(f'Antamasi tilinumero {tilinumero} on oikea IBAN.')
        muotoilu = iban.format(tilinumero)
        print(f'Tilinumero muotoiluna: {muotoilu}')
    else:
        print(f'Antamasi tilinumero {tilinumero} ei ole oikea IBAN.')

if __name__ == '__main__':
    main()