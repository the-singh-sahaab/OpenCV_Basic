import cv2
import numpy as np 
# =============================================================================================================================================================================
#                           what is an image
# 3 type of image:
# 1. black and white : each cell is marked as 0,1 where 0 is white and 1 is black
# 2. grey scale photo : each cell is marked in between the 0 to 255 which show the shade of the grey where 0 is black and 255 is white and inbetween is shade of grey 
# 3. color photo: shown in the representation of RGB where each of three is in the form of layer to each other. Red--> Green--> Blue
# each of it is scaled again in 0 to 255. where 0 is white and 255 is the black and in between is the shade of respected layer
# resolulation is the number of cells in row x colon 
# ex. 1080 x 820
# =============================================================================================================================================================================

#                          reading the image
# read an image
img = cv2.imread("opencv\image\images (1).jpeg")
print(img)# this will show how the open cv see the image
print(type(img))
print(img.shape)#this will show what is the resolution and what type of image it is : (172, 292, 3)--> here the [172 x 292 --> is resolution|| 3 show the RGB](bxl)

# =========================================================================================================================================================================
# print image
cv2.imshow("bool", img)
cv2.waitKey(0)  #here the 0 show the infite time that the image will be there 

# ========================================================================================================================================================

#                          converting the image to grayscale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)#cv2.cvtcolor(x, y):[x is the img and y is the type of image you want it to change it in]
cv2.imshow("bool2", img_gray)
cv2.waitKey(0)
img[:,:,0] = 0#this is use to display the choised layer of the Rgb
cv2.imshow("l",img)
cv2.waitKey(0)

# ========================================================================================================================================================

#                          image resizing
image_resize = cv2.resize(img,(550, 450))#increasing the size by puting the number where 550 = lenght, 450 = height
print(image_resize.shape)
cv2.imshow("hooo", image_resize)
cv2.waitKey(0)
img_resize = cv2.resize(img,(img.shape[1]*5, img.shape[0]*1))
cv2.imshow("hooo", img_resize)
cv2.waitKey(0)

# ========================================================================================================================================================
#                        fliping the image
hey_img = cv2.flip(img, 00)
# flip code : 0 [makes the photo upside down]
# flip code : 1 or anyother number [makes the photo flip in the horizontal axis]
# filp code : -1 [combination of 1 and 0]
cv2.imshow("hooo", hey_img)
cv2.waitKey(0)



# ========================================================================================================================================================

#                           cropping the image
img_crop = img[100:300,200:500]#[x ,y]x = heigh, y  = breatth
cv2.imshow("window", img_crop)
cv2.waitKey(0)

# ========================================================================================================================================================
#                           enhanceing the image 
median = cv2.medianBlur(img, 5)
cv2.imshow("hey",median)
cv2.waitKey(0)







# ========================================================================================================================================================

#                            drawing shapes and text on image
img3 = np.zeros((512,512,3))
# rectangle || giving the pt1 for the one point of the rectangle and pt2 for the point diagonal to it.
cv2.rectangle(img3, pt1 = (100,100), pt2 = (300, 300), color= (255,0,0), thickness=-3)#boreder in positive will make outline and border -1 will comple colored box 
# circle
cv2.circle(img3, center = (100,400), radius= 50, color=(0,0,255), thickness=3)
# line
cv2.line(img3, pt1 = (0,0), pt2=(512, 512), color=(0,255,0), thickness=1)
# text
cv2.putText(img3,text="hey well",fontFace=cv2.FONT_HERSHEY_COMPLEX, org=(100,400), fontScale= 4, color=(0,255,0), thickness=4, lineType=cv2.LINE_AA)
cv2.imshow("____", img3)
cv2.waitKey(0)

# ========================================================================================================================================================

#                            working with the open cv events

drawing = False
ix = -1
iy = -1
def draw(event, x, y, flags, params):#event{tell you the value associated with your event}, (x,y){tell you the position of your cursor on window}
    # print(event)
    #here event have 3 values :  0 : when the mouse is hovering the window 
    #                            1 : when the click event gets completed on the window 
    #                            4: when the click happend on the window
    global drawing, ix, iy
    
    if event == 1:
        drawing = True
        ix = x
        iy = y
        
    elif event  == 0:
        if drawing == True:
            cv2.rectangle(img, pt1 = (ix, iy),pt2 = (x,y), color=(0, 255,255), thickness=1)
            
    if event == 4:
        drawing = False
        cv2.rectangle(img, pt1 = (ix, iy),pt2 = (x,y), color=(0, 255,255), thickness=1)
    
    
cv2.namedWindow("window")#you have to tell what window name have you given like here i have taken window
cv2.setMouseCallback("window", draw)

img = np.zeros((1012,1012,3))

while True:
    cv2.imshow("window",img)
    if cv2.waitKey(1) & 0xFF == ord('x'):#0xFF == ord("x"){tell that if you press the x key then}
        break
cv2.destroyAllWindows()#closing all the tabs of image

# ========================================================================================================================================================
#                                croping out the selected sector


img = cv2.imread(r"C:\Users\shubh\OneDrive\Desktop\workspace\opencv\image\images.jpeg")
flag = False
ix = -1
iy = -1
def crop(event, x, y, flags, params):
    global flag, ix, iy
    if event == 1:
        flag = True
        ix = x
        iy = y
    # elif  event == 0:
    #     if flag == True:
    #         cv2.rectangle(img, pt1=(ix, iy), pt2 = (x, y), thickness=1, color=(0,0,0))  
    elif event == 4:
        fx = x
        fy = y
        flag = False
        cv2.rectangle(img, pt1 = (ix, iy),pt2 = (x,y), color=(0,0,0), thickness=1)
        chop = img[iy:fy, ix:fx]
        cv2.imshow("new", chop)
        cv2.waitKey(0)


cv2.namedWindow(winname="window")
cv2.setMouseCallback("window", crop)
    

while True:
    cv2.imshow("window",img)
    if cv2.waitKey(1) & 0xFF == ord("x"):
        break
cv2.destroyAllWindows()
