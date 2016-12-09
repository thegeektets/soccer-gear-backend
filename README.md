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

## Lipisha API

env_variables['LIPISHA_DEV_API_KEY'] = '391181e094f0c2c25575db5a62dda225'
env_variables['LIPISHA_DEV_API_SIGNATURE'] = '4+t24jJtOxT8E9C46MY0j8+P1G3xQ9fQWdI0PVTYZ4k6n3/oPRbIevl+C/gXyVTPWydk7wZlss8Ryi61IpbWSEtRf699l+Jd/Wj1V/kKzJt+p5/XZFF8c60XhgHgvZJFl7bwL7U3a/Kg1LeTc2LZX3BdoIhtNr96h0HeF+uO0KM='

env_variables['LIPISHA_API_KEY'] = 'f8895acecf41ebac5cb0c5e113785273'
env_variables['LIPISHA_API_SIGNATURE'] = '13XbODwamIU35b3JnCoScxdesi85RviRhhzGxQGqIS9zy4FS7nZBR6wuiyJ/wL80MyOgQb/XhAPXlSjB1OaWEfvL2YGqMQybPgpJbkePLolSU0XH7wAmuX+s2ta4mFnp6H0iVRcqAAFw6HsN9kC8+PKMy0wtxtbJAfLE0HwRa9E='


