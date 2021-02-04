import microcontroller,board
from unatsort import natsort
allpins = []
for pin in dir(microcontroller.pin):
	if isinstance(getattr(microcontroller.pin, pin), microcontroller.Pin):
		pins = []
		for alias in dir(board):
			if getattr(board, alias) is getattr(microcontroller.pin, pin):
				pins.append("board.{}".format(alias))
			natsort(pins)
		if len(pins)>0:
			allpins.append(" ".join(pins))
natsort(allpins)
for pins in allpins: print(pins)
