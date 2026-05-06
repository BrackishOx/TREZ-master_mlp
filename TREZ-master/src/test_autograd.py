import sys
import os
sys.path.append(os.path.dirname(__file__))

from autograd import Tensor

# Test mathematical expressions with Autograd
x = Tensor(-2.0)
y = Tensor(5.0)
z = Tensor(-4.0)

# Computational graph
q = x + y
f = q * z

# Backpropagation
f.backward()

assert x.grad == -4.0
assert y.grad == -4.0
assert z.grad == 3.0

print("Autograd works successfully! Gradients matched MicroGrad.")
