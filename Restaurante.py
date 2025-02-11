import time

pedidos = []
precos = {1: 15, 2: 30, 3: 5}

while True:
    print("\nMenu:")
    print("1 - Hambúrguer - R$ 15,00")
    print("2 - Pizza - R$ 30,00")
    print("3 - Refrigerante - R$ 5,00")
    print("4 - Finalizar pedido")
    
    escolha = int(input("Escolha uma opção: "))
    
    if escolha == 4:
        break
    elif escolha in precos:
        pedidos.append(escolha)
        print("Item adicionado ao pedido!\n")
    else:
        print("Opção inválida! Tente novamente.")

if pedidos:
    total = sum(precos[item] for item in pedidos)
    print(f"Total do pedido: R$ {total:.2f}")
else:
    print("Nenhum item foi pedido.")

print("Obrigado por usar nosso sistema!")
time.sleep(2)