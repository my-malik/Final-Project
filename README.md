# Final-Project
To create a web application that integrates with a database and demonstrates CRUD functionality.

To utilise containers to host and deploy your application.

To create a continuous integration (CI)/continuous deployment (CD) pipeline that will automatically test, build and deploy your application.

**link to screen recording: **

https://drive.google.com/file/d/1P29GLC0EJdxXxmjDh9fub3nliGAuDy0U/view?usp=sharing

**Project:**

•	The fantasy football app created is a web application which uses the Flask web framework that has CRUD functionality. It uses a database with a one-to-many relationship, where one team has many players.

•	The frontend uses HTML templates, allowing the user to perform CRUD functionality and the backend uses SQLAlchemy to model and integrates with the database.

•	The pipeline works by the code being pushed up to the github repository, where a webhook is used in order to trigger the pipeline on Jenkins, which is the automation server used. On Jenkins, the following stages are run: setup, test, build, push and deploy. 

**Project Management:**

Github was used for project tracking, which can be seen below:
![image](https://user-images.githubusercontent.com/93129113/147976227-83969d37-bff4-47c4-9b7d-f3cb77ab058c.png)

**Jenkins pipeline:**

CI/CD pipelines allow any errors to be identified quicker as a result can be deployed quicker. The following stages were implemented in the pipeline:

•	**Setup:**

    o	Installation of docker and docker-compose, allows docker login
•	**Tests:**

    o	Creates virtual environment and installs requirements
    
    o	Runs pytest and produces test reports
    
•	**Build:**

    o	Docker-compose is built. Builds the image    
    
•	**Push**

    o	Pushes image to dockerhub	
    
•	**Deploy**

    o	Deployed to docker swarm
    
**Unit Testing**:

Unit testing was carried out on Jenkins as part of the pipeline when triggered from a webhook. Below are the tests run and their success as well as a coverage report:

![image](https://user-images.githubusercontent.com/93129113/147976002-704ceb07-a7a2-47ac-9f9d-8151957d8787.png)

**Entity Relationship diagram:**


![image](https://user-images.githubusercontent.com/93129113/147976108-9de7d4ba-1604-4181-b4d9-7737e0ed7dba.png)

**Full CI/CD pipeline diagram:**

![image](https://user-images.githubusercontent.com/93129113/147976137-89193786-086a-4350-86ac-579d0c5d863b.png)


**Application interacting with database:**

![image](https://user-images.githubusercontent.com/93129113/147976173-807518a7-0699-4ed2-bac5-f82ef3a0cb13.png)




**Risk assessment:**


•	VM for Jenkins/development and deployment server goes down:

    o	Does not allow CI/CD of changes to the code and any improvements made.
    
    o	Will not allow access to the web app although likelihood is low.
    
    o	If deployment server goes down, a new VM can be started up relatively easily and will be able to interact with the development server once connected.
    
•	Credentials being visible on github when they are pushed to the repository:

    o	Ensure that any credentials are not hard coded which will not allow any user access to the database.
    
•	Merge conflicts occurring when changing code to multiple branches:

    o	Ensure that different files are being worked on different branched to prevent code being corrupted when merging.
    
•	Updates failing to work when deployed:

    o	Ensure tests are integrated on Jenkins, preventing failed updates to be deployed.
    

**Improvements:**

•	More unit tests could be performed.

•	The time taken for the pipeline on jenkins can be reduced.
