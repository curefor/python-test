import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
import pandas as pd
from torch.utils.data import DataLoader, TensorDataset

# 设置随机种子，以保证结果的可重复性
torch.manual_seed(0)

class GRUCellModel(nn.Module):
    def __init__(self, input_size, hidden_size):
        super(GRUCellModel, self).__init__()
        self.grucell = nn.GRUCell(9, 20)
        self.input_seq = torch.randn(24, 10, 9)  # 维度为 (seq_length, batch_size, input_size)
        self.hx = torch.randn(10, 20)  # 维度为 (batch_size, hidden_size)

    def forward(self, input_seq):
        output = []
        for i in range(len(input_seq)):
            hx = self.grucell(input_seq[i])
            output.append(hx)

        return torch.stack(output, dim=1)

class GRUModel(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers):
        super(GRUModel, self).__init__()
        self.gru = nn.GRU(20, 20, 2,batch_first=True)  # 输入大小为 10，隐藏状态大小为 20，层数为 2
    def forward(self, input):
        input = torch.randn(5, 3, 20)
        h0 = torch.randn(2, 5, 20)
        output, hn = self.gru(input, h0)
        return output






class TimeSeriesPredictionModel(nn.Module):
    def __init__(self, input_size, hidden_size, output_size, num_layers):
        super(TimeSeriesPredictionModel, self).__init__()
        self.gru_cell_model = GRUCellModel(9, 20)
        self.gru_model = GRUModel(20, 20, 2)
        self.linear = nn.Linear(20, 1)

    def forward(self, input_seq):
        gru_cell_output = self.gru_cell_model(input_seq)
        gru_output = self.gru_model(gru_cell_output)
        gru_output_split = torch.split(gru_output, split_size_or_sections=gru_output.size(1)//3, dim=1)
        outputs = torch.cat(gru_output_split, dim=1)
        # 修改的代码
        _, h = self.gru_model.gru(outputs)
        h = h[-1]  # 取最后一个时刻的隐藏状态作为输出
        predictions = self.linear(h)
        return predictions


model = TimeSeriesPredictionModel(input_size=10, hidden_size=20, output_size=1, num_layers=2)

# 准备数据
def prepare_data(data, seq_length):
    X, y = [], []
    for i in range(len(data) - seq_length):
        X.append(data[i:i + seq_length])
        y.append(data[i + seq_length])
    return np.array(X), np.array(y)

# 超参数设置
input_size = 9
hidden_size = 20
output_size = 1
seq_length = 9
num_epochs = 24
batch_size = 24
learning_rate = 0.001
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# 加载数据
data = pd.read_excel('data_2018-11-01.xlsx',usecols='C:K')
data = np.array(data)

# 划分输入特征和输出标签

train_data = data[:int(0.8 * len(data))]
test_data = data[int(0.8 * len(data)):]

# 数据归一化
train_mean = np.mean(train_data)
train_std = np.std(train_data)
train_data = (train_data - train_mean) / train_std
test_data = (test_data - train_mean) / train_std

# 准备训练和测试数据集
train_X, train_y = prepare_data(train_data, seq_length)
test_X, test_y = prepare_data(test_data, seq_length)

train_dataset = TensorDataset(torch.from_numpy(train_X).float(), torch.from_numpy(train_y).float())
test_dataset = TensorDataset(torch.from_numpy(test_X).float(), torch.from_numpy(test_y).float())

train_dataloader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
test_dataloader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)

# 定义损失函数和优化器
criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=learning_rate)

input_seq = torch.randn(24, 10, 9)  # 输入序列
target_seq = torch.randn(9, 1)
# 训练模型
for epoch in range(num_epochs):
    model.train()
    for i, (input_seq, target_seq) in enumerate(train_dataloader):

        optimizer.zero_grad()
        outputs = model(input_seq)
        outputs = outputs.repeat(1, target_seq.size(1))
        target_seq = torch.unsqueeze(target_seq, 1)
        loss = criterion(outputs[-10:], target_seq[-10:])
        loss.backward()
        optimizer.step()
    criterion = nn.MSELoss()  # 使用均方误差作为损失函数
    optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)  # 定义优化器



    if (epoch + 1) % 1== 0:
        print('Epoch [{}/{}], Loss: {:.4f}'.format(epoch + 1, num_epochs, loss.item()))

# 测试模型
model.eval()
with torch.no_grad():
    test_loss = 0
    predictions = []
    for input_seq, target_seq in test_dataloader:
        outputs = model(input_seq)
        test_loss += criterion(outputs, target_seq).item()
        predictions += outputs.tolist()

test_loss /= len(test_dataloader)
predictions = np.array(predictions) * train_std + train_mean
test_y = test_y * train_std + train_mean

mse = np.mean((predictions - test_y) ** 2)
mae = np.mean(np.abs(predictions - test_y))
r2 = 1 - np.sum((predictions - test_y) ** 2) / np.sum((test_y - np.mean(test_y)) ** 2)


print('Test Loss: {:.4f}, MSE: {:.4f}, MAE: {:.4f}, R2: {:.4f}'.format(test_loss, mse, mae, r2))
predictions=predictions.repeat(2,axis=1).reshape(-1)
test_y=test_y.reshape(-1)
# 保存预测结果和真实标签到Excel文件
df = pd.DataFrame({'Prediction': predictions, 'Actual': test_y})
df.to_excel('predictions.xlsx', index=False)
