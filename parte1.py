# Objeto Produto -> Recebe as características do produto
class Produto():
    def __init__(self, nome_produto, qtd_comprada, preco):
        self._nome_produto = nome_produto
        self._qtd_comprada = qtd_comprada
        self._preco = preco
    
    def get_nome_produto(self):
        return self._nome_produto
    
    def get_qtd_comprada(self):
        return self._qtd_comprada
    
    def get_preco(self):
        return self._preco


# Objeto Mercado -> Funções de caixa
class Mercado():
    def __init__(self):
        self.lista_produtos = []
        self._valor_compra = 0
        self._desconto_aplicado = 0
    

    def registrar_venda(self, produto):
        self.lista_produtos.append(produto)

    def calcular_valor_total(self):
        self._valor_compra = 0 # recalcula do 0 se chamado novamente
        for produto in self.lista_produtos:
            self._valor_compra += (produto.get_qtd_comprada() * produto.get_preco())
        
        return self._valor_compra
    
    def calcular_desconto(self):
        if self._valor_compra > 100:
            self._desconto_aplicado = self._valor_compra * 0.10
            return self._desconto_aplicado
        
        return 0.0

    def listar(self):
        for produto in self.lista_produtos:
            print(
                f'Produto: {produto.get_nome_produto()}',
                f'Quantidade: {produto.get_qtd_comprada()}',
                f'Preço: {produto.get_preco(): .2f}', sep='\n'
            )
            print("-" * 30)

# Inicio 
print('======== Sistema de Mercado ========')
sistema_mercado = Mercado() # Instância do sistema de mercado

while True:
    nome_produto = input('Digite o nome do produto: ').lower().strip()

    if not nome_produto:
        print('O nome do produto não pode ser vaio!')
        continue

    qtd_em_texto = input('Quantidade: ').strip()

    # verifica se a quantidade digitada é válida
    if not qtd_em_texto.isdigit() or int(qtd_em_texto) <= 0:
        print('Atenção: A quantidade deve ser um número inteiro maior que zero!\n')
        continue
    qtd = int(qtd_em_texto)

    # O replace renomeia um trecho específico do texto
    preco_em_texto = input('Digite o preço do produto: ').strip().replace(',', '.')
    try:
        preco = float(preco_em_texto)
        if preco < 0:
            print('Atenção: O preço não pode ser negativo!\n')
            continue
    except ValueError:
        print('Atenção: Digite um preço válido! [Ex: 15.50]\n')
        continue

    novo_produto = Produto(
        nome_produto=nome_produto,
        qtd_comprada=int(qtd),
        preco=float(preco)
    )
    
    sistema_mercado.registrar_venda(novo_produto)
    
    opcao = input('\nDeseja adicionar mais produtos? Pressione [s/n]: ').lower().strip()
    print()
    if opcao == 's':
        continue
    elif opcao == 'n':
        break
    else:
        break

print('\n==== Nota Fiscal ====')
sistema_mercado.listar()

valor_total = sistema_mercado.calcular_valor_total()
valor_desconto = sistema_mercado.calcular_desconto() # se n houver desconto retorna 0.0
valor_total_final = valor_total - valor_desconto

print(f'Valor original da compra: R$ {valor_total: .2f}')

if valor_desconto > 0:
    print(f'Desconto de 10% aplicado: R$ {valor_desconto:.2f}')
    print(f'Valor final a pagar: R$ {valor_total_final: .2f}')
else:
    print('Nenhum desconto aplicado!')
            
