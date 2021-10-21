def calculate_payment(qtt_hours, cost_hour):
    hour = float(qtt_hours)
    rate = float(cost_hour)
    if hours <= 40:
        salary = hour * rate
    else:
        overtime = hours - 40
        salary = 40 * rate + (overtime * rate)
    return salary

workedHours = float(input('Horas trabalhadas: '))
rate = float(input('Digite a taxa: '))
salary = (workedHours * rate)
print('O valor total do seu salário é:', salary)