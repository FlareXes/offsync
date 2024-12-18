# OffSync

<p align="center"><strong>OffSync</strong> is a simple open-source stateless password manager inspired by LessPass. <br>The significant difference is that it allows users to store profiles (site, username, password length, etc.) locally without creating an account. So, no bloated web and online accounts.</p>

<p align="center">
    <img src="./assets/preview.png" alt="Demo GIF" />
</p>

### What does stateless actually mean?
`Stateless` simply means that your password is never being stored. You just store some information about your account locally. And, Passwords get generated on the fly depending on the account info you provided and the secret key. There is no master password. Every secret key is master password. Didn't understand, [check out yourself here](https://www.lesspass.com/).

---
## How this works?
OffSync asks you four simple questions `site`, `username / e-mail`, `length`, `counter`.

`Counter` is just an integer which has a default value of `1`. `counter` can be used to change the password of any profile that you saved before. For instance, if you have a GitHub account and after some time you want to change its password without changing the basic parameters like `site`, `username/e-mail`, `length` then you can change the value of `counter` may be like `2`.

### Concept Description
1. Create a **salt**: `site` + `username / e-mail` + `length` + `counter`
2. Create a **seed** from [KDF](https://en.wikipedia.org/wiki/Key_derivation_function): KDF(**salt**, **master password**)
3. **Seed** the [PRNG](https://en.wikipedia.org/wiki/Pseudorandom_number_generator) to generate a strong password

# Install
```bash
git clone https://github.com/FlareXes/offsync && cd offsync
chmod +x ./setup.sh
./setup.sh
```

# Uninstall
```bash
sudo rm -rf /usr/local/bin/offsync /opt/offsync/ ~/.config/offsync/
pip uninstall rich
```
# License
This work by [FlareXes](https://github.com/FlareXes) is Licensed under the terms of [GNU GPLv3](LICENSE).
