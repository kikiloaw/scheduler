#!/usr/bin/env python3
"""
Export Sample Data to CSV Files
This script exports the sample data into separate CSV files:
- One CSV file per section
- One CSV file per room
- One CSV file per employee
"""

import csv
import os
import datetime
from sample_data import sample_class_data, employee_info, rooms

def export_section_csvs():
    """Export one CSV file per section"""
    print("Exporting section CSV files...")
    
    for section_data in sample_class_data:
        if not section_data['Courses']:
            continue
            
        section_name = section_data['Courses'][0]['section']
        filename = f"section_{section_name}_weekly.csv"
        
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['ClassID', 'coursename', 'section', 'duration', 'roomid', 'roomtype', 'employeeid', 'day']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            
            for course in section_data['Courses']:
                for schedule in course['classschedule']:
                    row = {
                        'ClassID': course['ClassID'],
                        'coursename': course['coursename'],
                        'section': course['section'],
                        'duration': schedule['duration'],
                        'roomid': schedule['roomid'],
                        'roomtype': schedule['roomtype'],
                        'employeeid': schedule['employeeid'],
                        'day': schedule['day']
                    }
                    writer.writerow(row)
        
        print(f"Created: {filename}")

def export_room_csvs():
    """Export one CSV file per room"""
    print("\nExporting room CSV files...")
    
    # Get all unique rooms from the data
    all_rooms = set()
    for section_data in sample_class_data:
        for course in section_data['Courses']:
            for schedule in course['classschedule']:
                all_rooms.add(schedule['roomid'])
    
    for room_id in sorted(all_rooms):
        filename = f"room_{room_id.replace(' ', '_')}_weekly.csv"
        
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['ClassID', 'coursename', 'section', 'duration', 'roomid', 'roomtype', 'employeeid', 'day']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            
            for section_data in sample_class_data:
                for course in section_data['Courses']:
                    for schedule in course['classschedule']:
                        if schedule['roomid'] == room_id:
                            row = {
                                'ClassID': course['ClassID'],
                                'coursename': course['coursename'],
                                'section': course['section'],
                                'duration': schedule['duration'],
                                'roomid': schedule['roomid'],
                                'roomtype': schedule['roomtype'],
                                'employeeid': schedule['employeeid'],
                                'day': schedule['day']
                            }
                            writer.writerow(row)
        
        print(f"Created: {filename}")

def export_employee_csvs():
    """Export one CSV file per employee"""
    print("\nExporting employee CSV files...")
    
    # Get all unique employees from the data
    all_employees = set()
    for section_data in sample_class_data:
        for course in section_data['Courses']:
            for schedule in course['classschedule']:
                all_employees.add(schedule['employeeid'])
    
    for employee_id in sorted(all_employees):
        filename = f"employee_{employee_id}_weekly.csv"
        
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['ClassID', 'coursename', 'section', 'duration', 'roomid', 'roomtype', 'employeeid', 'day']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            
            for section_data in sample_class_data:
                for course in section_data['Courses']:
                    for schedule in course['classschedule']:
                        if schedule['employeeid'] == employee_id:
                            row = {
                                'ClassID': course['ClassID'],
                                'coursename': course['coursename'],
                                'section': course['section'],
                                'duration': schedule['duration'],
                                'roomid': schedule['roomid'],
                                'roomtype': schedule['roomtype'],
                                'employeeid': schedule['employeeid'],
                                'day': schedule['day']
                            }
                            writer.writerow(row)
        
        print(f"Created: {filename}")

def print_summary():
    """Print a summary of the exported files"""
    print("\n" + "="*60)
    print("EXPORT SUMMARY")
    print("="*60)
    
    # Count section files
    section_files = [f for f in os.listdir('.') if f.startswith('section_') and f.endswith('.csv')]
    print(f"Section CSV files: {len(section_files)}")
    for file in sorted(section_files):
        print(f"  - {file}")
    
    # Count room files
    room_files = [f for f in os.listdir('.') if f.startswith('room_') and f.endswith('.csv')]
    print(f"\nRoom CSV files: {len(room_files)}")
    for file in sorted(room_files):
        print(f"  - {file}")
    
    # Count employee files
    employee_files = [f for f in os.listdir('.') if f.startswith('employee_') and f.endswith('.csv')]
    print(f"\nEmployee CSV files: {len(employee_files)}")
    for file in sorted(employee_files):
        print(f"  - {file}")
    
    print("="*60)

def get_time_slots(start="6:00 AM", end="9:00 PM", interval_minutes=30):
    """Generate a list of time slot strings from start to end in interval_minutes."""
    slots = []
    start_dt = datetime.datetime.strptime(start, "%I:%M %p")
    end_dt = datetime.datetime.strptime(end, "%I:%M %p")
    curr = start_dt
    while curr < end_dt:
        next_slot = curr + datetime.timedelta(minutes=interval_minutes)
        # Use %I for hour and strip leading zero for Windows compatibility
        curr_str = curr.strftime('%I:%M %p').lstrip('0')
        next_str = next_slot.strftime('%I:%M %p').lstrip('0')
        slots.append(f"{curr_str} - {next_str}")
        curr = next_slot
    return slots

time_slots = get_time_slots()
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

def time_to_slot_index(start_time, duration):
    """Given a start time (e.g. '8:00 AM') and duration ('1:30'), return the slot indices covered."""
    start_dt = datetime.datetime.strptime(start_time, "%I:%M %p")
    h, m = map(int, duration.split(":"))
    end_dt = start_dt + datetime.timedelta(hours=h, minutes=m)
    indices = []
    curr = start_dt
    while curr < end_dt:
        slot_str = f"{curr.strftime('%-I:%M %p')} - {(curr + datetime.timedelta(minutes=30)).strftime('%-I:%M %p')}"
        if slot_str in time_slots:
            indices.append(time_slots.index(slot_str))
        curr += datetime.timedelta(minutes=30)
    return indices

def parse_time_24h(time_str):
    """Convert '8:00' or '13:30' to '8:00 AM' or '1:30 PM'"""
    dt = datetime.datetime.strptime(time_str, "%H:%M")
    return dt.strftime("%-I:%M %p")

def export_timegrid_csvs():
    # Helper to get all unique employees, sections, rooms
    all_employees = set()
    all_sections = set()
    all_rooms = set()
    for section_data in sample_class_data:
        for course in section_data['Courses']:
            all_sections.add(course['section'])
            for sched in course['classschedule']:
                all_employees.add(sched['employeeid'])
                all_rooms.add(sched['roomid'])

    def build_grid(filter_type, filter_value):
        grid = [["" for _ in days] for _ in time_slots]
        # Filtered courses for this entity
        filtered_courses = []
        for section_data in sample_class_data:
            for course in section_data['Courses']:
                if filter_type == 'section' and course['section'] != filter_value:
                    continue
                for sched in course['classschedule']:
                    if filter_type == 'employee' and sched['employeeid'] != filter_value:
                        continue
                    if filter_type == 'room' and sched['roomid'] != filter_value:
                        continue
                    filtered_courses.append((course, sched))
        # Place each class at the earliest available slot for its day
        for course, sched in filtered_courses:
            cell = None
            if filter_type == 'employee':
                cell = f"{course['coursename']}\n{course['section']}\n{sched['roomid']}"
            elif filter_type == 'section':
                cell = f"{course['coursename']}\n{employee_info.get(sched['employeeid'], sched['employeeid'])}\n{sched['roomid']}"
            elif filter_type == 'room':
                cell = f"{course['coursename']}\n{course['section']}\n{employee_info.get(sched['employeeid'], sched['employeeid'])}"
            day_idx = days.index(sched['day'])
            h, m = map(int, sched['duration'].split(":"))
            n_slots = (h * 60 + m) // 30
            # Find first available slot for this day
            for slot_idx in range(len(time_slots)):
                # Check if enough consecutive slots are empty
                if all(not grid[slot_idx + offset][day_idx] for offset in range(n_slots) if slot_idx + offset < len(time_slots)):
                    for fill_idx in range(n_slots):
                        if slot_idx + fill_idx < len(time_slots):
                            grid[slot_idx + fill_idx][day_idx] = cell
                    break
        return grid

    # Export for employees
    for emp_id in sorted(all_employees):
        filename = f"employee_{emp_id}_timegrid.csv"
        grid = build_grid('employee', emp_id)
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Time Slot"] + days)
            for i, slot in enumerate(time_slots):
                writer.writerow([slot] + grid[i])

    # Export for sections
    for section in sorted(all_sections):
        filename = f"section_{section}_timegrid.csv"
        grid = build_grid('section', section)
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Time Slot"] + days)
            for i, slot in enumerate(time_slots):
                writer.writerow([slot] + grid[i])

    # Export for rooms
    for room in sorted(all_rooms):
        filename = f"room_{room.replace(' ', '_')}_timegrid.csv"
        grid = build_grid('room', room)
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Time Slot"] + days)
            for i, slot in enumerate(time_slots):
                writer.writerow([slot] + grid[i])

    print("Timegrid CSV export completed!")

if __name__ == "__main__":
    print("Starting CSV export process...")
    
    # Export all CSV files
    export_section_csvs()
    export_room_csvs()
    export_employee_csvs()
    export_timegrid_csvs()
    
    # Print summary
    print_summary()
    
    print("\nExport completed successfully!") 