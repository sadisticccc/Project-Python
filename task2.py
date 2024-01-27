import sys
import statistics as stats

def analyze_cat_shelter(file_path):
    try:
        with open(file_path,"rt") as file:
            lines = file.readlines()
            lines.pop()


    #initializing variables
        ours_cat = 0
        theirs_cat = 0
        our_cat_time = []
    
    #process each line in the file
        for i in lines:
            num = i.split(",")
        
        #correct cat or intruder
            time_diff = int(num[2]) - int(num[1])
            if num[0] == "THEIRS":
                theirs_cat +=1
            else:
                ours_cat +=1
                our_cat_time.append(time_diff)
        print(f"Cat Visits: {ours_cat}")
        print(f"Other Cats: {theirs_cat}")
           
        
    #longest, shortest and average visit of the correct cat.
        largest = max(our_cat_time)
        smallest = min(our_cat_time)
        avg = stats.mean(our_cat_time)
        avg = round(avg)
        total = sum(our_cat_time)
        print(f"Longest Visit: {largest}")
        print(f"Shortest Visit: {smallest}")
        print(f"Average Visit Length: {avg}")
    
    #total hours and minutes spent by the correct cat in the house.
        hours = total//60
        minute = total % 60
        print(f"Total time in house: {hours} hours {minute} minutes")
        
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


    # Check if a command-line argument (file path) is provided
if len(sys.argv) != 2:
    print("Usage: python analyze_cat_shelter.py <file_path>")
else:
    file_path = sys.argv[1]
    analyze_cat_shelter(file_path)
    
   