# Upload Image

**URL** : `image/`

**Method** : `POST`

**Auth required** : Yes, TokenAuthentication

**Permissions required** : IsAuthenticated

**Form**

```
{
  "original": image_file,
}
```

**Headers**

```
Authorization : Token sample_token
```

## Success Response

**Code** : `201 Created`

**Data**

```json
{
  "id": 1,
  "original": "https://resizinatorbucket.s3.amazonaws.com/private/sample.png?AWSAccessKeyId=Key&Signature=signature%3D&Expires=1716059106",
  "small": null,
  "medium": null,
  "updated_at": "2024-05-18T18:05:06.009201Z",
  "created_at": "2024-05-18T18:05:06.009238Z",
  "user": 1
}
```

## Error Response

**Condition** : If the image is not provided.
**Code** : `422 Unprocessable Entity`
**Data** :

```json
{
  "original": ["No file was submitted."]
}
```

# List Images

**URL** : `image/`

**Method** : `GET`

**Auth required** : Yes, TokenAuthentication

**Permissions required** : IsAuthenticated

**Headers**

```
Authorization : Token sample_token
```

## Success Response

**Code** : `200 OK`

**Data**

```json
{
  "count": 1,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 1,
      "original": "https://resizinatorbucket.s3.amazonaws.com/private/sample.png?AWSAccessKeyId=Key&Signature=Signature%3D&Expires=1716059257",
      "small": null,
      "medium": null,
      "updated_at": "2024-05-18T18:05:06.009201Z",
      "created_at": "2024-05-18T18:05:06.009238Z",
      "user": 1
    }
  ]
}
```

# Get Images

**URL** : `image/<id>/`

**Method** : `GET`

**Auth required** : Yes, TokenAuthentication

**Permissions required** : IsAuthenticated

**Headers**

```
Authorization : Token sample_token
```

## Success Response

**Code** : `200 OK`

**Data**

```json
{
  "id": 1,
  "original": "https://resizinatorbucket.s3.amazonaws.com/private/sample.png?AWSAccessKeyId=Key&Signature=signature%3D&Expires=1716059106",
  "small": null,
  "medium": null,
  "updated_at": "2024-05-18T18:05:06.009201Z",
  "created_at": "2024-05-18T18:05:06.009238Z",
  "user": 1
}
```
