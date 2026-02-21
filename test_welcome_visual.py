#!/usr/bin/env python3
"""Simple visual test of the welcome screen."""

from textual.app import App, ComposeResult
from textual.widgets import Static
from vibe.setup.onboarding.screens.welcome import WelcomeScreen, WELCOME_TEXT

class TestWelcomeApp(App):
    def compose(self) -> ComposeResult:
        yield Static(f"Welcome message: {WELCOME_TEXT}", classes="highlight")
        yield Static("\nThis shows your DEVKAPR change is working!", classes="success")

if __name__ == "__main__":
    app = TestWelcomeApp()
    app.run()