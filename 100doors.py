state = [False] * 100
for i in range(1, 101, 1):
    for j in range(i, len(state), i):
        state[j] = not state[j]

print(state)

print([i for i in range(len(state)) if state[i]])


# https://cscircles.cemc.uwaterloo.ca/visualize
# https://visualgo.net/en