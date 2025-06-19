#!/usr/bin/env python3
"""
Sample Data for School Scheduling System
This file contains comprehensive sample data with:
- 10 sections (2A, 2B, 2C, 2D, 2E, 3A, 3B, 3C, 3D, 3E)
- 8 courses per section (total 80 courses)
- 20 employees assigned to various courses
- Mix of lab and lecture room requirements
- Various class durations
"""

import random

# Room code to RoomID mapping (from room.json)
ROOM_CODE_TO_ID = {
    'EB 301': 18,
    'EB 302': 19,
    'EB 303': 20,
    'EB 304': 21,
    'EB 305': 22,
    'EB 309': 26,
    'EB 310': 27,
    'EB 311': 28,
    'EB 204': 11,
    'EB 205': 12,
    'EB 206': 13,
    'EB 207': 14,
    'EB 208': 15,
    'EB 209': 16,
    'EB 210': 17,
    'EB 201': 8,
    'EB 202': 9,
    'EB 203': 10,
    'CL 1': 31,
    'CL 2': 32,
    'CL 3': 33,
    'CL 4': 34,
    'CL 5': 35,
    # Add more mappings as needed
}

def map_roomid(roomid):
    if isinstance(roomid, list):
        return [ROOM_CODE_TO_ID.get(r, r) for r in roomid]
    elif isinstance(roomid, str):
        # For demonstration, if a course is a lab, assign two roomids if possible
        rid = ROOM_CODE_TO_ID.get(roomid, roomid)
        # Pick a second roomid if available (e.g., next room in the mapping)
        roomids = list(ROOM_CODE_TO_ID.values())
        if rid in roomids:
            idx = roomids.index(rid)
            if idx + 1 < len(roomids):
                return [rid, roomids[idx + 1]]
        return [rid]
    else:
        return [roomid]

# Sample data with 10 sections, 8 courses each, 20 employees
sample_class_data = [
    # Section 2A - Computer Science Focus
    {
        'Courses': [
            {
                'courseid': 101,
                'coursename': 'IT 326 - IOT Applications',
                'section': '2A',
                'classschedule': [
                    {'duration': '2:00', 'roomid': [18, 19], 'employeeid': 201},
                    {'duration': '1:30', 'roomid': 26, 'employeeid': 201},
                ]
            },
            {
                'courseid': 102,
                'coursename': 'DB 325 - Database Management',
                'section': '2A',
                'classschedule': [
                    {'duration': '1:30', 'roomid': 19, 'employeeid': 202},  # Database Lab (EB 302)
                    {'duration': '1:00', 'roomid': 27, 'employeeid': 202},  # Database Theory (EB 310)
                ]
            },
            {
                'courseid': 103,
                'coursename': 'MA 324 - Mathematics',
                'section': '2A',
                'classschedule': [
                    {'duration': '2:30', 'roomid': 20, 'employeeid': 203},  # Mathematics (EB 303)
                ]
            },
            {
                'courseid': 104,
                'coursename': 'IT 323 - Web Development',
                'section': '2A',
                'classschedule': [
                    {'duration': '1:00', 'roomid': 21, 'employeeid': 204},  # Web Development Lab (EB 304)
                    {'duration': '1:00', 'roomid': 28, 'employeeid': 204},  # Web Development Theory (EB 311)
                ]
            },
            {
                'courseid': 105,
                'coursename': 'EN 322 - English',
                'section': '2A',
                'classschedule': [
                    {'duration': '1:30', 'roomid': 22, 'employeeid': 205},  # English (EB 305)
                ]
            },
            {
                'courseid': 106,
                'coursename': 'CN 321 - Networking',
                'section': '2A',
                'classschedule': [
                    {'duration': '1:00', 'roomid': [18, 19], 'employeeid': 206},  # Networking Lab (EB 301, EB 302)
                    {'duration': '1:30', 'roomid': 26, 'employeeid': 206},  # Networking Theory (EB 309)
                ]
            },
            {
                'courseid': 107,
                'coursename': 'PH 320 - Physics',
                'section': '2A',
                'classschedule': [
                    {'duration': '2:00', 'roomid': 20, 'employeeid': 207},  # Physics (EB 303)
                ]
            },
            {
                'courseid': 108,
                'coursename': 'SE 319 - Software Engineering',
                'section': '2A',
                'classschedule': [
                    {'duration': '1:30', 'roomid': 21, 'employeeid': 208},  # Software Engineering Lab (EB 304)
                    {'duration': '1:00', 'roomid': 28, 'employeeid': 208},  # Software Engineering Theory (EB 311)
                ]
            }
        ]
    },
    
    # Section 2B - Engineering Focus
    {
        'Courses': [
            {
                'courseid': 109,
                'coursename': 'CAD 318 - Computer-Aided Design',
                'section': '2B',
                'classschedule': [
                    {'duration': '2:00', 'roomid': 'EB 302', 'employeeid': 209},  # CAD Lab
                    {'duration': '1:00', 'roomid': 'EB 310', 'employeeid': 209},  # CAD Theory
                ]
            },
            {
                'courseid': 110,
                'coursename': 'MA 317 - Engineering Mathematics',
                'section': '2B',
                'classschedule': [
                    {'duration': '1:30', 'roomid': 'EB 303', 'employeeid': 210},  # Engineering Mathematics
                ]
            },
            {
                'courseid': 111,
                'coursename': 'EL 316 - Electronics',
                'section': '2B',
                'classschedule': [
                    {'duration': '2:30', 'roomid': 'EB 301', 'employeeid': 211},  # Electronics Lab
                    {'duration': '1:00', 'roomid': 'EB 309', 'employeeid': 211},  # Electronics Theory
                ]
            },
            {
                'courseid': 112,
                'coursename': 'EN 315 - Engineering Drawing',
                'section': '2B',
                'classschedule': [
                    {'duration': '1:00', 'roomid': 'EB 305', 'employeeid': 212},  # Engineering Drawing
                ]
            },
            {
                'courseid': 113,
                'coursename': 'ME 314 - Mechanics',
                'section': '2B',
                'classschedule': [
                    {'duration': '1:30', 'roomid': 'EB 304', 'employeeid': 213},  # Mechanics Lab
                    {'duration': '1:30', 'roomid': 'EB 311', 'employeeid': 213},  # Mechanics Theory
                ]
            },
            {
                'courseid': 114,
                'coursename': 'TH 313 - Thermodynamics',
                'section': '2B',
                'classschedule': [
                    {'duration': '2:00', 'roomid': 'EB 303', 'employeeid': 214},  # Thermodynamics
                ]
            },
            {
                'courseid': 115,
                'coursename': 'MS 312 - Materials Science',
                'section': '2B',
                'classschedule': [
                    {'duration': '1:00', 'roomid': 'EB 302', 'employeeid': 215},  # Materials Lab
                    {'duration': '1:00', 'roomid': 'EB 310', 'employeeid': 215},  # Materials Science
                ]
            },
            {
                'courseid': 116,
                'coursename': 'EN 311 - Engineering Ethics',
                'section': '2B',
                'classschedule': [
                    {'duration': '1:30', 'roomid': 'EB 305', 'employeeid': 216},  # Engineering Ethics
                ]
            }
        ]
    },
    
    # Section 2C - Business Focus
    {
        'Courses': [
            {
                'courseid': 117,
                'coursename': 'CA 310 - Computer Applications',
                'section': '2C',
                'classschedule': [
                    {'duration': '1:30', 'roomid': 'EB 301', 'employeeid': 217},  # Computer Applications Lab
                    {'duration': '1:00', 'roomid': 'EB 309', 'employeeid': 217},  # Computer Applications
                ]
            },
            {
                'courseid': 118,
                'coursename': 'BM 309 - Business Mathematics',
                'section': '2C',
                'classschedule': [
                    {'duration': '2:00', 'roomid': 'EB 303', 'employeeid': 218},  # Business Mathematics
                ]
            },
            {
                'courseid': 119,
                'coursename': 'BC 308 - Business Communication',
                'section': '2C',
                'classschedule': [
                    {'duration': '1:00', 'roomid': 'EB 305', 'employeeid': 219},  # Business Communication
                ]
            },
            {
                'courseid': 120,
                'coursename': 'AC 307 - Accounting',
                'section': '2C',
                'classschedule': [
                    {'duration': '1:30', 'roomid': 'EB 304', 'employeeid': 220},  # Accounting Lab
                    {'duration': '1:30', 'roomid': 'EB 311', 'employeeid': 220},  # Accounting Theory
                ]
            },
            {
                'courseid': 121,
                'coursename': 'EC 306 - Economics',
                'section': '2C',
                'classschedule': [
                    {'duration': '2:00', 'roomid': 'EB 302', 'employeeid': 201},  # Economics
                ]
            },
            {
                'courseid': 122,
                'coursename': 'MK 305 - Marketing',
                'section': '2C',
                'classschedule': [
                    {'duration': '1:00', 'roomid': 'EB 301', 'employeeid': 202},  # Marketing Lab
                    {'duration': '1:00', 'roomid': 'EB 309', 'employeeid': 202},  # Marketing Theory
                ]
            },
            {
                'courseid': 123,
                'coursename': 'BL 304 - Business Law',
                'section': '2C',
                'classschedule': [
                    {'duration': '1:30', 'roomid': 'EB 305', 'employeeid': 203},  # Business Law
                ]
            },
            {
                'courseid': 124,
                'coursename': 'FN 303 - Finance',
                'section': '2C',
                'classschedule': [
                    {'duration': '1:00', 'roomid': 'EB 304', 'employeeid': 204},  # Finance Lab
                    {'duration': '1:30', 'roomid': 'EB 311', 'employeeid': 204},  # Finance Theory
                ]
            }
        ]
    },
    
    # Section 2D - Science Focus
    {
        'Courses': [
            {
                'courseid': 125,
                'coursename': 'CH 302 - Chemistry',
                'section': '2D',
                'classschedule': [
                    {'duration': '2:00', 'roomid': 'EB 301', 'employeeid': 205},  # Chemistry Lab
                    {'duration': '1:00', 'roomid': 'EB 309', 'employeeid': 205},  # Chemistry Theory
                ]
            },
            {
                'courseid': 126,
                'coursename': 'BI 301 - Biology',
                'section': '2D',
                'classschedule': [
                    {'duration': '1:30', 'roomid': 'EB 302', 'employeeid': 206},  # Biology Lab
                    {'duration': '1:30', 'roomid': 'EB 310', 'employeeid': 206},  # Biology Theory
                ]
            },
            {
                'courseid': 127,
                'coursename': 'PH 200 - Physics Advanced',
                'section': '2D',
                'classschedule': [
                    {'duration': '2:30', 'roomid': 'EB 303', 'employeeid': 207},  # Physics Advanced
                ]
            },
            {
                'courseid': 128,
                'coursename': 'ES 201 - Environmental Science',
                'section': '2D',
                'classschedule': [
                    {'duration': '1:00', 'roomid': 'EB 301', 'employeeid': 208},  # Environmental Science Lab
                    {'duration': '1:00', 'roomid': 'EB 309', 'employeeid': 208},  # Environmental Science
                ]
            },
            {
                'courseid': 129,
                'coursename': 'MA 202 - Mathematics Advanced',
                'section': '2D',
                'classschedule': [
                    {'duration': '1:30', 'roomid': 'EB 303', 'employeeid': 209},  # Mathematics Advanced
                ]
            },
            {
                'courseid': 130,
                'coursename': 'GE 203 - Geology',
                'section': '2D',
                'classschedule': [
                    {'duration': '1:00', 'roomid': 'EB 301', 'employeeid': 210},  # Geology Lab
                    {'duration': '1:30', 'roomid': 'EB 309', 'employeeid': 210},  # Geology Theory
                ]
            },
            {
                'courseid': 131,
                'coursename': 'AS 204 - Astronomy',
                'section': '2D',
                'classschedule': [
                    {'duration': '2:00', 'roomid': 'EB 303', 'employeeid': 211},  # Astronomy
                ]
            },
            {
                'courseid': 132,
                'coursename': 'MB 205 - Microbiology',
                'section': '2D',
                'classschedule': [
                    {'duration': '1:30', 'roomid': 'EB 302', 'employeeid': 212},  # Microbiology Lab
                    {'duration': '1:00', 'roomid': 'EB 310', 'employeeid': 212},  # Microbiology Theory
                ]
            }
        ]
    },
    
    # Section 2E - Arts & Humanities Focus
    {
        'Courses': [
            {
                'courseid': 133,
                'coursename': 'AR 206 - Art Studio',
                'section': '2E',
                'classschedule': [
                    {'duration': '2:00', 'roomid': 'EB 304', 'employeeid': 213},  # Art Studio
                    {'duration': '1:00', 'roomid': 'EB 311', 'employeeid': 213},  # Art History
                ]
            },
            {
                'courseid': 134,
                'coursename': 'LI 207 - Literature',
                'section': '2E',
                'classschedule': [
                    {'duration': '1:30', 'roomid': 'EB 305', 'employeeid': 214},  # Literature
                ]
            },
            {
                'courseid': 135,
                'coursename': 'MU 208 - Music',
                'section': '2E',
                'classschedule': [
                    {'duration': '1:00', 'roomid': 'EB 301', 'employeeid': 215},  # Music Lab
                    {'duration': '1:30', 'roomid': 'EB 309', 'employeeid': 215},  # Music Theory
                ]
            },
            {
                'courseid': 136,
                'coursename': 'HI 209 - History',
                'section': '2E',
                'classschedule': [
                    {'duration': '2:00', 'roomid': 'EB 303', 'employeeid': 216},  # History
                ]
            },
            {
                'courseid': 137,
                'coursename': 'DR 210 - Drama',
                'section': '2E',
                'classschedule': [
                    {'duration': '1:30', 'roomid': 'EB 304', 'employeeid': 217},  # Drama Lab
                    {'duration': '1:00', 'roomid': 'EB 311', 'employeeid': 217},  # Drama Theory
                ]
            },
            {
                'courseid': 138,
                'coursename': 'PH 211 - Philosophy',
                'section': '2E',
                'classschedule': [
                    {'duration': '1:00', 'roomid': 'EB 305', 'employeeid': 218},  # Philosophy
                ]
            },
            {
                'courseid': 139,
                'coursename': 'PH 212 - Photography',
                'section': '2E',
                'classschedule': [
                    {'duration': '1:30', 'roomid': 'EB 304', 'employeeid': 219},  # Photography Lab
                    {'duration': '1:00', 'roomid': 'EB 311', 'employeeid': 219},  # Photography Theory
                ]
            },
            {
                'courseid': 140,
                'coursename': 'SO 213 - Sociology',
                'section': '2E',
                'classschedule': [
                    {'duration': '2:00', 'roomid': 'EB 305', 'employeeid': 220},  # Sociology
                ]
            }
        ]
    },
    
    # Section 3A - Advanced Computer Science
    {
        'Courses': [
            {
                'courseid': 141,
                'coursename': 'IT 402 - Advanced Programming',
                'section': '3A',
                'classschedule': [
                    {'duration': '2:30', 'roomid': 'EB 301', 'employeeid': 201},  # Advanced Programming Lab
                    {'duration': '1:30', 'roomid': 'EB 309', 'employeeid': 201},  # Advanced Programming Theory
                ]
            },
            {
                'courseid': 142,
                'coursename': 'DS 401 - Data Structures',
                'section': '3A',
                'classschedule': [
                    {'duration': '2:00', 'roomid': 'EB 302', 'employeeid': 202},  # Data Structures Lab
                    {'duration': '1:00', 'roomid': 'EB 310', 'employeeid': 202},  # Data Structures Theory
                ]
            },
            {
                'courseid': 143,
                'coursename': 'AL 400 - Algorithms',
                'section': '3A',
                'classschedule': [
                    {'duration': '1:30', 'roomid': 'EB 301', 'employeeid': 203},  # Algorithms Lab
                    {'duration': '1:30', 'roomid': 'EB 309', 'employeeid': 203},  # Algorithms Theory
                ]
            },
            {
                'courseid': 144,
                'coursename': 'CA 403 - Computer Architecture',
                'section': '3A',
                'classschedule': [
                    {'duration': '2:00', 'roomid': 'EB 303', 'employeeid': 204},  # Computer Architecture
                ]
            },
            {
                'courseid': 145,
                'coursename': 'OS 404 - Operating Systems',
                'section': '3A',
                'classschedule': [
                    {'duration': '1:00', 'roomid': 'EB 301', 'employeeid': 205},  # Operating Systems Lab
                    {'duration': '1:30', 'roomid': 'EB 309', 'employeeid': 205},  # Operating Systems Theory
                ]
            },
            {
                'courseid': 146,
                'coursename': 'CN 405 - Computer Networks',
                'section': '3A',
                'classschedule': [
                    {'duration': '1:30', 'roomid': 'EB 302', 'employeeid': 206},  # Computer Networks Lab
                    {'duration': '1:00', 'roomid': 'EB 310', 'employeeid': 206},  # Computer Networks Theory
                ]
            },
            {
                'courseid': 147,
                'coursename': 'DM 406 - Discrete Mathematics',
                'section': '3A',
                'classschedule': [
                    {'duration': '2:00', 'roomid': 'EB 303', 'employeeid': 207},  # Discrete Mathematics
                ]
            },
            {
                'courseid': 148,
                'coursename': 'ST 407 - Software Testing',
                'section': '3A',
                'classschedule': [
                    {'duration': '1:00', 'roomid': 'EB 301', 'employeeid': 208},  # Software Testing Lab
                    {'duration': '1:00', 'roomid': 'EB 309', 'employeeid': 208},  # Software Testing Theory
                ]
            }
        ]
    },
    
    # Section 3B - Advanced Engineering
    {
        'Courses': [
            {
                'courseid': 149,
                'coursename': 'ACAD 408 - Advanced CAD',
                'section': '3B',
                'classschedule': [
                    {'duration': '2:00', 'roomid': 'EB 302', 'employeeid': 209},  # Advanced CAD Lab
                    {'duration': '1:00', 'roomid': 'EB 310', 'employeeid': 209},  # Advanced CAD Theory
                ]
            },
            {
                'courseid': 150,
                'coursename': 'ROB 409 - Robotics',
                'section': '3B',
                'classschedule': [
                    {'duration': '1:30', 'roomid': 'EB 301', 'employeeid': 210},  # Robotics Lab
                    {'duration': '1:30', 'roomid': 'EB 309', 'employeeid': 210},  # Robotics Theory
                ]
            },
            {
                'courseid': 151,
                'coursename': 'AE 410 - Advanced Electronics',
                'section': '3B',
                'classschedule': [
                    {'duration': '2:30', 'roomid': 'EB 303', 'employeeid': 211},  # Advanced Electronics
                ]
            },
            {
                'courseid': 152,
                'coursename': 'CS 411 - Control Systems',
                'section': '3B',
                'classschedule': [
                    {'duration': '1:00', 'roomid': 'EB 301', 'employeeid': 212},  # Control Systems Lab
                    {'duration': '1:00', 'roomid': 'EB 309', 'employeeid': 212},  # Control Systems Theory
                ]
            },
            {
                'courseid': 153,
                'coursename': 'FM 412 - Fluid Mechanics',
                'section': '3B',
                'classschedule': [
                    {'duration': '1:30', 'roomid': 'EB 302', 'employeeid': 213},  # Fluid Mechanics Lab
                    {'duration': '1:30', 'roomid': 'EB 310', 'employeeid': 213},  # Fluid Mechanics Theory
                ]
            },
            {
                'courseid': 154,
                'coursename': 'AT 413 - Advanced Thermodynamics',
                'section': '3B',
                'classschedule': [
                    {'duration': '2:00', 'roomid': 'EB 303', 'employeeid': 214},  # Advanced Thermodynamics
                ]
            },
            {
                'courseid': 155,
                'coursename': 'MT 414 - Manufacturing',
                'section': '3B',
                'classschedule': [
                    {'duration': '1:00', 'roomid': 'EB 301', 'employeeid': 215},  # Manufacturing Lab
                    {'duration': '1:30', 'roomid': 'EB 309', 'employeeid': 215},  # Manufacturing Theory
                ]
            },
            {
                'courseid': 156,
                'coursename': 'EM 415 - Engineering Management',
                'section': '3B',
                'classschedule': [
                    {'duration': '1:30', 'roomid': 'EB 302', 'employeeid': 216},  # Engineering Management
                ]
            }
        ]
    },
    
    # Section 3C - Advanced Business
    {
        'Courses': [
            {
                'courseid': 157,
                'coursename': 'AXL 416 - Advanced Excel',
                'section': '3C',
                'classschedule': [
                    {'duration': '1:30', 'roomid': 'EB 301', 'employeeid': 217},  # Advanced Excel Lab
                    {'duration': '1:00', 'roomid': 'EB 309', 'employeeid': 217},  # Advanced Excel Theory
                ]
            },
            {
                'courseid': 158,
                'coursename': 'BS 417 - Business Statistics',
                'section': '3C',
                'classschedule': [
                    {'duration': '2:00', 'roomid': 'EB 303', 'employeeid': 218},  # Business Statistics
                ]
            },
            {
                'courseid': 159,
                'coursename': 'BA 418 - Business Analytics',
                'section': '3C',
                'classschedule': [
                    {'duration': '1:00', 'roomid': 'EB 301', 'employeeid': 219},  # Business Analytics Lab
                    {'duration': '1:30', 'roomid': 'EB 309', 'employeeid': 219},  # Business Analytics Theory
                ]
            },
            {
                'courseid': 160,
                'coursename': 'AAC 419 - Advanced Accounting',
                'section': '3C',
                'classschedule': [
                    {'duration': '1:30', 'roomid': 'EB 302', 'employeeid': 220},  # Advanced Accounting Lab
                    {'duration': '1:00', 'roomid': 'EB 310', 'employeeid': 220},  # Advanced Accounting Theory
                ]
            },
            {
                'courseid': 161,
                'coursename': 'IB 420 - International Business',
                'section': '3C',
                'classschedule': [
                    {'duration': '2:00', 'roomid': 'EB 303', 'employeeid': 201},  # International Business
                ]
            },
            {
                'courseid': 162,
                'coursename': 'DMK 421 - Digital Marketing',
                'section': '3C',
                'classschedule': [
                    {'duration': '1:00', 'roomid': 'EB 301', 'employeeid': 202},  # Digital Marketing Lab
                    {'duration': '1:00', 'roomid': 'EB 309', 'employeeid': 202},  # Digital Marketing Theory
                ]
            },
            {
                'courseid': 163,
                'coursename': 'BS 422 - Business Strategy',
                'section': '3C',
                'classschedule': [
                    {'duration': '1:30', 'roomid': 'EB 302', 'employeeid': 203},  # Business Strategy
                ]
            },
            {
                'courseid': 164,
                'coursename': 'FM 423 - Financial Modeling',
                'section': '3C',
                'classschedule': [
                    {'duration': '1:00', 'roomid': 'EB 301', 'employeeid': 204},  # Financial Modeling Lab
                    {'duration': '1:30', 'roomid': 'EB 309', 'employeeid': 204},  # Financial Modeling Theory
                ]
            }
        ]
    },
    
    # Section 3D - Advanced Science
    {
        'Courses': [
            {
                'courseid': 165,
                'coursename': 'ACH 424 - Advanced Chemistry',
                'section': '3D',
                'classschedule': [
                    {'duration': '2:00', 'roomid': 'EB 301', 'employeeid': 205},  # Advanced Chemistry Lab
                    {'duration': '1:00', 'roomid': 'EB 309', 'employeeid': 205},  # Advanced Chemistry Theory
                ]
            },
            {
                'courseid': 166,
                'coursename': 'MB 425 - Molecular Biology',
                'section': '3D',
                'classschedule': [
                    {'duration': '1:30', 'roomid': 'EB 302', 'employeeid': 206},  # Molecular Biology Lab
                    {'duration': '1:30', 'roomid': 'EB 310', 'employeeid': 206},  # Molecular Biology Theory
                ]
            },
            {
                'courseid': 167,
                'coursename': 'QP 426 - Quantum Physics',
                'section': '3D',
                'classschedule': [
                    {'duration': '2:30', 'roomid': 'EB 303', 'employeeid': 207},  # Quantum Physics
                ]
            },
            {
                'courseid': 168,
                'coursename': 'CS 427 - Climate Science',
                'section': '3D',
                'classschedule': [
                    {'duration': '1:00', 'roomid': 'EB 301', 'employeeid': 208},  # Climate Science Lab
                    {'duration': '1:00', 'roomid': 'EB 309', 'employeeid': 208},  # Climate Science Theory
                ]
            },
            {
                'courseid': 169,
                'coursename': 'AC 428 - Advanced Calculus',
                'section': '3D',
                'classschedule': [
                    {'duration': '1:30', 'roomid': 'EB 303', 'employeeid': 209},  # Advanced Calculus
                ]
            },
            {
                'courseid': 170,
                'coursename': 'SE 429 - Seismology',
                'section': '3D',
                'classschedule': [
                    {'duration': '1:00', 'roomid': 'EB 301', 'employeeid': 210},  # Seismology Lab
                    {'duration': '1:30', 'roomid': 'EB 309', 'employeeid': 210},  # Seismology Theory
                ]
            },
            {
                'courseid': 171,
                'coursename': 'AS 430 - Astrophysics',
                'section': '3D',
                'classschedule': [
                    {'duration': '2:00', 'roomid': 'EB 303', 'employeeid': 211},  # Astrophysics
                ]
            },
            {
                'courseid': 172,
                'coursename': 'GN 431 - Genetics',
                'section': '3D',
                'classschedule': [
                    {'duration': '1:30', 'roomid': 'EB 301', 'employeeid': 212},  # Genetics Lab
                    {'duration': '1:00', 'roomid': 'EB 309', 'employeeid': 212},  # Genetics Theory
                ]
            }
        ]
    },
    
    # Section 3E - Advanced Arts & Humanities
    {
        'Courses': [
            {
                'courseid': 173,
                'coursename': 'AR 432 - Art Criticism',
                'section': '3E',
                'classschedule': [
                    {'duration': '2:00', 'roomid': 'EB 302', 'employeeid': 213},  # Advanced Art Studio
                    {'duration': '1:00', 'roomid': 'EB 309', 'employeeid': 213},  # Art Criticism
                ]
            },
            {
                'courseid': 174,
                'coursename': 'CW 433 - Creative Writing',
                'section': '3E',
                'classschedule': [
                    {'duration': '1:30', 'roomid': 'EB 301', 'employeeid': 214},  # Creative Writing
                ]
            },
            {
                'courseid': 175,
                'coursename': 'MU 434 - Music Composition',
                'section': '3E',
                'classschedule': [
                    {'duration': '1:00', 'roomid': 'EB 302', 'employeeid': 215},  # Advanced Music Lab
                    {'duration': '1:30', 'roomid': 'EB 310', 'employeeid': 215},  # Music Composition
                ]
            },
            {
                'courseid': 176,
                'coursename': 'WH 435 - World History',
                'section': '3E',
                'classschedule': [
                    {'duration': '2:00', 'roomid': 'EB 303', 'employeeid': 216},  # World History
                ]
            },
            {
                'courseid': 177,
                'coursename': 'DR 436 - Theater Production',
                'section': '3E',
                'classschedule': [
                    {'duration': '1:30', 'roomid': 'EB 302', 'employeeid': 217},  # Advanced Drama Lab
                    {'duration': '1:00', 'roomid': 'EB 309', 'employeeid': 217},  # Theater Production
                ]
            },
            {
                'courseid': 178,
                'coursename': 'ETH 437 - Ethics',
                'section': '3E',
                'classschedule': [
                    {'duration': '1:00', 'roomid': 'EB 301', 'employeeid': 218},  # Ethics
                ]
            },
            {
                'courseid': 179,
                'coursename': 'DP 438 - Photography Techniques',
                'section': '3E',
                'classschedule': [
                    {'duration': '1:30', 'roomid': 'EB 302', 'employeeid': 219},  # Digital Photography Lab
                    {'duration': '1:00', 'roomid': 'EB 309', 'employeeid': 219},  # Photography Techniques
                ]
            },
            {
                'courseid': 180,
                'coursename': 'CA 439 - Cultural Anthropology',
                'section': '3E',
                'classschedule': [
                    {'duration': '2:00', 'roomid': 'EB 301', 'employeeid': 220},  # Cultural Anthropology
                ]
            }
        ]
    }
]

# Employee information for reference
employee_info = {
    201: "Dr. Smith - Computer Science",
    202: "Prof. Johnson - Database Systems",
    203: "Dr. Williams - Mathematics",
    204: "Prof. Brown - Web Development",
    205: "Dr. Davis - English",
    206: "Prof. Miller - Networking",
    207: "Dr. Wilson - Physics",
    208: "Prof. Moore - Software Engineering",
    209: "Dr. Taylor - CAD/Engineering",
    210: "Prof. Anderson - Engineering Math",
    211: "Dr. Thomas - Electronics",
    212: "Prof. Jackson - Engineering Drawing",
    213: "Dr. White - Mechanics",
    214: "Prof. Harris - Thermodynamics",
    215: "Dr. Martin - Materials Science",
    216: "Prof. Garcia - Engineering Ethics",
    217: "Dr. Rodriguez - Computer Applications",
    218: "Prof. Lewis - Business Math",
    219: "Prof. Lee - Business Communication",
    220: "Prof. Walker - Accounting"
}

# Course categories for reference
course_categories = {
    "Computer Science": [101, 102, 104, 106, 108, 141, 142, 143, 144, 145, 146, 147, 148],
    "Engineering": [109, 111, 113, 115, 149, 150, 151, 152, 153, 154, 155, 156],
    "Business": [117, 118, 119, 120, 121, 122, 123, 124, 157, 158, 159, 160, 161, 162, 163, 164],
    "Science": [125, 126, 127, 128, 129, 130, 131, 132, 165, 166, 167, 168, 169, 170, 171, 172],
    "Arts & Humanities": [133, 134, 135, 136, 137, 138, 139, 140, 173, 174, 175, 176, 177, 178, 179, 180]
}

rooms = [
    {"RoomID": 11, "RoomType": 2, "Floor": 2, "RoomName": "Computer Engineering Lab 1"},
    {"RoomID": 170, "RoomType": 4, "Floor": 1, "RoomName": "Automotive Lab"},
    {"RoomID": 231, "RoomType": 3, "Floor": 1, "RoomName": "Hydraulic Engineering Lab"},
    {"RoomID": 267, "RoomType": 5, "Floor": 1, "RoomName": "Mechanical Shop Room"},
    {"RoomID": 16, "RoomType": 6, "Floor": 2, "RoomName": "ITE Laboratory 4"},
    {"RoomID": 18, "RoomType": 1, "Floor": 3, "RoomName": "CEIT Room 301"}
]

roomid_to_type = {r['RoomID']: r['RoomType'] for r in rooms}
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

def assign_roomid_and_day(classschedule):
    for entry in classschedule:
        # Ensure roomtype is present
        if 'roomtype' not in entry:
            if 'roomid' in entry:
                entry['roomtype'] = roomid_to_type.get(entry['roomid'], 1)
            else:
                entry['roomtype'] = 1
        # Assign roomid as a list of all possible rooms of the correct type
        possible_rooms = [r['RoomID'] for r in rooms if r['RoomType'] == entry['roomtype']]
        entry['roomid'] = possible_rooms
        # Assign random day
        entry['day'] = random.choice(days)
    return classschedule

# Ensure every entry has roomtype (if roomid is present), or default to 1
for section in sample_class_data:
    for course in section['Courses']:
        for entry in course['classschedule']:
            if 'roomtype' not in entry:
                if 'roomid' in entry:
                    entry['roomtype'] = roomid_to_type.get(entry['roomid'], 1)
                else:
                    entry['roomtype'] = 1

# Now assign roomid and day (roomtype will always be present)
for section in sample_class_data:
    for course in section['Courses']:
        course['classschedule'] = assign_roomid_and_day(course['classschedule'])

# After defining sample_class_data and roomid_to_type
for section in sample_class_data:
    for course in section['Courses']:
        for entry in course['classschedule']:
            entry['roomtype'] = roomid_to_type[entry['roomid'][0]] if isinstance(entry['roomid'], list) else roomid_to_type[entry['roomid']]

# --- BEGIN PATCH: Make all roomid fields arrays in the raw sample_class_data ---
room_type_map = {r['RoomID']: r['RoomType'] for r in rooms}
room_type_to_rooms = {1: [r['RoomID'] for r in rooms if r['RoomType'] == 1], 2: [r['RoomID'] for r in rooms if r['RoomType'] == 2]}
for section in sample_class_data:
    for course in section['Courses']:
        for entry in course['classschedule']:
            # If roomid is a string, convert to array of all rooms of that type
            if isinstance(entry['roomid'], str):
                rtype = room_type_map.get(entry['roomid'], 1)
                entry['roomid'] = room_type_to_rooms[rtype]
# --- END PATCH ---

# --- PATCH: Update all classschedule entries to use RoomID(s) ---
for section in sample_class_data:
    for course in section['Courses']:
        for entry in course['classschedule']:
            entry['roomid'] = map_roomid(entry['roomid'])
# --- END PATCH ---

def print_sample_data_summary():
    """Print a summary of the sample data"""
    print("="*80)
    print("SAMPLE DATA SUMMARY")
    print("="*80)
    
    total_courses = sum(len(section['Courses']) for section in sample_class_data)
    total_sections = len(sample_class_data)
    total_employees = len(employee_info)
    
    print(f"Total Sections: {total_sections}")
    print(f"Total Courses: {total_courses}")
    print(f"Total Employees: {total_employees}")
    
    print(f"\nSections:")
    for i, section in enumerate(sample_class_data, 1):
        section_name = section['Courses'][0]['section']
        course_count = len(section['Courses'])
        print(f"  {i}. Section {section_name}: {course_count} courses")
    
    print(f"\nEmployees:")
    for emp_id, name in employee_info.items():
        print(f"  {emp_id}: {name}")
    
    print(f"\nCourse Categories:")
    for category, courses in course_categories.items():
        print(f"  {category}: {len(courses)} courses")
    
    print("="*80)

if __name__ == "__main__":
    print_sample_data_summary() 