import os
import sys 




def open_file(input_file,output_file) :
    try:
        with open (input_file,"r") as A:
            lines =A.readlines()
            line_count=len(lines)
            mid_point=float(line_count/2)
            to_print=[]
            if line_count%2 ==0 : #even count
                print(f"line count is even and has {line_count} lines")
                line_to_print1,line_to_print2 =int(mid_point-1),int(mid_point+1)
                to_print.append(lines[line_to_print1])
                to_print.append(lines[line_to_print2])
            else:
                print(f"line count is odd and has {line_count} lines")
                line_to_print=int(mid_point-0.5)
                to_print.append(lines[line_to_print])
                
            with open(output_file,"w") as B:
                for lines in to_print:
                    B.write(lines.strip()+'\n')
                print(f"all file has been written ")
            
            return to_print
                
            
    except FileNotFoundError:
        print(f"Error: the file '{input_file}' is not found")
    
    except Exception as e:
        print (f"and unexpcted error '{e}' was encontered ")
                
        

def main():
    stra ='apple'
    pwd = os.getcwd()
    problem_name="print_median/file"
    output_file_name='print_median/solution.csv'
    solution_file_path=os.path.join(pwd,output_file_name)
    problem_file_path =os.path.join(pwd,problem_name)
    if os.path.exists(problem_file_path):
        print(f"processing the file '{problem_name}' from '{problem_file_path}'")
        open_file(problem_file_path,solution_file_path)
        
        if os.path.exists(solution_file_path):
            print(f"Over writing the existing file '{output_file_name}'")
        
        else:
            print(f"the file '{output_file_name}' does not exist Creating a new one'")
        
            
    else:
        print(f"the file '{problem_name}' does not exist in '{problem_file_path}'")
        
    

if __name__ == '__main__':
    main()
