
# Pomodoro Project

## Project Overview

Pomodoro is a time management application that helps users manage their tasks using the Pomodoro Technique. This technique involves breaking work into intervals, traditionally 25 minutes 
in length, separated by short breaks.

## Features

- Create and manage timers for Pomodoro intervals, short breaks, and long breaks.
- Automatically start Pomodoros and breaks.
- Manage tasks and track their completion.
- Receive notifications when timers end.

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/yourusername/pomodoro.git
    cd pomodoro
    ```

2. **Create a virtual environment:**

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Apply migrations:**

    ```sh
    python manage.py migrate
    ```

5. **Run the development server:**

    ```sh
    python manage.py runserver
    ```

## Usage

- Access the application at `http://127.0.0.1:8000/`.
- Navigate to the settings page to configure your Pomodoro intervals and breaks.
- Use the timer page to start and manage your Pomodoro sessions.
- Manage your tasks and track their completion from the tasks page.

## Project Structure

- **asgi.py:** ASGI configuration for the project.
- **wsgi.py:** WSGI configuration for the project.
- **models.py:** Contains database models for Timer, Notification, and Task.
- **views.py:** Contains the view functions for handling requests.
- **urls.py:** URL routing for the application.
- **forms.py:** Contains form definitions for handling user input.
- **index.js:** JavaScript file for handling AJAX requests.

## Models

### Timer

- **pomodoro:** Duration of the Pomodoro interval.
- **short_break:** Duration of the short break.
- **long_break:** Duration of the long break.
- **auto_start_pomodoros:** Automatically start Pomodoros.
- **auto_start_breaks:** Automatically start breaks.
- **number_of_interval:** Number of intervals.
- **published_date:** Date the timer was published.

### Notification

- **timer:** Foreign key to the Timer model.
- **notification_text:** Text of the notification.
- **send_when:** When to send the notification.
- **send_time:** Time to send the notification.

### Tasks

- **task_text:** Description of the task.
- **completed:** Whether the task is completed.
- **published_date:** Date the task was published.
- **end_time:** Time the task was completed.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.

## Acknowledgements

- [Django Documentation](https://docs.djangoproject.com/en/4.0/)
- [Pomodoro Technique](https://en.wikipedia.org/wiki/Pomodoro_Technique)
