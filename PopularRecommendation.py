import pandas as pd
from flask import Flask
from flask import jsonify
from flask import request
from flask import json
test={'result':'xyz'}
image={'path':'','name':''}
app = Flask(__name__) 
@app.route('/popularrecommendation/qwerty',methods=['POST'])
def index(): 
        print(json.dumps(request.json))
        return jsonify(test)
    
@app.route('/image/qwerty',methods=['POST'])
def index(): 
        print(json.dumps(request.json))
        return jsonify(test)
if __name__ == '__main__': 
        app.run(host= '192.168.0.8')
# =============================================================================
# =============================================================================
# frame = pd.read_csv("C:/Users/abcdef/Downloads/Ex_Files_Intro_Python_Rec_Systems/Exercise Files/01_02/rating_final.csv")
# cuisine = pd.read_csv("C:/Users/abcdef/Downloads/Ex_Files_Intro_Python_Rec_Systems/Exercise Files/01_02/chefmozcuisine.csv")
# rating_count = pd.DataFrame(frame.groupby(['placeID'])['rating'].count())
# rating_Top_Five = rating_count.sort_values('rating',ascending=False).head()
# rating_Top_Five.reset_index().head()
# rating_Top_Five.drop(['rating'], axis = 1, inplace = True)
# summary = pd.DataFrame(rating_Top_Five).reset_index().head()
# summary.to_json(orient='records')
# print(summary.to_json(orient='records'))
# =============================================================================
