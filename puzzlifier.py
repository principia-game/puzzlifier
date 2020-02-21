import sys

def main(file):
	print("==Puzzlifier==")
	with open(file, "rb+") as f:
		level_version = f.read(1)
		if not level_version >= bytes(0) and level_version <= bytes(29):
			print("[ERROR] File isn't a principia level or has an unsupported level version.")
		level_type = f.read(4)
		print("Level version: 0x%s" % level_version.hex())
		print("Level type: 0x%s" % level_type.hex())
		print("Changing level type to 0x00 (Puzzle)")
		f.seek(1)
		f.write(b"\0")


if __name__ == "__main__":
	if len(sys.argv) < 2:
		#print("[WARNING] No file chosen, will use test.plvl in working directory.")
		#main("test.plvl")
		print("no file!")
	else:
		main(sys.argv[1])
