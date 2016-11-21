def smart_str(x):
  if x != None:
    if isinstance(x, unicode):
      return unicode(x).encode("utf-8")
    elif isinstance(x, int) or isinstance(x, float) or isinstance(x, list):
      return str(x)
    else:
      return x
  else:
    x = "None"
    return x
  return x