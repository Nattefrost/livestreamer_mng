$scriptPath = split-path -parent $MyInvocation.MyCommand.Definition
If (Test-Path "$scriptPath\start.bat")
{
	Remove-Item "$scriptPath\start.bat"
}

echo "=========================================================="
echo "Downloading Python language"
echo "When the installer pops up, follow instructions and be sure to check 'add python to PATH'"
echo "It may take a while..."
echo "=========================================================="

<# downloading python3.4.2 installer from python.org
$url = "https://www.python.org/ftp/python/3.4.2/python-3.4.2.msi"
$output = "$scriptPath\python3.msi"
$start_time = Get-Date

$wc = New-Object System.Net.WebClient
(New-Object System.Net.WebClient).DownloadFile($url, $output)

Write-Output "Time taken: $((Get-Date).Subtract($start_time).Seconds) second(s)"
#>

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
echo "=========================================================="
echo "Install over, double-click start.bat on your desktop"
echo "=========================================================="
$HOST.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown") | OUT-NULL
$HOST.UI.RawUI.Flushinputbuffer()