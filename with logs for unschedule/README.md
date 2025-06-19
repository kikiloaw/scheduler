# School Scheduling System

An automated scheduling system for schools that handles course scheduling with conflict resolution for students, employees, and rooms.

## Features

- **Conflict-Free Scheduling**: Ensures no conflicts between:
  - Students in the same section
  - Employees teaching multiple classes
  - Rooms being used simultaneously
- **Duration-Based Scheduling**: Uses actual class durations from your data
- **Multiple Room Types**: Supports lab rooms (type 1) and lecture rooms (type 2)
- **Multiple Employees**: Handles scheduling for multiple teachers
- **Conflict Detection**: Advanced scheduler detects and reports conflicts
- **Statistics**: Provides utilization statistics for rooms and employees
- **Export**: Saves schedules to JSON files

## Files

- `scheduler.py` - Basic scheduling system
- `advanced_scheduler.py` - Advanced system with conflict detection and statistics
- `example_usage.py` - Examples showing how to use the system
- `README.md` - This documentation

## Data Format

The system expects data in this format:

```python
class_data = [
    {
        'Courses': [
            {
                'courseid': 1,
                'section': '2A',
                'classschedule': [ 
                    {'duration': '3:30', 'roomtype': 1, 'employeeid': 120},
                    {'duration': '1:00', 'roomtype': 2, 'employeeid': 120},
                    {'duration': '1:15', 'roomtype': 2, 'employeeid': 120}
                ]
            }
        ]
    }
]
```

### Data Structure Explanation

- **courseid**: Unique identifier for the course
- **section**: Student section (students in same section cannot have overlapping classes)
- **duration**: Class duration in format 'H:MM' or 'H' (hours)
- **roomtype**: 1 for lab room, 2 for lecture room
- **employeeid**: Teacher/employee ID (same employee cannot teach multiple classes simultaneously)

## Usage

### Basic Usage

```python
from scheduler import SchoolScheduler

# Your class data
class_data = [...]  # Your data here

# Create scheduler and generate schedule
scheduler = SchoolScheduler()
schedule = scheduler.generate_schedule(class_data)

# Print the schedule
scheduler.print_schedule()

# Export to JSON
scheduler.export_schedule("my_schedule.json")
```

### Advanced Usage

```python
from advanced_scheduler import AdvancedSchoolScheduler

# Your class data
class_data = [...]  # Your data here

# Create advanced scheduler
scheduler = AdvancedSchoolScheduler()
schedule = scheduler.generate_schedule(class_data)

# Print the schedule
scheduler.print_schedule()

# Get statistics
stats = scheduler.get_schedule_statistics()
print(f"Total classes: {stats['total_classes']}")
print(f"Conflicts detected: {stats['conflicts_detected']}")

# Export to JSON
scheduler.export_schedule("advanced_schedule.json")
```

### Running Examples

```bash
python example_usage.py
```

This will run 4 different examples and save the results to JSON files.

## School Hours

The system operates during school hours:
- **Start Time**: 8:00 AM
- **End Time**: 5:00 PM
- **Time Slots**: 30-minute intervals

## Conflict Resolution

The system prevents these types of conflicts:

1. **Section Conflicts**: Students in the same section cannot have overlapping classes
2. **Employee Conflicts**: Teachers cannot teach multiple classes at the same time
3. **Room Conflicts**: Rooms cannot be used by multiple classes simultaneously

## Output Format

The system generates schedules with the following information:

```json
[
  {
    "course_id": 1,
    "section": "2A",
    "start_time": 480,
    "end_time": 690,
    "duration": 210,
    "room_type": 1,
    "employee_id": 120,
    "start_time_str": "08:00",
    "end_time_str": "11:30"
  }
]
```

## Schedule Display

The system prints schedules in multiple views:

1. **By Section**: Shows all classes for each student section
2. **By Room**: Shows room utilization
3. **By Employee**: Shows teacher schedules
4. **Statistics**: Shows utilization percentages and workload

## Customization

You can customize the system by:

1. **Modifying School Hours**: Change `school_start` and `school_end` in the scheduler
2. **Adding Room Types**: Extend the `rooms` dictionary
3. **Changing Time Slots**: Modify the interval in `find_available_slot`
4. **Adding Constraints**: Implement additional conflict detection rules

## Example Output

```
================================================================================
GENERATED SCHOOL SCHEDULE
================================================================================

Section: 2A
--------------------------------------------------
  08:00 - 11:30 | Course 1 | Lab Room | Employee 120
  13:00 - 14:00 | Course 2 | Lab Room | Employee 120
  14:30 - 15:45 | Course 1 | Lecture Room | Employee 120

Section: 2B
--------------------------------------------------
  08:00 - 09:00 | Course 3 | Lab Room | Employee 120
  09:30 - 11:30 | Course 3 | Lecture Room | Employee 120
  13:00 - 14:00 | Course 4 | Lab Room | Employee 120

================================================================================
ROOM UTILIZATION
================================================================================

Lab Room Schedule:
  08:00 - 11:30 | Course 1 | Section 2A | Employee 120
  08:00 - 09:00 | Course 3 | Section 2B | Employee 120
  13:00 - 14:00 | Course 2 | Section 2A | Employee 120
  13:00 - 14:00 | Course 4 | Section 2B | Employee 120

Lecture Room Schedule:
  14:30 - 15:45 | Course 1 | Section 2A | Employee 120
  09:30 - 11:30 | Course 3 | Section 2B | Employee 120
```

## Requirements

- Python 3.6+
- No external dependencies required

## Installation

1. Download the files to your project directory
2. Run the examples: `python example_usage.py`
3. Modify the data structure for your needs
4. Use the scheduler in your own code

## Troubleshooting

- **No slots available**: The system may not find available slots if there are too many conflicts. Try reducing class durations or adding more employees.
- **Conflicts detected**: The advanced scheduler will show specific conflicts. Review your data for overlapping requirements.
- **Long classes**: Very long classes (4+ hours) may be difficult to schedule within school hours.

## License

This project is open source and available under the MIT License. 