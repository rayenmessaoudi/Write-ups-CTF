I was sniffing some important piece of data transmitted via USB. 
This pcap file contains all what we need to recover the flag can you help ?

Solution : 

The pcap file showed 3 files being transferred to the USB drive.

![](https://github.com/rayenmessaoudi/Write-ups-CTF/blob/master/HackZone%20VI/USB%20Transfer/images/fore.png?raw=true)
a text file is one of the interresting files contains some base64 code, we extract the file using wireshark we decode it we got a maxicode pic using online decoder https://zxing.org/w/decode.jspx we got the flag : 

HZVI{m4x1c0d3_15_4w350m3}

