>Maybe something missing there .
[Link](https://github.com/rayenmessaoudi/Write-ups-CTF/blob/master/MSSP%20CTF/c892bca9396fe285fdbaafdd55632d5c%20(8).corrupted?raw=true)

just open the file with a hex editor we can see that the hex signature started with 89 4E 47 0D 0A 1A 0A which is a png signature missing some bytes.
After fixing them the flag was : **msspctf{C0rrupT3d_PnG_Sign4tur3}**

![ss](https://github.com/rayenmessaoudi/Write-ups-CTF/blob/master/MSSP%20CTF/corrupted_fixing.PNG)
