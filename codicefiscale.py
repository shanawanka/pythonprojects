# Funzione per il calcolo del codice fiscale
def calcola_codice_fiscale(nome, cognome, data_di_nascita, sesso, luogo_di_nascita):
    
    # Import delle librerie necessarie
    import hashlib
    import datetime
    
    # Dizionario per la conversione dei mesi in numeri
    mesi = {'01': 'A', '02': 'B', '03': 'C', '04': 'D', '05': 'E', '06': 'H',
            '07': 'L', '08': 'M', '09': 'P', '10': 'R', '11': 'S', '12': 'T'}
    
    # Estrazione dei dati dalla data di nascita
    anno = str(datetime.datetime.strptime(data_di_nascita, '%d/%m/%Y').year)[-2:]
    mese = mesi[datetime.datetime.strptime(data_di_nascita, '%d/%m/%Y').strftime('%m')]
    giorno = datetime.datetime.strptime(data_di_nascita, '%d/%m/%Y').strftime('%d')
    
    # Conversione del cognome
    cognome_consonanti = ''
    cognome_vocali = ''
    for lettera in cognome:
        if lettera in 'aeiouAEIOU':
            cognome_vocali += lettera
        else:
            cognome_consonanti += lettera
    
    if len(cognome_consonanti) >= 3:
        codice_cognome = cognome_consonanti[:3]
    else:
        codice_cognome = cognome_consonanti + cognome_vocali[:3-len(cognome_consonanti)]
    
    # Conversione del nome
    nome_consonanti = ''
    nome_vocali = ''
    for lettera in nome:
        if lettera in 'aeiouAEIOU':
            nome_vocali += lettera
        else:
            nome_consonanti += lettera
            
    if len(nome_consonanti) == 3:
        codice_nome = nome_consonanti
    elif len(nome_consonanti) > 3:
        codice_nome = nome_consonanti[0] + nome_consonanti[2] + nome_consonanti[3]
    else:
        codice_nome = nome_consonanti + nome_vocali[:3-len(nome_consonanti)]
        
    # Codice del luogo di nascita
    with open('comuni.txt', 'r', encoding='utf-8') as f:
        for line in f:
            if line.split('\t')[1] == luogo_di_nascita.upper():
                codice_luogo_di_nascita = line.split('\t')[4]
                break
    
    # Codice del sesso
    if sesso == 'Maschio':
        if int(giorno) <= 9:
            codice_sesso = '0' + giorno
        else:
            codice_sesso = giorno
    else:
        codice_sesso = str(int(giorno) + 40)
    
    # Calcolo del codice fiscale
    codice_fiscale = codice_cognome + codice_nome + anno + mese + codice_luogo_di_nascita + codice_sesso
    
    # Controllo del codice fiscale
    check = ''
    dispari = {'0': 1, '1': 0,
