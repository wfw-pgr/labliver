#!/bin/zsh

USER="user"
IP="192.168.1.101"

MOUNTPOINT="$HOME/mnt/oneDrive"
REMOTEPATH="/mnt/d/OneDrive/OneDrive - XXX"
LOG="$HOME/mnt/sshfs_command/sshfs_debug.log"
OPTIONS=allow-other,umask=000,idmap=user,ServerAliveInterval=15,ServerAliveCountMax=3

# -- keychain -- #
eval $(keychain --quiet --agents ssh id_ed25519)
source $HOME/.keychain/$HOST-sh
echo "SSH agent socket: $SSH_AUTH_SOCK" >> $LOG
ssh-add -l >> $LOG 2>&1

# -- sshfs -- #
if ! mount | grep -q "$MOUNTPOINT"; then
    nohup sshfs $USER@$IP:"$REMOTEPATH" "$MOUNTPOINT" -o $OPTIONS >> $LOG 2>&1 &
fi

# -- open  -- #
/usr/local/bin/wslstart $MOUNTPOINT
