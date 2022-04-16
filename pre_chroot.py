import os
a = input("which disk do you want to use :  ")
b = input("which partition do you want to use for a boot partiton :  ")
c = input("which partition do you want to use for a root partition :  ")
print("now the installation will begin . You will have to do nothing any more . ")

# fdisk
print("now fdisk will be executed . ")
os.system("wipefs -a " + a)
os.system("fdisk " + a)

# now paritioning
os.system("mkfs.vfat " + b)
os.system("mkfs.ext4 " + c)

e = input("which partition do you want to use for a swap partition :  ")

if e == 'No' or 'no' or 'NO' or 'n' or 'N':
    pass

else:
    os.system("mkswap " + e)


# mount

os.system("mount " + c + " /mnt")
os.system("mkdir /mnt/boot")
os.system("mount " + b + " /mnt/boot")
os.system("swapon " + e)

# install

os.system("pacstrap /mnt base base-devel linux linux-firmware grub networkmanager network-manager-applet xorg xorg-xinit bspwm sxhkd zsh")
os.system("genfstab -U /mnt >> /mnt/etc/fstab")
os.system("cd ..")
os.system("mv aqainstall /mnt")
os.system("arch-chroot /mnt")