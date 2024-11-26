from pathlib import Path

#Determining the directory where the script file is located
file_path = Path(__file__).parent

def get_total_salary(path):
    try:
        # Opening a file using the context manager
        with open(path, 'r', encoding='utf-8') as file:
            total_salary_amount = 0
            company_developers = 0

            # Processing each line in a file
            for line in file:
                # Remove extra spaces and newline characters
                line = line.strip()
                try:
                    # Split a string into name and salary
                    name, salary = line.split(',')
                    # Add salary to total
                    total_salary_amount += float(salary)
                    # Increase developer counter
                    company_developers += 1
                except ValueError:
                    print(f"Invalid line format: {line}")

            # Calculating the average salary
            if company_developers > 0:
                average_salary = total_salary_amount / company_developers
            else:
                # Avoiding division by 0
                average_salary = 0

            return total_salary_amount, average_salary
        
    except FileNotFoundError:
        print(f"File not found at {path}")
        return 0, 0
    except Exception as e:
        print(f"An error equed: {e}")
        return 0, 0

# Function testing
if __name__ == "__main__":
    path = file_path / "salary_file.txt"
    total, average = get_total_salary(path)
    print(f'Total salary amount is: {total}, average salary is: {average}')