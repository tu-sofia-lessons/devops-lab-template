# Lab servers / Сървъри за упражненията

Four small Debian 13 servers with systemd and SSH (web1, web2, db, lb), for the Ansible lab. / Четири малки сървъра с Debian 13, systemd и SSH, за упражнението с Ansible.

```bash
test -f ~/.ssh/id_ed25519 || ssh-keygen -t ed25519 -N "" -f ~/.ssh/id_ed25519
docker compose -f infra/servers/compose.yaml up -d --build
ssh -p 2201 -o StrictHostKeyChecking=no ansible@127.0.0.1 hostname   # web1
```

| Server | SSH port | Other |
|---|---|---|
| web1 | 2201 | |
| web2 | 2202 | |
| db | 2203 | |
| lb | 2204 | port 80 → 8080 |

User `ansible` with passwordless sudo; your public key is used for login. Inside their network the servers reach each other by name (`db`, `web1`, ...). / Потребител `ansible` със sudo без парола; входът е с вашия публичен ключ. В своята мрежа сървърите се намират по име.
