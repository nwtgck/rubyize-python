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


# === object class extensions ===

def object_to_str(self):
    return str(self)

curse(object, 'to_str', object_to_str)

# === list class extesions ===
def list_length(self):
    return len(self)

curse(list, 'map',    common_map)
curse(list, 'filter', common_filter)
curse(list, 'length', list_length)
curse(list, 'inject', common_inject)
curse(list, 'reduce', common_inject)

# === range class extesions ===

curse(range, "to_list", common_to_list)
curse(range, "map",     common_map)
curse(range, "filter",  common_filter)
curse(range, 'inject',  common_inject)
curse(range, 'reduce',  common_inject)



# === map class extesions ===

curse(map, "to_list", common_to_list)
curse(map, "map",     common_map)
curse(map, "filter",  common_filter)
curse(map, 'inject',  common_inject)
curse(map, 'reduce',  common_inject)

# === filter class extesions ===

curse(filter, "to_list", common_to_list)
curse(filter, "map",     common_map)
curse(filter, "filter",  common_filter)
curse(filter, 'inject',  common_inject)
curse(filter, 'reduce',  common_inject)