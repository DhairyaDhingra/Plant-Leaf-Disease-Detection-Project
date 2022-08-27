
#Import necessary libraries
from flask import Flask, render_template, request

import numpy as np
import os

from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model

filepath = '/Users/parthsharma/Important/Plant-Leaf-Disease-Prediction-main/model_inception.h5'
model = load_model(filepath)
print(model)

print("Model Loaded Successfully")

def pred_tomato_dieas(tomato_plant):
  test_image = load_img(tomato_plant, target_size = (224,224)) 
  print("@@ Got Image for prediction")
  
  test_image = img_to_array(test_image)/255 
  test_image = np.expand_dims(test_image, axis = 0) 
  
  result = model.predict(test_image) 
  print('@@ Raw result = ', result)
  
  pred = np.argmax(result, axis=1)
  print(pred)

  if pred==0:
      return "Apple - Cedar Rust",'Apple_cedar_rust.html'

  elif pred==1:
      return "Cherry - Powdery mildew",'Cherry_powdery_mildew.html'

  elif pred==2:
      return "Corn (maize) - Gray leaf spot",'Corn_gray_spot.html'

  elif pred==3:
      return "Corn (maize) - Common rust",'Corn_common_rust.html'
 
  elif pred==4:
      return "Corn (maize) - Northern Leaf Blight",'Corn_northern_leaf_blight.html'
    
  elif pred==5:
      return "Grape - Black rot",'Grape_black_rot.html'
    
  elif pred==6:
      return "Grape - Black Measles (Esca)",'Grape_black_measles.html'    

  elif pred==7:
      return "Orange - Citrus greening",'Orange_citrus_greening.html'
    
  elif pred==8:
      return "Peach - Bacterial spot",'Peach_bacterial_spot.html'

  elif pred==9:
      return "Potato - Early blight",'Potato_early_blight.html'
    
  elif pred==10:
      return "Potato - Late blight",'Potato_late_blight.html'
    
  elif pred==11:
      return "Strawberry - Leaf scorch",'Strawberry___Leaf_scorch_.html'
          
  elif pred==12:
      return "Tomato - Bacterial_spot",'Tomato-Bacteria Spot.html' 
      
  elif pred==13:
      return "Tomato - Early Blight Disease",'Tomato-Early_Blight copy.html'       
        
  elif pred==14:
      return "Tomato - Late Blight Disease",'Tomato - Late_blight.html'
       
  elif pred==15:
      return "Tomato - Leaf Mold Disease",'Tomato - Leaf_Mold.html'
        
  elif pred==16:
      return "Tomato - Septoria Leaf Spot Disease",'Tomato - Septoria_leaf_spot.html'       
        
  elif pred==17:
      return "Tomato - Tomoato Yellow Leaf Curl Virus Disease",'Tomato - Tomato_Yellow_Leaf_Curl_Virus.html'
      
  elif pred==18:
      return "Tomato - Tomato Mosaic Virus Disease",'Tomato - Tomato_mosaic_virus.html'
    

# Create flask instance
app = Flask(__name__)

# render index.html page
@app.route("/", methods=['GET', 'POST'])
def home():
        return render_template('index.html')
    
 
# get input image from client then predict class and render respective .html page for solution
@app.route("/predict", methods = ['GET','POST'])
def predict():
     if request.method == 'POST':
        file = request.files['image'] # fet input
        filename = file.filename        
        print("@@ Input posted = ", filename)
        
        file_path = os.path.join('/Users/parthsharma/Important/Plant-Leaf-Disease-Prediction-main/static/upload', filename)
        file.save(file_path)

        print("@@ Predicting class......")
        pred, output_page = pred_tomato_dieas(tomato_plant=file_path)
              
        return render_template(output_page, pred_output = pred, user_image = file_path)
    
# For local system & cloud
if __name__ == "__main__":
    app.run(threaded=False,port=8080) 
    
    
