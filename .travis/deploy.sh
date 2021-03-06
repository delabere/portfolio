#!/bin/bash
set -e
git config --global push.default simple # we only want to push one branch — master
# specify the repo on the live server as a remote repo, and name it 'production'
# <user> here is the separate user you created for deploying
git remote add production ssh://git@157.245.37.38/home/git/prod_portfolio
git push production master # push our updates
ssh git@157.245.37.38 "cd prod_portfolio && sudo docker-compose up -d --no-deps --build"
