def exp_doz(x, terms=50):
    if x < 0:
        return 1.0 / exp_doz(-x, terms)
    res = 1.0
    term = 1.0
    for i in range(1, terms):
        term *= (x / i)
        res += term
        if term < 1e-10:
            break
    return res

def relu(x):
    if isinstance(x, (int, float)):
        return max(0, x)
    if isinstance(x, list):
        return [relu(i) for i in x]

def sigmoid(x):
    if isinstance(x, (int, float)):
        return 1 / (1 + exp_doz(-x))
    if isinstance(x, list):
        return [sigmoid(i) for i in x]
