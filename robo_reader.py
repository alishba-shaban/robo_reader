import pyttsx3

if __name__ == "__main__":
    print("Welcome to Robo Speaker 1.1 Created by the great Alishba Shaban")
    
    # Initialize the TTS engine outside the loop for efficiency
    engine = pyttsx3.init()
    
    while True:
        x = input("Enter what you want to speak (or 'q' to quit): ")
        if x.lower() == "q":
            print("Thanks for using me!!")
            break
        else:
            engine.say(x)
            engine.runAndWait()
 
    # Clean up resourc
    engine.stop()
