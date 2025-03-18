import networkx as nx
import matplotlib.pyplot as mp
from matplotlib import colors as mcolors
import random

class GraphNode:  # classe que representa um nó de um grafo
    next = None  # atributo usado para enlaçar nós em uma lista ligada de vértices adjacentes
    valor = 0  # valor guardado no vértice (geralmente o índice dele na lista de todos os vértices)

    def __init__(self, valor):
        self.next = None  #a lista de adjacências do nó inicia vazia
        self.valor = valor


class Graph:
    conjunto_vertices = []  # conjunto de vértices do grafo
    grafo_networkx = nx.Graph()  # grafo do networkx usado para mostrar o grafo na tela
    lista_cliques_max = []  # lista usada para guardar os cliques maximais encontrados

    def adiciona_vertice(self, valor):  # adiciona um vértice com um valor passado como argumento
        novo_vertice = GraphNode(valor)  # cria-se um novo nó
        self.conjunto_vertices.append(novo_vertice)  # adiciona-se o nó na lista de vértices

    def adiciona_aresta(self, vertice_1: int, vertice_2: int):  # adiciona uma aresta entre dois vértices (os dois inteiros passados como argumento são os indíces
                                                                # dos vértices na lista geral de vértices)
        self.grafo_networkx.add_edge(vertice_1 + 1, vertice_2 + 1)  # adiciona a aresta na representação do grafo em networkx para depois desenhá-lo
        if vertice_2 > len(self.conjunto_vertices) or vertice_1 > len(self.conjunto_vertices):  # verifica se o valor passado está fora do tamanho da lista de vértices atual
            print("Um ou mais vértices não existem")
        else:  
            # cria um nó para o vértice 2 e o adiciona a lista de adjacências do vértice 1, usando a lógica de uma lista ligada
            node_2 = GraphNode(vertice_2)
            if self.conjunto_vertices[vertice_1].next is None:
                self.conjunto_vertices[vertice_1].next = node_2
            else:
                temp = self.conjunto_vertices[vertice_1].next
                self.conjunto_vertices[vertice_1].next = node_2
                node_2.next = temp
            node_1 = GraphNode(vertice_1)  # repetido o mesmo funcionamento para o vértice 1
            if self.conjunto_vertices[vertice_2].next is None:
                self.conjunto_vertices[vertice_2].next = node_1
            else:
                temp = self.conjunto_vertices[vertice_2].next
                self.conjunto_vertices[vertice_2].next = node_1
                node_1.next = temp

    
    #acha os vértices vizinhos de um vértice cujo indíce foi passado como argumento, passando por sua lista de adjacêcnias
    def acha_adjacentes(self, indice_vertice: int):
        lista_adjacentes = []  # lista para guardar os vértices vizinhos achados
        no_atual = self.conjunto_vertices[indice_vertice]  # acha o vértice pelo índice passado como argumento
        while no_atual.next != None:  #passa pela lista de adjacências do vértice
            lista_adjacentes.append(no_atual.next.valor)
            no_atual = no_atual.next
        lista_adjacentes.sort()  # ordena os vértices em ordem crescente
        return lista_adjacentes

    def lista_valores_vertices(self):  # faz uma lista de valores usadas para achar os cliques maximais do grafo
        lista_valores = []
        for i in self.conjunto_vertices:  # iterando pelo conjunto de vértices e obtendo seus valores
            lista_valores.append(i.valor)
        lista_valores.sort()
        return lista_valores

    def cliques_max(self, clique: set, candidatos: set, excluidos: set):  # implementação de bron-kerbosch
        if (len(candidatos) == 0 and len(excluidos) == 0):  # verificando se o conjunto de candidatos e de excluídos são vazios
            self.lista_cliques_max.append(clique)

        # conjunto candidatos passado como parâmetro da função set para criar uma nova referência e evitar iterar sobre um conjunto que está sendo modificado
        for vert in set(candidatos):

            # cria um novo clique com os vértices do clique passado como argumento e com o vértice sendo analisado
            novo_clique = (clique.copy())  
            novo_clique.add(vert)

            # acha os vértices adjacentes do vértice sendo analisado
            vizinhos = set(self.acha_adjacentes(vert))  
            novos_candidatos = candidatos.intersection(vizinhos)

            # faz a intersecção de candidatos/excluidos com vizinhos para criar novas listas
            novos_excluidos = excluidos.intersection(vizinhos)
            self.cliques_max(novo_clique, novos_candidatos, novos_excluidos) #chama recursivamente bron-kerbosch
            candidatos.remove(vert) #remove o vértice do conjunto de candidatos
            excluidos.add(vert) #adiciona o vértice ao conjunto de excluídos

    def imprime_cliques(self):
        # cópia da lista de cliques para poder incrementar 1 em cada vértice sem alterar na representação original
        lista_imprime_cliques = self.lista_cliques_max.copy()

        for clique in range(len(lista_imprime_cliques)):
  
            # transforma cada clique presente na lista de set para list, para poder alterar seu valor
            lista_imprime_cliques[clique] = list(lista_imprime_cliques[clique]) 

            # itera por cada vértice do clique incrementado-o em 1 
            for v in range(len(lista_imprime_cliques[clique])):  
                lista_imprime_cliques[clique][v] += 1
            lista_imprime_cliques[clique].sort()  #ordena os elementos do clique em ordem crescente
        lista_imprime_cliques.sort(key=len)  # ordena a lista de cliques baseado no número de vértices em cada clique, em ordem crescente
        print("\nCliques maximais encontrados:")
        for clique in lista_imprime_cliques:
            print(f"Clique: {clique}. Número de vértices do clique: {len(clique)}.")

    
    # função que utiliza uma função disponível no networkx para calcular o coeficiente de aglomeração de um vértice passado como argumento
    def coef_aglomeracao_no(self, vertex_index: int):
        indice_geral = dict(nx.clustering(self.grafo_networkx))  # disponivel na documentação do networkx
        return indice_geral[vertex_index + 1]

    def coef_aglomeracao_grafo(self):
        aglomeracao_individual = 0
        for no in (self.conjunto_vertices):  # calcula o somatório dos coeficientes de aglomeração de cada vértice
            aglomeracao_individual += self.coef_aglomeracao_no(no.valor)
        if len(self.conjunto_vertices) > 0:  # para evitar erro de divisão por 0
            return aglomeracao_individual / len(self.conjunto_vertices)  # divide o somatório pelo número de vértices no grafo
        else:
            return 0

    def mostra_grafo(self):  # função que imprime a lista de vértices do grafo com o respectivo grau e coeficiente de aglomeração
        for no in range(len(self.conjunto_vertices)):  # para cada vértice, são impressos o grau, a lista de vértices adjacentes e o coeficiente de aglomeração daquele vértice
            if self.acha_adjacentes(no) == []:
                print( f"Grau do vértice {no+1}: 0. Coeficiente de aglomeração: 0.")  # é usado no+1 pois, na lista com o conjunto de vértices, o indíce dos vértices começa do indíce 0
            else:
                lista_adjacentes = self.acha_adjacentes(no)
                #arredonda o coeficiente de aglomeração em até 5 casas decimais
                print(f"Grau do vértice {no+1}: {len(lista_adjacentes)}. Coeficiente de Aglomeração: {round (self.coef_aglomeracao_no(no),5)}")
        print(f"O Coeficiente médio de Aglomeração deste grafo é {round (self.coef_aglomeracao_grafo(),5)}")  # para imprimir o coeficiente de aglomeração médio do grafo

    def colorir_cliques(self):
        self.lista_cliques_max.sort(key=len)  # ordena os cliques em ordem crescente

        # Obter cores disponíveis
        todas_cores = list(mcolors.CSS4_COLORS.keys())  # uma lista com todas as cores possíveis da biblioteca
        cores_excluidas = {"black"}  # Cores que você deseja excluir para não atrapalhar a visualização do grafo
        cores_filtradas = [cor for cor in todas_cores if cor not in cores_excluidas]  # adiciona todas as cores aptas a uma lista
        
        # Sortear cores aleatórias para os cliques
        cores_disponiveis = random.sample(cores_filtradas, len(self.lista_cliques_max))

        # Criar dicionário de cores para os vértices
        cores = {}

        # O enumerate retorna um índice (i) e um elemento da lista (clique) a cada iteração
        for i, clique in enumerate(self.lista_cliques_max):
            cor_atual = cores_disponiveis[i]  # A variável cor atual seleciona uma cor disponível correspondente ao i
            for vertice in clique:  # Percorre cada vértice dentro do clique atual
                cores[vertice + 1] = (cor_atual)  # Vértice + 1 para coincidir com o grafo do networkx
        return cores  # Retornar dicionário de cores


grafo_golfinhos = Graph()  # cria o objeto de grafo para o grafo que será analisado

arquivo_grafo = open("soc-dolphins.mtx", "r") # abre o arquivo contendo os vértices e arestas do grafo, usando a função "read"
while True:  # itera até o começo das informações sobre o grafo no arquivo
    linha = arquivo_grafo.readline().split()
    if linha[0][0] != "%":  #quando "%" não estiver no começo da linha,irão começar as informações sobre o grafo
        break
for vertice in range(int(linha[0])):  #gera um grafo com o número de vértices definido no arquivo
    grafo_golfinhos.adiciona_vertice(vertice)
arestas = int(linha[2])     #le o numero de arestas
for aresta in range(arestas):   #itera ate o final do arquivo adicionando as arestas definidas
    linha = arquivo_grafo.readline().split()
    grafo_golfinhos.adiciona_aresta(int(linha[0]) - 1, int(linha[1]) - 1)

grafo_golfinhos.cliques_max(set(), set(grafo_golfinhos.lista_valores_vertices()), set())  # chama bron-kerbosch para o grafo
grafo_golfinhos.mostra_grafo()  #imprime grau e coeficientes de aglomeração para cada vértice e o coeficiente médio do grafo
grafo_golfinhos.imprime_cliques() #imprime a quantidade e a lista de cliques maximais

# Colorir os cliques
cores = grafo_golfinhos.colorir_cliques()
# Desenhar o grafo com as cores atribuídas aos cliques
nx.draw(
    grafo_golfinhos.grafo_networkx,  # o grafo a ser desenhado, um objeto networkX
    # Define as posições dos vértices no layout do grafo
    pos=nx.spring_layout(grafo_golfinhos.grafo_networkx, k=1),
    # 'spring_layout' posiciona os vértices utilizando o algoritmo de força (force-directed)
    # O parâmetro 'k' ajusta a distância ideal entre os vértices
    # Define a cor dos vértices.
    node_color=[cores.get(no, "gray") for no in grafo_golfinhos.grafo_networkx.nodes],
    # Para cada vérice no grafo, busca sua cor no dicionário 'cores'
    # Caso o vértice não tenha uma cor definida, usa "gray" como padrão
    edge_color="gray",  # Todas as arestas são cinza
    with_labels=True,  # enumera os vértices
)
mp.show()  #imprime a imagem do grafo em uma nova janela