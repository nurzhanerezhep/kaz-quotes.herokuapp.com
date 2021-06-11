The main command to use app

To the start the heroku:

    heroku login

You need to open app path:

    cd /python_kaz_3week

Initialise git:

    git init

Create heroku app:

    #heroku git:remote -a kaz-quotes

Add some change, commit and send apps in heroku:

    git status
    git add .
    git commit -am "make it better"
    git push heroku master