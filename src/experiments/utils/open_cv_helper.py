import cv2 as cv
from logging import getLogger
logger = getLogger(__name__)
class OpenCVHelper:
    def __init__(self, camera_index: int = 0, api_preference: int = cv.CAP_ANY):
        self.cap = cv.VideoCapture(camera_index, api_preference)
        if not self.cap.isOpened():
            print(f"[OpenCVHelper] Could not open camera at index {camera_index}. Running without camera.")
    
    def read_image(self, image_path:str):
        """Read an Image from a file path

        Args:
            image_path (str): The path to the image file (local address)

        Returns:
            The image read from the file path, or None if the image could not be read
        """
        return cv.imread(image_path)
    
    def show_image(self, image_path:str, image_name: str | None = None) -> None:
        """Show an image in a window

        Args:
            image_name (str | None): The name of the image window without the extension
            image_path (str): The path to the image file (local address)
        """
        image = self.read_image(image_path)
        if image is None:
            logger.error(f"[OpenCVHelper] Failed to read image from '{image_path}'.")
            return
        try:
            cv.imshow(
                image_name if image_name else "image.jpg", 
                image
            )
            cv.waitKey(0)
            cv.destroyAllWindows()
        except cv.error as e:
            logger.error(f"[OpenCVHelper] Display not available (likely no GUI). Skipping imshow.")
            logger.error(f"[OpenCVHelper] OpenCV error: {e}")

    def make_live_video(self): 
        """
        Make a live video from the camera. To quit the video, press the 'q' key.
        """
        if not self.cap.isOpened():
            print("[OpenCVHelper] Camera is not available. Exiting live video.")
            return
        while True:
            logger.info("Starting live video...")
            ret, frame = self.cap.read()
            if not ret or frame is None:
                logger.error("[OpenCVHelper] Failed to read frame from camera. Exiting.")
                break
            try:
                cv.imshow('frame', frame)
                logger.info("Displaying frame...")
                if cv.waitKey(1) & 0xFF == ord('q'):
                    logger.info("Quitting live video...")
                    break
            except cv.error as e:
                logger.error("[OpenCVHelper] Display not available (likely no GUI). Exiting live video.")
                logger.error(f"[OpenCVHelper] OpenCV error: {e}")
                break
        if self.cap:
            self.cap.release()
        try:
            cv.destroyAllWindows()
        except cv.error:
            pass

if __name__ == "__main__":
    open_cv_helper = OpenCVHelper()
    open_cv_helper.make_live_video()