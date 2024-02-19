# 1 - O programa deve começar solicitando ao usuário que insira seu nome.
nome_usuario = input("Digite o nome do usuário: ")

# 2 - Em seguida, o programa deve pedir ao usuário para inserir o valor do seu salário. Considere que este valor pode ser um número decimal.
salario_usuario = float(input("Digite o salário do usuário: "))

# 3 - Depois, o programa deve solicitar a porcentagem do bônus recebido pelo usuário, que também pode ser um número decimal.
bonus_usuario = float(input("Digite a porcentagem do bonus do usuário: "))

# 4 - O cálculo do KPI do bônus de 2024 é de 1000 + salario * bônus
resultado_kpi = 1000 + salario_usuario * bonus_usuario

# 5 - Finalmente, o programa deve imprimir uma mensagem no seguinte formato: "Olá [nome], o seu valor bônus foi de 5000".
print(f"Olá {nome_usuario}, o seu valor bônus foi de {resultado_kpi}")
