# TODO APP

This app allows to create and authenticate users, each user can create and delete different tasks. Also the app has an API call to [the movie database api](https://developers.themoviedb.org/3) which retrieves and shows the most popular movies.

## App endpoints
This app runs in localhost port 5000 and has the following endpoints:

- /home: Allows the user to see, create and delete tasks.
- /auth/login: Allows the user to login.
- /auth/logout: Allows the user to logout from his account.
- /user/signup: Creates a new user in the database.
- /task/delete/<task_id>: Deletes the specified task.
- /movies: Shows the most popular movies and his review score.

## How to build this app?

You should have installed Terraform, Ansible and have configured your aws credentials in your laptop.

## Terraform

Before running terraform you should create a new ssh key in your aws named "us-west-key" and save it in your computer. Go to the terraform directory and run the following commands:

    terraform init
    terraform plan
    terraform apply

This will create three instances and a load balancer in your aws console.

## Ansible

After running terraform you must run ansible with the following command:

    ansible-playbook -i aws_ec2.yml -u ec2_user --private-key <your-ssh-key> playbook.yml

Your app should be available through the load balancer.