if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    student_name = student_marks.get(query_name)
    avg= sum(student_name)/len(student_name)
    print(f'{avg:.2f}')
