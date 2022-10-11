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
For building this app you should install docker and run the following commands on your terminal.

    docker-compose build
    docker-compose up -d

For stop the app, run the following command:

    docker-compose down
