Go to: https://gear-api.tunaweza.com:8443/admin for the deployed admin.


Deploy Commands
```
ssh soccergear@gitlab.tunaweza.com -i ~/.ssh/tw-gitlab.pem ./deploy.sh;
ssh ubuntu@gitlab.tunaweza.com -i ~/.ssh/tw-gitlab.pem "sudo apachectl restart";
```

Deploy Script in server
```
source ~/venv/bin/activate;
cd soccer-gear-backend;
git fetch;
git checkout dev;
git pull;
python manage.py migrate;
python manage.py collectstatic --noinput;
cd ~/soccer-gear-frontend/;
git fetch;
git checkout dev;
git pull;
gulp build --env=production;
```