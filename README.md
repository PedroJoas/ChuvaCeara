# ChuvaCeara
Utilizando dados da FUNCEME fazer todo o processo de engenharia de dados.


# Executar

execute o seguinte comando no diretório do projeto:
```
make all
```

Isso criará a estrutura de armazenamento de dados necessário.


# Estrutura de Diretórios

```plaintext
📂 data/ 
├── 📂 raw/ # Contém os dados brutos
├── 📂 bronze/ # Contém os dados processados em estágio inicial. 
├── 📂 silver/ # Contém os dados processados em estágio intermediário. 
📂 src/
├── 📂 ingestors/ # Ingestores de cada camada
│   ├── 📂 raw/
│   ├── 📂 bronze/
│   ├── 📂 silver/
├── 📂 transformers/ # Transformadores de a cada camada
│   ├── 📂 raw/
│   ├── 📂 bronze/
│   ├── 📂 silver/
```