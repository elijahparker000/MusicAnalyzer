#This file is just so I can paste lyrics from azlyrics.com and it'll remove the line breaks and put the lyrics in the correct spot in the json file
#it's dumb and slow, but it's what I got right now


import json

lyrics = """Ain't it just like the night to play tricks when you're tryin' to be so quiet ?
We sit here stranded, though we're all doing our best to deny it
And Louise holds a handful of rain, tempting you to defy it
Lights flicker from the opposite loft
In this room the heat pipes just cough
The country music station plays soft
But there's nothing really nothing to turn off
Just Louise and her lover so entwined
And these visions of Johanna that conquer my mind.

In the empty lot where the ladies play blindman's bluff with the key chain
And the all-night girls they whisper of escapades out on the D-train
We can hear the night watchman click his flashlight
Ask himself if it's him or them that's really insane
Louise she's all right she's just near
She's delicate and seems like the mirror
But she just makes it all too concise and too clear
That Johanna's not here
The ghost of electricity howls in the bones of her face
Where these visions of Johanna have now taken my place.

Now, little boy lost, he takes himself so seriously
He brags of his misery, he likes to live dangerously
And when bringing her name up
He speaks of a farewell kiss to me
He's sure got a lotta gall to be so useless and all
Muttering small talk at the wall while I'm in the hall
Oh, how can I explain ?
It's so hard to get on
And these visions of Johanna they kept me up past the dawn.

Inside the museums, Infinity goes up on trial
Voices echo this is what salvation must be like after a while
But Mona Lisa musta had the highway blues
You can tell by the way she smiles
See the primitive wallflower frieze
When the jelly-faced women all sneeze
Hear the one with the mustache say, "Jeeze
I can't find my knees."
Oh, jewels and binoculars hang from the head of the mule
But these visions of Johanna, they make it all seem so cruel.

The peddler now speaks to the countess who's pretending to care for him
Saying, "Name me someone that's not a parasite and I'll go out and say a prayer for him."
But like Louise always says
"Ya can't look at much, can ya man."

As she, herself prepares for him
And Madonna, she still has not showed
We see this empty cage now corrode
Where her cape of the stage once had flowed
The fiddler, he now steps to the road
He writes everything's been returned which was owed
On the back of the fish truck that loads
While my conscience explodes
The harmonicas play the skeleton keys and the rain
And these visions of Johanna are now all that remain."""


# Remove line breaks
lyrics = lyrics.replace("\n", " ")

# Read the JSON file
with open("BaseLineSongs.json", "r") as file:
#with open("ContemporaryChristian.json", "r") as file:
    data = json.load(file)

# Update the lyrics for the first song
data[12]["lyrics"] = lyrics
#data[3]["lyrics"] = lyrics

# Save the updated JSON data to the file
with open("BaseLineSongs.json", "w") as file:
#with open("ContemporaryChristian.json", "w") as file:
    json.dump(data, file, indent=4)