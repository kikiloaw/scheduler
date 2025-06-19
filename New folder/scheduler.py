import json
from datetime import datetime, timedelta
from typing import List, Dict, Set, Tuple
import random

class SchoolScheduler:
    def __init__(self):
        self.rooms = {
            1: {"type": "lab", "capacity": 30, "available": True},
            2: {"type": "lecture", "capacity": 50, "available": True}
        }
        self.employees = {}  # Will store employee schedules
        self.sections = {}   # Will store section schedules
        self.room_schedules = {}  # Will store room schedules
        self.schedule = []
        
    def parse_duration(self, duration_str: str) -> int:
        """Convert duration string (e.g., '1:30') to minutes"""
        if ':' in duration_str:
            hours, minutes = map(int, duration_str.split(':'))
            return hours * 60 + minutes
        else:
            return int(duration_str) * 60
    
    def format_time(self, minutes: int) -> str:
        """Convert minutes to time string (e.g., '09:30')"""
        hours = minutes // 60
        mins = minutes % 60
        return f"{hours:02d}:{mins:02d}"
    
    def is_time_conflict(self, start1: int, duration1: int, start2: int, duration2: int) -> bool:
        """Check if two time slots conflict"""
        end1 = start1 + duration1
        end2 = start2 + duration2
        return not (end1 <= start2 or end2 <= start1)
    
    def find_available_slot(self, duration: int, section: str, employee_id: int, room_type: int) -> Tuple[int, int]:
        """Find an available time slot for a class"""
        # School hours: 8:00 AM to 5:00 PM (9 hours = 540 minutes)
        school_start = 8 * 60  # 8:00 AM
        school_end = 17 * 60   # 5:00 PM
        
        # Try each 30-minute slot
        for start_time in range(school_start, school_end - duration, 30):
            end_time = start_time + duration
            
            # Check if this slot conflicts with section schedule
            section_conflict = False
            if section in self.sections:
                for existing_class in self.sections[section]:
                    if self.is_time_conflict(start_time, duration, 
                                           existing_class['start_time'], existing_class['duration']):
                        section_conflict = True
                        break
            
            if section_conflict:
                continue
            
            # Check if this slot conflicts with employee schedule
            employee_conflict = False
            if employee_id in self.employees:
                for existing_class in self.employees[employee_id]:
                    if self.is_time_conflict(start_time, duration, 
                                           existing_class['start_time'], existing_class['duration']):
                        employee_conflict = True
                        break
            
            if employee_conflict:
                continue
            
            # Check if this slot conflicts with room schedule
            room_conflict = False
            if room_type in self.room_schedules:
                for existing_class in self.room_schedules[room_type]:
                    if self.is_time_conflict(start_time, duration, 
                                           existing_class['start_time'], existing_class['duration']):
                        room_conflict = True
                        break
            
            if room_conflict:
                continue
            
            # If no conflicts, this slot is available
            return start_time, end_time
        
        # If no slot found, return None
        return None, None
    
    def schedule_class(self, course_id: int, section: str, duration: int, 
                      room_type: int, employee_id: int) -> Dict:
        """Schedule a single class"""
        start_time, end_time = self.find_available_slot(duration, section, employee_id, room_type)
        
        if start_time is None:
            return None  # No available slot found
        
        class_info = {
            'course_id': course_id,
            'section': section,
            'start_time': start_time,
            'end_time': end_time,
            'duration': duration,
            'room_type': room_type,
            'employee_id': employee_id,
            'start_time_str': self.format_time(start_time),
            'end_time_str': self.format_time(end_time)
        }
        
        # Update schedules
        if section not in self.sections:
            self.sections[section] = []
        self.sections[section].append(class_info)
        
        if employee_id not in self.employees:
            self.employees[employee_id] = []
        self.employees[employee_id].append(class_info)
        
        if room_type not in self.room_schedules:
            self.room_schedules[room_type] = []
        self.room_schedules[room_type].append(class_info)
        
        self.schedule.append(class_info)
        return class_info
    
    def generate_schedule(self, class_data: List[Dict]) -> List[Dict]:
        """Generate complete schedule from class data"""
        self.schedule = []
        self.sections = {}
        self.employees = {}
        self.room_schedules = {}
        
        # Sort classes by duration (longer classes first) to optimize scheduling
        all_classes = []
        for class_group in class_data:
            for course in class_group['Courses']:
                for schedule_item in course['classschedule']:
                    all_classes.append({
                        'course_id': course['courseid'],
                        'section': course['section'],
                        'duration': self.parse_duration(schedule_item['duration']),
                        'room_type': schedule_item['roomtype'],
                        'employee_id': schedule_item['employeeid']
                    })
        
        # Sort by duration (descending) to schedule longer classes first
        all_classes.sort(key=lambda x: x['duration'], reverse=True)
        
        # Schedule each class
        for class_info in all_classes:
            scheduled = self.schedule_class(
                class_info['course_id'],
                class_info['section'],
                class_info['duration'],
                class_info['room_type'],
                class_info['employee_id']
            )
            
            if scheduled is None:
                print(f"Warning: Could not schedule course {class_info['course_id']} "
                      f"for section {class_info['section']}")
        
        return self.schedule
    
    def print_schedule(self):
        """Print the generated schedule in a readable format"""
        if not self.schedule:
            print("No schedule generated.")
            return
        
        print("\n" + "="*80)
        print("GENERATED SCHOOL SCHEDULE")
        print("="*80)
        
        # Group by section
        sections = {}
        for class_info in self.schedule:
            section = class_info['section']
            if section not in sections:
                sections[section] = []
            sections[section].append(class_info)
        
        for section in sorted(sections.keys()):
            print(f"\nSection: {section}")
            print("-" * 50)
            
            # Sort by start time
            section_classes = sorted(sections[section], key=lambda x: x['start_time'])
            
            for class_info in section_classes:
                room_type_name = "Lab" if class_info['room_type'] == 1 else "Lecture"
                print(f"  {class_info['start_time_str']} - {class_info['end_time_str']} | "
                      f"Course {class_info['course_id']} | "
                      f"{room_type_name} Room | "
                      f"Employee {class_info['employee_id']}")
        
        # Print room utilization
        print(f"\n" + "="*80)
        print("ROOM UTILIZATION")
        print("="*80)
        
        for room_type in sorted(self.room_schedules.keys()):
            room_name = "Lab" if room_type == 1 else "Lecture"
            classes = sorted(self.room_schedules[room_type], key=lambda x: x['start_time'])
            print(f"\n{room_name} Room Schedule:")
            for class_info in classes:
                print(f"  {class_info['start_time_str']} - {class_info['end_time_str']} | "
                      f"Course {class_info['course_id']} | "
                      f"Section {class_info['section']} | "
                      f"Employee {class_info['employee_id']}")
        
        # Print employee schedules
        print(f"\n" + "="*80)
        print("EMPLOYEE SCHEDULES")
        print("="*80)
        
        for employee_id in sorted(self.employees.keys()):
            classes = sorted(self.employees[employee_id], key=lambda x: x['start_time'])
            print(f"\nEmployee {employee_id} Schedule:")
            for class_info in classes:
                room_type_name = "Lab" if class_info['room_type'] == 1 else "Lecture"
                print(f"  {class_info['start_time_str']} - {class_info['end_time_str']} | "
                      f"Course {class_info['course_id']} | "
                      f"Section {class_info['section']} | "
                      f"{room_type_name} Room")
    
    def export_schedule(self, filename: str = "schedule.json"):
        """Export schedule to JSON file"""
        with open(filename, 'w') as f:
            json.dump(self.schedule, f, indent=2)
        print(f"\nSchedule exported to {filename}")

def main():
    # Your class data
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
                },
                {
                    'courseid': 2,
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
                    'courseid': 3,
                    'section': '2B',
                    'classschedule': [
                        {'duration': '1:00', 'roomtype': 1, 'employeeid': 120},
                        {'duration': '2:00', 'roomtype': 2, 'employeeid': 120},
                    ]
                },
                {
                    'courseid': 4,
                    'section': '2B',
                    'classschedule': [
                        {'duration': '1:00', 'roomtype': 1, 'employeeid': 120},
                    ]
                }
            ]
        }
    ]
    
    # Create scheduler and generate schedule
    scheduler = SchoolScheduler()
    schedule = scheduler.generate_schedule(class_data)
    
    # Print the schedule
    scheduler.print_schedule()
    
    # Export to JSON
    scheduler.export_schedule()
    
    return schedule

if __name__ == "__main__":
    main() 