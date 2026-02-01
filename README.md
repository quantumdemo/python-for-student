# Learn Python Platform

An interactive, web-based Python learning platform for secondary school students.

## Features
- 6 interactive Jupyter Notebook lessons.
- Embedded JupyterLite for in-browser Python execution (via Pyodide).
- Responsive landing page.
- Student-friendly interface.

## Lessons
1. **Print Statement**: Learn how to display messages.
2. **Input Statement**: Get user input.
3. **Variables & Data Types**: Store and manage data.
4. **Control Structures**: Make decisions with `if` and `else`.
5. **Loops**: Repeat actions with `for` and `while`.
6. **Concatenation & Type Conversion**: Join strings and convert data types.

## How to Build
To rebuild the JupyterLite environment:
1. Install dependencies:
   ```bash
   pip install jupyterlite-core jupyterlite-pyodide-kernel jupyter-server jupyterlab nbformat
   ```
2. Run the build command:
   ```bash
   jupyter lite build
   ```

The built site will be in the `_output` directory.

## How to Run
Serve the root directory using any web server. For example:
```bash
python3 -m http.server 3000
```
Then open `http://localhost:3000` in your browser.

## Deployment
For instructions on how to deploy this platform for free, see [DEPLOYMENT.md](DEPLOYMENT.md).

## Author
Afeez Alimi
