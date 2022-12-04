def new(name_or_class, *args, **kwargs):
    if isinstance(name_or_class, str):
        return globals()[name_or_class](*args, **kwargs)
    else:
        return name_or_class(*args, **kwargs)
