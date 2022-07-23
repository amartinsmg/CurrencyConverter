all: compile

compile:
	pyinstaller program.spec

clean:
	rm build/* dist/*
