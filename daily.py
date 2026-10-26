#!/usr/bin/env python3
"""Digest quotidien d'anglais pour Telegram.

3 expressions + 5 mots + 3 révisions, choisis de façon déterministe à partir
du jour de l'année (même contenu toute la journée, rotation sur tout le corpus).
Aucune dépendance. Lit src/data.json.
"""
import json
import pathlib
import random
from datetime import date

ROOT = pathlib.Path(__file__).parent
_src = ROOT / "src" / "all.json"
if not _src.exists():
    _src = ROOT / "src" / "data.json"
DATA = json.loads(_src.read_text(encoding="utf-8"))
APP = "https://jura39bot.github.io/anglais/"

ADULT = ["A1", "A2", "B1", "B2"]


def all_items():
    out = []
    for lvl in ADULT:
        for it in DATA[lvl]:
            out.append({**it, "lvl": lvl})
    return out


def pick_pool(items, pred):
    return [i for i in items if pred(i)]


def main():
    today = date.today()
    seed = today.toordinal()
    rnd = random.Random(seed)

    items = all_items()
    phrases = pick_pool(items, lambda x: " " in x["e"] or x["lvl"] in ("B1", "B2"))
    words = pick_pool(items, lambda x: " " not in x["e"] and x["lvl"] in ("A1", "A2"))

    exps = rnd.sample(phrases, 3)
    wds = rnd.sample(words, 5)
    used = {x["e"] for x in exps + wds}
    revs = rnd.sample([x for x in items if x["e"] not in used], 3)

    L = []
    L.append(f"🇬🇧 *Anglais du jour* — {today.strftime('%d/%m/%Y')}")
    L.append("")
    L.append("💬 *3 expressions*")
    for x in exps:
        L.append(f"• *{x['e']}* — {x['f']}")
        L.append(f"   _ {x['p']} _")
        L.append(f"   {x['x']}")
        L.append(f"   → {x['xf']}")
    L.append("")
    L.append("📚 *5 mots*")
    for x in wds:
        L.append(f"• *{x['e']}* — {x['f']}  _ {x['p']} _")
    L.append("")
    L.append("🔁 *Révisions* — trouve la traduction")
    for n, x in enumerate(revs, 1):
        L.append(f"{n}. *{x['e']}*")
    L.append("")
    L.append("_Réponses :_ " + " · ".join(f"{n}. {x['f']}" for n, x in enumerate(revs, 1)))
    L.append("")
    L.append(f"▶️ [Continuer la leçon]({APP}) — 10 min suffisent.")

    print("\n".join(L))


if __name__ == "__main__":
    main()
