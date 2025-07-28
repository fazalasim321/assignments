{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOsRnVfm5cwznYc+qcWVc3W",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/fazalasim321/assignments/blob/main/Practical%20work%20of%20Oops.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# -------------------------------\n",
        "# Student Class\n",
        "# -------------------------------\n",
        "class Student:\n",
        "    # Class variable - common for all students\n",
        "    school = \"Al Yousaf Public School Sohdra\"\n",
        "\n",
        "    # Constructor: runs when object is created\n",
        "    def __init__(self, name, age, score):\n",
        "        self.name = name\n",
        "        self.age = age\n",
        "        self.score = score\n",
        "\n",
        "    # Show student info\n",
        "    def display_info(self):\n",
        "        print(f\"{self.name} is {self.age} years old and scored {self.score}.\")\n",
        "\n",
        "    # Check pass/fail\n",
        "    def has_passed(self):\n",
        "        return self.score >= 50\n",
        "\n",
        "    # Nice print format\n",
        "    def __str__(self):\n",
        "        return f\"Student(Name: {self.name}, Age: {self.age}, Score: {self.score})\"\n",
        "\n",
        "\n",
        "# -------------------------------\n",
        "# Teacher Class\n",
        "# -------------------------------\n",
        "class Teacher:\n",
        "    def __init__(self, name, subject):\n",
        "        self.name = name\n",
        "        self.subject = subject\n",
        "\n",
        "    def teach(self):\n",
        "        print(f\"{self.name} is teaching {self.subject}.\")\n",
        "\n",
        "\n",
        "# -------------------------------\n",
        "# Course Class\n",
        "# -------------------------------\n",
        "class Course:\n",
        "    def __init__(self, title):\n",
        "        self.title = title\n",
        "        self.students = []\n",
        "\n",
        "    # Add student to course\n",
        "    def add_student(self, student):\n",
        "        self.students.append(student)\n",
        "\n",
        "    # Calculate average score\n",
        "    def average_score(self):\n",
        "        if not self.students:\n",
        "            return 0\n",
        "        total = sum(student.score for student in self.students)\n",
        "        return total / len(self.students)\n",
        "\n",
        "\n",
        "# -------------------------------\n",
        "# Testing the Classes\n",
        "# -------------------------------\n",
        "\n",
        "# Create students\n",
        "student1 = Student(\"Fazal Asim \", 18, 85)\n",
        "student2 = Student(\"Arman\", 17, 40)\n",
        "\n",
        "# Use Student methods\n",
        "student1.display_info()\n",
        "print(\"Passed?\", student1.has_passed())\n",
        "print(\"School:\", student1.school)\n",
        "\n",
        "# Create teacher\n",
        "teacher = Teacher(\"Sir Umar\", \"Physics\")\n",
        "teacher.teach()\n",
        "\n",
        "# Create course and add students\n",
        "course = Course(\"Python Programming\")\n",
        "course.add_student(student1)\n",
        "course.add_student(student2)\n",
        "\n",
        "# Calculate and print average\n",
        "print(\"Average Score:\", course.average_score())\n",
        "\n",
        "# Use __str__\n",
        "print(student1)\n",
        "\n",
        "# Use dir to list everything in student1\n",
        "print(\"\\nDIR of student1:\")\n",
        "print(dir(student1))\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "1MEcJxakAqZc",
        "outputId": "056c9613-51ef-4d94-9708-4f3e8403fd9e"
      },
      "execution_count": 10,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Fazal Asim  is 18 years old and scored 85.\n",
            "Passed? True\n",
            "School: Al Yousaf Public School Sohdra\n",
            "Sir Umar is teaching Physics.\n",
            "Average Score: 62.5\n",
            "Student(Name: Fazal Asim , Age: 18, Score: 85)\n",
            "\n",
            "DIR of student1:\n",
            "['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'age', 'display_info', 'has_passed', 'name', 'school', 'score']\n"
          ]
        }
      ]
    }
  ]
}