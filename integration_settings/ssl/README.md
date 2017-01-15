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

## Renewals

    sudo letsencrypt certonly --manual

There will be a prompt for the acme challenge:

    mkdir -p /tmp/letsencrypt/public_html/.well-known/acme-challenge
    cd /tmp/letsencrypt/public_html
    printf "%s" LmCcIweXN5LS-gTkZQJnlfafXacn36WN95bVAnswPj4.FXM5sZV0zkzMFrkNMeL0wtbi2VErKpUEywhiHLXXdhA > .well-known/acme-challenge/LmCcIweXN5LS-gTkZQJnlfafXacn36WN95bVAnswPj4

With the django-acme-challenge app, you can simply update these vars on the server:

 - `ACME_CHALLENGE_URL_SLUG`
 - `ACME_CHALLENGE_TEMPLATE_CONTENT`

### Heroku

Hub example:

    sudo heroku certs:add /etc/letsencrypt/live/hub.aashe.org/fullchain.pem /etc/letsencrypt/live/hub.aashe.org/privkey.pem --app aashe-hub-prod

Or update:

    sudo heroku certs:update /etc/letsencrypt/live/hub.aashe.org/fullchain.pem /etc/letsencrypt/live/hub.aashe.org/privkey.pem --app aashe-hub-prod

`sudo` is necessary because of access to that directory

### CloudFront

#### Recommended:

I created `cf_ssl_renew.sh` to run through this process quickly

#### If you have to do it manually:

With cloudfront (for hub-media.aashe.org), you have to upload the file manually.
It may take a minute or two for CloudFront to serve the new file, so just keep
pinging it, for example:

    curl -D - http://hub-media.aashe.org/.well-known/acme-challenge/LfOJP4dOTVoPi1yQ4lfjZ6yu0Z87ceKinJMC0xoA1eM

    sudo aws iam upload-server-certificate \
    --server-certificate-name hub-media.aashe.org \
    --certificate-body file:///etc/letsencrypt/live/hub-media.aashe.org/cert.pem \
    --private-key file:///etc/letsencrypt/live/hub-media.aashe.org/privkey.pem \
    --certificate-chain file:///etc/letsencrypt/live/hub-media.aashe.org/chain.pem \
    --path /cloudfront/
