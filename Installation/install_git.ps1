$url = "https://vscode.download.prss.microsoft.com/dbazure/download/stable/0ee08df0cf4527e40edc9aa28f4b5bd38bbff2b2/VSCodeSetup-x64-1.85.1.exe"
$vscode_dest = "C:\temp\VSCodeSetup-x64-1.85.1.exe"
Invoke-RestMethod -Uri $url -OutFile $vscode_dest

$url = "https://github.com/git-for-windows/git/releases/download/v2.43.0.windows.1/Git-2.43.0-64-bit.exe"
$git_dest = "Git-2.43.0-64-bit.exe"
Invoke-RestMethod -Uri $url -OutFile $git_dest



Start-Process -FilePath $vscode_dest -Argument "/VERYSILENT /NORESTART /MERGETASKS=!runcode,desktopicon,addcontextmenufiles,addcontextmenufolders"

code --install-extenstion "GitHub.vscode-pull-request-github"
code --install-extenstion "ms-python.python"
code --install-extenstion "emeraldwalk.RunOnSave"
code --install-extenstion "donjayamanne.githistory"
code --install-extenstion "Dart-Code.flutter"
code --install-extenstion "Dart-Code.dart-code"



Start-Process -FilePath $git_dest -Argument "/VERYSILENT /NORESTART"


# studio.exe --silent --all-users --install-location=C:\Your\Installation\Path --accept-license
