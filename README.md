# quizzler-app-start
A quizzler app game.

**README**

# Quizzler App

This is a simple console-based quiz application, the Quizzler App, designed to ask True/False questions and evaluate the user's answers. The project is built using Python and utilizes the Tkinter library for the graphical user interface (GUI).

## Components

### 1. `question_model.py`

This module defines the `Question` class, which represents a quiz question. Each question has text and a correct answer.

### 2. `data.py`

In this file, data for the quiz is obtained from the Open Trivia Database API using the `requests` library. The questions retrieved are stored in the `question_data` variable.

### 3. `quiz_brain.py`

The `QuizBrain` class is implemented in this module. It manages the flow of the quiz, keeps track of the score, and evaluates user answers.

### 4. `ui.py`

The `QuizInterface` class is defined in this file using the Tkinter library. It creates the graphical user interface for the quiz, displaying questions, buttons for True/False answers, and providing feedback.

## How to Run

Make sure you have Python installed on your machine. To run the Quizzler App:

1. Clone the repository:

    ```bash
    git clone https://github.com/BrunnoChampZ/quizzler-app-start.git
    ```

2. Navigate to the project directory:

    ```bash
    cd quizzler-app-start
    ```

3. Run the main script:

    ```bash
    python main.py
    ```

## Usage

- The quiz starts by displaying a True/False question on the Tkinter GUI.
- Click the "True" or "False" button to answer the question.
- The GUI provides immediate feedback with a green background for correct answers and a red background for incorrect answers.
- The score is displayed at the top, and the next question is automatically loaded after a brief pause.

After completing the quiz, the final score is printed to the console.

Have fun and enjoy the Quizzler App!
