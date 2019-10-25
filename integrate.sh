python ../YGitBookIntegration/integrate.py . -ll 2
echo "---
description: Sitede neler olup bittiğinin 📜 raporudur. Buradaki terimleri 🔍 arama motorunda aratarak sayfaya erişebilirsin
---
" > CHANGELOG.md

ygitchangelog.exe >> CHANGELOG.md
bash github .
