I have forgotten the password of my favourite password manager all what i have is this spreadsheet file.

We are given an xlsm file (Microsoft Excel 2007) with a protected vba macro.
![](https://github.com/rayenmessaoudi/Write-ups-CTF/blob/master/HackZone%20VI/Recover%20My%20Secret/images/clik.png?raw=true)
Some tricks to break the protection : 

- http://datapigtechnologies.com/blog/index.php/hack-into-password-protected-vba-projects/
- olevba command

![](https://github.com/rayenmessaoudi/Write-ups-CTF/blob/master/HackZone%20VI/Recover%20My%20Secret/images/olevba.png?raw=true)

then we use the secret code to open the keepass database and find the flag.
![](https://github.com/rayenmessaoudi/Write-ups-CTF/blob/master/HackZone%20VI/Recover%20My%20Secret/images/keepass.png?raw=true)

HZVI{k33p455_15_my_f4v0ur173_p455w0rd_m4n463r}
