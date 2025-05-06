#!/bin/bash

ENV_FILE="/home/kent/.ssh/ssh-agent.env"

if [ -f "$ENV_FILE" ]; then
    source "$ENV_FILE" > /dev/null 2>&1
    echo "[ssh_cleanup] Killing ssh-agent PID $SSH_AGENT_PID"
    ssh-agent -k > /dev/null
    rm -f "$ENV_FILE"
    unset SSH_AGENT_PID
    unset SSH_AUTH_SOCK
    echo "[ssh_cleanup] Cleanup complete."
else
    echo "[ssh_cleanup] No active ssh-agent found."
fi
