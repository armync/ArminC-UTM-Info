package Catalog;

import java.util.ArrayList;

public class Subject {
	private String name;
	private Teacher teacher;
	private ArrayList<Student> enrolledStudents;

	public Subject(String newSubjectName) {
		this.name = newSubjectName;
		enrolledStudents = new ArrayList<Student>();
	}

	public String getName() {
		return name;
	}

	public void Subject1(String name) {
		this.name = name;
	}

	public Teacher getTeacher() {
		return teacher;
	}

	public void assignTeacher(Teacher teacher) {
		this.teacher = teacher;
	}

	public void enrollStudent(Student student) {
		enrolledStudents.add(student);
	}

	public ArrayList<Student> getEnrolledStudents() {
		return enrolledStudents;
	}
}
