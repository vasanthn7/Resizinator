# Create User

**URL** : `user/register/`

**Method** : `POST`

**Auth required** : No

**Permissions required** : None

**Data**

```json
{
  "username": "[username]",
  "password": "[password]"
}
```

## Success Response

**Code** : `201 Created`

## Error Response

**Condition** : If the username already exists.
**Code** : `400 BAD REQUEST`
**Data** :

```json
{
  "error": "Username already exists"
}
```

# Login User

**URL** : `user/login/`

**Method** : `POST`

**Auth required** : No

**Permissions required** : None

**Data**

```json
{
  "username": "[username]",
  "password": "[password]"
}
```

## Success Response

**Code** : `200 OK`

**Data**

```json
{
  "token": "sample_token"
}
```

## Error Response

**Condition** : If the username does not exist.
**Code** : `401 Unauthorized`
**Data** :

```json
{
  "error": "Invalid credentials"
}
```

**Condition** : If the password is incorrect.
**Code** : `401 Unauthorized`
**Data** :

```json
{
  "error": "Invalid credentials"
}
```
