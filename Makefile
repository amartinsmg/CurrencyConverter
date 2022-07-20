all: compile
	echo program successfully bundled

compile:
	pyinstaller program.spec
