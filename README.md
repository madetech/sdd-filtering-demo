# SDD Filtering Demo

## Set up Drone CI

This runs in AWS Elastic Beanstalk. Your environment will need the following environment variables setting...

    DRONE_GITHUB_CLIENT_ID
    DRONE_GITHUB_CLIENT_SECRET
    DRONE_RPC_SECRET

Then you upload `docker-compose.yml` and let Elastic Beanstalk do its thing.

Once you have logged into Drone with GitHub and set up the project, you need to add the aws_access_key_id and aws_secret_access_key of a user which has Cloud Formation access to the secrets for the project so that it can deploy.

In GitHub set up a webhook posting JSON to <Your_Elastic_Beanstalk_URL>/hook.
