all: compile

compile:
	pyinstaller program.spec

clean:
	rm -rf build/* dist/*
