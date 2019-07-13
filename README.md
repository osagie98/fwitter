# Fwitter
Fwitter (fake - twitter) is a web app built with a ReactJS frontend and a Python/Flask backnend, backed by a sqlite3 database.
The app will be designed to mimic the core elements of Twitter, with features such as:
  * Account creation and deletion
  * Searching by hashtag
  * Tweeting (of course)! Or should it be fweeting?
  * Liking and retweeting other tweets
  * And more as time goes on
## Usage
Fwitter in its current form is far from usable, but feel free to take a look at how it runs!
1. Clone or dowload this repo and and navigate to it on the command line
2. Create a virtual environment with `python3 -m venv env` and then activate it with `source env/bin/activate`
3. Install packages by running `pip install -e .` and `npm install .` right after
4. Initialize the database by running `./bin/init demo`
5. Run the server with `./bin/run` and naviagate to localhost:5000 for the app!
Once the app is more complete, this setup process will become much simpler
