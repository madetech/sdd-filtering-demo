# SDD Filtering Demo

## Set up Drone CI

This runs in AWS Elastic Beanstalk. Your environment will need the following environment variables setting...

    DRONE_GITHUB_CLIENT_ID
    DRONE_GITHUB_CLIENT_SECRET
    DRONE_RPC_SECRET

Then you upload `docker-compose.yml`.

In GitHub set up a webhook posting JSON to <Your_Elastic_Beanstalk_URL>/hook.
