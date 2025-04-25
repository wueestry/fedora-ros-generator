#!/usr/bin/env bash
sudo dnf install python3-devel python3-pygraphviz python3-defusedxml python3-rosdep python3-rosinstall_generator python3-copr python3-termcolor python3-jinja2 rpmdevtools

sudo rosdep init
rosdep update