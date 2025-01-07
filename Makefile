# Makefile for the Sign-Changer Project

# PHONY specifies commands that aren't filenames
.PHONY: clean run test

# Remove all __pycache__ directories
clean:
	find . -name "__pycache__" -exec rm -rf {} +

# Run the main program
run:
	python3 run.py

# Run the unit tests
test:
	python3 unittest_signchange.py
