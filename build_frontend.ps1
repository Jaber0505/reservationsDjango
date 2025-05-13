# Chemins relatifs à partir de la racine du projet (adaptés à ta structure)
$reactBuild = "C:\Users\jaber\Documents\GitHub\MonTravail\reservationsDjango\frontend\build"
$djangoStatic = "C:\Users\jaber\Documents\GitHub\MonTravail\reservationsDjango\backend\static"
$djangoTemplates = "C:\Users\jaber\Documents\GitHub\MonTravail\reservationsDjango\backend\templates"

# Vérification des chemins
if (!(Test-Path $reactBuild)) {
    Write-Error "Le dossier React build ($reactBuild) n'existe pas. As-tu lancé 'npm run build' ?"
    exit 1
}

# Nettoyage de l'ancien contenu statique
Write-Host "🧹 Suppression de l'ancien contenu statique..."
Remove-Item -Recurse -Force "$djangoStatic\*" -ErrorAction SilentlyContinue

# Copie du contenu de /build/static → /static
Write-Host "📁 Copie des fichiers statiques React dans Django..."
Copy-Item -Recurse -Force "$reactBuild\static\*" "$djangoStatic"

# Copie de index.html → templates/
Write-Host "📄 Copie de index.html dans templates..."
Copy-Item -Force "$reactBuild\index.html" "$djangoTemplates\index.html"

Write-Host "✅ Intégration du build React dans Django terminée."
