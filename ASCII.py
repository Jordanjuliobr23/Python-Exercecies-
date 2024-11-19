# Parametros (Linha 2-4)
Fdin = open(input('Digite o nome de um arquivo de origem: '), 'rb')  # Modo binário
password = input('Digite a palavra-passe: ')
Fdout = open(input('Digite o nome de um arquivo destino: '), 'wb')  # Modo binário

# Converte as letras da palavra-passe em seu respectivo valor ASCII, armazenando na lista b_word
b_word = []
for c in password:
    b_word.append(ord(c))  # Adiciona o valor ASCII de cada caractere à lista

l_word = len(b_word)  # Comprimento da palavra-passe

# Leitura dos bytes do arquivo de origem
b_in = Fdin.read()

# Operação "xor" para cada byte do arquivo de origem e depois escrever o resultado no arquivo destino
i = 0
for b in b_in:
    b_final = b ^ b_word[i]  # Aplica o XOR

    Fdout.write(bytes([b_final]))  # Escreve o byte processado no arquivo de destino

    # Atualiza o índice para o próximo byte da palavra-passe, ciclo com % l_word
    i = (i + 1) % l_word

# Fecha os arquivos
Fdin.close()
Fdout.close()

# Imprime mensagem de sucesso
print(f"Arquivo processado com sucesso! Resultado salvo em: {Fdout.name}")



