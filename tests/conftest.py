"""Setup Pytest testing environment."""

import os
import sys

# Add parent directory of the tests folder to import search path
# so that 'apiapp' package can be imported for testing
ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.insert(0, ROOT_DIR)
