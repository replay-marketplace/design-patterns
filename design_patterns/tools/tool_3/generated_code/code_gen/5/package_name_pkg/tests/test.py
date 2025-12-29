import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'package_name')))
from hello_world import hello_world

def test_hello_world():
    assert hello_world() == 'Hello, World!'
