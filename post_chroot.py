import os
print("this is the post_chroot install , you can skip this if you want a barebones install . But if you want a fully operable system , you have to do this . ")
a = input("plese enter the disk you want to install grub on : ")

# install and configuration
os.system("grub-install --target=i386-pc --recheck " + a)
os.system("grub-mkconfig -o /boot/grub/grub.cfg")
os.system("systemctl enable NetworkManager")
os.system("pacman -S picom neofetch cmatrix htop ranger")

# hostname
os.system("echo 'tux' > /etc/hostname")
os.system("echo '127.0.0.1  localhost' >> /etc/hosts")
os.system("echo '::1  localhost' >> /etc/hosts")
os.system("echo '127.0.1.1  tux.localdomain  tux' >> /etc/hosts")

# time configuraton
os.system("ln -sf /usr/share/zoneinfo/Asia/Kolkata /etc/localtime")
os.system("hwclock --systohc --localtime")

# locale
os.system("echo 'en_US.UTF-8 UTF-8' >> /etc/locale.gen")
os.system("locale-gen")

# user
os.system("useradd -m -g users -G wheel -s /bin/bash tux")
os.system("passwd tux")
os.system("echo '%wheel ALL=(ALL) ALL' >> /etc/sudoers")

# adding my arch rice
os.system("pacman -S git")
os.system("git clone https://github.com/Domilinux/dominus_config.git")
os.system("cd dominus_config")
os.system("mv alacritty bspwm sxhkd ~/.config")
os.system("mv wallpapers ~")
os.system("sudo pacman -S feh")
os.system("sudo pacman -S rofi")
os.system("zsh")
os.system("mv ~/dominus_dotfiles/zsh/zshrc ~/.zshrc")
os.system("cp /etc/X11/xinit/xinitrc ~/.xinitrc")
os.system("sed -i 's/twm &/ /g' ~/.xinitrc")
os.system("sed -i 's/xclock -geometry 50x50-1+1 &/ /g' ~/.xinitrc")
os.system("sed -i 's/xterm -geometry 80x50+494+51 &/ /g' ~/.xinitrc")
os.system("sed -i 's/xterm -geometry xterm -geometry 80x20+494-0 & &/ /g' ~/.xinitrc")
os.system("sed -i 's/exec xterm -geometry 80x66+0+0 -name login/ /g' ~/.xinitrc")
os.system("echo 'sxhkd &' >> ~/.xinitrc")
os.system("echo 'feh --bg-scale ~/wallpapers/a.jpg' >> ~/.xinitrc")
os.system("echo 'exec bspwm' >> ~/.xinitrc")
print("full system is now installed . feel free to reboot . ")


