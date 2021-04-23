

Step 1 --> Create your model or database
Step 2 --> To make the API use serializers(which will interact the api with the database)
step 3 --> Specify the data(fields) you will push to the api or just retrive from database and see. in the serializers
Step 4 --> In the views make a class of the APIView from the rest_framework.views
Step 5 --> here you can make 2 types of request to the database 
Step 6 --> If you use post request you can manipulte the data stored in api in json format.
Step 7 --> If you use get request you can only able to retrive the data from the database in the api
Step 8 --> Only post method needs to be validated bcz it's the method which manipulating our api data.
Step 9 --> from rest_framework.response import Response--> This response method will show us the response of the api.



# In order to fetch the data from API (get) or to feed the data to the API(post) we need to authentication system
To get the data user needs to be authenticated and to ensure that I use rest_framework.permissions.IsAuthenticated class
access it in our own class as the permission_classes and that's it.

Here is 2 kinds of authentication system--->
dajango rest_framework's own authentication system ---> we use authtoken authentication system

rest_framework also allows the third-party authentication systems it actually recommends it.
So as the second method I use dj-rest-auth package it has many more built in authentication functions
