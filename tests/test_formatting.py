import subprocess
import unittest


class TestFormatting(unittest.TestCase):

    def test_black_formatting(self):
        """
        Test that all python files are formatted with black.
        """
        result = subprocess.run(
            ["black", "--check", "."], capture_output=True, text=True
        )
        self.assertEqual(result.returncode, 0, msg=result.stdout)
