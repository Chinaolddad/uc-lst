function getIP{
(Get-NetIPAddress).IPv4Address | select-string "192"
}
write-Host(getIP)
$IP = getIP
write-Host("This is out machine's IP :$IP")
write-Host("This machine's IP is {0}" -f $IP)