import os
import fwitter

class TestScripts():
    """Testing shell scripts"""

    def test_run_exists(self):
        """Ensure ./bin/run can run"""

        assert os.path.isfile("bin/run")

    def test_init_exists(self):
        """Ensure ./bin/init can run"""

        assert os.path.isfile("bin/init")
