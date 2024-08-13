package Catalog;

import java.util.ArrayList;
import java.util.List;

public class Teacher {
	private String name;
	private ArrayList<Subject> subjectsTaught;

	public Teacher(String name) {
		this.name = name;
		subjectsTaught = new ArrayList<>();
	}

	public String getName() {
		return name;
	}

	public void assignSubject(Subject selectedSubject) {
		selectedSubject.assignTeacher(this);
		subjectsTaught.add(selectedSubject);
	}

	public void addSubjectTaught(Subject subject) {
		subjectsTaught.add(subject);
	}

	public List<Subject> getTaughtSubjects() {
		return subjectsTaught;
	}
}