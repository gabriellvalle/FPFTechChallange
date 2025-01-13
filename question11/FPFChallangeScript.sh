#!/bin/bash

mkdir gabrielvalle
mkdir gabrielvalle/resultado
wget -q https://vanilton.net/v1/download/zip.zip 
unzip -q zip.zip -d gabrielvalle 
find gabrielvalle -maxdepth 1 -type f -exec mv {} gabrielvalle/resultado \;
rm zip.zip 
echo "Script executado com sucesso. Confira na pasta 'gabrielvalle/resultado.'"
