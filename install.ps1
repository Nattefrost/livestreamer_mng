$scriptPath = split-path -parent $MyInvocation.MyCommand.Definition
If (Test-Path "$scriptPath\start.bat")
{
	Remove-Item "$scriptPath\start.bat"
}

write-host "==========================================================" -background "darkblue"
write-host "Downloading Python language"                                -foreground "green"
write-host "When the installer pops up, follow instructions and be sure to check 'add python to PATH'" -foreground "green"
write-host "It may take a while..."                                     -foreground "yellow" -background "DarkRed"
write-host "==========================================================" -background "darkblue"

# downloading python3.4.2 installer from python.org
$url = "https://www.python.org/ftp/python/3.4.2/python-3.4.2.msi"
$output = "$scriptPath\python3.msi"
$start_time = Get-Date

$wc = New-Object System.Net.WebClient
(New-Object System.Net.WebClient).DownloadFile($url, $output)

Write-Output "Time taken: $((Get-Date).Subtract($start_time).Seconds) second(s)"


# installing python3 and the livestreamer package through the packet manager
Start-Process .\python3.msi -Wait
& pip install livestreamer

# Creating symlink on desktop
$shell = New-Object -ComObject WScript.Shell
$desktop = [System.Environment]::GetFolderPath('Desktop')
$shortcut = $shell.CreateShortcut("$desktop\livestreamer_manager.lnk")

# write .bat file corresponding to proper directory
$cmd = "python $scriptPath\main.py"
$cmd | out-file "./start.bat" -Encoding ascii
$shortcut.TargetPath = "$scriptPath\start.bat"
$shortcut.IconLocation = "$scriptPath\ico.ico"
$shortcut.Save()
write-host "=========================================================="-background "darkblue"
write-host "Install over, double-click start.bat on your desktop" -foreground "magenta"
write-host "==========================================================" -background "darkblue"
$HOST.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown") | OUT-NULL
$HOST.UI.RawUI.Flushinputbuffer()
