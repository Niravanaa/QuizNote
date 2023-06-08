# QuizNote
This repository contains Python scripts for taking notes, generating interview questions and answers.

## Contents

- [NotesSummary.py](NotesSummary.py): A script for taking notes for different classes and chapters.
- [QuizletSummary.py](QuizletSummary.py): A script for generating interview questions and answers.

## About

The `NotesSummary.py` script allows users to take notes for different classes and chapters of textbooks. It provides a user-friendly interface to enter the class, chapter, section name, and content. The notes are formatted and appended to the 'notes_output.txt' file for easy feeding into ChatGPT.

The `QuizletSummary.py` script generates prompts that can later be fed into ChatGPT to generate interview-level questions and answers. Users can enter the content, and the script formats it as a question and answer pair. The generated pairs are appended to the 'quizlet_output.txt' file, which can be used for interview preparation or creating flashcards.

## Usage

To use the `NotesSummary.py` script, run the following command:

```bash
python NotesSummary.py
```
The script will prompt you to enter the class, chapter, section name, and content for your notes. Press 'q' to quit entering sections. The notes will be saved in the 'notes_output.txt' file.

To use the QuizletSummary.py script, run the following command:
```bash
python QuizletSummary.py
```

The script will prompt you to enter the content for the interview questions and answers. Press 'q' to quit entering content. The question and answer pairs will be saved in the 'quizlet_output.txt' file.

Contributing
Contributions to this repository are welcome. You can submit bug reports, feature requests, or pull requests through the GitHub repository.

License
This repository is licensed under the MIT License. See the [LICENSE](https://opensource.org/license/mit/) file for more information.
