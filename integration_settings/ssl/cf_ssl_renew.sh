#!/bin/bash

# cf_ssl_renew.sh

# Deploys a new ssl cert to CloudFront
#
# Requires: letsencrypt-s3front
#
#  pip install letsencrypt-s3front
#
# Must set these env vars:
#
#  AWS_ACCESS_KEY_ID
#  AWS_SECRET_ACCESS_KEY
#  AWS_STORAGE_BUCKET_NAME
#  AWS_STORAGE_BUCKET_REGION=us-west-2
#  LETSENCRYPT_DOMAIN
#  CF_DIST_ID

letsencrypt --agree-tos -a letsencrypt-s3front:auth \
--letsencrypt-s3front:auth-s3-bucket $AWS_STORAGE_BUCKET_NAME \
--letsencrypt-s3front:auth-s3-region $AWS_STORAGE_BUCKET_REGION \
-i letsencrypt-s3front:installer \
--letsencrypt-s3front:installer-cf-distribution-id $CF_DIST_ID \
-d $LETSENCRYPT_DOMAIN \
--renew-by-default --text
