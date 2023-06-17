import os
import cv2

img = cv2.imread("solar-system.jpg")
#sun
cv2.putText(img,
            "Sun",
            (20, 300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255, 255, 255)
            )
#mercury
cv2.putText(img,
            "Mercury",
            (100, 175),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255, 255, 255)
            )
#venus
cv2.putText(img,
            "Venus",
            (180, 175),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255, 255, 255)
            )
#earth
cv2.putText(img,
            "Earth",
            (290, 280),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255, 255, 255)
            )
#mars
cv2.putText(img,
            "Mars",
            (380, 280),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255, 255, 255)
            )
#jupiter
cv2.putText(img,
            "Jupiter",
            (550, 50),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255, 255, 255)
            )
#saturn
cv2.putText(img,
            "Saturn",
            (770, 130),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255, 255, 255)
            )
#uranus
cv2.putText(img,
            "Uranus",
            (970, 130),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255, 255, 255)
            )
#neptune
cv2.putText(img,
            "Venus",
            (1100, 130),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255, 255, 255)
            )
cv2.imshow("output", img)
cv2.waitKey(0)
cv2.imwrite("Solar_systemwithname.jpg",img)
