import cv2

img = cv2.imread('/home/aryan-garg/Pictures/Silverwolf-4.jpg')
img_rgb=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        b, g, r = img[y, x]
        print(f"Coordinates: ({x}, {y}), RGB values: ({r}, {g}, {b})")
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = f"RGB: ({r}, {g}, {b})"
        cv2.putText(img, text, (x, y), font, 0.5,(255, 255, 255), 2, cv2.LINE_AA)

cv2.imshow('sample', img)
cv2.setMouseCallback('Image', click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()

