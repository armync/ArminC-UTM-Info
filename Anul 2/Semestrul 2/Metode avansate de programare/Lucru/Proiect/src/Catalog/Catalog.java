package Catalog;

import java.util.ArrayList;
import java.util.List;

public class Catalog {
	private List<Student> students;
	private List<Teacher> teachers;
	private List<Subject> subjects;

	public Catalog() {
		students = new ArrayList<>();
		teachers = new ArrayList<>();
		subjects = new ArrayList<>();
	}

	public void addStudent(Student student) {
		if (findStudent(student.getName()) != null) {
			System.out.println("A student with the same name already exists.");
			return;
		}
		students.add(student);
	}

	public void addTeacher(Teacher teacher) {
		teachers.add(teacher);
	}

	public void addSubject(Subject subject) {
		subjects.add(subject);
	}

	public Student findStudent(String name) {
		for (Student student : students) {
			if (student.getName().equals(name)) {
				return student;
			}
		}
		return null;
	}

	public Student getStudentByName1(String name) {
		for (Student student : students) {
			if (student.getName().equals(name)) {
				return student;
			}
		}
		return null;
	}

	public Subject findSubject(String subjectName) {
		for (Subject subject : subjects) {
			if (subject.getName().equals(subjectName)) {
				return subject;
			}
		}
		return null;
	}

	public void assignStudentToSubject(String studentName, String subjectName) {
		Student student = findStudent(studentName);
		Subject subject = findSubject(subjectName);
		if (student == null) {
			System.out.println("Student not found.");
			return;
		}
		if (subject == null) {
			System.out.println("Subject not found.");
			return;
		}
		if (student.getSubjects().containsKey(subject.getName())) {
			System.out.println(studentName + " is already enrolled in " + subjectName + ".");
			return;
		}
		subject.enrollStudent(student);
		student.addSubject(subject);
		System.out.println(studentName + " has been enrolled in " + subjectName + ".");
	}

	public List<Student> getStudents() {
		return students;
	}

	public Student getStudentByName(String name) {
		for (Student student : students) {
			if (student.getName().equals(name)) {
				return student;
			}
		}
		return null; // if student not found
	}

	public Teacher findTeacher(String teacherName) {
		for (Teacher teacher : teachers) {
			if (teacher.getName().equals(teacherName)) {
				return teacher;
			}
		}
		return null;
	}

	public List<Teacher> getTeachers() {
		return teachers;
	}

	public List<Subject> getSubjects() {
		return subjects;
	}

	public void assignSubjectsToTeachers() {
		for (Teacher teacher : teachers) {
			List<Subject> subjects = teacher.getTaughtSubjects();
			for (Subject subject : subjects) {
				subject.assignTeacher(teacher);
			}
		}
	}
}