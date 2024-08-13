package Catalog;

import java.util.Map;
import java.util.List;
import java.util.Scanner;

public class Main {

	private static Catalog catalog = new Catalog();

	private static void createSampleData() {
		Subject math = new Subject("Matematica");
		Subject ap = new Subject("Programare avansata");
		Subject english = new Subject("Engleza");
		Subject oop = new Subject("Programare orientata obiect");

		Teacher p1 = new Teacher("prof. dr. Dragomirescu Damian");
		p1.addSubjectTaught(math);
		p1.addSubjectTaught(oop);

		Teacher p2 = new Teacher("prof. conf. Stanescu Stefan");
		p2.addSubjectTaught(english);

		Student s1 = new Student("Alex Andrei", 0, LearningType.DE); // Enum
		s1.addSubject(oop);
		s1.addGrade(oop, 9.5);

		Student s2 = new Student("Robert Cristian", 0, LearningType.FT);
		s2.addSubject(english);
		s2.addGrade(english, 8.0);

		Student s3 = new Student("Alexandra Sandra", 0, LearningType.FT);
		s3.addSubject(math);
		s3.addSubject(english);
		s3.addGrade(math, 7.5);
		s3.addGrade(english, 9.0);

		catalog.addSubject(math);
		catalog.addSubject(ap);
		catalog.addSubject(english);
		catalog.addSubject(oop);

		catalog.addTeacher(p1);
		catalog.addTeacher(p2);

		catalog.addStudent(s1);
		catalog.addStudent(s2);
		catalog.addStudent(s3);

		catalog.assignSubjectsToTeachers();
	}

	public static void main(String[] args) {
		createSampleData();

		Scanner scanner = new Scanner(System.in);
		int choice = 0;

		while (choice != 9) {
			System.out.println("Select an option: \n");
			System.out.println("1. Display all students");
			System.out.println("2. Display all teachers");
			System.out.println("3. Display all subjects");
			System.out.println("4. Display subjects for a student");
			System.out.println("5. Add a new student");
			System.out.println("6. Add a new subject");
			System.out.println("7. Add a new teacher");
			System.out.println("8. View grades for a specific student");
			System.out.println("9. Assign grade to a student");
			System.out.println("0. Exit \n");

			choice = scanner.nextInt();
			scanner.nextLine();

			switch (choice) {
			case 1:
				List<Student> students = catalog.getStudents();
				System.out.println("List of all students:");
				for (Student student : students) {
					System.out.println(student.getName() + " - " + student.getLearningType());
				}

				AuditLog.writeAuditLog("Displayed all students");

				break;
			case 2:
				List<Teacher> teachers = catalog.getTeachers();
				System.out.println("List of all teachers: \n");
				for (Teacher teacher : teachers) {
					System.out.print(teacher.getName() + " teaches: \n");
					List<Subject> taughtSubjects = teacher.getTaughtSubjects();
					if (taughtSubjects == null || taughtSubjects.isEmpty()) {
						System.out.println("none");
					} else {
						for (Subject subject : taughtSubjects) {
							System.out.print(subject.getName() + " ");
						}
						System.out.println();
					}
				}

				AuditLog.writeAuditLog("Displayed all teachers");

				break;

			case 3:
				List<Subject> subjects = catalog.getSubjects();
				System.out.println("List of all subjects:");
				for (Subject subject : subjects) {
					System.out.println(subject.getName());
				}

				AuditLog.writeAuditLog("Displayed all subjects");

				break;

			case 4:
				System.out.println("Enter the name of the student:");
				String studentName = scanner.nextLine();
				Student student = catalog.findStudent(studentName);
				if (student == null) {
					System.out.println("Student not found");
				} else {
					Map<String, Subject> studentSubjects = student.getSubjects();
					System.out.println(student.getName() + " is taking the following subjects:");
					for (Map.Entry<String, Subject> entry : studentSubjects.entrySet()) {
						System.out.println(entry.getKey());
					}
				}

				AuditLog.writeAuditLog("Displayed subjects for student: " + studentName);

				break;

			case 5:
				// Case 5: Add a new student
				System.out.println("Enter student name: ");
				String studentName1 = scanner.nextLine();

				Student student1 = catalog.findStudent(studentName1);
				if (student1 == null) {
					System.out.println("Enter student learning type (DE/FT): ");
					String learningTypeStr = scanner.nextLine();
					LearningType learningType = LearningType.valueOf(learningTypeStr.toUpperCase());
					student1 = new Student(studentName1, 0, learningType);
				}

				String subjectName = "";
				while (true) {
					System.out.println("Enter subject(s) name (type 'done' when desired): ");
					subjectName = scanner.nextLine();
					if (subjectName.equalsIgnoreCase("done")) {
						break;
					}
					Subject subject = catalog.findSubject(subjectName);
					if (subject == null) {
						System.out.println("Subject not found.");
						continue;
					}
					student1.addSubject(subject);
				}

				catalog.addStudent(student1);
				System.out.println("Subjects added successfully.");
				AuditLog.writeAuditLog("New student added: " + student1.getName());
				break;

			case 6:
				// Case 6: Add a new subject
				System.out.println("Enter subject name: ");
				String subjectName2 = scanner.nextLine();

				Subject subject2 = catalog.findSubject(subjectName2);
				if (subject2 == null) {
					subject2 = new Subject(subjectName2);
				} else {
					System.out.println("Subject already exists.");
					break;
				}

				System.out.println("Enter teacher name for the subject: ");
				String teacherName = scanner.nextLine();
				Teacher teacher = catalog.findTeacher(teacherName);
				if (teacher == null) {
					teacher = new Teacher(teacherName);
					catalog.addTeacher(teacher);
				}

				subject2.assignTeacher(teacher);
				catalog.addSubject(subject2);

				System.out.println("Subject added successfully.");
				AuditLog.writeAuditLog("New subject added: " + subject2.getName());
				break;

			case 7:
				System.out.println("Enter teacher name: ");
				String teacherName2 = scanner.nextLine();

				Teacher teacher2 = catalog.findTeacher(teacherName2);
				if (teacher2 == null) {
					teacher2 = new Teacher(teacherName2);
					catalog.addTeacher(teacher2);
				} else {
					System.out.println("Teacher already exists.");
					break;
				}

				System.out.println("Enter subject name for the teacher: ");
				String subjectName3 = scanner.nextLine();
				Subject subject3 = catalog.findSubject(subjectName3);
				if (subject3 == null) {
					subject3 = new Subject(subjectName3);
					catalog.addSubject(subject3);
				}

				teacher2.assignSubject(subject3);

				System.out.println("Teacher added successfully.");
				AuditLog.writeAuditLog("New teacher added: " + teacher2.getName());
				break;

			case 8:
				System.out.println("Enter student name: ");
				String studentName2 = scanner.nextLine();

				Student student2 = catalog.findStudent(studentName2);
				if (student2 == null) {
					System.out.println("Student not found");
				} else {
					System.out.println("Grades for " + student2.getName() + ":");
					Map<Subject, Double> grades = student2.getGrades();
					for (Map.Entry<Subject, Double> entry : grades.entrySet()) {
						System.out.println(entry.getKey().getName() + ": " + entry.getValue());
					}
				}
				break;

			case 9:
				boolean isAddingGrades = true;

				while (isAddingGrades) {
					System.out.println("Enter student name (or 'done' to go back): ");
					String studentName9 = scanner.nextLine();

					if (studentName9.equalsIgnoreCase("done")) {
						System.out.println("Going back to the main menu...(press 1)");
						isAddingGrades = false;
						choice = scanner.nextInt();

						break;
					}

					Student student9 = catalog.findStudent(studentName9);
					if (student9 == null) {
						System.out.println("Student not found.");
						continue;
					}

					boolean isAddingSubjectGrade = true;

					while (isAddingSubjectGrade) {
						System.out.println("Enter subject name (or 'done' to go back): ");
						String subjectName9 = scanner.nextLine();

						if (subjectName9.equalsIgnoreCase("done")) {
							if (student9.getGrades().isEmpty()) {
								System.out.println("Cannot go back without adding a grade.");
								continue;
							} else {
								System.out.println("Going back to the main menu...(press 1)");
								isAddingGrades = false;
								isAddingSubjectGrade = false;
								choice = scanner.nextInt();

								break;
							}
						}

						Subject subject9 = catalog.findSubject(subjectName9);
						if (subject9 == null) {
							System.out.println("Subject not found.");
							continue; // Restart the inner loop to prompt for subject name again
						}

						System.out.println("Enter grade: ");
						double grade9 = scanner.nextDouble();
						scanner.nextLine();

						student9.addGrade(subject9, grade9);
						System.out.println("Grade added successfully.");

						AuditLog.writeAuditLog("Grade added for " + subject9.getName() + " - Student: "
								+ student9.getName() + " - Grade: " + grade9);
					}
				}
				break;

			case 0:
				System.out.println("Exiting program...");
				System.exit(0);

			default:
				System.out.println("Invalid option. Please try again.");
				break;
			}

			System.out.println();
		}

		scanner.close();
	}
}
