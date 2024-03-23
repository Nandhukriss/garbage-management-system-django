# Garbage Management System

## 🧑‍💻 Tech Stack 🧑‍💻
<div class="row">
  <div class="col">
    💡 <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="Python" width="20"/> Python
    💡 <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/javascript/javascript-original.svg" alt="JavaScript" width="20"/> JavaScript
    💡 <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/sqlite/sqlite-original.svg" alt="SQLite" width="20"/> SQLite
  </div>
  <div class="col">
    💡 <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/html5/html5-original.svg" alt="HTML5" width="20"/> HTML
    💡<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/css3/css3-original.svg" alt="CSS3" width="20"/> CSS
    💡 <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/bootstrap/bootstrap-original.svg" alt="Bootstrap" width="20"/> Bootstrap
  </div>
</div>




### 📌 Home Page 

![home page](https://github.com/rohanjijovarghese/garbage-management-system-django/assets/103727372/16fc66d4-5ee0-44ee-ac7e-6ede31bb89db)

### 📌 Driver jobs 

![jobs](https://github.com/rohanjijovarghese/garbage-management-system-django/assets/103727372/c49b53e4-3697-4ee7-8107-209055520707)

###  📌 Your Complaints(User) 

![your complaints](https://github.com/rohanjijovarghese/garbage-management-system-django/assets/103727372/1bde45b4-6351-441b-b80a-b7634645ed2c)

### 📌 Post Your Complaints  

![Post Your Complaints](https://github.com/rohanjijovarghese/garbage-management-system-django/assets/103727372/e723d150-4670-41f9-8587-0d848bb3f96e)


## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/rohanjijovarghese/garbage-management-system-django.git
    ```

2. **Navigate to the project directory:**

    ```bash
    cd garbage-management-system-django
    ```

3. **Create a virtual environment (optional but recommended):**

    ```bash
    python -m venv venv
    ```

4. **Activate the virtual environment:**

    - On Windows:

      ```bash
      venv\Scripts\activate
      ```

    - On macOS/Linux:

      ```bash
      source venv/bin/activate
      ```

5. **Install project dependencies using the requirements file:**

    ```bash
    pip install -r requirements.txt
    ```

6. **Set up environmental variables using Python dotenv:**

    Create a file named `.env` in the root directory of the project and add the following lines, replacing `'your email'` and `'your password'` with your actual email and password:

    ```plaintext
    HOST_EMAIL='your email'
    HOST_PASSWORD='your password'
    ```

## Running the Project

1. **Apply database migrations:**

    ```bash
    python manage.py migrate
    ```

2. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your web browser to access the Django development server.

