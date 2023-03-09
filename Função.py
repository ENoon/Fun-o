#Prg que calculará a receita, os custos e o lucro de uma operação.

price = float(input("Qual o preço do serviço? "))
pdc = float(input("Quanto é gasto com produtos a cada serviço? "))
wel = float(input("Qual o preço da água e luz? "))
num_works = float(input("Quantos funcionarios têm? "))
pay_workers = float(input("Quanto é pago por funcionario? "))
obrs = float(input("Porcentagem paga de obrigações sociais para cada funcionario? "))
comm = float(input("Valor da comissão por serviço feito? "))
rent = float(input("Valor do aluguel? "))
serv = float(input("Quantidade de serviços prestados? "))

#Formula para calcular a receita
rev = price * serv
#Formulas para calcular os custos
cv = pdc + (comm * obrs/100) + comm
cf = wel + (pay_workers * num_works) + (pay_workers * num_works * obrs/100) + rent
ct = cf + (cv * serv)
#Formula para calcular o lucro bruto
lb = rev - ct
#Formula para calcular o ponto de equilibrio
pe = cf / (price - cv)

print("Terá R${:.2f} de custos totais".format(ct))
print("Terá R${:.2f} de receita".format(rev))
print("Obterá R${:.2f} de lucro bruto".format(lb))
print("É necessario fazer {} serviços para conseguir não ter prejuizos".format(round(pe + 0.5)))