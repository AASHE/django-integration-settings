# SSL

I've been using [Let's Encrypt](http://letsencrypt.org/) for certificate creation and this seems to have worked well.

## The process

Get the Let's Encrypt app:

    brew install letsencrypt
    
Create a certificate:

    sudo letsencrypt certonly --manual
    
You'll need to ensure that you're serving the acme-challenge. I built a quick django app to support that: [django-acme-challenge](https://github.com/jamstooks/django-acme-challenge).

Heroku has an SSL endpoint addon (unfortunately $20/month - so we may go with CloudFront eventually), but to configure it:

    heroku addons:create ssl:endpoint
    sudo heroku certs:update /etc/letsencrypt/live/<domain>/fullchain.pem /etc/letsencrypt/live/<domain>/privkey.pem
    
We are currently using CloudFront for our media files, so I had to update that too. [This tutorial](https://nparry.com/2015/11/14/letsencrypt-cloudfront-s3.html) was helpful.
