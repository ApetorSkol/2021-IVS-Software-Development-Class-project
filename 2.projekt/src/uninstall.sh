whiptail --yesno "Do you really want to uninstall the IVS calculator?" 0 0 || exit 1
rm -f /usr/bin/ivscalculator
rm -f /usr/share/pixmaps/ivscalculator.png
rm -f /usr/share/applications/ivscalculator.desktop

# remove self
rm -f /usr/bin/ivscalculator-uninstall
