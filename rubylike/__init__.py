from forbiddenfruit import curse

# === common extensions ===

def common_to_list(self):
    return list(self)

def common_map(self, f):
    return map(f, self)

def common_filter(self, p):
    return filter(p, self)

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

# === range class extesions ===

curse(range, "to_list", common_to_list)
curse(range, "map",     common_map)
curse(range, "filter",  common_filter)


# === map class extesions ===

curse(map, "to_list", common_to_list)
curse(map, "map",     common_map)
curse(map, "filter",  common_filter)

# === filter class extesions ===

curse(filter, "to_list", common_to_list)
curse(filter, "map",     common_map)
curse(filter, "filter",  common_filter)