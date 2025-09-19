#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from dotenv import load_dotenv

load_dotenv()


def main():
    """Run administrative tasks."""
    setting_module = os.getenv("DJANGO_SETTINGS_MODULE", "config.settings.development")

    if "--prod" in sys.argv:
        # setting_module = os.getenv(
        #     "DJANGO_SETTINGS_MODULE", "config.settings.production"
        # )
        setting_module = "config.settings.production"
        sys.argv.remove("--prod")

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", setting_module)
    # os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.development")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
