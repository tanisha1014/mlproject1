## for creating web app we are going to use flask
from DimondPricePrediction.pipelines.prediction_pipeline import CustomData,PredictPipeline
from flask import Flask,request,render_template,jsonify
from DimondPricePrediction.logger import logging

app=Flask(__name__)

@app.route('/')
def home_page():
    return render_template("index.html")

@app.route("/predict", methods=["GET", "POST"])
def predict_datapoint():
    if request.method == "GET":
        return render_template("form.html") 

    else:
        try:
            # Log the incoming form data
            logging.info("Form data received: %s", request.form)

            carat = request.form.get('carat')
            depth = request.form.get('depth')
            table = request.form.get('table')
            x = request.form.get('x')
            y = request.form.get('y')
            z = request.form.get('z')
            cut = request.form.get('cut')
            color = request.form.get('color')
            clarity = request.form.get('clarity')

            # Raise ValueError if any field is missing
            if None in (carat, depth, table, x, y, z, cut, color, clarity) or \
               "" in (carat, depth, table, x, y, z, cut, color, clarity):
                raise ValueError("All fields must be filled out.")

            # Convert to float
            data = CustomData(
                carat=float(carat),
                depth=float(depth),
                table=float(table),
                x=float(x),
                y=float(y),
                z=float(z),
                cut=cut,
                color=color,
                clarity=clarity
            )
            ...
        except Exception as e:
            logging.info('Error in predict_datapoint: %s', e)
            return render_template("form.html", error=str(e))

        final_data=data.get_data_as_dataframe() 
        predict_pipeline=PredictPipeline()
        pred=predict_pipeline.predict(final_data)

        result=round(pred[0],2)

        return render_template("result.html",final_result=result)   

if __name__ =='__main__':
    app.run(host="0.0.0.0",port=8080) 
     