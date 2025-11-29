import sys

def read_data():
    n, m = map(int, sys.stdin.readline().strip().split())
    data = []
    for _ in range(n):
        line = list(map(float, sys.stdin.readline().strip().split()))
        features = line[:-1]
        label = 1 if line[-1] == 1 else -1
        data.append((features, label))
    return n, m, data

def perceptron(data, m, max_iterations=10000):
    a = [0.0] * m
    for _ in range(max_iterations):
        error_found = False
        for features, label in data:
            prediction = sum(a[j] * features[j] for j in range(m))
            if label * prediction <= 0:
                error_found = True
                for j in range(m):
                    a[j] += label * features[j]
        if not error_found:
            break
    return a

def main():
    n, m, data = read_data()
    a = perceptron(data, m)
    print(' '.join(map(str, a)))

if __name__ == "__main__":
    main()
