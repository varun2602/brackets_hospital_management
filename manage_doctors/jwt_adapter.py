


import datetime
import jwt

from django.contrib.auth.hashers import check_password

SECRET_KEY = 'SECRET_KEY'  


def get_jwt_by_email_password(email, password, user_model):
    
    user = user_model.objects.get(email=email)

    
    if user.password == password:  
       
        current_time = datetime.datetime.utcnow()
        expiration_15_min = current_time + datetime.timedelta(minutes=15)

        
        jwt_token = jwt.encode(
            {'username': email, 'exp': expiration_15_min, 'iat': current_time - datetime.timedelta(seconds=15)},
            SECRET_KEY, algorithm='HS256')

        # Return the JWT tokens as a dictionary
        return jwt_token
    else:
        # Return None if username and password do not match
        return None


def validate_jwt_token(jwt_token, user_model):
    try:
        # Decode the JWT token
        decoded_jwt = jwt.decode(jwt_token, 'SECRET_KEY', algorithms=['HS256'])

        # Extract the username from the JWT payload
        email = decoded_jwt.get('username')

        # Check if the username is valid in the user_model
        if user_model.objects.filter(email=email).exists():

            # Check if the JWT token is not expired
            expiration_time = datetime.datetime.fromtimestamp(decoded_jwt['exp'])
            current_time = datetime.datetime.utcnow()
            if expiration_time > current_time:
                return email
            else:
                # Return None if the JWT token is expired
                return None
        else:
            # Return None if the username is not valid in the user_model
            return None
    except jwt.ExpiredSignatureError:
        # Handle the case where JWT token is expired
        return None
    except jwt.InvalidTokenError:
        # Handle any other invalid token errors
        return None


# This function is not part of JWT but does call above functions to check if the user is logged in

def is_logged_in(request) -> bool:
    # print('sssssssssssssssssssssssssssssssssssssssssssssssssss')
    token = request.COOKIES.get('token')  # Get the token from the cookies
    print('cookie get token: ' + str(token))
    if token:
        username_extracted_from_token = validate_jwt_token(token)  # returns username/email if validated
        if username_extracted_from_token:
            print('username of logged in user: ' + username_extracted_from_token)
            print('login successful')
            return True
        else:
            return False
    else:
        return False
