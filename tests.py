import unittest
import os
import tempfile
from app import app, classify_risk, get_files, get_risk_counts

class TestCyberRiskMonitor(unittest.TestCase):

    def setUp(self):
        """Set up test fixtures"""
        self.app = app.test_client()
        self.app.testing = True

    def test_classify_risk_high(self):
        """Test high risk file classification"""
        self.assertEqual(classify_risk('malware.exe'), 'high')
        self.assertEqual(classify_risk('script.bat'), 'high')
        self.assertEqual(classify_risk('library.dll'), 'high')

    def test_classify_risk_medium(self):
        """Test medium risk file classification"""
        self.assertEqual(classify_risk('archive.zip'), 'medium')
        self.assertEqual(classify_risk('document.pdf'), 'medium')
        self.assertEqual(classify_risk('spreadsheet.xlsx'), 'medium')

    def test_classify_risk_low(self):
        """Test low risk file classification"""
        self.assertEqual(classify_risk('text.txt'), 'low')
        self.assertEqual(classify_risk('image.jpg'), 'low')
        self.assertEqual(classify_risk('code.py'), 'low')

    def test_home_page(self):
        """Test home page loads successfully"""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Employee Cyber Risk Monitoring', response.data)

    def test_risk_counts_calculation(self):
        """Test risk counts calculation"""
        test_files = [
            ('safe.txt', 100, 'timestamp', 'low'),
            ('dangerous.exe', 200, 'timestamp', 'high'),
            ('archive.zip', 300, 'timestamp', 'medium')
        ]
        high, medium, low = get_risk_counts(test_files)
        self.assertEqual(high, 1)
        self.assertEqual(medium, 1)
        self.assertEqual(low, 1)

if __name__ == '__main__':
    unittest.main()