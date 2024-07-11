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
	$(STACK) build --file-watch

.PHONY: all build run test clean watch
