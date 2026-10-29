import datetime
from babel.dates import format_date

data = datetime.date(2024, 12, 21)
print(data)

hoje = datetime.date.today()
print(hoje)
print(hoje.strftime("%d/%m/%Y"))

data_extenso = format_date(
    hoje, format="'São Paulo, 'd 'de' MMMM", locale="pt_BR")
print(data_extenso)
