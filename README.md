# Sudoku Solver

#### Video Demo:  <URL HERE>

#### Description

This Sudoku Solver, implemented in C using a backtracking algorithm, is designed to find solutions to Sudoku puzzles. Additionally, the solver can be integrated with Flask to provide a web interface for solving Sudoku puzzles.

## Project Structure

The project directory is structured as follows:

* `templates`: Contains HTML templates for the Flask application.
  + `layout.html`: Common layout template.
  + `history_ss.html`: Template for displaying Sudoku solving history.
  + `apology.html`: Apology template.
  + `solve_sudoku.html`: Template for solving Sudoku puzzles.
  + `base.html`: Base template.
  + `register.html`: Template for user registration.
  + `login.html`: Template for user login.

* `requirements.txt`: Lists project dependencies.

* `c_files`: Contains C source code for the Sudoku solver.
  + `ss`: (Already compiled code for bash only. Use compile with c compiler in your device for better performance.) [Check Tutorial](#building-the-project-1) for building cfiles.
  + `ss.c`: C source code for the Sudoku solver simplex and only for getting values without formatted.
  + `solve_sudoku`: (Already compiled code for bash only. Use compile with c compiler in your device for better performance.) [Check Tutorial](#building-the-project-1) for building cfiles.
  + `solve_sudoku.c`: C source code for the Sudoku solver use for getting values formatted.

* `helpers.py`: Python script containing helper functions.

* `test.db`: SQLite database file.

* `static`: Contains static files for the Flask application.
  + `css`: Directory for CSS files.
    - `solve_sudoku.css`: CSS file for styling the Solve Sudoku page.
    - `style.css`: General stylesheet.
    - `history_ss.css`: CSS file for styling the Sudoku solving history page.
  + `script`: Directory for JavaScript files.
    - `history_ss.js`: JavaScript file for the Sudoku solving history page.
    - `script.js`: General JavaScript file.
    - `solve_sudoku.js`: JavaScript file for the Solve Sudoku page.
  + `favicon.ico`: Favicon icon.

* `app.py`: Flask application script.

## Usage

### Website usage

This is a web-based Sudoku solver implemented in Flask. It allows users to input Sudoku puzzles, either through a string or manual entry, and displays the solved puzzle along with backtracking complexity.

#### Web Interface

1. Open the Sudoku Solver website on your browser.

2. You can access the Sudoku solver by visiting the following URL:
   

```
   https://sudoku.solver.naye.xyz/ss
   ```

3. You can access the Sudoku solver history by visiting the following URL:
   

```
   https://sudoku.solver.naye.xyz/history_ss
   ```

4. Use the web interface to interact with the solver:
   - **Toggle Input Area:** Click the "Toggle Input Area" button to show/hide the input area.
   - **Input Area:** Enter the Sudoku puzzle either as a string without spaces or manually input row by row.
   - **Check Button:** Click the "Check" button to solve the Sudoku puzzle.
   - **Result:** The solved Sudoku puzzle will be displayed below the input area.
   - **Highlighting:** Use the "Highlight" dropdown to highlight specific numbers in the solved puzzle.

5. Additionally, you can share a specific Sudoku puzzle by appending the `?s=` parameter to the URL. For example:
   

```
   https://sudoku.solver.naye.xyz/ss?s=090600800000503400807000610000050007000790100000006300070000020040000000203061784
   ```

   This will directly display the solution for the provided Sudoku puzzle.

#### Command Line

If you prefer a command-line interface, you can use the following API endpoint:

* **Endpoint:**
  

```
  https://sudoku.solver.naye.xyz/api/ss?sudoku=<81chars_sudoku_string_without_space>
  ```

* **Example:**
  

```
  https://sudoku.solver.naye.xyz/api/ss?sudoku=090600800000503400807000610000050007000790100000006300070000020040000000203061784
  ```

* **Using Curl:**
You can also use the Sudoku solver API by making a GET request with `curl` . Here's an example:
  

```bash
  curl 'https://sudoku.solver.naye.xyz/api/ss?sudoku=835416907290057431000000000069134782123678000000000063650000000000345276374900000&token=2024' -H 'cookie: session=eyJ1c2VyX2lkIjoxMX0.ZYiBIg.OvOgYfHQHDtEJ45kKZzNFo6__4Y'
  ```

   If you don't have any key, use this one:
   

```bash
   curl 'https://sudoku.solver.naye.xyz/api/ss?sudoku=835416907290057431000000000069134782123678000000000063650000000000345276374900000&token=2024' -H 'cookie: session=eyJ1c2VyX2lkIjoxMX0.ZYiBIg.OvOgYfHQHDtEJ45kKZzNFo6__4Y'
   ```

### Building the flask Project 

To run the project locally or deploy it, follow these steps:

1. Clone the repository:
   

```bash
   git clone https://github.com/naye2m/sudoku-solver.git
   ```

2. Install dependencies:
   

```bash
   pip install -r requirements.txt
   ```

3. Run the Flask application:
   

```bash
   flask run
   ```

4. Open the Sudoku Solver website in your browser and follow [the usage instructions above](#flask-integration-for-web-interface).

### Command Line usage

#### Building the C Project

To compile the project using a C compiler (e.g., gcc), use the following command:
   

```bash
   gcc sudoku_solver.c -o sudoku_solver
   ```

To use the solver with a Sudoku puzzle represented as a string of 81 characters without spaces, use the following command-line format:
   

```bash
   ./sudoku_solver <81chars_sudoku_string_without_space>
   ```

Example:
   

```bash
   ./sudoku_solver 090600800000503400807000610000050007000790100000006300070000020040000000203061784
   ```

If no command-line argument is provided, the program will prompt the user to enter the Sudoku puzzle row by row. Use the following command:
   

```bash
   ./sudoku_solver
   ```

#### Flask Integration for Web Interface

The Sudoku solver can be integrated with Flask to provide a web interface for solving Sudoku puzzles. The Flask app is available in the `./app.py` file. To run the Flask app:
   

```bash
   python app.py
   ```

Visit `http://127.0.0.1:5000` in your web browser to access the web interface.

### Notes

* The efficiency of the solver is influenced by the complexity of the Sudoku puzzle.

## License

This project is licensed under the  NoLicense. For details, see the [LICENSE](LICENSE) file.
