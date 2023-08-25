def create_matrix():
    number_of_rows = int(input("number of rows :  "))
    number_of_columns = int(input("number of columns :  "))
    
    matrix = []
    
    for i in range(number_of_rows):
        row = []
        for j in range(number_of_columns):
            number = int(input("enter a number:"))
            row.append(number)
        matrix.append(row)
        
    print(matrix)
    
create_matrix
    