"""
Leia quatro valores interios A, B, C e D. A seguir calcule e mostre a diferença do produto de A e B pelo produto de C e D.
Segundo a fórmula: DIFERENCA = (A * B - C * D)
"""
def main():
    _A = int(input())
    _B = int(input())
    _C = int(input())
    _D = int(input())

    DIFERENÇA = (_A * _B) - (_C * _D)

    print(f"DIFERENÇA = {DIFERENÇA}")

main()
