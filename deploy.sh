ssh soccergear@gitlab.tunaweza.com -i ~/.ssh/tw-gitlab.pem ./deploy.sh;
ssh ubuntu@gitlab.tunaweza.com -i ~/.ssh/tw-gitlab.pem "sudo apachectl restart";
