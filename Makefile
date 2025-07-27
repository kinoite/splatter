# Makefile for splatter.py

.PHONY: install uninstall clean

install:
	@echo "Installing splatter to /usr/bin..."
	@echo "This operation requires superuser privileges."
	sudo cp splatter.py /usr/bin/splatter
	sudo chmod +x /usr/bin/splatter
	@echo "splatter installed successfully to /usr/bin/splatter"
	@echo "You can now run it from anywhere by typing 'splatter'"

uninstall:
	@echo "Uninstalling splatter from /usr/bin..."
	@echo "This operation requires superuser privileges."
	sudo rm -f /usr/bin/splatter
	@echo "splatter uninstalled."

clean:
	@echo "No temporary files to clean."
