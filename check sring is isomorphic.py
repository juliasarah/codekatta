a = raw_input("")
b = raw_input("")

x = {}; y = {}
def is_isomorphic(a, b):
    if len(a) != len(b):
        return False
    else:
        for i, v in enumerate(a):
            if v in x and x[v] != b[i]:
                return False
            else:
                x[v] = b[i]
            if b[i] in y and y[b[i]] != v:
                return False
            else:
                y[b[i]] = v
        return True

print is_isomorphic(a, b)
