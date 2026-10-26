# Anglais — mots & expressions

Application web installable (PWA) pour apprendre l'anglais par petites leçons.

- Niveaux : A1, A2, B1, B2 + un parcours enfant
- 180 mots et expressions, avec phonétique, exemple et traduction
- Révisions espacées (boîtes de Leitner : 0/1/2/4/7/15/30/60 jours)
- Suivi : XP, série, minutes/heures, taux de réussite, progression par niveau
- Profil, export JSON, fonctionnement hors-ligne

## Installer sur iPhone
Safari → Partager → « Sur l'écran d'accueil ».

## Développer
```bash
python3 build.py          # src/template.html + src/data.json -> index.html
python3 daily.py          # digest quotidien (cron)
```
Après toute modification de `index.html`, incrémenter `CACHE` dans `sw.js` (`anglais-v1` → `v2`).
