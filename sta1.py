def read_file(filename):
    prices = []
    with open(filename, 'r') as f:
        for line in f:
            if 'Adj Close' in line:
                continue
            data = line.strip().split(',')
            prices.append(data[5])
    return prices


def three_days(data): # 判斷買進、賣出訊號
    output = []
    for i in range(len(data)):
        if i < 3: # 在判斷的當下是不會知道當天收盤價的，所以我們應該要做的事情為判斷"前三天"的收盤價狀況。
            output.append(0) # e.g. 第四天判斷第一、二、三天的收盤價
        elif data[i] > data[i - 1] > data[i - 2] > data[i - 3]:
            output.append(1)
        elif data[i] < data[i - 1] < data[i - 2] < data[i - 3]:
            output.append(-1)
        else:
            output.append(0)
    return output