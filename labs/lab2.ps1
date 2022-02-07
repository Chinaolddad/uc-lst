function getIP{
(Get-NetIPAddress).IPv4Address | select-string "192"
}
write-Host(getIP)

$IP = getIP
$Date = Get-Date
$Host1 = $Host1 = $Host.Version.Major
$Hostname = Get-WinObject Win32_computerSystem | select Name
$Body = "This machine's IP is $IP. User is $env:username. Hostname is $Hostname. PowerShell version $Host1. Today's Date is $Date"

Write-Host($Body)
Send-MailMessage -To "liu2sg@mail.uc.edu" -From "liushitong1998@gmail.com" -Subject "IT3038C windows Sysinfo" - Body $Body -smtpServer smtp.google.com -port 587 -UseSsl -Cerdential (Get-Certificate)