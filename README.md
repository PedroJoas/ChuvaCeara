# ChuvaCeara
Utilizando dados da FUNCEME fazendo todo o processo de engenharia de dados.


# Executar

execute o seguinte comando no diretório do projeto:
```
make all 
```

Isso criará a estrutura de armazenamento de dados necessário e instalará as dependências necessárias para o projeto.

Se quiser gerar separados, utilize os seguintes códigos:

Para criação da estrutura de armazenamento
```
make create_dirs
```

Para instalação das dependências
```
make requirements
```

# Estrutura de Diretórios

```plaintext
📂 data/ 
├── 📂 raw/ # Contém os dados brutos
├── 📂 bronze/ # Contém os dados processados em estágio inicial. 
├── 📂 silver/ # Contém os dados processados em estágio intermediário. 
📂 database/ # Contém a criação do banco de dados
├── 📃 create.sql
📂 src/
├── 📂 raw/
├── 📂 bronze/
├── 📂 silver/
```