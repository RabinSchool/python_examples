$url = "https://github.com/git-for-windows/git/releases/download/v2.43.0.windows.1/Git-2.43.0-64-bit.exe"
$git_dest = "Git-2.43.0-64-bit.exe"
Invoke-RestMethod -Uri $url -OutFile $git_dest



Start-Process -FilePath $git_dest -Argument "/VERYSILENT /NORESTART"

