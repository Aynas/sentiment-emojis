import sys,tweepy,csv,re
from textblob import TextBlob
import matplotlib.pyplot as plt
class SentimentAnalysis:

    def __init__(self):
        self.tweets = []
        self.tweetText = []
        self.pos,self.spos,self.wpos,self.neg,self.sneg,self.wneg,self.neu,self.search=0,0,0,0,0,0,0,0
        self.term = ''


    def DownloadData(self):
        # authenticating
        consumerKey = 'DoDNAwLNaR5r3yojcTYkxELU4'
        consumerSecret = 'SB8NeUmRJrwzdGp8VTqoTXVruvetDes33mapdO1FfDhBur0vyw'
        accessToken = '781536365263683584-G2b4LblH9LT6TbF4x6cy9OXfZIVLp2d'
        accessTokenSecret = 'sUxMFK3YKfcYMSEk3xBOAhrcPMtUQ7PL0Xo1xBOWoGFMA'
        auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
        auth.set_access_token(accessToken, accessTokenSecret)
        api = tweepy.API(auth)
        searchTerm = v.get()
        NoOfTerms = int(u.get())

        self.tweets = tweepy.Cursor(api.search, q=searchTerm, lang = "en").items(NoOfTerms)


        # input for term to be searched and how many tweets to search
       
      
        # Open/create a file to append data to
        csvFile = open('result.csv', 'a')

        # Use csv writer
        csvWriter = csv.writer(csvFile)


        # creating some variables to store info
        polarity = 0
        positive = 0
        wpositive = 0
        spositive = 0
        negative = 0
        wnegative = 0
        snegative = 0
        neutral = 0


        # iterating through tweets fetched
        for tweet in self.tweets:
            #Append to temp so that we can store in csv later. I use encode UTF-8
            self.tweetText.append(self.cleanTweet(tweet.text).encode('utf-8'))
            # print (tweet.text.translate(non_bmp_map))    #print tweet's text
            analysis = TextBlob(tweet.text)
            # print(analysis.sentiment)  # print tweet's polarity
            polarity += analysis.sentiment.polarity  # adding up polarities to find the average later

            if (analysis.sentiment.polarity == 0):  # adding reaction of how people are reacting to find average later
                neutral += 1
            elif (analysis.sentiment.polarity > 0 and analysis.sentiment.polarity <= 0.3):
                wpositive += 1
            elif (analysis.sentiment.polarity > 0.3 and analysis.sentiment.polarity <= 0.6):
                positive += 1
            elif (analysis.sentiment.polarity > 0.6 and analysis.sentiment.polarity <= 1):
                spositive += 1
            elif (analysis.sentiment.polarity > -0.3 and analysis.sentiment.polarity <= 0):
                wnegative += 1
            elif (analysis.sentiment.polarity > -0.6 and analysis.sentiment.polarity <= -0.3):
                negative += 1
            elif (analysis.sentiment.polarity > -1 and analysis.sentiment.polarity <= -0.6):
                snegative += 1


        # Write to csv and close csv file
        csvWriter.writerow(self.tweetText)
        csvFile.close()

        # finding average of how people are reacting
        positive = self.percentage(positive, NoOfTerms)
        wpositive = self.percentage(wpositive, NoOfTerms)
        spositive = self.percentage(spositive, NoOfTerms)
        negative = self.percentage(negative, NoOfTerms)
        wnegative = self.percentage(wnegative, NoOfTerms)
        snegative = self.percentage(snegative, NoOfTerms)
        neutral = self.percentage(neutral, NoOfTerms)

        # finding average reaction
        polarity = polarity / NoOfTerms

        # printing out data
        print("How people are reacting on " + searchTerm + " by analyzing " + str(NoOfTerms) + " tweets.")
        print()
        print("General Report: ")

        if (polarity == 0):
            print("Neutral")

        elif (polarity > 0 and polarity <= 0.3):
            print("Weakly Positive")
        elif (polarity > 0.3 and polarity <= 0.6):
            print("Positive")
        elif (polarity > 0.6 and polarity <= 1):
            print("Strongly Positive")
        elif (polarity > -0.3 and polarity <= 0):
            print("Weakly Negative")
        elif (polarity > -0.6 and polarity <= -0.3):
            print("Negative")
        elif (polarity > -1 and polarity <= -0.6):
            print("Strongly Negative")

        print()
        print("Detailed Report: ")
        print(str(positive)+ "% people thought it was positive")
        print(str(wpositive) + "% people thought it was weakly positive")
        print(str(spositive) + "% people thought it was strongly positive")
        print(str(negative) + "% people thought it was negative")
        print(str(wnegative) + "% people thought it was weakly negative")
        print(str(snegative) + "% people thought it was strongly negative")
        print(str(neutral) + "% people thought it was neutral")
        self.pos = positive
        self.wpos = wpositive
        self.spos = spositive
        self.neg = negative
        self.sneg =snegative
        self.wneg = wnegative
        self.neu = neutral
        self.term = NoOfTerms
        self.search = searchTerm
        return self.pos,self.wpos,self.spos,self.neg,self.sneg,self.wneg,self.neu,self.search,self.term 

        #self.plotPieChart(positive, wpositive, spositive, negative, wnegative, snegative, neutral, searchTerm, NoOfTerms)


    def cleanTweet(self, tweet):
        # Remove Links, Special Characters etc from tweet
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) | (\w +:\ / \ / \S +)", " ", tweet).split())

    # function to calculate percentage
    def percentage(self, part, whole):
        temp = 100 * float(part) / float(whole)
        return format(temp, '.2f')

import matplotlib.figure
import matplotlib.patches
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
import tkinter
from tkinter import *
gui = Tk()
gui.state('normal')
gui.configure(background='pink')

#Label-heading
l = Label(gui,text='sentiment analyser',fg='white',bg= 'pink',height=10)
font = ('times',20,'bold')
l.config(font=font)
l.pack(anchor='center')

#Label-text
label = Label(gui,text='Enter the input Here',bg='pink',fg='white').pack()
label = Label(gui,text='Enter the input Here',fg='#38A1F3',bg='pink').pack()

#Input
v = StringVar()
entry = Entry(gui,bd=3,width=45,textvariable=v).pack()
label = Label(gui,text='Enter the tweets Here',fg='#38A1F3',bg='#38A1F3').pack()
u = StringVar()
entry = Entry(gui,bd=3,width=45,textvariable=u).pack()
label = Label(gui,text='Enter the search Here',fg='#38A1F3',bg='#38A1F3').pack()

def newframe():
    sa = SentimentAnalysis()
    positive,spositive,wpositive,negative,snegative,wnegative, neutral, searchTerm, noOfSearchTerms=sa.DownloadData()
    def plotPieChart(positive,spositive,wpositive,negative,snegative,wnegative, neutral, searchTerm, noOfSearchTerms):
        labels = ['Positive  [' + str(positive) + '%]', 'Weakly Positive [' + str(wpositive) + '%]', 'Strongly Positive [' + str(spositive) + '%]','Neutral [' + str(neutral) + '%]','Negative [' + str(negative) + '%]', 'Weakly Negative [' + str(wnegative) + '%]','Strongly Negative [' + str(snegative) + '%]']      
        sizes = [positive,spositive,wpositive, neutral, negative,snegative,wnegative]
        colors = ['yellowgreen', 'gold', 'red','pink','purple','black','white']

        #patches, texts = plt.pie(sizes, colors=colors, startangle=90)
        #plt.legend(patches, labels, loc="best")
        fig = matplotlib.figure.Figure(figsize=(5,5))
        ax = fig.add_subplot(111)
        ax.pie(sizes) 
        ax.legend(['Positive \U0001f600 [' + str(positive) + '%]', 
                   'Weakly Positive \U0001f607 [' + str(wpositive) + '%]',
                    'Strongly Positive \U0001f60E[' + str(spositive) + '%]',
                    'Neutral \U0001f610 [' + str(neutral) + '%]',
                    'Negative \U0001f612 [' + str(negative) + '%]', 
                    'Weakly Negative \U0001f61F [' + str(wnegative) + '%]',
                    'Strongly Negative \U0001f621 [' + str(snegative) + '%]'])
        circle=matplotlib.patches.Circle( (0,0), 0.7, color='white' )
        ax.add_artist(circle)
        window= tk.Tk()
        label = Label(window,text='search='+v.get(),bg='blue').pack()
        label = Label(window,text='noOftweets='+u.get(),bg='white').pack()
        label = Label(window,text='Analysis',fg='white').pack()
        canvas = FigureCanvasTkAgg(fig, master=window)
        canvas.get_tk_widget().pack()
        canvas.draw()
        window.mainloop()
        
    plotPieChart(positive,spositive,wpositive,negative,snegative,wnegative, neutral, searchTerm, noOfSearchTerms)
    print(positive,spositive,wpositive,negative,snegative,wnegative, neutral, searchTerm, noOfSearchTerms)
    print("")
    button = Button(frame,text='click here to quit',command=newframe.destroy).pack()
    
button = Button(gui,text='Calculate sentiment',command=newframe).pack()

gui.mainloop()







   
