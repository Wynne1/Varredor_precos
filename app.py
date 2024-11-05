import schedule
from time import sleep
import os

# Mudar uma vez para o diretório que contém o prejeto scrapy
print(os.getcwd())
os.chdir('varredor_precos')
print(os.getcwd())

# Criar uma função que será executada periodicamente
def rodar_botprecos():
    os.system('scrapy crawl dolarpreco')

# Agendar essa execução
schedule.every(1).minute.do(rodar_botprecos)
print(str(schedule.next_run()))
# Colocar esse agendamento na file
while True:
    schedule.run_pending()
    sleep(1)