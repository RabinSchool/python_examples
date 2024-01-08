$url = "https://raw.githubusercontent.com/RabinSchool/python_examples/main/settings.json"
$dest = "$Env:USERPROFILE\appdata\Roaming\code\user\settings.json"
Invoke-RestMethod -Uri $url -OutFile $dest
pause


