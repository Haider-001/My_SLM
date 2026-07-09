text = open("data.txt").read()

chars = sorted(list(set(text)))

stoi = {ch:i for i,ch in enumerate(chars)}
itos = {i:ch for i,ch in enumerate(chars)}

data = [stoi[c] for c in text]

x = data[:10]
y = data[1:11]

print("Input :", x)
print("Target:", y)
for inp, tgt in zip(x, y):
    print(
        f"{itos[inp]} -> {itos[tgt]}"
    )