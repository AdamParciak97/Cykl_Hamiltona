import itertools
import time
import tracemalloc

tracemalloc.start()
start = time.perf_counter_ns()

# wykres 8 wierzchołków poniżej. Ma cykl Hamiltona [0-1-2-3-4-5-6-7-0]

# (0)-----------(1)
#  | `.       ,´ |
#  |  (7)---(6)  |
#  |   |     |   |
#  |  (4)---(5)  |
#  | ,´       `. |
# (3)-----------(2)


# grafo = {0: [0, 1, 0, 0, 1, 1, 0, 0, 0, 0],
#          1: [1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
#          2: [0, 1, 0, 1, 0, 0, 0, 0, 0, 1],
#          3: [0, 0, 1, 0, 1, 0, 0, 1, 0, 0],
#          4: [1, 0, 0, 1, 0, 1, 0, 0, 0, 0],
#          5: [0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
#          6: [1, 0, 0, 0, 0, 1, 0, 1, 0, 0]}

# grafo = {0: [0, 1, 0, 1, 0, 0, 0, 1],
#          1: [1, 0, 1, 0, 0, 0, 1, 0],
#          2: [0, 1, 0, 1, 0, 1, 0, 0],
#          3: [1, 0, 1, 0, 1, 0, 0, 0],
#          4: [0, 0, 0, 1, 0, 1, 0, 1],
#          5: [0, 0, 1, 0, 1, 0, 1, 0],
#          6: [0, 1, 0, 0, 0, 1, 0, 1],
#          7: [1, 0, 0, 0, 1, 0, 1, 0]}

# 5 wykres wierzchołkowy narysowany poniżej. Ma cykl Hamiltona [0-1-2-3-4-0]

# (0)--(1)--(2)
#  |   / \   |
#  |  /   \  |
#  | /     \ |
# (4)-------(3)

# grafo = {0: [0, 1, 0, 0, 1],
#          1: [1, 0, 1, 1, 1],
#          2: [0, 1, 0, 1, 0],
#          3: [0, 1, 1, 0, 1],
#          4: [1, 1, 0, 1, 0]}

# grafo = {0: [0, 1, 0, 0, 1, 1, 0, 0, 0, 0],
#          1: [1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
#          2: [0, 1, 0, 1, 0, 0, 0, 0, 0, 1],
#          3: [0, 0, 1, 0, 1, 0, 0, 1, 0, 0],
#          4: [1, 0, 0, 1, 0, 1, 0, 0, 0, 0],
#          5: [0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
#          6: [1, 0, 0, 0, 0, 1, 0, 1, 0, 0],
#          7: [0, 0, 0, 1, 0, 0, 1, 0, 1, 0],
#          8: [0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
#          9: [0, 0, 1, 0, 0, 0, 0, 0, 1, 0]}

grafo = {0: [0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
         1: [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
         2: [0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
         3: [0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
         4: [1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
         5: [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
         6: [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
         7: [0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0],
         8: [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
         9: [0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
         10: [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
         11: [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1]}

# zmienna do przechowywania liczby wierzchołków
vert = grafo.__len__()

# funkcja permutacji zwraca listę ze wszystkimi możliwymi kombinacjami KLUCZY słownika reprezentującego wykres
rotas = itertools.permutations(grafo)

# zapisuje odmiany cyklu, zaczynając od różnych punktów
hamRotes = []
# ostatni dodany wierzchołek pozostaje
last = -1

itj = 0
itk = 0
# liczba kombinacji otrzymanych z powyższej funkcji permutatacji
rotes = 0

# każde i jest trasą (kombinacją)
for i in rotas:
    rotes += 1
    # każda nowa iteracja powoduje ponowne uruchomienie ścieżki
    path = []
    # i ustaw ostatni trwały na „domyślny”
    last = -1
    # każde j jest wierzchołkiem trasy (kombinacja)
    for j in i:
        itj += 1
        # jeśli ostatnia jest domyślna, wstawiana jest pierwsza
        if last == -1:
            # ostatni teraz staje się wstawionym
            last = j
            path.append(j)
            # następna iteracja
            continue
        # każde k będzie reprezentować indeksy listy przylegania wierzchołka j
        for k in range(vert):
            itk += 1
            # jeśli w k jest krawędź z jek, to ostatni dodany wierzchołek to są sąsiadujące
            if grafo[j][k] == 1 and k == last:
                # ostatni staje się wstawiany
                last = j
                # dodaj wierzchołek do ścieżki trasy
                path.append(j)
                break

        # jeśli wszystkie wierzchołki zostały wstawione
        if len(path) == vert:
            # a ostatni wstawiony sąsiaduje z początkowym, następnie powstał cykl Hamiltona
            if grafo[last][path[0]] == 1:
                # inicjał jest dodawany ponownie, aby pojawił się na trasie
                path.append(path[0])
                # i utrzymanie zmienności cyklu, który może zaczynać się od dowolnego punktu
                hamRotes.append(path)

for i in hamRotes:
    # wypisywanie tylko wersji zaczynającej się od ZERA tylko z definicji ponieważ uważane jest za centrum
    if i[0] >= 0:
        print("Istnieje trasa, która tworzy cykl Hamiltona. Trasa to: ", i)
        print("\nMożliwe kombinacje: " + str(rotes))
        break
else:
    print("Nie ma trasy Hamiltona")

# print("" + str(itj) + " iteracje porównania wykonalności następnego punktu (j) i " + str(
#     itk) + " sprawdzenie przylegania (k).")

peak = tracemalloc.get_traced_memory()[1]
end = time.perf_counter_ns()
tracemalloc.stop()
time_of_execution = (end - start) / 10 ** 9
memory_used = peak / 10 ** 6
print("Czas wynosi:", time_of_execution)
print("Pamięć wynosi", memory_used, "MB")
