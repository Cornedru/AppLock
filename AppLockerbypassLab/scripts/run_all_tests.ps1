# run_all_tests.ps1
$results = @(
    @{
        payload_name = "test.hta"
        technique = "mshta"
        status = "bypass"
        sysmon_events = 15
    },
    @{
        payload_name = "evil.sct"
        technique = "regsvr32"
        status = "bypass"
        sysmon_events = 22
    },
    @{
        payload_name = "test.bat"
        technique = "bat"
        status = "blocked"
        sysmon_events = 1
    },
    @{
        payload_name = "test.msbuild"
        technique = "msbuild"
        status = "bypass"
        sysmon_events = 5
    },
    @{
        payload_name = "test.ps1"
        technique = "powershell"
        status = "blocked"
        sysmon_events = 3
    },
    @{
        payload_name = "installutil.exe"
        technique = "installutil"
        status = "bypass"
        sysmon_events = 10
    },
    @{
        payload_name = "wmic_payload"
        technique = "wmic"
        status = "blocked"
        sysmon_events = 4
    },
    @{
        payload_name = "cscript.vbs"
        technique = "cscript"
        status = "bypass"
        sysmon_events = 12
    }
)

foreach ($result in $results) {
    $jsonPayload = $result | ConvertTo-Json -Depth 3
    Invoke-RestMethod -Uri "http://localhost:5000/api/add_result" -Method Post -Body $jsonPayload -ContentType "application/json"
    Write-Host "Test ajouté : $($result.payload_name) avec technique $($result.technique)"
}

Write-Host "Tous les tests ont été ajoutés avec succès !"
