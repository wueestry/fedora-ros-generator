#!/usr/bin/env bash

# ./ros_generator.py --build --copr-owner wueestry --user_string "Ryan Wüest" --copr-project ros --chroot fedora-40-x86_64 desktop --recursive --distro humble --changelog "Generate initial config for all packages"

# Input 1: Fedora chroot
# Input 2: Changelog
 ./ros_generator.py --build --copr-owner wueestry --user_string "Ryan Wüest" --copr-project ros --chroot $1 desktop --recursive --distro humble --changelog $2
