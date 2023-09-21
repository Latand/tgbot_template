# # importing required modules
# import PyPDF2
#
# # creating a pdf file object
# pdfFileObj = open('5784-Tishrei_Minsk.pdf', 'rb')
#
# # creating a pdf reader object
# pdfReader = PyPDF2.PdfReader(pdfFileObj)
#
# # printing number of pages in pdf file
# print(len(pdfReader.pages))
#
# # creating a page object
# pageObj = pdfReader.pages[0]
#
# # extracting text from page
# print(pageObj.extract_text())
#
# # closing the pdf file object
# pdfFileObj.close()


import threading
import queue

def producer(q):
    for i in range(5):
        q.put(i)

def consumer(q):
    while True:
        item = q.get()
        if item is None:
            break
        print(f"Consumed: {item}")

q = queue.Queue()
producer_thread = threading.Thread(target=producer, args=(q,))
consumer_thread = threading.Thread(target=consumer, args=(q,))

producer_thread.start()
consumer_thread.start()

producer_thread.join()
# Signal the consumer thread to exit
q.put(None)
consumer_thread.join()
