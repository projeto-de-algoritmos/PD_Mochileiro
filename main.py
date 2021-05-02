def knapsack(wt, val, W, n):

    if n == 0 or W == 0:
        return 0
    if t[n][W] != -1:
        return t[n][W]
 
    # choice diagram code
    if wt[n-1] <= W:
        t[n][W] = max(
            val[n-1] + knapsack(
                wt, val, W-wt[n-1], n-1),
            knapsack(wt, val, W, n-1))
        return t[n][W]
    elif wt[n-1] > W:
        t[n][W] = knapsack(wt, val, W, n-1)
        return t[n][W]

itns = []
val = []
wt = []
W = int(input("Adicione o peso limite da mochila:"))
n = int(input("Digite o número de itens que podem ser escolhidos:"))

print("Adicione os itens, seus respectivos pesos e o valor de importância de cada um:")

z = 0
while(z < n):
    print("Item ", z+1, ":")
    aux = int(input())
    itns.append(aux)
    print("Valor de importância do item ", z+1, ":")
    aux = int(input())
    val.append(aux)
    print("Peso do item ", z+1, ":")
    aux = int(input())
    wt.append(aux)

    z = z+1

t = [[-1 for i in range(W + 1)] for j in range(n + 1)]

print("A mochila no máximo vai estar com ", knapsack(wt, val, W, n), " de importância.")