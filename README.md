## Setup

clone this repo with by adding this command to your terminal and move to the directory:
```console
$ git clone https://github.com/mildlycoder/fastapi-blog.git
$ cd fastapi-blog #movet to directory
$ source venv/bin/activate #to activate the environment
```

add a .env file in the directory with following key:

```console
DB_URI=YOUR_MONGO_DB_URI_GOES_HERE
```


## Test API
use this command to run the api:
```console
$ uvircorn server:app --reload
```

go to http://127.0.0.1:8000/docs to test the different routes







