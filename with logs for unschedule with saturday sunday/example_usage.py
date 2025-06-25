#!/usr/bin/env python3
"""
Example usage of the School Scheduler
This script demonstrates how to use the scheduler with different scenarios
"""

from scheduler import SchoolScheduler
from advanced_scheduler import AdvancedSchoolScheduler
import json

def example_1_basic_scheduling():
    """Example 1: Basic scheduling with your original data"""
    print("="*60)
    print("EXAMPLE 1: Basic Scheduling")
    print("="*60)
    
    # Your original class data
    class_data = [
        {
            'Courses': [
                {
                    'ClassID': 1,
                    'section': '2A',
                    'classschedule': [ 
                        {'duration': '3:30', 'roomtype': 1, 'employeeid': 120},
                        {'duration': '1:00', 'roomtype': 2, 'employeeid': 120},
                        {'duration': '1:15', 'roomtype': 2, 'employeeid': 120}
                    ]
                },
                {
                    'ClassID': 2,
                    'section': '2A',
                    'classschedule': [
                        {'duration': '1:00', 'roomtype': 1, 'employeeid': 120},
                        {'duration': '1:30', 'roomtype': 2, 'employeeid': 120}
                    ]
                }
            ]
        },
        {
            'Courses': [
                {
                    'ClassID': 3,
                    'section': '2B',
                    'classschedule': [
                        {'duration': '1:00', 'roomtype': 1, 'employeeid': 120},
                        {'duration': '2:00', 'roomtype': 2, 'employeeid': 120},
                    ]
                },
                {
                    'ClassID': 4,
                    'section': '2B',
                    'classschedule': [
                        {'duration': '1:00', 'roomtype': 1, 'employeeid': 120},
                    ]
                }
            ]
        }
    ]
    
    # Use basic scheduler
    scheduler = SchoolScheduler()
    schedule = scheduler.generate_schedule(class_data)
    scheduler.print_schedule()
    
    return schedule

def example_2_multiple_employees():
    """Example 2: Scheduling with multiple employees"""
    print("\n" + "="*60)
    print("EXAMPLE 2: Multiple Employees")
    print("="*60)
    
    class_data = [
        {
            'Courses': [
                {
                    'ClassID': 1,
                    'section': '2A',
                    'classschedule': [ 
                        {'duration': '2:00', 'roomtype': 1, 'employeeid': 101},
                        {'duration': '1:30', 'roomtype': 2, 'employeeid': 102},
                    ]
                },
                {
                    'ClassID': 2,
                    'section': '2A',
                    'classschedule': [
                        {'duration': '1:00', 'roomtype': 1, 'employeeid': 103},
                        {'duration': '1:30', 'roomtype': 2, 'employeeid': 101},
                    ]
                }
            ]
        },
        {
            'Courses': [
                {
                    'ClassID': 3,
                    'section': '2B',
                    'classschedule': [
                        {'duration': '1:30', 'roomtype': 1, 'employeeid': 102},
                        {'duration': '2:00', 'roomtype': 2, 'employeeid': 103},
                    ]
                },
                {
                    'ClassID': 4,
                    'section': '2B',
                    'classschedule': [
                        {'duration': '1:00', 'roomtype': 1, 'employeeid': 101},
                    ]
                }
            ]
        }
    ]
    
    # Use advanced scheduler
    scheduler = AdvancedSchoolScheduler()
    schedule = scheduler.generate_schedule(class_data)
    scheduler.print_schedule()
    
    # Show statistics
    stats = scheduler.get_schedule_statistics()
    print(f"\nEmployee Workload:")
    for emp_id, workload in stats['employee_workload'].items():
        print(f"  Employee {emp_id}: {workload['classes']} classes, "
              f"{workload['total_duration']} minutes ({workload['workload_percentage']:.1f}%)")
    
    return schedule

def example_3_conflict_scenario():
    """Example 3: Demonstrating conflict detection"""
    print("\n" + "="*60)
    print("EXAMPLE 3: Conflict Detection")
    print("="*60)
    
    # This data will create conflicts
    class_data = [
        {
            'Courses': [
                {
                    'ClassID': 1,
                    'section': '2A',
                    'classschedule': [ 
                        {'duration': '4:00', 'roomtype': 1, 'employeeid': 101},  # Very long class
                        {'duration': '2:00', 'roomtype': 1, 'employeeid': 101},  # Same employee, same room
                    ]
                },
                {
                    'ClassID': 2,
                    'section': '2A',
                    'classschedule': [
                        {'duration': '2:00', 'roomtype': 1, 'employeeid': 101},  # Same employee, same room
                    ]
                }
            ]
        }
    ]
    
    # Use advanced scheduler to detect conflicts
    scheduler = AdvancedSchoolScheduler()
    schedule = scheduler.generate_schedule(class_data)
    scheduler.print_schedule()
    
    return schedule

def example_4_custom_data():
    """Example 4: Using custom data from user"""
    print("\n" + "="*60)
    print("EXAMPLE 4: Custom Data Input")
    print("="*60)
    
    # You can modify this data structure for your needs
    custom_data = [
        {
            'Courses': [
                {
                    'ClassID': 101,
                    'section': 'CS101',
                    'classschedule': [ 
                        {'duration': '1:30', 'roomtype': 1, 'employeeid': 201},  # Lab
                        {'duration': '1:00', 'roomtype': 2, 'employeeid': 201},  # Lecture
                    ]
                },
                {
                    'ClassID': 102,
                    'section': 'CS101',
                    'classschedule': [
                        {'duration': '1:00', 'roomtype': 1, 'employeeid': 202},  # Lab
                        {'duration': '1:30', 'roomtype': 2, 'employeeid': 202},  # Lecture
                    ]
                }
            ]
        },
        {
            'Courses': [
                {
                    'ClassID': 201,
                    'section': 'MATH101',
                    'classschedule': [
                        {'duration': '2:00', 'roomtype': 2, 'employeeid': 203},  # Lecture only
                    ]
                }
            ]
        }
    ]
    
    scheduler = AdvancedSchoolScheduler()
    schedule = scheduler.generate_schedule(custom_data)
    scheduler.print_schedule()
    
    return schedule

def save_schedule_to_file(schedule, filename):
    """Save schedule to a JSON file"""
    with open(filename, 'w') as f:
        json.dump(schedule, f, indent=2)
    print(f"Schedule saved to {filename}")

def main():
    """Run all examples"""
    print("School Scheduling System - Examples")
    print("="*60)
    
    # Run all examples
    schedule1 = example_1_basic_scheduling()
    schedule2 = example_2_multiple_employees()
    schedule3 = example_3_conflict_scenario()
    schedule4 = example_4_custom_data()
    
    # Save all schedules
    save_schedule_to_file(schedule1, "example1_schedule.json")
    save_schedule_to_file(schedule2, "example2_schedule.json")
    save_schedule_to_file(schedule3, "example3_schedule.json")
    save_schedule_to_file(schedule4, "example4_schedule.json")
    
    print("\n" + "="*60)
    print("All examples completed!")
    print("Check the generated JSON files for the schedules.")
    print("="*60)

if __name__ == "__main__":
    main() 