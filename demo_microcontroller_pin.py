""" Test on circuitpython: list microcontroller pins in natsort order """

import microcontroller,board
from unatsort import natsort
allpins = []
for pin in dir(microcontroller.pin):
	if isinstance(getattr(microcontroller.pin, pin), microcontroller.Pin):
		mp = "{:28s} ".format("microcontroller.pin."+pin)
		pins = []
		for alias in dir(board):
			if getattr(board, alias) is getattr(microcontroller.pin, pin):
				pins.append("board.{}".format(alias))
			natsort(pins)
		allpins.append(mp+" ".join(pins))

natsort(allpins)
for pins in allpins: print(pins)
