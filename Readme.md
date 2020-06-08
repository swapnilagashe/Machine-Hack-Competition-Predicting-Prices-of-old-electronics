This is a repository for a hackathon I participated on the Machine Hack website(My first hackathon on Machine Hack :p)

We are given data containing the model information, state, city and some description about all the items.
(The data is complete garbage and we need to extract features properly)

Note : This is a Regression type problem and not a classification problem

Training data : 1. Brand_name 2. Model_Info, 3.Additional_Description, 4. State, 5. City, 6.Locality, 7.Price(To be predicted)


Models used : 

For this competition, I used total 8 types of model and blended the predictions from each of the model to arrive at the final results.

1. Deep Neural Network (I like using neural networks wherever possible, although they work best when we have tons of data(which is not the case here))
2. Light gbm 
2. SVR (Support Vector regressor)
3. XgBoost Regressor
4. GBR (Gradient Boosting Regressor)
5. Ridge Regressor
6. Random Forest Regressor
7. StackingCV Regressor(I used stackgen here to stack all the above models except the DNN together)

Finally combining all of them in a blended model by assigning weight to each of the models. I did the assigning weights process by
hit and trial but we can use a neural network here too so that we get the optimised weights. 

"""
Check if any ideas I used in Housing prices prediction competition are applicable here.

Strategy:
    by looking at the data it seems that all the data is regarding old phones ans no other type of electronics(would have been better if machine hack had clarified this by their own)
    
So what affects the price of a phone
1. Brand (iphone will cost much more compared to androids)
2. Model
3. Condition the phone is in (can use sentiment analysis here)
4. How old the phone is
5. RAM
6. Storage space
7. Operating system (won't matter much i think)
8. Camera type (Megapixels)
9. Accessories provided if any
10. Battery capacity
11. CURRENT MARKET PRICE FOR THE PARTICULAR MODEL (THIS FEATURE MIGHT PROVE TO BE A GAME CHANGER)"""


"""Let's first try to run a basic model and see how it compares on the leaderboard, for now i am using flair's sentiment analysis tool, will develop my own later """


"""We can see that the :
    1.model_info mostly contains info about specs of the phone, some parts contain info about the condition as well and name0 and name87 comes up a lot of time
    2.Additional_Description mostly contains info about condition of the phone and some part contain info like accessories available(charger, earphones etc)"""


"""
Initial Approach:
    1.last three columns (locality, city, state contain very less information) these will be treated as categorical variables
    2.Make sepearate columns for (Brand, Model, Camera, Storage, condition, Battery, RAM, OS, Accesories)
    Search for specific strings in model_info and additional info columns, like for
    a.Brand: iphone, android, all common brands(asus, Mi, samsung etc., Make a list of them) and add the brand name if present to brand column
    b.Model: Identify model name using some type of regex pattern and put the value in model column
    c.Curr_market_value: Now since we have the Brand and model name we can search the web to check its current price from Amazon or flipkart(Don't know how this is done, but this might be a great feature so I definitely have to do this)
    d.Perform same thing for camera, storage etc.,
    e.Condition : This can be done in several ways, I can make categories like: brand_new, new, avg, old, very_old (Search for keywords like new, brand new, old etc or 1 year old, 2 year old etc)
    f.Sentiment: Can generate a sentiment around the condition of the phone or otherwise(using description column and model info columns)
    g.Accesories: search for keywords like earphones, headphones, charger etc., None if you don't find the keyword
    h.
    
    
    """
