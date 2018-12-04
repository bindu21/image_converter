import cv2
def main_fun():
	imag=input("Provide the name of the image with extension  ")
	
	r=cv2.imread(imag,0)
	cv2.imwrite("new_{}".format(imag),r)

	print("\n File created with name new_{} at same path".format(imag))
if __name__=="__main__":
	main_fun()