import os
import sys


# Bothost usually runs the entry file directly from /app.
# Ensure package imports from /app/src work even without editable install.
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.join(ROOT_DIR, "src")
if SRC_DIR not in sys.path:
    sys.path.insert(0, SRC_DIR)

from shop_bot.__main__ import main  # noqa: E402


if __name__ == "__main__":
    main()
