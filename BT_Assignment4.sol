pragma solidity ^0.6;

contract Student_Management {
    struct Student {
        int256 stud_id;
        string name;
        string dept;
    }
    Student[] Students;

    function add_stud(
        int256 stud_id,
        string memory name,
        string memory dept
    ) public {
        Student memory stud = Student(stud_id, name, dept);
        Students.push(stud);
    }

    function getStudent(int256 stud_id)
        public
        view
        returns (string memory, string memory)
    {
        for (uint256 i = 0; i < Students.length; i++) {
            Student memory stud = Students[i];
            if (stud.stud_id == stud_id) {
                return (stud.name, stud.dept);
            }
        }
        return ("Not Found", "Not Found");
    }
}
