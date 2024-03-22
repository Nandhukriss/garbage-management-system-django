# Garbage Management System

### Home Page 

![home page](https://github.com/Nandhukriss/Nandhukriss/assets/103727372/cd77452b-76dd-4630-ada2-ff66a3a8c432)

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

