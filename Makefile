all: compile
	echo program successfully bundled

compile:
	pyinstaller program.spec

clean:
	rm build/* dist/*
