#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Farhida Islam Toushi_REG-ICT-WADP-L4-001587_Portfolio.settings")
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
