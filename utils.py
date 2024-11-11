import pandas as pd
import io

def read_file(full_path_in):
    f_t = open(full_path_in, "r", encoding="UTF-8", errors = 'ignore')
    text_t = f_t.read() #reads entire file
    #text_t = clean_txt(text_t)
    f_t.close()
    return text_t

def file_crawler(path_in):
    import os
    import pandas as pd
    my_pd_t = pd.DataFrame()
    for root, dirs, files in os.walk(path_in, topdown=False):
       for name in files:
           try:
               txt_t = read_file(root + "/" + name)
               if len(txt_t) > 0:
                   the_lab = root.split("/")[-1]
                   tmp_pd = pd.DataFrame(
                       {"body": txt_t, "label": the_lab}, index=[0])
                   my_pd_t = pd.concat(
                       [my_pd_t, tmp_pd], ignore_index=True)
           except:
               print (root + "/" + name)
               pass
    return my_pd_t

def read_pdf_as_corpus(pdf_path):
    """
    Define the function to read the PDF and extract text
    :param pdf_path: pdf file path
    :return: list of corpus for the pdf with each page as an object
    """
    import fitz  # PyMuPDF
    corpus = []
    # Open the PDF file
    with fitz.open(pdf_path) as pdf:
        # Iterate over all pages
        for page_num in range(pdf.page_count):
            page = pdf.load_page(page_num)  # Load the page
            text = page.get_text()  # Extract text from the page
            corpus.append(text)  # Add page text to the corpus

    return corpus

def SpeakText(command):
        import pyttsx3
        # Initialize the engine
        engine = pyttsx3.init()
        engine.say(command)
        engine.runAndWait()

def speechrecognition():
        import speech_recognition as sr
        r = sr.Recognizer()
        while (1):
            try:
                # use the microphone as source for input.
                with sr.Microphone() as source2:
                    r.adjust_for_ambient_noise(source2, duration=0.2)
                    audio2 = r.listen(source2)

                    # Using google to recognize audio
                    MyText = r.recognize_google(audio2)
                    MyText = MyText.lower()
                    SpeakText(MyText)

            except sr.RequestError as e:
                print("Could not request results; {0}".format(e))

            except sr.UnknownValueError:
                print("unknown error.")



