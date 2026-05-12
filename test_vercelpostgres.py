# test_vercelpostgres.py
"""
Tests for VercelPostgres module.
"""

import unittest
from vercelpostgres import VercelPostgres

class TestVercelPostgres(unittest.TestCase):
    """Test cases for VercelPostgres class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = VercelPostgres()
        self.assertIsInstance(instance, VercelPostgres)
        
    def test_run_method(self):
        """Test the run method."""
        instance = VercelPostgres()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
