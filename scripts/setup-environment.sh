#!/usr/bin/env bash

setup_env() {
  python3 -m venv .venv

  source .venv/bin/activate

  pip install --upgrade pip

  pip install -r requirements.txt

  deactivate

  cd ..
}

cd twitch_bot
setup_env

cd twitch_events
setup_env

cd widgets
setup_env
