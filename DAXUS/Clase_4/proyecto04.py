import cv2
from cvzone.HandTrackingModule import HandDetector

# Inicializa la camara web
webcam = cv2.VideoCapture(0)

# Iniciliza el rastreador de manos
rastreador = HandDetector(detectionCon=0.6,maxHands=2)

while True:
    # captura la imagen de la camara web
    exito,imagen = webcam.read()

    # Detecta las manos en el cuadro
    hands, hands_image = rastreador.findHands(imagen)

    # Muestra el cuadro con las marcas
    cv2.imshow('Proyecto 4 IA',hands_image)

    # Cierra la aplicacion cuando se presiona cualquier tecla
    if cv2.waitKey(1) != -1:
        break

# Libera la camara y cieraa las ventanas
webcam.release()
cv2.destroyAllWindows()