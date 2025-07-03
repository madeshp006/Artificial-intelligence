def vacuum_cleaner(environment, location):
    print("Initial Environment:", environment)
    print("Vacuum Cleaner starts at Location", location)
    
    score = 0

    if environment[location] == "Dirty":
        print(f"Location {location} is Dirty. Cleaning...")
        environment[location] = "Clean"
        score += 1
    other_location = 'B' if location == 'A' else 'A'
    print(f"Moving to Location {other_location}")
    score -= 1  

    if environment[other_location] == "Dirty":
        print(f"Location {other_location} is Dirty. Cleaning...")
        environment[other_location] = "Clean"
        score += 1

    print("Final Environment:", environment)
    print("Performance Score:", score)
if __name__ == "__main__":
    env = {
        'A': 'Dirty',
        'B': 'Dirty'
    }
    vacuum_cleaner(env, location='A')
