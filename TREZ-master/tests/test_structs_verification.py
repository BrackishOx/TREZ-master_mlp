import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../src'))

from lib.structsdoz.structsdoz import TrezQueue, TrezStack
from lib.lossesdoz.lossdoz import mse, mse_grad
from lib.activationsdoz.activationsdoz import relu, sigmoid


def check(name, got, expected):
    if got == expected:
        print(f"OK  {name}")
    else:
        print(f"FAIL {name}")
        print(f"     got:      {got}")
        print(f"     expected: {expected}")
        sys.exit(1)


def test_queue():
    print("\n--- Queue ---")
    q = TrezQueue()
    check("isEmpty inicial", q.is_empty(), True)
    check("size inicial", q.size(), 0)

    q = q.enqueue(10).enqueue(20).enqueue(30)
    check("size tras 3 enqueue", q.size(), 3)
    check("peek FIFO", q.peek(), 10)
    check("toList", q.to_list(), [10, 20, 30])

    val, q2 = q.dequeue()
    check("dequeue val", val, 10)
    check("toList tras dequeue", q2.to_list(), [20, 30])
    check("original intacto", q.to_list(), [10, 20, 30])

    val2, q3 = q2.dequeue()
    check("2do dequeue", val2, 20)
    check("size tras 2 dequeues", q3.size(), 1)


def test_stack():
    print("\n--- Stack ---")
    s = TrezStack()
    check("isEmpty inicial", s.is_empty(), True)

    s = s.push(1).push(2).push(3)
    check("size tras 3 push", s.size(), 3)
    check("peek LIFO", s.peek(), 3)
    check("toList", s.to_list(), [1, 2, 3])

    top, s2 = s.pop()
    check("pop val", top, 3)
    check("toList tras pop", s2.to_list(), [1, 2])
    check("original intacto", s.to_list(), [1, 2, 3])

    top2, s3 = s2.pop()
    check("2do pop", top2, 2)
    check("size final", s3.size(), 1)


def test_activations():
    print("\n--- Activaciones ---")
    check("relu negativo", relu(-5), 0)
    check("relu cero", relu(0), 0)
    check("relu positivo", relu(3), 3)
    check("relu lista", relu([-1, 0, 2]), [0, 0, 2])

    sig = sigmoid(0)
    check("sigmoid(0) == 0.5", abs(sig - 0.5) < 1e-6, True)
    sig_lista = sigmoid([-1, 0, 1])
    check("sigmoid lista len", len(sig_lista), 3)
    check("sigmoid lista simetria", abs(sig_lista[0] + sig_lista[2] - 1.0) < 1e-6, True)


def test_losses():
    print("\n--- Perdidas ---")
    y_true = [0.0, 1.0, 0.5]
    y_pred = [0.1, 0.9, 0.4]

    error = mse(y_true, y_pred)
    check("mse > 0", error > 0, True)
    check("mse ~ 0.01", abs(error - 0.01) < 1e-6, True)

    grad = mse_grad(y_true, y_pred)
    check("mse_grad len", len(grad), 3)
    # grad[0] = 2*(0.1 - 0.0)/3 = 0.0667
    check("mse_grad[0] positivo", grad[0] > 0, True)
    # grad[1] = 2*(0.9 - 1.0)/3 = -0.0667
    check("mse_grad[1] negativo", grad[1] < 0, True)

    # Escalar
    check("mse escalar", mse(1.0, 0.0), 1.0)
    check("mse_grad escalar", mse_grad(1.0, 0.0), -2.0)


if __name__ == '__main__':
    test_queue()
    test_stack()
    test_activations()
    test_losses()
    print("\nTodas las pruebas de estructuras y libs pasaron.\n")
