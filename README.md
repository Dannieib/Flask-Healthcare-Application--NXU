**Flask Healthcare Application**

git clone https://github.com/Dannieib/Flask-Healthcare-Application--NXU.git
cd src

Install Dependencies
Ensure you have Python 3+ installed, then install required packages:

**pip install flask pymongo pandas matplotlib seaborn**


Run MongoDB
Make sure MongoDB is running locally or update the connection string in app.py: You can download Atlas

client = MongoClient("mongodb://localhost:27017/")


Start the Flask App
**python app.py** or navigate to the containing folder and **flask run**

Access app on -> http://127.0.0.1:5000

Input all fields the execute


Navigation Patterns
Route	Method	Description
/	GET, POST	Displays the form & stores user data.
**http://127.0.0.1:5000/export**	GET	Exports the survey data to survey_data.csv.
**http://127.0.0.1:5000/visualize**	GET	Generates charts for income & spending trends.
