from flask import Flask,render_template,request
import pickle
from utils.recommendations import get_recommendations

app = Flask(__name__)

model,season_encoder,rain_encoder,target_encoder = pickle.load(open("model.pkl","rb"))

@app.route("/",methods=["GET","POST"])
def index():

    prediction=None
    rainwater=None
    advice=None

    if request.method=="POST":

        people=int(request.form["people"])
        season=request.form["season"]
        rainfall=request.form["rainfall_level"]
        daily_usage=float(request.form["daily_usage"])
        roof_area=float(request.form["roof_area"])
        rainfall_amount=float(request.form["rainfall_amount"])

        season_encoded=season_encoder.transform([season])[0]
        rain_encoded=rain_encoder.transform([rainfall])[0]

        pred=model.predict([[people,season_encoded,rain_encoded,daily_usage]])

        prediction=target_encoder.inverse_transform(pred)[0]

        rainwater=roof_area*rainfall_amount*0.9

        advice=get_recommendations(prediction)

    return render_template(
    "index.html",
    prediction=prediction,
    rainwater=rainwater,
    advice=advice
    )

if __name__=="__main__":
    app.run(debug=True)