# Teach2Give Industrial Attachment Technical Test

This repository contains the solution to the technical test that was part of the application process for the industrial attachment at Teach2Give. The test evaluates core programming skills in algorithmic thinking, data structures, and frontend development, which are essential for the role of a software developer.

## Table of Contents
- [Description](#description)
- [Files](#files)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)

## Description
This repository includes solutions to the following problems:

### Section 1: Algorithmic Thinking and Data Structures
1. **Capitalize Each Word in a String**:
   - **Problem**: Write a program that accepts a string as input, capitalizes the first letter of each word in the string, and returns the result string.
   - **Example**:
     - Input: `"hi"`
     - Output: `"Hi"`
     - Input: `"i love programming"`
     - Output: `"I Love Programming"`
   
2. **Frontend Development Challenge**: 
   - **Problem**: Build a Simple FAQ Accordion using only HTML and CSS.
   - **Requirements**:
     - Create an FAQ component where users can click a question to show or hide its answer.
     - If another question is clicked, the previous answer should hide (accordion behavior).
     - Ensure the component is responsive:
       - On mobile, the questions and answers should stack vertically.
       - On larger screens (like tablets or desktops), the layout can display horizontally or as needed.

## Files

The repository includes the following files:

- **`Section 1.py`**: Solution to Problem 1 — Capitalizes the first letter of each word in a string.
- **`index.html`** and **`style.css`** : Solution to Problem 2 — Simple FAQ accordion implemented using HTML and CSS.

## Setup Instructions

To run the code locally, follow the steps below:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/OyoriObegi/Teach2Give-Technical-Test.git
   ```

2. **Navigate to the project directory:**
   ```bash
   cd Teach2Give-Technical-Test
   ```

3. **For the Python solution (Section 1.py)**:
   - Ensure Python 3 is installed on your machine.
   - Run the script to test the string capitalization functionality:
     ```bash
     python Section 1.py
     ```

4. **For the FAQ accordion (index.html)**:
   - Open `index.html` in any modern web browser (Chrome, Firefox, etc.) to view and interact with the FAQ accordion.

## Usage

### 1. `Section 1.py`:
   - This script takes a string as input, capitalizes the first letter of each word, and returns the result.
   - Example usage:
     ```bash
     python Section 1.py
     ```
   - Input: `"hello world"`
   - Output: `"Hello World"`

### 2. `index.html`:
   - Open the `index.html` file in a web browser.
   - Click on any question to toggle the visibility of its corresponding answer.
   - The accordion behavior will ensure that only one answer is visible at a time, and clicking another question will hide the previous one.

## Technologies Used

- **Python 3**: For solving the algorithmic problem.
- **HTML**: Used for structuring the FAQ component.
- **CSS**: Used for styling the FAQ accordion and implementing responsive design.
  
## Contributing

Feel free to fork this repository and contribute by making improvements or adding more features. To contribute, please follow these steps:

1. Fork the repository.
2. Create a feature branch.
3. Implement your changes.
4. Submit a pull request detailing the changes you've made.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
