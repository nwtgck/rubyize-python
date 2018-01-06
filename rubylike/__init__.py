from forbiddenfruit import curse

# === common extensions ===

def common_to_list(self):
    return list(self)

def common_map(self, f):
    return map(f, self)

def common_filter(self, p):
    return filter(p, self)

def common_inject(self, a, b=None):
    if b is None:
        zero = self[0]
        seq  = self[1:]
        f    = a
    else:
        seq  = self
        zero = a
        f    = b
    accum = zero
    for e in seq:
        accum = f(accum, e)
    return accum


def common_take(self, n):
    return self[:n]

def common_drop(self, n):
    return self[n:]

def common_group_by(iter, f):
    dict = {}
    for e in iter:
        group = f(e)
        if group in dict:
            dict[group].append(e)
        else:
            dict[group] = [e]
    return dict

def common_compact(iter):
    return filter(lambda e: e is not None, iter)

# === object class extensions ===
def object_to_str(self):
    return str(self)
curse(object, 'to_str', object_to_str)

# === list class extensions ===
def list_length(self):
    return len(self)

for method_name, func in [
        ('to_list',  common_to_list),
        ('map',      common_map),
        ('filter',   common_filter),
        ('length',   list_length),
        ('inject',   common_inject),
        ('reduce',   common_inject),
        ('take',     common_take),
        ('drop',     common_drop),
        ('group_by', common_group_by),
        ('compact',  common_compact),
    ]:
    curse(list, method_name, func)


# === range class extensions ===
for method_name, func in [
        ('to_list',  common_to_list),
        ('map',      common_map),
        ('filter',   common_filter),
        ('inject',   common_inject),
        ('reduce',   common_inject),
        ('take',     common_take),
        ('drop',     common_drop),
        ('group_by', common_group_by),
        ('compact',  common_compact),
]:
    curse(range, method_name, func)


# === map class extensions ===
for method_name, func in [
        ('to_list',  common_to_list),
        ('map',      common_map),
        ('filter',   common_filter),
        ('inject',   common_inject),
        ('reduce',   common_inject),
        ('take',     common_take),
        ('drop',     common_drop),
        ('group_by', common_group_by),
        ('compact',  common_compact),
]:
    curse(map, method_name, func)


# === filter class extensions ===
for method_name, func in [
        ('to_list',  common_to_list),
        ('map',      common_map),
        ('filter',   common_filter),
        ('inject',   common_inject),
        ('reduce',   common_inject),
        ('take',     common_take),
        ('drop',     common_drop),
        ('group_by', common_group_by),
        ('compact',  common_compact),
]:
    curse(filter, method_name, func)