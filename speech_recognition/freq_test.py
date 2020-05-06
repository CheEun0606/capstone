#5/6
'''
<해야할 것>
면접관 모드 파이썬 코드 
음성 결과에 대해 점수를 매기는 방식임. 
키워드 값 제대로 인식부터 하고, good 이면 어펙티바로 키워드 전송
bad 이면 어펙티바로 키워드 전송
bad이면 어펙티바로 bad 전송
1. 단, 클로바 더빙이 잘 적용되어 있어야함. -> 이건 기업체 미팅 이후로 미루기 
2. //또한, 사전에 이름을 입력하고 이걸 바로 출력해서 질문을 할 수 있어야 함.
3. //질문 묻는거도 추가해야함. 
4. 잘못들었을 때 예외처리 다시 해주기
5. // 질문마다 음성인식 함수 불러와서 호출한다음 그거 종료시켜야하는데 잘 안됨. 
6. //random 질문 수행하기
7. //돌발 질문 묻기 
8. 음성 분석 점수 매길때 이거 파이썬해서 해주는게 좋을듯.... 
9. 난수 중복안되게 !! 
'''

#필요한 것들 import 해주기
import speech_recognition as spr
import requests
from collections import Counter
import pyaudio
import numpy as np
import pylab
import time
import os
import sys
import socket
import math
import matplotlib.pyplot as plt
from gtts import gTTS
import win32com.client as wincl
import pyximport
from random import randint, uniform
import random

pyximport.install()

RATE = 44100        # time resolution of the recording device (Hz)
CHUNK = int(RATE/2) # RATE / number of updates per second
TARGET = 2100
# 1. 주파수 max-> mean값으로 수정
# 2. 음성 Sapivoice에서 음성파일 출력으로 
# 3. delay 줄이는 작업 수행
# 4. 음성 작을때 출력하는거 좀 줄이기 
# 5. 음성 합성 현정이한테 소스 받아서 하기 
# 6. 음성 변환 파일 재생 

# 로컬은 127.0.0.1의 ip로 접속한다.   

#HOST = '203.252.121.216'   
'''
# 로컬은 127.0.0.1의 ip로 접속한다.   
HOST = '127.0.0.1'   
# port는 위 서버에서 설정한 9999로 접속을 한다.   
PORT = 9999   
# 소켓을 만든다.   
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   
# connect함수로 접속을 한다.   
client_socket.connect((HOST, PORT))   
#정식버전
'''
'''
def classify(text):
    key = "627ea570-73ea-11ea-8411-e561fc3bf68fd69fb9ee-5840-41a4-a3e4-f3e77b4ad941"
    url = "https://machinelearningforkids.co.uk/api/scratch/"+ key + "/classify"
    response = requests.get(url, params={ "data" : text })
    if response.ok:
        responseData = response.json()
        topMatch = responseData[0]
        return topMatch
    else:
        response.raise_for_status()
'''
#간단한 버전
'''
def classify(text):
    key = "96635130-4ee5-11ea-bf70-d3926e1c25088409b813-c901-4326-8185-18eaaa9b2dbe"
    url = "https://machinelearningforkids.co.uk/api/scratch/"+ key + "/classify"
    response = requests.get(url, params={ "data" : text })
    if response.ok:
        responseData = response.json()
        topMatch = responseData[0]
        return topMatch
    else:
        response.raise_for_status()
'''
'''
**cheeun**
# and return the top result with the highest confidence
def classify(text):
    key = "627ea570-73ea-11ea-8411-e561fc3bf68fd69fb9ee-5840-41a4-a3e4-f3e77b4ad941"
    url = "https://machinelearningforkids.co.uk/api/scratch/"+ key + "/classify"

    response = requests.get(url, params={ "data" : text })

    if response.ok:
        responseData = response.json()
        topMatch = responseData[0]
        return topMatch
    else:
        response.raise_for_status()

'''


'''
**cheeun**
def soundplot(stream):
    
    while 1:
        data = np.frombuffer(stream.read(CHUNK),dtype=np.int16)
        peak=np.average(np.abs(data))*2 # 왜 곱하기 2 하는지?
        print("peak %04d"%(peak))
        if (peak<300 and peak>60):
            print("더 크게 말해주세요")
            #os.system("start 1.mp3")
            speak = wincl.Dispatch("SAPI.SpVoice")
            speak.Speak("잘 들리지 않습니다. 더 크게 말해주세요")
        elif (peak>310 and peak<3000):
            interview(stream)
'''
'''
**cheeun**
#이건 안쓰는거?
def soundcheck(stream):
    
    while 1:
        data = np.frombuffer(stream.read(CHUNK),dtype=np.int16)
        peak=np.average(np.abs(data))*2
        print("peak %04d"%(peak))
        if (peak<300 and peak>60):
            print("더 크게 말해주세요")
            #os.system("start 1.mp3")
            speak = wincl.Dispatch("SAPI.SpVoice")
            speak.Speak("잘 들리지 않습니다. 더 크게 말해주세요")
'''            


def interview(stream):
    '''
    **cheeun**
    print("starting program...")
    
    print("이름을 입력해 주세요.")
    s= input()

    speak = wincl.Dispatch("SAPI.SpVoice")
    speak.Speak("안녕하세요 %s 씨, 반갑습니다. 자리에 앉아주세요."%(s))
    speak.Speak("그럼 지금부터, 면접을 시작하겠습니다.")
    time.sleep(2)
    
    speak.Speak("간단한 자기소개 부탁드립니다. ")
    '''
    sr(stream)
    #quit()
    #soundcheck(stream)
    
    '''
    **cheeun**
    numbers=[]
    
    i=0
   
    
    while i<3 :
        number =random.randint(0,5)
        if number not in numbers:
            numbers.append(number)
            print(number)

        i = i + 1
        
        alert =random.randint(0,5)
        print(alert)
        
        
        
        if (number ==0):
            if(alert==1):
                time.sleep(2)
                speak.Speak("위기 극복 사례가 있으시면 말씀해주세요.")
                time.sleep(2)
                speak.Speak("잠 깐 !!!!")
                speak.Speak("만약 당신이 일을 하는 동안 직장상사가 비도덕적인 일을 맡긴다면 어떻게 하시겠습니까?")
                sr(stream)
            else:
                time.sleep(2)
                speak.Speak("위기 극복 사례가 있으시면 말씀해주세요.")
                sr(stream)
            
        elif (number ==1):
            if(alert==1):
                time.sleep(2)
                speak.Speak("%s 씨께서 ,저희 회사에 지원한 이유와, 입사 후 이루고 싶은 목표에 대해, 들어보고 싶네요" %(s))
                time.sleep(2)
                speak.Speak("잠깐!")
                speak.Speak("만약 당신이 일을 하는 동안 직장상사가 비도덕적인 일을 맡긴다면 어떻게 하시겠습니까?")
                sr(stream)
            else:
                time.sleep(2)
                speak.Speak("%s 씨께서 ,저희 회사에 지원한 이유와, 입사 후 이루고 싶은 목표에 대해, 들어보고 싶네요" %(s))
                sr(stream)
            
        elif (number ==2):
            if(alert==1):
                time.sleep(2)
                speak.Speak("왜 저희가 %s 씨를 뽑아야 하는지 이유를 말씀해 주세요. 다른 사람과 차별화되는 본인만의 장점이 있나요?" %(s))
                time.sleep(2)
                speak.Speak("잠깐!")
                speak.Speak("만약 당신이 일을 하는 동안 직장상사가 비도덕적인 일을 맡긴다면 어떻게 하시겠습니까?")
                sr(stream)
            else: 
                time.sleep(2)
                speak.Speak("왜 저희가 %s 씨를 뽑아야 하는지 이유를 말씀해 주세요. 다른 사람과 차별화되는 본인만의 장점이 있나요?" %(s))
                sr(stream)
            
        elif (number ==3):
            if(alert==1):
                time.sleep(2)
                speak.Speak("자신의 장단점에 대해 말씀해 주세요")
                time.sleep(2)
                speak.Speak("잠깐!")
                speak.Speak("만약 당신이 일을 하는 동안 직장상사가 비도덕적인 일을 맡긴다면 어떻게 하시겠습니까?")
                sr(stream)
            else: 
                time.sleep(2)
                speak.Speak("자신의 장단점에 대해 말씀해 주세요")
                sr(stream)
        
        elif (number==4):
            if(alert==1):
                time.sleep(2)
                speak.Speak("사회 기여 경험이 있으신가요?")
                time.sleep(2)
                speak.Speak("잠깐!")
                speak.Speak("만약 당신이 일을 하는 동안 직장상사가 비도덕적인 일을 맡긴다면 어떻게 하시겠습니까?")
                sr(stream)
            else: 
                time.sleep(2)
                speak.Speak("사회 기여 경험이 있으신가요?")
                sr(stream)
    
        
    '''
    
    
    
    
    
    '''
    time.sleep(1)
    speak.Speak("%s 씨께서 ,저희 회사에 지원한 이유와, 입사 후 이루고 싶은 목표에 대해, 들어보고 싶네요" %(s))
    sr(stream)
   
    #soundcheck(stream)
    time.sleep(1)
    speak.Speak("왜 저희가 %s 씨를 뽑아야 하는지 이유를 말씀해 주세요. 다른 사람과 차별화되는 본인만의 장점이 있나요?" %(s))
    sr(stream)
    #soundcheck(stream)
    
    time.sleep(1)
    speak.Speak("마지막으로 더 하시고 싶은 말씀 있으신가요?")
    sr(stream)
    
    
    '''
    '''
    **cheeun**
    time.sleep(1)
    speak.Speak("이것으로 면접을 마치겠습니다. 수고많으셨습니다.")
    
    
    
    
    speak.Speak("잠시만 기다리시면 결과를 알려드리겠습니다")
    
    
    #d= facial 
    #v= tone 
    #k= keyword
    
    d= 90
    v= 85
    k= 80
    speak.Speak("모의 면접 결과, %s씨께서는  얼굴 표정에서 %d점,목소리 톤에서 %d점, 발언 내용에서 %d점을 받으셨습니다."%(s,d,v,k))
    
    
    if (d>=90):
        speak.Speak("표정이 좋습니다. 이대로 잘 유지해주세요")
    elif(d>=80 and d<90):
        speak.Speak("표정에 조금만 더 신경써주시면 좋을것 같네요.")
    elif(d>=70 and d<80):
        speak.Speak("표정 점수가 미흡합니다. 틈틈이 계속 연습하셔야겠네요")
    
    if (v>=90):
        speak.Speak("목소리 톤이 좋습니다. 이대로 잘 유지해주세요")
    elif(v>=80 and v<90):
        speak.Speak("목소리 톤에 조금만 더 신경써주시면 좋을듯 합니다")
    elif(v>=70 and v<80):
        speak.Speak("톤 점수가 미흡합니다. 크고 분명한 목소리를 내주세요")
        
    if(k>=90):
        speak.Speak("발언 내용이 좋습니다. 이대로 잘 유지해주세요")
    elif(k>=80 and k<90):
        speak.Speak("발언 내용이 조금 미흡합니다. 애매한 표현을 자제해주세요")
    elif (k>=70 and k<80):
        speak.Speak("발언 내용이 많이 미흡합니다. 확실한 표현 위주로 말씀해주세요")
        
    result=d+v+k
    time.sleep(0.5)
    speak.Speak("점수 총합은 %d 점 입니다. 다음에 더 좋은 모습으로 뵙겠습니다"%(result))
        
    sys.exit(1)
    '''
    #soundcheck(stream)

    #or v>=90 or k>=90
    #d>=85 or v>=85 or k>=85
    #speak.Speak("표정,톤, 내용 모두 준수합니다. 이대로 끝까지 잘 준비하시길 바랍니다.")
    '''
    if (result>270):
        speak.Speak("표정,톤, 내용 모두 준수합니다. 이대로 끝까지 잘 준비하시길 바랍니다.")
    
    elif(result >250):
        speak.Speak("조금만 더 잘 준비해봅시다.")
    '''
def sr(stream):
    #print("A moment of silence, please...")
    #with m as source: r.adjust_for_ambient_noise(source)
    #print("Set minimum energy threshold to {}".format(recog.energy_threshold))    
    print("Say something!")
    #while True:
    #with mc as source: audio = recog.listen(source,stream=='True') #time limit 2s로 설정 
    with mc as source: audio = recog.listen(source,stream=='True', phrase_time_limit=5)
    
        
        
    print("Got it! Now to recognize it...")
        
    try:
            # recognize speech using Google Speech Recognition
        #value = recog.recognize_google(audio,language="ko-KR")
        #print("You said {}".format(value))
           
        #demo = classify(value)
        '''
        **cheeun**    
        label = demo["class_name"]
        confidence = demo["confidence"]
        print ("result: '%s' with %d%% confidence" % (label, confidence))
        '''

#여기서부터 fft 분석 다시 해보기
        data = np.frombuffer(stream.read(CHUNK),dtype=np.int16)
        
        fft = abs(np.fft.fft(data).real)
        #fft = fft[:int(len(fft)/2)] # keep only first half
        freq = np.fft.fftfreq(CHUNK,1.0/RATE)
           
        freq = freq[:int(len(freq)/2)] # keep only first half
        
        
        freqPeak = freq[np.where(fft==np.max(fft))[0][0]]+1
        print("peak frequency: %d Hz"%freqPeak)
        
        '''
        msg = label
        data = msg.encode();   
        # 메시지 길이를 구한다.   
        length = len(data);   
        # server로 big 엔디언 형식으로 데이터 길이를 전송한다.   
        client_socket.sendall(length.to_bytes(4, byteorder="big"));   
        # 데이터를 전송한다.   
        client_socket.sendall(data);
        
        '''
        
        
        
        '''
        **cheeun**
        time.sleep(1.5)
        if (label=='good'):
           
            speak = wincl.Dispatch("SAPI.SpVoice")
            
            speak.Speak("네 그렇군요")
      
        elif(label == 'bad'):
            speak = wincl.Dispatch("SAPI.SpVoice")
            speak.Speak("흐으으음...")
        '''    
        
    
    except spr.UnknownValueError:
        print("Oops! Didn't catch that")
            
    except spr.RequestError as e:
        print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
            
            


if __name__=="__main__":
    
    spr.__version__
    recog = spr.Recognizer()
    mc = spr.Microphone()
    p = pyaudio.PyAudio()
    #sum=100
    stream=p.open(format=pyaudio.paInt16,channels=1,rate=RATE,input=True,
                  frames_per_buffer=CHUNK)
    for i in range(int(30*RATE/CHUNK)): #do this for 10 seconds
        #soundplot(stream)
        interview(stream)
    stream.stop_stream()
    stream.close()
    p.terminate()
        

#client_socket.close();
