import time

# attempt to access movie review file online
try:

    connection= open ('movie_reviews.txt', "r")
    
    data = connection.read()
    
    connection.close()

except:
    print( "Something went wrong." )
    
else:
    start = time.time()
    
    print( "Initializing sentiment database" )
    # split the lines into individual reviews
    allreviews = data.split("\n")

    # set up a dictionary to hold all of our words
    sentiment = {}
    
    # set up a loop to examine all of the reviews
    for review in allreviews:

        # extract score
        score = int(review[0])

        # extract the rest of the review
        rest = review[2:]

        # extract the words from the review
        words = rest.split(" ")

        #visit every word
        for w in words:

            # clean up every non-words
            clean = ""

            for c in w:
                if c.isalpha():
                    clean += c.lower()

            # see if this is a brand new word
            if clean not in sentiment.keys():
                sentiment[clean] = [1, score]
            else:
                sentiment[clean][0] += 1
                sentiment[clean][1] += score
                            
    end = time.time()

    print ("Done")
    #print ("There are: ", len(sentiment.keys()), "words in the database")
    print ("Total unique words analyzed: ", len(sentiment.keys()))
    print ("Analysis took", format(float((end-start)),'.2f') , "seconds to complete")
    print ()
    
    # right after the for loop
    #ask the user for a phrase
    phrase = input("Enter a phrase: ")

    # isolate the words in the user's phrase
    words = phrase.split(" ")

    #set up accumulators
    total = 0
    num = 0

    #visit every word
    for w in words:

        #do we know about this word?
        if w in sentiment:

            #extract average
            avg = sentiment[w][1] / sentiment[w][0]
            print ("* '", w, "' appears", sentiment.get(w)[0], "times with an average rating of", avg)

            #add to accumulators
            total += avg
            num += 1

        else:
            num += 0
            print("* '", w, "' does not have a rating")

    if num == 0:
        print("2.0")
    else:
        #compute overall average
        overall = total / num
        print ("Overall score: ", overall)
        if overall >= 2.1:
            print ("This is a positive phrase.")
        else:
            print ("This is a negative phrase.")

