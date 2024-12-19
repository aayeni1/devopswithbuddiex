import os 



def solution(input_file,output_file):
    unique_collection=set()
    try :
        with open(input_file,'r') as file:
            lines =file.readlines()
            for line in lines:
                unique_collection.add(line.strip())
    
    except Exception as e:
        print({e})
        
    finally:
        print("This is the end of the solution block of code ")
            
    try :
        with open (output_file,'w') as A:
            for lines in unique_collection:
                A.write(lines+'\n')
    except Exception as e:
        print(f"Error message {e} ")
        
    finally :     
        print(f"\t\n\nunique items have been saved in >>>>> '{output_file}'\n\n")

def main():
    
    pwd =os.getcwd()
    input_file ='dedup_large_file/file'
    output_file='dedup_large_file/adetunji_file'

    input_path= os.path.join(pwd,input_file)
    output_path= os.path.join(pwd,output_file)

    solution(input_path,output_path)

if __name__ == '__main__':
    main()