from typing import List


class OnlineCourse:

    def __init__(self, title: str, instructor: str, duration_hours: int) -> None:
        self.title: str = title
        self.instructor: str = instructor
        self.duration_hours: int = duration_hours
        self._students: List[str] = []
        self.__internal_id: int = id(self)

    def enroll_student(self, student_name: str) -> None:
        self._students.append(student_name)

    def calculate_duration(self) -> int:
        return self.duration_hours

    def __str__(self) -> str:
        return f"Course '{self.title}' by {self.instructor}, duration: {self.duration_hours} hours"

    def __repr__(self) -> str:
        return f"OnlineCourse(title={self.title!r}, instructor={self.instructor!r}, duration_hours={self.duration_hours!r})"


class ProgrammingCourse(OnlineCourse):

    def __init__(
        self,
        title: str,
        instructor: str,
        duration_hours: int,
        language: str,
        projects: int
    ) -> None:
        super().__init__(title, instructor, duration_hours)
        self.language: str = language
        self.projects: int = projects

    def calculate_duration(self) -> int:
        return self.duration_hours + self.projects * 5

    def __str__(self) -> str:
        return (
            f"Programming course '{self.title}' ({self.language}) "
            f"by {self.instructor}, projects: {self.projects}"
        )

    def __repr__(self) -> str:
        return (
            f"ProgrammingCourse(title={self.title!r}, instructor={self.instructor!r}, "
            f"duration_hours={self.duration_hours!r}, language={self.language!r}, projects={self.projects!r})"
        )


if __name__ == "__main__":
    course = ProgrammingCourse(
        title="Python Development",
        instructor="Ivan Petrov",
        duration_hours=40,
        language="Python",
        projects=4
    )

    course.enroll_student("Alex")
    course.enroll_student("Maria")

    print(course)
    print("Total duration:", course.calculate_duration())