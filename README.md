# Gekitai - Jogo desenvolvido com Socket em Python
Desenvolvimento realizado para a disciplina de programação paralela e distribuida pelo Instituto Federal de Ciência e Tecnologia do Ceará.

### Sobre o Jogo
Gekitai, traduzido do Japonês significa repelir, e as peças ao serem colocadas vão repelindo
ou empurrando outras peças que já estão no tabuleiro. O tabuleiro é quadrado com 6 linhas
e 6 colunas, ou seja, são 36 casas. Um jogo para dois jogadores e cada um tem 8 peças.

### Objetivo do jogo
Colocar três peças alinhadas em qualquer direção depois de realizar os “empurrões” ou
deixar as oito peças de um mesmo jogador no tabuleiro.

### Regras
Cada jogador joga uma peça no tabuleiro de forma intercalada. Ao posicionar uma peça, a
mesmo “empurra” outras peças que estão nas casas ao redor, inclusive as do próprio
jogador. Não se pode empurrar duas ou mais peças alinhadas. Ao empurrar uma peça e essa
sair do tabuleiro, a mesma retorna ao jogador.

# Funcionalidades Básicas
- Controle de turno, com definição de quem inicia a partida
- Movimentação de peças do tabuleiro
- Desistência
- Chat para comunicação durante toda a partida

# Como Iniciar
### 1. Clone o repositório do projeto:
```
git clone https://github.com/seuusuario/gekitai.git
```

### 2. Navegue até o diretório do projeto:
```
cd gekitai
```

### 2. Navegue até o diretório do projeto:
```
sudo ./start.sh
```

## Referências
https://tesera.ru/images/items/1665162/Gekitai_Rules.pdf
https://www.youtube.com/watch?v=tNV7umy6JyE


## Prints do Jogo 
#### Tela inicial do jogo 
Demonstração do que foi desenvolvido, ao lado esquerdo é possível ver o chat iniciado com dois jogadores chamado Davi e Pedro e ao lado direito é possível ver o tabuleiro, onde cada jogador tem seu controle de turno e sua cor definida.</br>
![image](https://github.com/user-attachments/assets/d70e72ee-2e30-4687-bef5-649397241450)

#### Alerta de Controle de turno 
![image](https://github.com/user-attachments/assets/84ea51b2-1b3d-4c9a-9bd3-15857814a005)

#### Alerta de Vitória!

![image](https://github.com/user-attachments/assets/c8a3af83-c7ac-407c-ba52-f241c0e27078)

#### Tela de Desistência
![image](https://github.com/user-attachments/assets/5bd14db4-b9ca-4203-b273-d6917a8c1f52)

#### Terminal linux após ser executado os 2 clientes e o servidor.
![image](https://github.com/user-attachments/assets/cd39f589-e085-42bb-a7c4-e598f29975a2)

