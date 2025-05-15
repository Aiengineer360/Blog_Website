# 📝 Blogging Website - Django Project

A full-featured blogging platform built using **Django**, enabling users to register, create, edit, and delete blog posts, comment on posts, and manage content through an admin panel.

![image](https://github.com/user-attachments/assets/16a30927-b26a-4ed1-b37b-8022c28c9674)

![image](https://github.com/user-attachments/assets/9a5b8eda-ea80-42a6-b7d5-06e3de837d71)

![image](https://github.com/user-attachments/assets/81050773-1da7-4993-8de7-d6f5477edc4a)

![image](https://github.com/user-attachments/assets/e61a54cd-8c08-4102-b1b4-f8c2e83eb8a2)


## 🚀 Features

### 🔐 User Features

* **Authentication**: Secure user registration, login, logout, and password reset via email.
* **Post Management**: Create, edit, and delete your own blog posts.
* **Post Filtering**: Filter posts by **category**, **tag**, or **author**.
* **Comment System**: Add and view comments under each blog post.
* **Access Control**: Users can only edit or delete their own posts.

### 🎨 Templates and UI

* **Navigation Bar**: Includes links to Home, Create Post, Login, Logout, and Register. Shows the logged-in user’s name.
* **Custom Styling**: Clean and user-friendly layout using custom CSS.

### 🛠 Admin Features

* Manage **users**, **posts**, and **comments** via Django admin panel.

### 🔐 Security

* Access restrictions in place to prevent unauthorized post editing or deletion.

---

## 🗂 Project Structure

```
├── blogging_website/
│   ├── settings.py, urls.py, wsgi.py, asgi.py
├── media/
│   └── post_images/
├── posts/
│   ├── models.py, views.py, forms.py, urls.py, admin.py
├── users/
│   ├── models.py, views.py, urls.py, admin.py
├── static/
│   └── css, js, images
├── templates/
│   ├── base.html, index.html, post_detail.html, user_profile.html
```

---

## ⚙️ Tech Stack

* **Backend**: Django (Python)
* **Database**: SQLite
* **Frontend**: HTML, CSS, JS (with Django Templates)

---

## 💻 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/Aiengineer360/Blog-Website
cd blogging_website
```

### 2. Set Up a Virtual Environment

```bash
python3 -m venv myenv
source myenv/bin/activate  # On Windows: myenv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply Migrations

```bash
python manage.py migrate
```

### 5. Create a Superuser

```bash
python manage.py createsuperuser
```

### 6. Run the Development Server

```bash
python manage.py runserver
```

### 7. Open in Browser

Visit: [http://localhost:8000](http://localhost:8000)

---

## 🔧 Optional Configuration

Set up environment variables for:

* `SECRET_KEY`
* `EMAIL_HOST_USER`
* `EMAIL_HOST_PASSWORD`

---

## 🔐 Security Recommendations

* Set `DEBUG = False` in `settings.py` for production.
* Update `ALLOWED_HOSTS` with your domain/IP.
* Use environment variables for sensitive credentials.

---
