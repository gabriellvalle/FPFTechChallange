# Define o interpretador do script como Bash. Essa linha é obrigatória para garantir a execução correta no ambiente Bash.
#!/bin/bash

# a. Cria um diretório com meu nome, chamado "gabrielvalle" no local onde o script está sendo executado.
mkdir gabrielvalle

# b. Cria um subdiretório chamado "resultado" dentro do diretório "gabrielvalle".
mkdir gabrielvalle/resultado

# c. Faz o download silencioso (opção -q) do arquivo "zip.zip" a partir do link fornecido.
wget -q https://vanilton.net/v1/download/zip.zip

# d. Extrai os arquivos contidos em "zip.zip" para o diretório "gabrielvalle" de forma silenciosa (opção -q).
unzip -q zip.zip -d gabrielvalle

# e. Procura por todos os arquivos (-type f) localizados no diretório "gabrielvalle" (sem incluir subdiretórios, graças ao -maxdepth 1) 
# e os move para o subdiretório "gabrielvalle/resultado" utilizando o comando `mv`.
find gabrielvalle -maxdepth 1 -type f -exec mv {} gabrielvalle/resultado \;

# f. Remove o arquivo compactado "zip.zip" do diretório atual, já que ele não é mais necessário.
rm zip.zip

# Exibe uma mensagem indicando que o script foi executado com sucesso e informa onde os resultados estão localizados.
echo "Script executado com sucesso. Confira na pasta 'gabrielvalle/resultado.'"
