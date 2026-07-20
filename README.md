# postmarketos-xfce4-customs-ardaninho
Custom scripts/apps for PostmarketOS on Xfce4
## Power menu
On some devices, to gain extra performance, you can disable compositing on Window Manager Tweaks. Regarding this app is that the compositing disables transparency.<br>Since the Xfce4 power menu contains transparency to darken the background, it will show a full black screen with the buttons working. You can add seperate buttons, but one misclick and you waste your time.<br>This is why I made this, in Python. Later porting to C++ using LLM. (or if anyone else is free to port it)<br>See [Xfce4#Performance on wiki.postmarketos.org](https://wiki.postmarketos.org/wiki/Xfce4#Performance)

To install: <code>sudo make power_menu_install</code><br>
And in Whiskermenu properties -> Commands, change `Log Out...` command to `ardaninho_power_menu`

Preview:
![res/image.png]()