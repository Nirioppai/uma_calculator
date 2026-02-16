"""
Sync assets from the UmaTools folder into new_app.
Copies and overrides CSS, JS, assets, and favicon files.

Usage:
    python sync_assets.py
"""

import shutil
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
REFERENCE_DIR = SCRIPT_DIR.parent / "UmaTools"

SYNC_MAP = {
    # CSS files
    "css/base.css": "css/base.css",
    "css/theme-d.build.css": "css/theme-d.build.css",
    "css/rating.css": "css/rating.css",
    "css/optimizer.css": "css/optimizer.css",
    "css/tutorial.css": "css/tutorial.css",
    # JS files
    "js/optimizer.js": "js/optimizer.js",
    "js/rating-shared.js": "js/rating-shared.js",
    "js/tutorial.js": "js/tutorial.js",
    "js/nav.js": "js/nav.js",
    "js/theme-toggle.js": "js/theme-toggle.js",
    # Assets
    "assets/skills_all.json": "assets/skills_all.json",
    "assets/uma_skills.csv": "assets/uma_skills.csv",
    "assets/rank_badges.png": "assets/rank_badges.png",
    # Favicons
    "favicon.ico": "favicon.ico",
    "favicon-16x16.png": "favicon-16x16.png",
    "favicon-32x32.png": "favicon-32x32.png",
    "apple-touch-icon.png": "apple-touch-icon.png",
    "site.webmanifest": "site.webmanifest",
}


def sync():
    updated = 0
    skipped = 0

    for src_rel, dst_rel in SYNC_MAP.items():
        src = REFERENCE_DIR / src_rel
        dst = SCRIPT_DIR / dst_rel

        if not src.exists():
            print(f"  SKIP  {src_rel} (not found in UmaTools)")
            skipped += 1
            continue

        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)
        print(f"  COPY  {src_rel}")
        updated += 1

    print(f"\nDone: {updated} copied, {skipped} skipped.")


if __name__ == "__main__":
    sync()
