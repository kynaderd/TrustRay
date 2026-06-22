# test_trustray.py
"""
Tests for TrustRay module.
"""

import unittest
from trustray import TrustRay

class TestTrustRay(unittest.TestCase):
    """Test cases for TrustRay class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = TrustRay()
        self.assertIsInstance(instance, TrustRay)
        
    def test_run_method(self):
        """Test the run method."""
        instance = TrustRay()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
