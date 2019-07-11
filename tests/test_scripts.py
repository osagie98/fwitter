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

    def test_init_begin(self):
        """Tests that init begin makes a database"""

        # Start by removing any possible database
        os.system("rm -rf var/fwitter.sqlite3")

        os.system("./bin/init begin")

        assert os.path.isfile("var/fwitter.sqlite3")
        os.system("rm -rf var/fwitter.sqlite3")
    
    def test_init_reset(self):
        """Tests that init reset restarts a database"""

        # This is essentially the same as the begin test, find a way to make it better
        
        # Start by removing any possible database
        os.system("rm -rf var/fwitter.sqlite3")

        os.system("./bin/init reset")

        assert os.path.isfile("var/fwitter.sqlite3")
        os.system("rm -rf var/fwitter.sqlite3")

    def test_init_erase(self):
        """Tests that init erase destroys a database"""

        # Start by making a dummy file
        os.system("rm -rf var/fwitter.sqlite3")
        os.system("touch var/fwitter.sqlite3")

        os.system("./bin/init erase")

        assert not os.path.isfile("var/fwitter.sqlite3")
        
        
