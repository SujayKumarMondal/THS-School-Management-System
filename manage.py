#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from dotenv import load_dotenv
load_dotenv()

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'THS.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    # If no command given, or if runserver is used without a port, add port 8006
    if len(sys.argv) == 1:
        sys.argv += ['runserver', '127.0.0.1:8006']
    elif sys.argv[1] == 'runserver' and len(sys.argv) == 2:
        sys.argv.append('127.0.0.1:8006')

    main()