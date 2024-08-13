package Catalog;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
import java.util.List;

public class Student {

    private String name;
    private Map<Subject, Double> grades;
    private Map<String, Subject> subjects;
    private LearningType learningType;

    public Student(String name, int gradeLevel, LearningType learningType) {
        this.name = name;
        grades = new HashMap<>();
        subjects = new HashMap<>();
        this.learningType = learningType;
    }

    public String getName() {
        return name;
    }

    public void addSubject(Subject subject) {
        subjects.put(subject.getName(), subject);
    }

    public Map<String, Subject> getSubjects() {
        return subjects;
    }

    public void addGrade(Subject subject, double grade) {
        grades.put(subject, grade);
    }

    public Map<Subject, Double> getGrades() {
        return grades;
    }

    public List<Subject> getEnrolledSubjects() {
        List<Subject> enrolledSubjects = new ArrayList<>();
        for (Subject subject : subjects.values()) {
            if (subject.getEnrolledStudents().contains(this)) {
                enrolledSubjects.add(subject);
            }
        }
        return enrolledSubjects;
    }

    public LearningType getLearningType() {
        return learningType;
    }

    public void setLearningType(LearningType learningType) {
        this.learningType = learningType;
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (obj == null || getClass() != obj.getClass()) return false;
        Student student = (Student) obj;
        return name.equals(student.name);
    }

    @Override
    public int hashCode() {
        return name.hashCode();
    }
}

enum LearningType {
    DE, FT
    // Enums: Distance Education or Full Time
}