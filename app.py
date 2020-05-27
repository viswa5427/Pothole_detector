from flask import Flask,render_template,request
import cv2
c=cv2.CascadeClassifier('cascade.xml')
app = Flask(__name__)
ans=''
@app.route("/",methods=['GET','POST'])
def home():
	img=request.form.get('pic')
	img3=cv2.imread(img,0)
	#img3=cv2.resize(img1,(500,500))
	#img3=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
	try:
		faces=c.detectMultiScale(img3,scaleFactor=1.4,minNeighbors=4,flags=cv2.CASCADE_SCALE_IMAGE)
		if faces.shape[0] <=1:
			ans="Sorry, your pothole hasn't detected"
			cv2.destroyAllWindows()
		else:
			ans="SOME POT HOLES ARE DETECTED"
			cv2.destroyAllWindows()

	except:
		ans="Sorry, your pothole hasn't been detected"
		cv2.destroyAllWindows() 
	return render_template('index.html',answer=ans)
if __name__ == '__main__':
	app.run(debug=True)


   
