# formula_changes
Формула изменения своей реальности


# Formula Changes - Change Readiness Diagnostic Tool

## Description
Formula Changes is a web application that implements the change readiness formula (D × V × F > R) for personal development and self-diagnosis. The application helps users assess their readiness for change based on four key factors:

- **D (Dissatisfaction)**: Level of dissatisfaction with the current state (0-10)
- **V (Vision)**: Clarity of the desired future state (0-10)
- **F (First Steps)**: Concrete first steps planned (0-10)
- **R (Resistance)**: Level of resistance to change (0-10)

The formula C = D × V × F > R determines if a person is ready to start making changes.

## Features
- Web-based interface for easy access
- CLI mode for terminal usage
- Detailed assessment and recommendations
- Identification of the weakest factor
- Suggested actions for improvement

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd formula_changes
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Web Application
1. Run the Flask application:
   ```bash
   python main.py
   ```

2. Open your browser and navigate to `http://localhost:5000`

3. Use the change diagnosis form at `/change_diagnosis`

### CLI Mode
Run the diagnosis directly from the terminal:
```bash
python diagnose.py
```

Follow the prompts to enter your D, V, F, and R values (0-10).

## API Endpoints
- `GET /` - Main page
- `GET /change_diagnosis` - Change diagnosis form
- `POST /change_diagnosis` - API endpoint for diagnosis (when activated)

## How It Works
The application calculates the product of D, V, and F values divided by 100, then compares it to the R value:
- If (D × V × F) / 100 > R: Ready to start changes
- If close to R: On the edge, requires support
- If (D × V × F) / 100 < R: Not ready yet

The application identifies the weakest factor and provides targeted suggestions for improvement.

## Project Structure
- `main.py` - Flask application entry point
- `diagnose.py` - Core logic for change readiness calculation
- `templates/` - HTML templates
- `static/` - Static files (JSON, YAML, PDF)
- `requirements.txt` - Python dependencies

## License
This project is open source and available under the MIT License.