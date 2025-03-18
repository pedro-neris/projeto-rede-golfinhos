# DESENVOLVEDORES DO PROJETO:
- **Pedro Neris**  
  - GitHub: [github.com/pedro-neris](https://github.com/pedro-neris)  
  - Linkedin: [www.linkedin.com/in/pedro-neris](https://www.linkedin.com/in/pedro-neris)  

- **Israel Honório**  
  - GitHub: [github.com/Israel-Honorio](https://github.com/Israel-Honorio)  
  - Linkedin: [www.linkedin.com/in/israel-honório-1285a3208/](https://www.linkedin.com/in/israel-hon%C3%B3rio-1285a3208/)  

---

# Sobre o Projeto
Este projeto tem o objetivo de, dado um arquivo (`"soc-dolphins.mtx"`) contendo informações sobre vértices e arestas de um grafo, fazer a leitura desse arquivo e produzir um programa em Python que fornece as seguintes informações como saída:

- Grau de cada vértice do grafo  
- Coeficiente de aglomeração de cada vértice do grafo  
- Coeficiente de aglomeração médio do grafo  
- Cliques maximais do grafo e vértices que pertencem a eles  
- Representação visual do grafo, com os cliques maximais destacados por cores diferentes  

---

# REQUISITOS PARA FUNCIONAMENTO
Para o funcionamento correto do código, o arquivo (`"soc-dolphins.mtx"`) contendo as informações sobre os vértices e arestas devem estar na mesma pasta do arquivo do programa (`"projeto_tag_1.py"`), e o programa deve ser executado nesta pasta.  

- **Python** deve estar instalado, além do gerenciador de pacotes **pip**.  
  - Link para instalação do Python: [https://www.python.org/downloads/](https://www.python.org/downloads/)  
  - Para instalar o pip, rode o seguinte comando no terminal do dispositivo:  
    ```bash
    python get-pip.py
    ```  
    *(Da versão 3.4 para frente do Python, pip já é incluso na instalação)*  

- As bibliotecas **Networkx** e **Matplotlib** também devem ter sido baixadas.  
  - Comandos para instalar as bibliotecas (executar no terminal do dispositivo):  
    ```bash
    pip install networkx
    python -m pip install -U matplotlib
    ```  

- A biblioteca **random** já vem inclusa com o Python, portanto, não é necessária sua instalação, somente sua importação.  

---

# COMO EXECUTAR O PROGRAMA
1. Navegue até o diretório contendo o arquivo do programa (`"main.py"`) e o arquivo com as informações do grafo (`"soc-dolphins.mtx"`) no terminal.  
2. Ao chegar ao diretório, digite e execute o comando:  
   ```bash
   python main.py
3. O grau de cada vértice junto do seu coeficiente de aglomeração, o coeficiente médio de aglomeração do grafo e os cliques maximais e os vértices que pertencem a eles são impressos no terminal que foi executado o código.
4. É aberta em uma nova página uma imagem com a representação visual do grafo. Para encerrar a execução do código, deve-se fechar a página com essa imagem.

---

# DOCUMENTAÇÃO DAS BIBLIOTECAS UTILIZADAS:
- **NetworkX**: [networkx.org/documentation](https://networkx.org/documentation)  
- **Matplotlib**: [matplotlib.org/stable/tutorials](https://matplotlib.org/stable/tutorials)  
