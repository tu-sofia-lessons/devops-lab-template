# A small Debian "server" with systemd and SSH, for the Ansible lab.
FROM debian:13-slim
ENV container=docker
RUN apt-get update \
 && apt-get install -y --no-install-recommends systemd systemd-sysv openssh-server python3 sudo \
 && rm -rf /var/lib/apt/lists/* \
 && useradd --create-home --shell /bin/bash ansible \
 && echo "ansible ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/ansible \
 && mkdir -p /home/ansible/.ssh && chmod 700 /home/ansible/.ssh && chown ansible:ansible /home/ansible/.ssh \
 && systemctl enable ssh \
 && systemctl mask systemd-modules-load.service
# Copies the mounted public key into place on every boot, with the right owner and mode.
RUN printf '[Unit]\nBefore=ssh.service\n[Service]\nType=oneshot\nExecStart=/bin/sh -c "install -o ansible -g ansible -m 600 /keys/authorized_keys /home/ansible/.ssh/authorized_keys"\n[Install]\nWantedBy=multi-user.target\n' > /etc/systemd/system/lab-keys.service \
 && systemctl enable lab-keys.service
STOPSIGNAL SIGRTMIN+3
CMD ["/lib/systemd/systemd"]
