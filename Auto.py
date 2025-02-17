import pywhatkit as kit
import time
import pandas as pd

# Lista de pedidos (exemplo usando um dicionário ou um CSV)
pedidos = [
    {"cliente": "João", "telefone": "+556992243289", "quantidade": 3, "endereco": "Rua A, 123", "data_entrega": "20/02/2025"},
    {"cliente": "Maria", "telefone": "+556992243289", "quantidade": 2, "endereco": "Av. B, 456", "data_entrega": "21/02/2025"}
]

# Número do fornecedor
fornecedor = "+556992243289"

# Mensagem para o fornecedor
quantidade_total = sum(p["quantidade"] for p in pedidos)
mensagem_fornecedor = f"Olá, preciso encomendar {quantidade_total} sacos de ração para gatos. Poderia confirmar a disponibilidade?"
kit.sendwhatmsg_instantly(fornecedor, mensagem_fornecedor, wait_time=10)

# Espera um tempo entre mensagens
time.sleep(10)

# Mensagens para os clientes
for pedido in pedidos:
    mensagem_cliente = (f"Olá {pedido['cliente']}, sua compra de {pedido['quantidade']} sacos de ração foi registrada. "
                        f"A entrega está prevista para {pedido['data_entrega']} no endereço {pedido['endereco']}. "
                        "Por favor, confirme se está correto.")
    kit.sendwhatmsg_instantly(pedido['telefone'], mensagem_cliente, wait_time=10)
    time.sleep(10)  # Pequena pausa entre mensagens para evitar bloqueios