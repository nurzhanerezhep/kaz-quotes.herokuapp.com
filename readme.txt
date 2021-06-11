
    heroku login

    cd /python_kaz_3week
    git init
    #heroku git:remote -a kaz-quotes

    git status
    git add .
    git commit -am "make it better"
    git push heroku master

    heroku git:remote -a kaz-quotes