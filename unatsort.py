import re as _re

def _coerce_to_int(x):
	if x != "" and x[0] in '0123456789':
		try:
			return int(x)
		except ValueError:
			return x
	else:
		return x

#_numbers = _re.compile(r'(\d+)')
#return [x for x in _numbers.split(str_in) if x != ""]
_spliter = _re.compile("(.*?)(\d+)(.*)")
def _split_components(str_in):
	dec = []
	ss = str_in
	while ss != "":
		mm = _spliter.match(ss)
		if mm:
			gr = mm.groups()
			dec += gr[0:2]
			ss = gr[-1]
		else:
			dec += [ss]
			break
	return dec

def _tokenize(str_in):
	sc = _split_components(str_in)
	return [_coerce_to_int(x) for x in sc]

def natsort(liste):
	liste.sort(key=_tokenize)

def natsorted(liste):
	ls = list(liste)
	ls.sort(key=_tokenize)
	return ls
