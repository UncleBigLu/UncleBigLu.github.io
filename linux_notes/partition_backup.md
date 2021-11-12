# Move /usr from one disk to another on the fly

Gparted 在磁盘挂载状态下无法对磁盘进行复制/resize等操作。/usr分区无法在开机状态下umount，故使用dd命令强行进行拷贝。

1. 在目标磁盘使用Gparted创建新分区

**目标分区可以大于原始分区，但会导致dd拷贝完成后多余的分区处于unallocated状态。使用gparted疑似可以在该分区未挂载时解决这一问题，但未进行尝试**

2. 使用dd命令拷贝原始分区至新分区

`dd bs=1M if=/dev/sdax of=/dev/nvmexxxx`

**dd \<other argv\> status=progress**可用于输出dd进度（未测试）

3. fsck 修复一下新分区和旧分区

由于未umount分区，dd操作相当于进行了一次拔电源，没有properly umount

4. 修改新分区uuid

uuid位于每个分区头部，可以通过`hexedit /dev/sda3`命令查看到。使用命令`lsblk -f`可以看到所有分区uuid。由于新分区由旧分区复制产生，因此uuid与旧分区相同，需要为新分区生成一个新的uuid。使用`tune2fs -U random /dev/sda3`修改新分区uuid。

5. 修改fstab, 把旧分区uuid 改为新分区uuid。重启计算机，新分区即可自动挂载。