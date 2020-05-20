if [[ -n $SSH_CONNECTION ]]; then export DISPLAY=$(echo "$SSH_CLIENT" | awk "{print \$1;}"):0.0; fi
alias wireshark = wireshark-gtk