from credenciais import login, senha
from imap_tools import MailBox, AND
from datetime import datetime
from time import sleep
import logging

login = login()
senha = senha()

meu_email = MailBox('outlook.office365.com').login(login, senha)

while True:
    try:
        finalizado = meu_email.fetch(AND(subject="Portal Vertsign informa: Documento Finalizado."))
        for mail in finalizado:
            meu_email.move(mail.uid, 'Finalizados')
            sleep(2)
            happened = datetime.now().strftime('%d/%m/%Y %H:%M')
            print(f"Foi alocado em finalizos em {happened}")
            print(30 * "=")
            logging.info(f'Foi alocado em finalizos em {happened}')
            logging.info(30 * "=")
    except:
        print("Não há emails finalizados")
        logging.info("Não há emails finalizados")
        sleep(2)