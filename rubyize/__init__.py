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

def common_compact(itr):
    return filter(lambda e: e is not None, itr)

def common_to_iter(itr):
    return iter(itr)

def common_flat_map(itr, f):
  for elem in itr:
    for e in f(elem):
      yield e

def common_each_cons(itr, n):
  tmp_list = []
  for e in itr:
    tmp_list.append(e)
    if len(tmp_list) == n:
      yield tmp_list
      # Shift
      tmp_list = tmp_list[1:]

def common_each_slice(itr, n):
  tmp_list = []
  for e in itr:
    tmp_list.append(e)
    if len(tmp_list) == n:
      yield tmp_list
      # Make it empty
      tmp_list = []

  if tmp_list != []:
    yield tmp_list

# === object class extensions ===
def object_to_str(self):
    return str(self)
curse(object, 'to_str', object_to_str)

# === list class extensions ===

def wrap_list_func(func):
    return lambda *args, **kwargs: list(func(*args, **kwargs))

def list_length(self):
    return len(self)

for method_name, func in [
        ('to_list',    common_to_list),
        ('map',        wrap_list_func(common_map)),
        ('filter',     wrap_list_func(common_filter)),
        ('length',     list_length),
        ('inject',     common_inject),
        ('reduce',     common_inject),
        ('take',       wrap_list_func(common_take)),
        ('drop',       wrap_list_func(common_drop)),
        ('group_by',   common_group_by),
        ('compact',    wrap_list_func(common_compact)),
        ('to_iter',    common_to_iter),
        ('flat_map',   wrap_list_func(common_flat_map)),
        ('each_cons',  wrap_list_func(common_each_cons)),
        ('each_slice', wrap_list_func(common_each_slice)),
    ]:
    curse(list, method_name, func)


# === Extensions of iterable classes ===

# TODO: Add all builtin iterator classes in https://github.com/python/cpython/blob/5ce0a2a100909104836f53a2c8823006ec46f8ad/Lib/_collections_abc.py
list_literator = type(iter([]))
range_iterator = type(iter(range(0)))
generator      = type((lambda: (yield))())

for iterable_class in [
        range,
        map,
        filter,
        zip,
        enumerate,
        generator,
        list_literator,
        range_iterator,
    ]:
    for method_name, func in [
            ('to_list',    common_to_list),
            ('map',        common_map),
            ('filter',     common_filter),
            ('inject',     common_inject),
            ('reduce',     common_inject),
            ('take',       common_take),
            ('drop',       common_drop),
            ('group_by',   common_group_by),
            ('compact',    common_compact),
            ('to_iter',    common_to_iter),
            ('flat_map',   common_flat_map),
            ('each_cons',  common_each_cons),
            ('each_slice', common_each_slice),
    ]:
        curse(iterable_class, method_name, func)
