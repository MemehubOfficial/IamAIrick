import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

import torchvision
import torchvision.transforms as transform
from brain.NeuralNetwork import Network

network = Network()

train_loader = torch.utils.data.DataLoader(train_set, batch_size=100)
optimizer = optim.Adam(network.parameters(), lr = 0.01)

losses = []
for epoch in range(7):
    total_loss = 0
    total_correct = 0
    for batch in train_loader:
        images, labels = batch

        preds = network(images)
        loss = F.cross_entropy(preds, labels)

        optimizer.zero_grad()
        loss.backwards()
        optimizer.step()

        total_loss += loss.item()
        total_correct += get_num_correct(preds, labels)
    losses.append(total_loss)
