$scriptPath = split-path -parent $MyInvocation.MyCommand.Definition
If (Test-Path "$scriptPath\start.bat")
{
	Remove-Item "$scriptPath\start.bat"
}

echo "Downloading Python language"
echo "When the installer pops up, follow instructions and be sure to check 'add python to PATH'"
echo "It may take a while..."


<#$webclient = New-Object System.Net.WebClient
$url = "https://www.python.org/ftp/python/3.4.2/python-3.4.2.msi"
$file = "./python.msi"
$webclient.DownloadFile($url,$file)
Start-Process .\python.msi
& pip install livestreamer
echo "Install over, launch start.bat" #>

$shell = New-Object -ComObject WScript.Shell
$desktop = [System.Environment]::GetFolderPath('Desktop')
$shortcut = $shell.CreateShortcut("$desktop\livestreamer_manager.lnk")

# write .bat file corresponding to proper directory
$cmd = "python3 $scriptPath\main.py"
$cmd | out-file "./start.bat" -Encoding ascii
$shortcut.TargetPath = "$scriptPath\start.bat"
$shortcut.IconLocation = "$scriptPath\ico.ico"
$shortcut.Save()
