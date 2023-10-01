import cv2
import pyzbar.pyzbar as pyzbar

def scan_qr_code():
    # Buka kamera
    cap = cv2.VideoCapture(0)

    while True:
        _, frame = cap.read()

        # Mencari QR code pada setiap frame
        decoded_objects = pyzbar.decode(frame)

        for obj in decoded_objects:
            # Ambil data QR code
            data = obj.data.decode('utf-8')
            
            # Tampilkan data QR code di layar
            cv2.putText(frame, data, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            
            # Tampilkan frame dengan data QR code
            cv2.imshow("QR Code Scanner", frame)

        # Tunggu tombol "q" ditekan untuk keluar
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Tutup kamera dan jendela tampilan
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    scan_qr_code()
