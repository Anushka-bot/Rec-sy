## Introduction
Rec-sy is a recognition system built using OpenCV and Python. 

## About Project
This Project is the implementation of face recognition system which identifies top notch criminals and fraudsters in the world just by using an image. The face recognition and detection is done by a face recognition model integrated in the backend part. User has to upload an image of the person that he/she wants to identify and after simulations, it will return the name of the person identified in the image from the data stored in the database.This project is also deployed on Heroku Server. 
**Go and check it out!**

  ## Instructions for the website
  - After that you are redirected to the website as shown below
    -![This is an image](https://user-images.githubusercontent.com/75663460/170486947-aa94ffe7-0762-48f6-9bdb-60b65603e224.png) 
    
 - Click on 'Test my project' button
 - You will be redirected to a new page where you will upload an image of the criminal that you want to identify
 - Read the instructions properly and before uploading
   -![This is an image](https://user-images.githubusercontent.com/75663460/170487732-2e3f3118-6698-455a-9782-29403b50ba8d.png)
 - Wait for some time..
 - And voila!! You will get the name of the criminal and about him (directly from wikipedia) as shown below
   -![This is an image](https://user-images.githubusercontent.com/75663460/170487993-0a4f4933-2708-400a-b2db-fabe9bd852f6.png)
   
Link to the project ->
   
## TechStack used
   - The Face recognition and detection model is build using OpenCV library in Python Language. OpenCV is a huge open-source library for computer vision, machine learning, and image processing. It recieves path of the image as input and after simulations return the name of the recognised person.
   - This Model is integrated with Flask server. Flask proves to be an excellent microframework for Web-Applications. After reciving output from the model, it redirects this input to the incorporated HTML page.
   - The Frontend Part of this Project is made using HTML, CSS and JavaScript. HTML page uses Jinja Tags to display the names recieved from the server on the website.

## How the project works
   - Firstly the user have to upload an image and submit it on the website. This user input is then passed to the server and saved in a local folder. The integrated Face Recognition model access that image via tha folder and after simulations, returns the name of person in the image back to the server. This name is then displayed on the website. Amazing? Try it out then!

## Required Libraries
  - You will require libraries and dependencies as mentioned below
    - python (Must be 64-bit version)
    - cmake
    - dlib
    - face_recognition
    - numpy
    - opencv-python
    - Flask
    - wikipidea
   - Tip: If you find difficulties in installing dlib, refer to the youtube video below, it helped me lot!!
     - [Check this out](https://www.youtube.com/watch?v=xaDJ5xnc8dc) 
 
## About Floders and Files in Source Code
1. app.py >> It is the Flask server and the file which you have to run. It integrates the face recognition model by importing it and interact with the frontend part. It takes input image from the user and send it to the face recognition model. After simulations, the model return an output to this server and the server again send it to the frontend part where it is displayed on the website.
2. face_rec.py >> It contains the face recognition and detection model.
3. faces folder >> It is basically the database for the face recognition model. It contains all the known faces. 
4. templates folder >> It contains all the HTML files of the Frontend Part.
5. static/uploads folder >> It contains all the CSS, JavaScript files along with images which are used for the website. It also stores the image given by the user.
6. requirements.txt >> It contains all the libraries that needs to be installed in the local machine in order to run the source code.

## How to run the code
   - Download code from above or clone this repository to your local local machine.
   - **To run from command prompt**
     - Go to the folder where all the files are stored
     - Right click and select 'open in terminal' and type
       ```
       python app.py (for windows)
       python3 app.py (for ubuntu)
       ```
     - the command prompt will look something like this
     
       -![cmd](https://user-images.githubusercontent.com/75663460/170492042-9863efb1-456e-4282-8308-151bea7ecae4.png) 
       
     - press and hold the 'ctrl' button and then click on the link as shown below
     
       - 
     - This link will redirect you to a website in your default browser
 
 - **To run from VS Code or other IDE**
     - Go to 'app.py' file and make sure all the libraries are installed in your local machine.
     - click on the run button in the IDE
     - the terminla will look something like this
       - If your terminal is giving error like 'run witn python3' or something, then just open the terminal in vs code and type the following command
     
     - press and hold the 'ctrl' button and then click on the link as shown below
     - This link will redirect you to a website in your default browser
