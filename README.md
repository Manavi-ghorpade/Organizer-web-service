# chessboard-website

created chessboard game using Django and GCP
Implement a full stack Organizer web service from scratch using all of the tools and technologies - HTML, CSS, Javascript, Bootstrap, Django & Python.

created docker image-

  step 1:  Create file requirements.txt with these contents:
  
    asgiref==3.2.10
    
    Django==3.0.9
    
    sqlparse==0.2.4
    
  step 2: Create file docker_run_server.sh, with the following contents:
  
    #!/bin/sh
    
    python manage.py runserver 0.0.0.0:80
    
  step 3:Create file Dockerfile, with the following contents
  
    FROM python:3.8.10
    
    COPY requirements.txt ./
    
    RUN pip3 install --user -r requirements.txt
    
    COPY . ./
    
    RUN chmod +x docker_run_server.sh
    
    EXPOSE 80
    
    ENTRYPOINT ["./docker_run_server.sh"]
    
   step 4:Build docker image from Dockerfile
   
    docker build -t <DOCKER_IMAGE_NAME> 
    
    test in local browser on localhost
    
   step 5:Create and run a docker container from your docker image:
   
    docker run -it -p 80:80 <DOCKER_IMAGE_NAME>
    
   step 6:view docker image
   
    docker image ls
    
used chartlist to create chart- 

  Include Chartist css & js
  
  	<link rel="stylesheet" href="//cdn.jsdelivr.net/chartist.js/latest/chartist.min.css">
  
  	<script src="//cdn.jsdelivr.net/chartist.js/latest/chartist.min.js">
	
  
	
Deployed website to Google Cloud Platform
