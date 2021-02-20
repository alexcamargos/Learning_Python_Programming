# Brute Force Decrypt

Implementação de um sistema de ataque por força bruta (brute-force password attack) para tentar acessar um arquivo PDF encriptado utilziando uma única palavra em portugues.

Este projeto tem caracter apenas educacional, não sendo uma solução estado da arte para uso no dia a dia.

## O que este programa faz?

1. Usando um arquivo texto contendo palavras em portugues do brasil, sem acentos, cria uma lista de strings.
2. Apos a leitura um loop tentará ter acesso ao arquivo utilizando a biblioteca PyPDF2.
3. Cada palavra sera tentada em sua versão totalmente em minisculas e maúsculas.

## Bilbiotecas utilizadas

- PyPDF2
- [Dicionário br.ispell](http://www.ime.usp.br/~ueda/br.ispell/)