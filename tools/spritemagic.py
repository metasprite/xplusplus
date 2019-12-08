import os
import sys
import platform

size = 64

if (len(sys.argv) < 3):
	print("magic.py - Automatic sprite ripping via ImageMagick. Usage: (directory) (name) [size]")
	sys.exit(0)
elif (len(sys.argv) > 3):
	size = int(sys.argv[3]);

files = []
for n in os.listdir(sys.argv[1]):
	if os.path.isfile(n):
		if (n.lower().endswith(".png") and len(n.split('_')) == 4):
			print(n)
			files.append(n)

i = 0
for f in files:
	i = i + 1
	ff = f.split('.')[0]
	tbl = ff.split('_')

	x = str(int(tbl[2])-(256/2))
	y = str(int(tbl[3])-(224/2))

	binary = "magick" if (platform.system().lower()[0] == 'w') else "convert"
	cmd = binary+' '+f+" -gravity center -extent 288x256 -alpha on -fill none -draw \"color 0,0 replace\" -fill none -draw \"color 33,33 replace\" -crop "+str(size)+"x"+str(size)+"+"+x+'+'+y+' +repage '+sys.argv[2]+'_'+tbl[1]+".png"
	print("\n"+cmd+"\n")
	os.system(cmd)
