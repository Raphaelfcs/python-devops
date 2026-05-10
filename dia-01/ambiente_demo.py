#!/usr/bin/env python3
import os

def main():
    print("Bem-vindo ao ambiente de desenvolvimento!")
    print(f"Processo ID: {os.getpid()}")

    for var in['USER', 'PATH', 'CUSTOM_VAR']:
        valor = os.getenv(var, "Não definida")
        if var =='PATH':
            valor = f"{len(valor.split(':'))} diretórios"
        print(f"{var}: {valor}")

    os.environ['TESTE'] = 'temporario'
    print(f"\nTESTE definida como: {os.getenv('TESTE')}")
    print(("mas não persistirá após o término do programa."))
if __name__ == "__main__":
    main()
    print()