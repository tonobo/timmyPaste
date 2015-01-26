import functools

def typehint(f):
    @functools.wraps(f)
    def decorated(*args, **kws):
        if args:
            for item, value in sorted_annotation(
                    f.__annotations__,f.__code__.co_varnames,
                    f.__code__.co_argcount, args,
                    f.__defaults__).items():
                if not isinstance(value[1],value[0]):
                    raise TypeError(
                            "%s expected but '%s' (%s) given" % (
                                value[0], value[1], value[1].__class__)
                            )
        if kws:
            for item, klazz in f.__annotations__.items():
                if not item == ('self','return'):
                    if not isinstance(kws[item],klazz):
                        raise TypeError(
                            "Element %s expected as %s, Item: %s, Kwargs: %s" % (
                            kws[item], klazz, item, kws))
        result = f(*args, **kws)
        returntype = f.__annotations__.get('return')
        if isinstance(returntype, type):
            assert isinstance(result, returntype), (
                "Return value should be type of '%s' instead of '%s'" % (
                    returntype, result))
        return result
    return decorated

def sorted_annotation(annotation, varnames, argcount, args, defaults):
    d = dict()
    varnames = list(varnames)
    args = list(args)
    x = 0
    if not defaults:
        defaults = list()
    if not (len(args)+len(defaults) == argcount):
        raise TypeError('Invalid amount of arguments.')
    if varnames[0] == 'self':
        argcount -= 1
        varnames.pop(0)
        args.pop(0)
    for i,var in enumerate(varnames[:argcount]):
        if i <= len(args)-1:
            d[var] = (annotation[var], args[i])
        else:
            d[var] = (annotation[var], defaults[x])
            x += 1
    return d
