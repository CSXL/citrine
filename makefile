# Define project name and paths
PROJECT_NAME = citrine
SRC_DIR = src
APP_DIR = app
TEST_DIR = test

# Define stack commands
STACK = stack
BUILD = $(STACK) build
EXEC = $(STACK) exec
TEST = $(STACK) test
CLEAN = $(STACK) clean
WATCH = $(STACK) build --file-watch
GHCI = $(STACK) ghci

# Default target
all: build

# Build the project
build:
	$(BUILD)

# Run the project
run:
	$(EXEC) $(PROJECT_NAME)-exe

# Run the test suite
test:
	$(TEST)

# Clean the project
clean:
	$(CLEAN)

# Watch for changes and rebuild
watch:
	$(WATCH)

ghci:
	$(GHCI)

.PHONY: all build run test clean watch ghci
