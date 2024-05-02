class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqs = defaultdict(set)
        for [course, prereq] in prerequisites:
            prereqs[course].add(prereq)
        
        taken = set()
        queue = deque([c for c in range(numCourses) if not prereqs[c]])
        
        while queue:
            course = queue.popleft()
            taken.add(course)
            
            for [next_course, next_course_prereqs] in prereqs.items():
                if next_course in taken:
                    continue
                if course in next_course_prereqs:
                    next_course_prereqs.remove(course)
                    if len(next_course_prereqs)==0:
                        queue.append(next_course)
                        # del prereqs[next_course]
        return len(taken) == numCourses
                    
                