import numpy as np

def unitStep(v):
    if v >= 0:
        return 1
    else:
        return 0

def perceptronModel(x, w, b):
    v = np.dot(w, x) + b
    y = unitStep(v)
    return y

def AND_logicFunction(x):
    w = np.array([1,1])
    b = -1.5
    return perceptronModel(x, w, b)

def OR_logicFunction(x):
    w = np.array([1,1])
    b = -0.5
    return perceptronModel(x, w, b)

def NOT_logicFunction(x):
    wNOT = -1
    bNOT = 0.5
    return perceptronModel(x, wNOT, bNOT)

def NOR_logicFunction(x):
    output_OR = OR_logicFunction(x)
    output_NOT = NOT_logicFunction(output_OR)
    return output_NOT

def NAND_logicFunction(x):
    output_AND = AND_logicFunction(x)
    output_NOT = NOT_logicFunction(output_AND)
    return output_NOT

def XOR_logicFunction(x):
    a, b = x
    y1 = NAND_logicFunction([a,a])
    y2 = NAND_logicFunction([b,b])
    y3 = NAND_logicFunction([a,y2])
    y4 = NAND_logicFunction([y1,b])
    finalOutput = NAND_logicFunction([y3,y4])
    return finalOutput

def XNOR_logicFunction(x):
    y1 = OR_logicFunction(x)
    y2 = AND_logicFunction(x)
    y3 = NOT_logicFunction(y1)
    final_x = np.array([y2, y3])
    finalOutput = OR_logicFunction(final_x)
    return finalOutput

# Test cases
test1 = np.array([0,1])
test2 = np.array([1,1])
test3 = np.array([0,0])
test4 = np.array([1,0])
test5 = np.array(1)
test6 = np.array(0)

# Testing all gates
print("AND Gate:")
print("AND({},{})={}".format(0,1,AND_logicFunction(test1)))
print("AND({},{})={}".format(1,1,AND_logicFunction(test2)))
print("AND({},{})={}".format(0,0,AND_logicFunction(test3)))
print("AND({},{})={}".format(1,0,AND_logicFunction(test4)))

print("\nOR Gate:")
print("OR({},{})={}".format(0,1,OR_logicFunction(test1)))
print("OR({},{})={}".format(1,1,OR_logicFunction(test2)))
print("OR({},{})={}".format(0,0,OR_logicFunction(test3)))
print("OR({},{})={}".format(1,0,OR_logicFunction(test4)))

print("\nNOT Gate:")
print("NOT({})={}".format(1, NOT_logicFunction(test5)))
print("NOT({})={}".format(0, NOT_logicFunction(test6)))

print("\nNOR Gate:")
print("NOR({}, {}) = {}".format(0, 1, NOR_logicFunction(test1)))
print("NOR({}, {}) = {}".format(1, 1, NOR_logicFunction(test2)))
print("NOR({}, {}) = {}".format(0, 0, NOR_logicFunction(test3)))
print("NOR({}, {}) = {}".format(1, 0, NOR_logicFunction(test4)))

print("\nNAND Gate:")
print("NAND({}, {}) = {}".format(0, 1, NAND_logicFunction(test1)))
print("NAND({}, {}) = {}".format(1, 1, NAND_logicFunction(test2)))
print("NAND({}, {}) = {}".format(0, 0, NAND_logicFunction(test3)))
print("NAND({}, {}) = {}".format(1, 0, NAND_logicFunction(test4)))

print("\nXOR Gate:")
print("XOR({}, {}) = {}".format(0, 1, XOR_logicFunction(test1)))
print("XOR({}, {}) = {}".format(1, 1, XOR_logicFunction(test2)))
print("XOR({}, {}) = {}".format(0, 0, XOR_logicFunction(test3)))
print("XOR({}, {}) = {}".format(1, 0, XOR_logicFunction(test4)))

print("\nXNOR Gate:")
print("XNOR({}, {}) = {}".format(0, 1, XNOR_logicFunction(test1)))
print("XNOR({}, {}) = {}".format(1, 1, XNOR_logicFunction(test2)))
print("XNOR({}, {}) = {}".format(0, 0, XNOR_logicFunction(test3)))
print("XNOR({}, {}) = {}".format(1, 0, XNOR_logicFunction(test4)))
