# Item catalog project

## Project Overview
This the second project on Udacity's Full Stack Web Developer Nanodegree. 
## How to Run ?
you can run this project from your Windows machine directly or from your Virtual Machine

### Option-1: Virtual Machine :

#### PreRequisites:
   * [_Python_ 3.6 or higher](https://www.python.org/) (python 3.7 RECOMMENDED ) 
  * [VirtualBox](https://www.virtualbox.org/)
  * [Vagrant](https://www.vagrantup.com/)
  * All required packages mentioned in requirements.txt file .
#### Setup Project:
  1. Install Vagrant and VirtualBox after dowload it From the links above
  2. Download or Clone [fullstack-nanodegree-vm](https://github.com/udacity/fullstack-nanodegree-vm) repository.
  3. Download or Clone [our catalog app](https://github.com/abousamraa/item-catalog-project.git) repository.
  4. navigate into the vagrant folder in fullstack-nanodegree-vm folder ,  (which is shared with your virtual machine)
  5. Put our catalog app files into the vagrant directory .
  
#### Launch your Virtual Machine:
  1. open your terminal ( such as git bash ) , then navigate into the vagrant folder in fullstack-nanodegree-vm folder , then run this command   
  ```
    $ vagrant up
  ```
  2. When vagrant up is finished running, you will get your shell prompt back , Then Log into using this command:
  
  ```
    $ vagrant ssh
  ```
  3. Change directory to /vagrant :
  ```
    $ cd /vagrant
  ```
  
#### install required packages for the app : 

  1. Run this command to install required packages from requirements.txt file:
  
  ```
    pip3 install -r requirements.txt --user
  ```
 OR ( if latest version of python has been installed ) :
  ```
    pip install -r requirements.txt --user
  ``` 
#### Creating database and populate it : 

  1. Create database file and populate it with some data for testing  :
  
  ```
    python3 db_populate.py 
  ```
 2. for testing , all categories and courses in this database created by this user data : 

> email : admin@test.com

> password = 'password'

#### Run server  : 

  1. Run the web server , then  :
  
  ```
    python3 runserver.py 
  ```
   OR ( if latest version of python has been installed ) :
  ```
    python runserver.py  
  ``` 
 
2.  Access the application on your host machine using  [http://localhost:5000](http://localhost:5000/)


### Option-2: Windows Machine (Host) :
you can run the application from Windows machine directly without the need to use virtual machine 
#### PreRequisites:
  * [_Python_ 3.6 or higher](https://www.python.org/) (python 3.7 RECOMMENDED ) 

  * All required packages mentioned in requirements.txt file .
  * (Optional) [ Virtualenv](https://virtualenv.pypa.io/en/latest/) a tool to create isolated Python environments .
#### (Optional) Setup your isolated Python environment  :
  * using this [Virtualenv user guide](https://virtualenv.pypa.io/en/latest/userguide/) , you can Setup your isolated Python environment before install required packages
#### install required packages for the app : 

  1. Run this command to install required packages from requirements.txt file:
  
  ```
    pip3 install -r requirements.txt --user
  ```
OR ( if latest version of python has been installed ) :
  ```
    pip install -r requirements.txt --user
  ``` 
#### Creating database and populate it : 

  1. Create database file and populate it with some data for testing by running :
  
  ```
    python3 db_populate.py 
  ```
 OR ( if latest version of python has been installed ) :
  ```
    python db_populate.py  
  ``` 

#### Run server  : 
  1. Run the web server , then  :
  
  ```
    python3 runserver.py 
  ```
  OR ( if latest version of python has been installed ) :
  ```
    python runserver.py  
  ``` 
2.  Access the application on your host machine using  [http://localhost:5000](http://localhost:5000/)

 ### Important Note :
*  you can change the application port (if you want ) to use these ports only : 
   ```
    Port:5000
    port:8080
    port:8000 
    ```
    any other port will cause an invalid client error when sign in by Google due to restriction of redirect urls applied by google API

## JSON Endpoints

  - Displays all Categories .
 `/catalog.JSON` OR `/categories.JSON`

   - Displays specific category
 `/category/<int:category_id>.json`

  - Displays all courses
`/courses.JSON`

   - Displays specific course
 `/course/<int:course_id>.json`
