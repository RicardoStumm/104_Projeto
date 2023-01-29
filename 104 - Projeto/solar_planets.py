import cv2

img = cv2.imread("solar-system.jpg")

cv2.putText(img,
            "Sol",
            (100, 80),
            cv2.FONT_HERSHEY_COMPLEX,
            2,
            (0, 0, 255)
            )
cv2.putText(img,
            "Mercurio",
            (110, 250),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (128, 128, 128)
            )
cv2.putText(img,
            "Venus",
            (185, 175),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (128, 128, 128)
            )
cv2.putText(img,
            "Terra",
            (285, 265),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (128, 128, 128)
            )
cv2.putText(img,
            "Marte",
            (385, 175),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (128, 128, 128)
            )
cv2.putText(img,
            "Jupter",
            (575, 375),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (128, 128, 128)
            )
cv2.putText(img,
            "Saturno",
            (775, 100),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (128, 128, 128)
            )
cv2.putText(img,
            "Urano",
            (975, 300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (128, 128, 128)
            )
cv2.putText(img,
            "Netuno",
            (1110, 150),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (128, 128, 128)
            )


cv2.imshow("resultado", img)
cv2.waitKey(0)
cv2.imwrite("Solar_systemwithname.jpg", img)
