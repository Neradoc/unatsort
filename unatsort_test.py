#import code_horloge
from unatsort import natsort,natsorted

def asserte(message,left,right):
	if left != right:
		print(f"{message}: ERROR")
	else:
		print(f"{message}: PASS")

l0 = ['D1', 'D2', 'D3', 'D9', 'D10', 'D30', 'D100']
l1 = ["D2","D10","D9","D3","D100","D1","D30"]
natsort(l1)
asserte("natsort___ 1",l1,l0)

l2 = ["D2","D10","D9","D3","D100","D1","D30"]
l3 = natsorted(l2)
asserte("natsorted_ 1",l3,l0)

l4_0 = ['22AA33DD', 'CC55FF88']
l4 = ["CC55FF88","22AA33DD"]
natsort(l4)
asserte("natsort___ 2",l4,l4_0)

l5_0 = ['50D9', '400D2', 'D1', 'D3U', 'D10', 'D30', 'D100']
l5 = ["400D2","D10","50D9","D3U","D100","D1","D30"]
natsort(l5)
asserte("natsort___ 3",l5,l5_0)
