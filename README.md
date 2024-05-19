# Resizinator

Resize images

Django application to resize images. It stores the original image and the resizes the images in the background, which is stored in S3.

## Installation

Requirements:

- Docker

1. Clone the repository
2. Copy the `.env.sample` file to `.env` and update the values
3. Run `docker-compose build`
4. Run `docker-compose up`

Project is hosted at [https://foobar.ing/](https://foobar.ing/)
Documentation is available at [https://foobar.ing/docs](https://foobar.ing/docs) and in the path resizinator/api_docs

User can upload an image and get the resized image in the response.
Step 1:
Register a user using the endpoint POST: /users/register/
Step 2:
Login using the endpoint POST: /users/login/. This will return a token which is required for the next steps. This token should be passed in the header as Authorization: Token <token>
Step 3:
Upload an image using the endpoint POST: /image/, requires authorization token in the header.
Step 4:
Get the resized image using the endpoint GET: /image/<image_id>/, requires authorization token in the header.
