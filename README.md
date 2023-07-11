# MusicAnalyzer
You know how contemporary christian music is really repetetive? I started this project to see if I could analyze the words in different kinds of music to see how true that claim is. 
So far, the code tells you the number of uses for each word in a song, tells you the total number of unique words, tells you the unique words per minute, and prints out a little histogram to help you visualize how repetetive the song is. 

For instance, Stairway To Heaven has 162 unique words, about 20 unique words per minute, and it's histogram looks like this. The correct interpretation of this histogram is that there are about 100 words which are only used a single time, and on the other end of the graph, there is only a single word which is used 17 times (the word "the"). 

![StairwayToHeaven](https://github.com/erp0015/MusicAnalyzer/assets/124807872/92811db0-e651-4f7e-84dc-fe6552dd43d8)



We can compare this to a contemporary christian song such as Defender by the band UPPERROOM, and we get the below histogram. Defender has 100 unique words, and about 11 unique words per minute. I'd say Defender is more repetetive because it is actually longer that Stairway To Heaven, yet it has significantly less words, and only about half as many unique words per minute. You can also see on the histogram that one word is used 34 times (the word "you"). 

![Defender](https://github.com/erp0015/MusicAnalyzer/assets/124807872/e6283008-6429-4ad6-857e-11d3a541cd80)



Here are a couple more examples to get a feel for some of the extremes. Eminem's Rap God has a blistering 100.66 unique words per minute and 609 unique words overall.

![RapGod](https://github.com/erp0015/MusicAnalyzer/assets/124807872/b62593bc-59cb-40dd-9d46-2b1879f9126a)



The Star Spangled Banner is a very unrepetetive song, which I suspect has to do with the fact that it was first a poem. It has 60 unique words and 40.22 unique words per minute. 52 of it's unique words are used only a single time. 

![StarSpangledBanner](https://github.com/erp0015/MusicAnalyzer/assets/124807872/452739f9-4da2-4f99-b4f2-f4b37cce5c62)



Hey Jude is one of the weirder ones. Despite being over 7 minutes long it has only 84 unique words giving it 11.86 unique words per minute. If you've ever heard Hey Jude before, you can probably guess that outlier word which was used 162 times according to azlyrics.com. Those words used 24 and 28 times are "hey" and "jude", respectively. 

![HeyJude](https://github.com/erp0015/MusicAnalyzer/assets/124807872/eddc3c96-e5f2-499c-be32-e198ae3086bf)



There are still several things to be done. So far, I've used lyricsFormatter.py to remove the returns in the strings of lyrics that I've copied and pasted from azlyrics.com, but this is slow. I'd like to make a web scraper that takes in a list of songs and fills out the json files for me so that I can analyze a bunch of songs together. I also think it would be helpful to look at the percentage of single use words as well as to remove the top 100 or so most common english language words because regardless of the song, words like "the", "a", and "I" are going to show up a lot. I'm also curious if there's something related to Benford's Law or something similar in these histograms. Obviously, the x-axis isn't limited to 1-9, so it wouldn't be perfect, but I'm interested to see what the histogram would look life if it were averaged over thousands of songs. 
