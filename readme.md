# ncov201912 Rumor Django App

This App(Rumor) will cooperate with volunteers from different provinces of China to provide authentic and certain information.

## Getting Started
I will instruct you to deploy this app on your local environment(mainly, Windows). Other system and take.

Steps are:

1. Clone or pull project: cd to your setected repository: git clone(or pull) https://github.com/HarleyCody/rumor.git
2. Activate virtual environment: a. cd to src under rumor. b. Windows: Scripts\activate; MacOS: source venv/bin/activate
3. Now, you will be in the virtual environment (rumor) which will appear head of your command line;
4. This app defauly will run at your localhost:127.0.0.1:8000, however, it was configured to run under: www.rumor.com. 
In this way, you need to revise your hosts file in this [way](https://support.rackspace.com/how-to/modify-your-hosts-file/)

5. Run App: python manage.py runserver; App will be lanched at www.rumor.com:8000. Moreover, Admin page will be at www.rumor.com:8000/Admin

ps: you may experience as client, however, if you need see the administrative information, please kindly contact me via email:
harleycodywzy@163.com.

### Requirments

If you encounter problem such as No module, No package stuff, run pip install -r requirements.txt before you launch App.

## Deployment
Rumor is deployed on Heroku, it provides postgresql as database. Sqlite can be used during development. But data will not be merged into production version

### And coding style

As I am mostly familiar with Java, most variables in models and views are named in way of Camel Case. Other varaibles follow standard of Django.

## Authors
Harley

## Acknowledgments
I may use several pictures from google as UI. If you feel offended by this, please contact me via email harleycodywzy@163.com
