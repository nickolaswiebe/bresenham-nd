def line(start, end):
	d = [abs(b - a) for a, b in zip(start, end)]
	s = [1 if a < b else -1 for a, b in zip(start, end)]
	i = dmax = max(d)
	err = [dmax // 2 for _ in start]
	pos = start
	while True:
		yield pos
		if i == 0: return
		i -= 1
		err = [ex - dx for ex, dx in zip(err, d)]
		pos = [x + sx if ex < 0 else x for x, sx, ex in zip(pos, s, err)]
		err = [ex + dmax if ex < 0 else ex for ex in err]
