# lists the kernel versions and enter to boot to your default kernels


def displayKernelsInstalled():
    """Print default kernels installed in system"""

    count = 0
    with open('/boot/grub/grub.conf') as f:
        print("----" * 20)
        print('Default','|','Kernels available to boot')
        print("----" * 20)
        for line in f.readlines():
            if 'title' in line:
                print(count,"\t\t|", line.strip())
                count+=1
        print("----" * 20)


if __name__ == '__main__':
    displayKernelsInstalled()




