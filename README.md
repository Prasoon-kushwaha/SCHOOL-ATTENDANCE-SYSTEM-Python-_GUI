# School Attendance System (Python GUI)

## Overview
The School Attendance System is a desktop application developed using Python and the Tkinter library. It provides a simple and efficient way to manage student attendance, featuring functionalities to mark attendance, view attendance records, and manage student data. This system is designed to streamline the attendance-taking process for educational institutions.

## Features
- **User-Friendly Interface:** Intuitive and easy-to-use graphical user interface (GUI) built with Tkinter.
- **Attendance Management:** Mark attendance for students with just a few clicks.
- **Student Data Management:** Add, update, and delete student records.
- **Attendance Records:** View and export attendance records for analysis.
- **Persistence:** Data is stored in a CSV file, ensuring data is saved between sessions.

## Prerequisites
- Python 3.x
- Tkinter library (usually included with Python installations)
- CSV module (included with Python standard library)

## Installation
1. **Clone the repository:**
    ```bash
    git clone https://github.com/Prasoon-kushwaha/SCHOOL-ATTENDANCE-SYSTEM-Python-_GUI.git
    ```
2. **Navigate to the project directory:**
    ```bash
    cd SCHOOL-ATTENDANCE-SYSTEM-Python-_GUI
    ```
3. **Run the application:**
    ```bash
    python main.py
    ```

## Usage
1. **Launching the Application:**
   - Run `main.py` to start the application.
   - The main window will appear with options to manage attendance and student data.

2. **Managing Students:**
   - Add new students by entering their details and clicking the "Add" button.
   - Update existing student records by selecting a student, modifying their details, and clicking the "Update" button.
   - Delete a student by selecting them and clicking the "Delete" button.

3. **Marking Attendance:**
   - Select a date and mark attendance for each student.
   - Save the attendance records by clicking the "Save" button.

4. **Viewing Attendance Records:**
   - View attendance records by selecting a date range.
   - Export attendance data to a CSV file for further analysis.

## Project Structure
```
SCHOOL-ATTENDANCE-SYSTEM-Python-_GUI/
│
├── main.py                # Entry point for the application
├── student_management.py  # Module for managing student data
├── attendance.py          # Module for handling attendance
├── gui.py                 # Module for creating the GUI
├── data/
│   ├── students.csv       # CSV file storing student data
│   └── attendance.csv     # CSV file storing attendance records
└── README.md              # Project README file

```