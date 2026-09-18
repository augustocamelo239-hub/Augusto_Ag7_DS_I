tipo = input("Digite o tipo de imóvel:")
consumo = float(input("Digite o consumo mensal de água em m3:"))

if tipo == "comercial":
    print("Tarifa comercial aplicada - consulte o plano corporativo.")

elif tipo == "apartamento" and consumo < 10:
    print("Consumo econômico - excelente controle de água.")

elif tipo in ["apartamento", "casa"] and consumo <= 25:
    print("Consumo moderado - dentro do padrão residencial.")

else:
    print("Consumo excessivo - adote medidas de economia e verifique vazamentos.")