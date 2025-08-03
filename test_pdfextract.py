# test_pdfextract.py
"""
Tests for PDFExtract module.
"""

import unittest
from pdfextract import PDFExtract

class TestPDFExtract(unittest.TestCase):
    """Test cases for PDFExtract class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = PDFExtract()
        self.assertIsInstance(instance, PDFExtract)
        
    def test_run_method(self):
        """Test the run method."""
        instance = PDFExtract()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
