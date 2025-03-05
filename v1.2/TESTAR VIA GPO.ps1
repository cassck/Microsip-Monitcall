# Caminho de origem do arquivo Contacts.xml em L:\
$caminhoOrigem = 'L:\Contacts.xml'

# Caminho de destino para onde você deseja importar o arquivo
$caminhoDestino = [System.IO.Path]::Combine($env:APPDATA, 'MicroSIP\Contacts.xml')

# Verifique se o arquivo de origem em L:\ existe antes de importá-lo
if (Test-Path $caminhoOrigem -PathType Leaf) {
    # Copie o arquivo
    Copy-Item -Path $caminhoOrigem -Destination $caminhoDestino -Force
    Write-Output "O arquivo $caminhoOrigem foi importado com sucesso para $caminhoDestino."
} else {
    Write-Output "O arquivo $caminhoOrigem não existe em L:\."
}
