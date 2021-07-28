#1947. Maximum Compatibility Score Sum
#There is a survey that consists of n questions where each question's answer is either 0 (no) or 1 (yes).

#The survey was given to m students numbered from 0 to m - 1 and m mentors numbered from 0 to m - 1. The answers of the students are represented by a 2D integer array students where students[i] is an integer array that contains the answers of the ith student (0-indexed). The answers of the mentors are represented by a 2D integer array mentors where mentors[j] is an integer array that contains the answers of the jth mentor (0-indexed).

#Each student will be assigned to one mentor, and each mentor will have one student assigned to them. The compatibility score of a student-mentor pair is the number of answers that are the same for both the student and the mentor.

#For example, if the student's answers were [1, 0, 1] and the mentor's answers were [0, 0, 1], then their compatibility score is 2 because only the second and the third answers are the same.
#You are tasked with finding the optimal student-mentor pairings to maximize the sum of the compatibility scores.

#Given students and mentors, return the maximum compatibility score sum that can be achieved.

 

#Example 1:

#Input: students = [[1,1,0],[1,0,1],[0,0,1]], mentors = [[1,0,0],[0,0,1],[1,1,0]]
#Output: 8
#Explanation: We assign students to mentors in the following way:
#- student 0 to mentor 2 with a compatibility score of 3.
#- student 1 to mentor 0 with a compatibility score of 2.
#- student 2 to mentor 1 with a compatibility score of 3.
#The compatibility score sum is 3 + 2 + 3 = 8.

class Solution:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        
        scores = [[None for _ in range(len(students))] for _ in range(len(mentors))]
        
        def get_score(stu_ans, men_ans):
            score = 0
            for i in range(len(stu_ans)):
                if stu_ans[i] == men_ans[i]:
                    score += 1
            return score
        
        
        for student_id in range(len(students)):
            for mentor_id in range(len(mentors)):
                scores[student_id][mentor_id] = get_score(students[student_id], mentors[mentor_id])
                
                
        out = 0
        
        def backtrack(cur_score, cur_student, used_mentors):
            nonlocal scores, out, mentors, students
            if cur_student == len(students):
                out = max(out, cur_score)
                return
            
            for mentor_i in range(len(mentors)):
                if mentor_i not in used_mentors:
                    used_mentors.add(mentor_i)
                    backtrack(cur_score + scores[cur_student][mentor_i], cur_student + 1, used_mentors)
                    used_mentors.remove(mentor_i)
        
        backtrack(0, 0, set())
        
        
        return out
                