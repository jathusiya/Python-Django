# your_app/management/commands/extract_data.py
import csv
import os
# import pandas as pd
from django.core.management.base import BaseCommand
from award.models import School,Subject,Answer,Assessment,Award,Summary,Classes,Student

class Command(BaseCommand):
    help = 'Extract data from CSV and update School model'

    def handle(self, *args, **options):
        csv_file_path = 'interview.csv'  # Replace with the actual path to your CSV file

        if not os.path.exists(csv_file_path):
            self.stdout.write(self.style.ERROR('CSV file does not exist'))
            return

        with open(csv_file_path, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            
            record_count = 0  # Initialize a counter to keep track of the number of records processed
            max_records = 100  # Define the maximum number of records to process

            for row in csv_reader:
                if record_count >= max_records:
                    break 

                name = row['School_Name']
                subject = row['Subject']
                subject_score = row['student_total_assessed']
                fullname = row['First name']
                assessment_name=row['Assessment Areas']
                answer =row['Answers']
                award =row['award']
                classes=row['Class']
                student_score=row['student_score']
                studentIc=['Student_ID']
                sydney_participant=row['sydney_participants'],
                sydney_percentile=row['sydney_percentile'],
                correct_answer=row['Correct Answers'],  # You should add this field to your CSV and map it
                correct_answer_percentage_per_class=row['correct_answer_percentage_per_class'],
                participant=row['participant'],
                year_level_name=row['Year Level'],
                # Add more fields as needed
                
                subject = str(subject)
                subject_score = str(subject_score)
                student_score = str(student_score)
                studentIc = str(studentIc)
                sydney_percentile=str(sydney_percentile),
                correct_answer_percentage_per_class=str(correct_answer_percentage_per_class)
            
                
                
                

                # Create or update the School model
                school, created = School.objects.get_or_create(name=name)
                school.save()
                
                # Create or update the Subject model
                subject, created = Subject.objects.get_or_create(subject=subject,subject_score=subject_score)
                subject.save()
                
                # Create or update the Student model
                student, created = Student.objects.get_or_create(fullname=fullname)
                student.save()
                
                # Create or update the Awards model
                award, created = Award.objects.get_or_create(award=award)
                award.save()
                
                # Create or update the Answer model
                answer, created = Answer.objects.get_or_create(answer=answer)
                answer.save()
                
                # Create or update the classes model
                classes, created = Classes.objects.get_or_create(classes=classes)
                classes.save()
                
                 # Create or update the assessment model
                assessment, created = Assessment.objects.get_or_create(assessment_name=assessment_name)
                assessment.save()
                
                #   # Create or update the summary model
                # summary, created = Summary.objects.get_or_create(subject=subject, school_name=name, classes=classes, award=award, assessment_name=assessment_name, answer=answer, year_level_name=year_level_name, participant=participant, correct_answer_percentage_per_class=correct_answer_percentage_per_class, correct_answer=correct_answer, sydney_percentile=sydney_percentile, student_score=student_score, studentIc=studentIc, sydney_participant=sydney_participant,)
                # summary.save()
                
                record_count += 1


                self.stdout.write(self.style.SUCCESS(f'Successfully updated '))