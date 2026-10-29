hoje = datetime.date.today()
print(hoje)
print(hoje.strftime("%d/%m/%Y"))
print(f"São Paulo, {dias_semana[hoje.weekday()]}, {hoje.day} de {meses[hoje.month - 1]} de {hoje.year}")

print(f"2024 é Bissexto: {calendar.isleap(2024)}")

print(f"É o ultimo dia do mês? {calendar.monthrange(2026, 10)[1]}")