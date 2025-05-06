#!/bin/bash

# 設定
KEY_PATH="/home/kent/.ssh/id_rsa_level7"
ENV_FILE="/home/kent/.ssh/ssh-agent.env"

# 環境変数をクリア（以前の値を邪魔させない）
unset SSH_AGENT_PID
unset SSH_AUTH_SOCK

# 既存のエージェントが使えるか確認
if [ -f "$ENV_FILE" ]; then
    source "$ENV_FILE" > /dev/null 2>&1
    if ! kill -0 "$SSH_AGENT_PID" 2>/dev/null; then
        echo "[ssh_setup] Dead agent found. Cleaning..."
        rm -f "$ENV_FILE"
        unset SSH_AGENT_PID
        unset SSH_AUTH_SOCK
    fi
fi

# 新しいエージェントの起動と環境保存（必要時のみ）
if [ -z "$SSH_AGENT_PID" ]; then
    echo "[ssh_setup] Starting new ssh-agent..."
    ssh-agent -s | grep -v '^echo ' > "$ENV_FILE"
    source "$ENV_FILE"
fi

# 鍵を登録（未登録なら）
if ! ssh-add -l 2>/dev/null | grep -q "$(basename "$KEY_PATH")"; then
    echo "[ssh_setup] Adding key: $KEY_PATH"
    ssh-add "$KEY_PATH"
else
    echo "[ssh_setup] Key already added: $(basename "$KEY_PATH")"
fi
