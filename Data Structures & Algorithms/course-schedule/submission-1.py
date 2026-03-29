class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq={}
        subjects = set()

        for prerequisite,subj in prerequisites:
            subjects.add(subj)
            subjects.add(prerequisite)
            
            if prerequisite in prereq:
                prereq[prerequisite].append(subj)
            else: 
                prereq[prerequisite] = [subj]
        
        indegree_count = {}
        for subject in subjects:
            indegree_count[subject] = 0
        
        for pre in prereq:
            for subject in prereq[pre]:
                indegree_count[subject]+=1
        
        subjects_with_indegree_zero = []
        for subject in indegree_count:
            if indegree_count[subject]==0:
                subjects_with_indegree_zero.append(subject)
        
        while subjects_with_indegree_zero:
            sub = subjects_with_indegree_zero.pop()
            
            # Check if `sub` has any dependents
            if sub in prereq:
                for dependent in prereq[sub]:
                    # Decrease the in-degree of dependent nodes
                    indegree_count[dependent] -= 1
                    # If in-degree becomes 0, add to the zero in-degree list
                    if indegree_count[dependent] == 0:
                        subjects_with_indegree_zero.append(dependent)
        
        # Check if all courses can be completed
        # If any course still has a non-zero in-degree, it means a cycle exists
        for count in indegree_count.values():
            if count != 0:
                return False
        
        return True

        






        


        