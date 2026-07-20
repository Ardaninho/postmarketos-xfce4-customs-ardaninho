

all:
	@echo "postmarketos-xfce4-customs-ardaninho: Custom scripts for xfce4 on PostmarketOS"
	@echo "Copyright (C) 2026 Ardaninho"
	@echo "Available options:"
	@echo "install: Install postmarketos-xfce4-customs-ardaninho (root)"
	@echo "uninstall: Uninstall postmarketos-xfce4-customs-ardaninho (root)"

.PHONY: install uninstall

check_root:
	@if [ "$$(id -u)" -ne 0 ]; then \
		echo "This action requires root. Please run: sudo make $(MAKECMDGOALS)"; \
		exit 1; \
	fi

power_menu_install: check_root
	@echo "postmarketos-xfce4-customs-ardaninho: Custom scripts for xfce4 on PostmarketOS"
	@echo "Copyright (C) 2026 Ardaninho"
	@printf "  %-8s %s\n" "MKDIR" "/usr/share/postmarketos-xfce4-customs-ardaninho"
	@mkdir -p /usr/share/postmarketos-xfce4-customs-ardaninho
	@printf "  %-8s %s\n" "INSTALL" "power_menu"
	@cp -R power_menu /usr/share/postmarketos-xfce4-customs-ardaninho
	@printf "  %-8s %s\n" "LN" "/bin/ardaninho_power_menu"
	@ln -sf /usr/share/postmarketos-xfce4-customs-ardaninho/power_menu/power_menu.py /bin/ardaninho_power_menu
	@echo "Installed. Please configure manually."

power_menu_uninstall: check_root
	@echo "postmarketos-xfce4-customs-ardaninho: Custom scripts for xfce4 on PostmarketOS"
	@echo "Copyright (C) 2026 Ardaninho"
	@printf "  %-8s %s\n" "RM" "/usr/share/postmarketos-xfce4-customs-ardaninho"
	@rm -rf /usr/share/postmarketos-xfce4-customs-ardaninho
	@printf "  %-8s %s\n" "RM" "/bin/ardaninho_power_menu"
	@rm -rf /bin/ardaninho_power_menu
	@echo "Uninstalled. Please configure manually."