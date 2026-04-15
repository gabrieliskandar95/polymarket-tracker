"""
debug_urls.py — prints URL-related fields from the Polymarket API for 5 markets.
Run this once, paste the output back to Claude.

Usage: python debug_urls.py
"""
import requests, json

resp = requests.get(
    "https://gamma-api.polymarket.com/markets",
    params={"active": "true", "closed": "false", "limit": 5,
            "order": "volume", "ascending": "false"},
    timeout=15,
)

fields = ["question", "id", "slug", "groupSlug", "conditionId", "url"]

for m in resp.json():
    print("-" * 60)
    for f in fields:
        print(f"  {f}: {m.get(f, '(not present)')}")
print("-" * 60)
