# Book-Cover-recognition-book-search-with-cover
Absrtact:
The purpose of this project is to recognize book covers from images that are taken by a regular digital camera, or already stored in computer or mobile or a webcam. The recognition will be made through image processing techniques, using de-skew algorithm, that will allow to identify the correct image that represents the cover from a database of covers. The input images will consist of a book cover and a background were the book was placed. When visiting bookstores, people always want to find more details about the book they are interested. Generally, we want to know more comments on that book, we may also want to compare the prices for the same book from online stores. Therefore, the goal of our project is to provide readers with more book information by just taking photos of the book cover. In this way, people can make better decisions on taking books in the bookstore.
2.	Capturing Images
In order to capture the book covers it will be using a webcam with average resolution. This webcam will allow us to obtain a medium quality picture of the cover. The quality of this picture will present us a more real environment of the capture of the book cover image. We chose to use this low-resolution device instead of a good resolution camcorder because the application will be use by users that have access to normal webcams than a camcorder (we assume that most of the users will be prefer the cheap option of a webcam instead an expensive camcorder). The algorithms used in the application will have to deal with lower resolution in order to get a better classification.
Since digital camera pictures have better resolution than webcam and people is prone to buy them nowadays, we chose to use also these images as inputs. The reason is it will be easier to implement with digital camera images because of the higher quality with respect a basic webcam. Once the problem is solved for digital camera images the program should be tuned to respond in the same way with a worse resolution.
With the webcam and the digital camera, we can deliver different sizes for the book cover pictures. Those sizes will be analysed in order to see which one gives the best result. For the digital camera in specific will be use the good quality.
 
3.	Region of Interest (ROI)
The region of interest will be defined as the area in the image where the complete book cover appears, vertically oriented. We can assume that more than the 80% percent of the book will be the book itself, and the rest the background. We can also assume that the book cover will be the central part of the picture. The whole image (background and book cover) will be use for recognize the text on book and will search that on Goodreads webpage.
4.	Features of Recognition 
The GUI allows user to take photos of the book cover. Then it will automatically detect features of the input image based on MSER algorithm, then it will filter out non-text features based on morphological difference between text and non-text regions
5.	Algorithm Overview:





  
6.	Pre-processing 
6.1	 Image Capture:
 	Considering the sources of the images in our daily lives, we implement two image capture ways. These are loading an image in your Algorithm Pipeline database or taking a real time image by webcam. We use Python GUI to automatically preview and take snapshot of book cover images in natural environment as input.
6.2	 Skew Correction: 
Some limitations of the captured images will influence the performances of character recognition, such as the geometrical distortions caused by the digital camera or the rotations when people took the photo. Thus we need to correct the rotations problem. Since we can use the edge detection algorithms like sobel edge detection to find the book cover’s edges, and edges always appear as direct lines, then we use Hough transform to do skew correction. In order to avoid false correction resulted from skews lines that appear in the book cover, we only take top 3 hough peaks.
6.3	 MSER: 
Before we extract text information from the book cover, we need to recognize which parts of the book contain text. MSER is a method that shows how we detect useful regions in an image that contains text. Basically, MSER will extract the regions where we observed large image gradient. 
6.4	Morphological filtering:
After the extraction of MSER, the next step is to filter out non-text regions based on the geometric difference between text characters and non-text regions. The properties weve chosen are: Aspect ratio, Eccentricity, Euler number. Extent and Solidity. Another common parameter used to discriminate between text and non-text region is stroke width. Stroke width is a measure of the width of the curves and lines that make up a character. Text regions tend to have little stroke width variation, whereas non-text regions tend to have larger variations. We use standard deviation to represent the level of stroke width variations. 
6.5	Bounding Boxes: 
After the detection of individual character bounding boxes, we need to merge individual characters into words to perform better Optical Character Recognition. We  has already implemented an algorithm for merging bounding boxes. However, the algorithm does not consider the individual text lines inside the merging boxes, and it will decrease the total recognition accuracy. We developed a new merging method which considers the single lines inside merged bounding boxes, which significantly improves the recognition accuracy. 
6.6	Optical Character Recognition (OCR)
In order to get better optical character recognition result, we used OCR functions. Which is generated from tesseract engine but the performances are not identical across different book covers. We will have a detailed comparison between these OCR functions in the next chapter.
6.7	 False detection inhibition and words auto correction
Because the diversity of font sizes and styles, OCR functions we implemented will have false detections. After the OCR, we first filtered out false detections by setting a word confidence cutoff, then we implement automatic word(typo) correction by downloading the English word database and compare the words detected with the words in the dictionary.
7.	User Interface
Our GUI of the project look like this in which we have different buttons as we can see from Figure: 
Figure 1 GUI of Book Finder
7.1	Capture Button
In this button we have added a feature to capture image from webcam. After clicking on the Capture button, it will open up the camera screen and after pressing “q” from keyboard it will save the picture. We can see in fig. how it will look like.
 
Figure 2 Captured from Camera
7.2	Load Button
In this button we have added an option for loading an image from your computer/device. After clicking on this button dialogue screen will pop up go to your desired directory and open up your image which you book you want to search. As shown in fig. 
 
Figure 3 Loading a Image
7.3	Preview Button
In this button we have added a feature to preview the image. After clicking the button, a screen will pop up and new image will be shown on which the box around text area will be visible and we will be able to see the highlighted text on image. As shown in fig below:
 
Figure 4 Bonding Box Image
7.4	Top Entry Field
In this field we have added the feature in which we can search the book by its name and we will be able to get the results directly this feature have noting to do with Image Processing but It will make more dynamic to our app and we will be able to test it with each and every possible aspects. 
 
Figure 5 Top Entry Field of GUI
7.5	Analyse Button 
After clicking on this button, it will analyse our image and read the text from book cover and it will send it to internet through the TCP connection and  search the book with this name and will get all the top 20 searches from “goodreads” website and it will return all the list and URLs. 
7.6	Output Field
It is output filed of our application where all the results will be displayed and we will be to get all the results here. After analyse button it will show all the searches return by the “search function” of our code. The user will be able to see all the results over here.  
Figure 6 Results after pressing Analyse Button
7.7	Lower Entry Field
In this field we have added the feature in which user have to enter the of book which he want to buy or want to read the reviews on book and we will be able to get the results directly this feature have nothing to do with Image Processing but It will make more dynamic to our app and we will be able to test it with each and every possible aspects. 
 
Figure 7 Lower Entry Field
7.8	View Online Button
After clicking on this button, it will open up the review page of the book on “goodreads” website and user will be able to read the reviews and compare the prices and all the necessary details we want to see.
 
Figure 8 Reviews Page in Web browser
8.	Logistical Issues
One of the logistical issues is to obtain the input data from the webcam/camera, that can be quiet time consuming. This is because is necessary to get an image that has the full front cover of the book (trying to avoid rotations and skews) and the fewest background possible. Another issue is sending the text read from book cover due to slow connections it causes some error like port data receive and sending from ports cause a lot of trouble.
9.	Conclusion
In this project, we have successfully developed a Python GUI with automatic book cover detection and recognition to help people take the advantages of both online shopping and real book store shopping, with emphasis on adding pre-process and post-process steps to improve the performance of OCR functions, and finally increase the rate of correct recognition. The GUI we developed is platform-invariant, robust, fast and accurate in providing good user interaction experience.
10.	References
[1] A.C. Berg, T.L. Berg, and J. Malik, Shape Matching and Object Recognition using Low Distortion Correspondence. CVPR 2005.
[2] Louka Dlagnekov, Video-based Car Surveillance: License Plate, Make, and Model Recognition, U.C. San Diego (Masters Thesis).
[3] Ho, W. T., Lim, H. W., & Tay, Y. H. (2009, April). Two-stage license plate detection using gentle Adaboost and SIFT-SVM. In Intelligent Information and Database Systems, 2009. ACIIDS 2009. First Asian Conference on (pp. 109-114). IEEE. 
[4] Chen, H., Tsai, S. S., Schroth, G., Chen, D. M., Grzeszczuk, R., & Girod, B. (2011, September). Robust text detection in natural images with edge-enhanced maximally stable extremal regions. In 2011 18th IEEE International Conference on Image Processing (pp. 2609-2612). IEEE. 
[5] Google open source Tesseract OCR https://code.google.com/archive/p/matlab-tesseractocr/downloads
