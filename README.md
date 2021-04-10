<p align="left">
    <a href="#" target="_blank">
        <img width="8%" src="https://garvitchittora.live/static/image/logo/logo.png" alt="GH-logo">
    </a>
</p>

# Cultural Societies of IIIT-A
:star: Star us on GitHub — it helps!
<br/>

Cultural Societies of IIIT-A website, aim for a dynamic and unique website that can be used in upcoming sessions too and 🙈 obvious it is a submittion of webkriti.

## 💻 Live-Link
[Live Link](https://garvitchittora.live/)

## 📷 Few snaps of the site
### Light Theme
![](https://i.ibb.co/tM7m7Rt/Screenshot-from-2021-04-10-21-27-51.png)

### Dark Theme

![](https://i.ibb.co/gWkkFw2/Screenshot-from-2021-04-10-21-27-39.png)

## 🧾 Table of contents
- Tech Stack
- Setup
- For Database Setup
- Runserver Steps
- Brief Repo Strucutre
- Frontend Frameworks
- Schema
- Theme Toggle functionality
- Overall Theme
- Footnotes


## 🛠 Tech Stack
1. Django
2. Python
3. HTML
4. SASS
5. JQuery
6. FontAwesome
7. JS

## 🚀 Setup
Get the code by cloning this repository using git
```
1. git clone  https://github.com/garvitchittora/webkriti-21.git
2. install virtualenv if not installed: sudo pip3 install virtualenv
3. create virtual environment: virtualenv .env
4. activate virtual env by: source .env/bin/activate
5. install all requirements by: pip3 install -r requirements.txt
```

### For Database Setup
```
1. cd task
2. python manage.py makemigrations core
3. python manage.py migrate
4. python manage.py createsuperuser
````

### 🧩 Runserver Steps
```
1. python3 manage.py runserver
2. Open Brower and go to http://localhost:8000/
```

## 📚 Brief Repo Structure
```
/
|-- task/			
 |-- core/             #Folder of App named core of the project(task)
 |-- static/           #Folder which contains static files of the project
 |-- task/             #Django project folder of the project named task
|
|-- .gitignore         #git ignore file
| 
|-- requirements.txt   # Requirements of the project
| 
|-- README.md          #ReadMe and documentation of the project
```

## 🎈 Frontend frameworks
Following CSS and Js frameworks/libraries are included in the project:
- [Bootstrap](https://getbootstrap.com/)
- [Font-Awesome](https://fontawesome.com/6?next=%2F)

## 🏷 Schema
| Society            |  User                |   Gallery         |     Event        |
|:------------------:|:--------------------:|:-----------------:|:-----------------|
| name               |  email               | image             | image            |  
| image              |  image               | alt               | bio              |
| bio                |  bio                 | society(F)        | society(F)       |
| slug               |  power_value(0/1/2)  |                   | name             |
| fb                 |  society(F)          |                   |                  |
|                    |  First Name          |                   |                  |
|                    |  Last Name           |                   |                  |
|                    |  Password            |                   |                  |

power value 0 is for admin, 1 for coordinator of society and 2 for member of society.
<br>
F   -> Foreign Key
<br>

### Theme Toggle functionality
A simple yet creative idea, you can toggle between dark and light mode in the website anytime, and your preference will be stored for future.

### Overall Theme
Keeping in mind the aesthetic look of the website, the theme of website is **minimalist, unique and uniform**.

## ✒ Footnotes
Aim of this project is to reduce the work for the upcoming years, so that the same website can be used without changing any piece of code, just simply update the members details dynamically and you're good to go.
