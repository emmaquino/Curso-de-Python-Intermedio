def run():
    
    # dictionary = {}

    # for i in range(1, 101):
    #     if i % 3 != 0: 
    #         dictionary[i] = i**3
    
    dictionary = {i: i**3 for i in range(1, 101) if i % 3 != 0}

    print(dictionary)

if __name__ == "__main__":
    run()