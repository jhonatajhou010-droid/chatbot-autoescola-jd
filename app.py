print("====================================")
print("      IA AUTOESCOLA JD")
print("====================================")

while True:

    print()
    print("Olá! Eu sou a IA da Autoescola JD.")
    print("Gostaria de saber quais são suas dúvidas.")
    print()

    print("1 - Quero tirar minha primeira habilitação")
    print("2 - Quero realizar meu processo de reciclagem ou cassação da CNH")
    print("3 - Tenho dúvidas sobre renovação ou categorias C, D e E")
    print("4 - Encerrar atendimento")
    print()

    opcao = input("Digite a opção desejada: ")

    print()

    if opcao == "1":

        print("Categorias disponíveis:")
        print("A - Moto")
        print("B - Carro")
        print("A/B - Carro e Moto")
        print()

        categoria = input("Qual seria sua categoria? ").upper()

        print()

        if categoria == "A":
            print("IA Autoescola JD:")
            print("Você escolheu categoria A - Moto.")
            print("Para informações, orçamentos e dúvidas,")
            print("chame no WhatsApp: 14 99760-0124")
            print("Para mais dúvidas é só me dizer.")

        elif categoria == "B":
            print("IA Autoescola JD:")
            print("Você escolheu categoria B - Carro.")
            print("Para informações, orçamentos e dúvidas,")
            print("chame no WhatsApp: 14 99760-0124")
            print("Para mais dúvidas é só me dizer.")

        elif categoria == "A/B" or categoria == "AB":
            print("IA Autoescola JD:")
            print("Você escolheu categoria A/B - Carro e Moto.")
            print("Para informações, orçamentos e dúvidas,")
            print("chame no WhatsApp: 14 99760-0124")
            print("Para mais dúvidas é só me dizer.")

        else:
            print("IA Autoescola JD:")
            print("Categoria inválida.")

    elif opcao == "2":
        print("IA Autoescola JD:")
        print("Podemos te ajudar com reciclagem ou cassação da CNH.")
        print("Para mais informações chame no WhatsApp: 14 99760-0124")

    elif opcao == "3":
        print("IA Autoescola JD:")
        print("Podemos ajudar com renovação")
        print("e categorias C, D e E.")
        print("Para mais informações chame no WhatsApp: 14 99760-0124")

    elif opcao == "4":
        print("IA Autoescola JD:")
        print("Atendimento encerrado.")
        break

    else:
        print("IA Autoescola JD:")
        print("Opção inválida.")
