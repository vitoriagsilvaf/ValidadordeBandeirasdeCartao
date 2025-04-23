import re

def identificar_bandeira(cartao):
    if len(cartao) == 13 or len(cartao) == 16:
        if cartao.startswith('4'):
            return "Visa"
    if len(cartao) == 16:
        if 51 <= int(cartao[:2]) <= 55:
            return "MasterCard"
        elif 2221 <= int(cartao[:4]) <= 2720:
            return "MasterCard"
    if len(cartao) == 15:
        if cartao.startswith('34') or cartao.startswith('37'):
            return "American Express"
    if len(cartao) == 16:
        if cartao.startswith('6011') or cartao.startswith('65') or 622126 <= int(cartao[:6]) <= 622925:
            return "Discover"
    
    return "Bandeira desconhecida"

