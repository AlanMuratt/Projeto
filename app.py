# app.py - Calculadora de Consumo de Energia

def main():
    print("🔌 Calculadora de Consumo de Energia 🔋\n")

    aparelho = input("Digite o nome do aparelho: ")
    potencia = float(input("Digite a potência do aparelho (em watts): "))
    horas_dia = float(input("Digite o tempo médio de uso diário (em horas): "))

    # Fórmula: (potência * horasDia * 30) / 1000
    consumo_mensal = (potencia * horas_dia * 30) / 1000

    # Cálculo de custo (valor fixo R$ 0,75/kWh)
    custo_estimado = consumo_mensal * 0.75

    print("\n📊 Resultado:")
    print(f"Aparelho: {aparelho}")
    print(f"Consumo estimado: {consumo_mensal:.2f} kWh/mês ⚡")
    print(f"Custo estimado: R$ {custo_estimado:.2f}/mês 💰  " )

if __name__ == "__main__":
    main()
