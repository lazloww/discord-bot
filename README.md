# discord-bot
A simple Discord bot for joining and leaving voice channels.

# Simple Discord Bot

This is my first Python project, a simple Discord bot that joins and leaves voice channels when I do. 🎉

## Features
- **Automatic Channel Join**: The bot joins a voice channel when I join.
- **Automatic Channel Leave**: The bot disconnects when I leave a voice channel.
- Written in Python using the [discord.py](https://discordpy.readthedocs.io/) library.

## How It Works
1. The bot listens for changes in voice channel activity using the `on_voice_state_update` event.
2. When it detects that **my user ID** has joined or left a channel:
   - It joins the same voice channel I enter.
   - It disconnects from the channel when I leave.

## Prerequisites
- Python 3.8 or newer.
- The `discord.py` library installed:
  ```bash
  pip install discord.py
