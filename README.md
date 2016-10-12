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
npm install;
gulp build --env=production;
```

## Structure for item atributes
item.attributes = Json object of an object:
```
{
    "color": ["white", "red", "yellow", "black", "orange"],
    "size": [5,6,7,8,9,10,11,12,13]
}
```
item.attribute_fields = Json object of an array of field objects:
```
[
    {
        "field": "color",
        "type": "string"
    },
    {
        "field": "size",
        "type": "number"
    }
]
```


