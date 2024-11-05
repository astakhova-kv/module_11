import inspect

def introspection_info(obj):
    info = {}
    info['type'] = type(obj).__name__
    attributes = [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith('__')]
    info['attributes'] = attributes
    methods = [method for method in dir(obj)]
    info['methods'] = methods
    info['module'] = obj.__module__ if hasattr(obj, '__module__') else None

    if isinstance(obj, (str, list, tuple, set, dict)):
        info['length'] = len(obj)

    if isinstance(obj, (int, float, complex)):
        info['is_integer'] = isinstance(obj, int)
        info['is_float'] = isinstance(obj, float)
        info['is_complex'] = isinstance(obj, complex)

    return info


number_info = introspection_info('obj')
print(number_info)