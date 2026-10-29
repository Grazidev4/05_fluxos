
import datetime
import calendar

meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho",
         "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]

data = datetime.date(2024, 12, 21)
print(data)

hoje = datetime.date.today()
print(hoje)
print(hoje.strftime("%d/%m/%Y"))
print(f"São Paulo, {hoje.day} de {meses[hoje.month - 1]}")


