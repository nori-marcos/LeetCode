# Com o Map, podemos salvar cada interação em uma coleção de dados.
# Primeiro, verficamos se o resto está presente na coleção
# Se sim, buscamos quem foi o número e seu índice salvo
# Se não, apenas salvamos o número atual da interação junto com o seu índice no Map.

nums = [3, 3]
target = 6

seen = {}

for i, value in enumerate(nums):
    remaining = target - nums[i]
    
    if remaining in seen:
        print([i, seen[remaining]])
    seen[value] = i
