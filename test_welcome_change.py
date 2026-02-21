#!/usr/bin/env python3
"""Simple script to test the welcome screen change."""

from vibe.setup.onboarding.screens.welcome import WELCOME_TEXT, WELCOME_HIGHLIGHT

print("Current welcome message:")
print(f"Full text: {WELCOME_TEXT}")
print(f"Highlight part: {WELCOME_HIGHLIGHT}")

# Check if the change was applied
if "devkapr" in WELCOME_TEXT.lower():
    print("\n✅ SUCCESS: Your change to 'devkapr' is working!")
else:
    print("\n❌ The change was not applied correctly")