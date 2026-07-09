import torch
import torch.nn as nn

text = open("data.txt").read()

chars = sorted(list(set(text)))

stoi = {ch:i for i,ch in enumerate(chars)}
itos = {i:ch for i,ch in enumerate(chars)}

data = torch.tensor([stoi[c] for c in text])

vocab_size = len(chars)

x = data[:-1]
y = data[1:]
model = nn.Embedding(vocab_size, vocab_size)
logits = model(x)

print(logits.shape)
loss_fn = nn.CrossEntropyLoss()

loss = loss_fn(logits, y)

print("Loss =", loss.item())
optimizer = torch.optim.AdamW(
    model.parameters(),
    lr=0.1
)

for step in range(200):

    logits = model(x)

    loss = loss_fn(logits, y)

    optimizer.zero_grad()

    loss.backward()

    optimizer.step()

    if step % 20 == 0:
        print(step, loss.item())
    idx = torch.tensor([stoi['h']])

for _ in range(20):

    logits = model(idx)

    probs = torch.softmax(logits[-1], dim=0)

    next_id = torch.multinomial(probs, num_samples=1)

    idx = torch.cat(
        [idx, next_id.view(1)]
    )

result = ''.join(
    [itos[i.item()] for i in idx]
)

print(result)