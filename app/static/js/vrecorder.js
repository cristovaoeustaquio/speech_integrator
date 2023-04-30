// collect DOMs
const display = document.querySelector('.display')
const controllerWrapper = document.querySelector('.controllers')

const State = ['Initial', 'Record', 'Download']
let stateIndex = 0
let mediaRecorder, chunks = [], audioURL = ''

// mediaRecorder setup for audio
if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
    console.log('mediaDevices supported..')
  
    navigator.mediaDevices.getUserMedia({
      audio: true
    }).then(stream => {
      mediaRecorder = new MediaRecorder(stream)
      const chunks = []
  
      mediaRecorder.ondataavailable = (e) => {
        chunks.push(e.data)
      }
  
      mediaRecorder.onstop = () => {
        const blob = new Blob(chunks, { 'type': 'audio/ogg; codecs=opus' })
        chunks = []
        audioURL = window.URL.createObjectURL(blob)
        document.querySelector('audio').src = audioURL
  
        // Send the audio data to the server
        const formData = new FormData()
        formData.append('audio', blob, 'recording.ogg')
        fetch('/upload.php', {
          method: 'POST',
          body: formData
        })
        .then(response => {
          console.log('File uploaded:', response)
        })
        .catch(error => {
          console.error('Error uploading file:', error)
        })
      }
  
      mediaRecorder.start()
  
      setTimeout(() => {
        mediaRecorder.stop()
      }, 5000)
  
    }).catch(error => {
      console.log('Following error has occured : ',error)
    })
  
  } else {
    stateIndex = ''
    application(stateIndex)
  }

const clearDisplay = () => {
    display.textContent = ''
}

const clearControls = () => {
    controllerWrapper.textContent = ''
}

const record = () => {
    stateIndex = 1
    mediaRecorder.start()
    application(stateIndex)
}

const stopRecording = () => {
    stateIndex = 2
    mediaRecorder.stop()
    application(stateIndex)
}


const downloadAudio = () => {
    const downloadLink = document.createElement('a')
    downloadLink.href = audioURL
    downloadLink.setAttribute('download', 'audio')
    downloadLink.click()
}

const addButton = (id, funString, text) => {
    const btn = document.createElement('button')
    btn.id = id
    btn.setAttribute('onclick', funString)
    btn.textContent = text
    controllerWrapper.append(btn)
}

const addMessage = (text) => {
    const msg = document.createElement('p')
    msg.textContent = text
    display.append(msg)
}

const addAudio = () => {
    const audio = document.createElement('audio')
    audio.controls = true
    audio.src = audioURL
    display.append(audio)
}

const application = (index) => {
    switch (State[index]) {
        case 'Initial':
            clearDisplay()
            clearControls()

            addButton('record', 'record()', 'Start Recording')
            break;

        case 'Record':
            clearDisplay()
            clearControls()

            addMessage('Recording...')
            addButton('stop', 'stopRecording()', 'Stop Recording')
            break

        case 'Download':
            clearControls()
            clearDisplay()


            addAudio()
            addButton('record', 'record()', 'Record Again')
            addButton('transcribe', 'transcribeAudio()', 'Transcribe')

            break

        default:
            clearControls()
            clearDisplay()

            addMessage('Your browser does not support mediaDevices')
            break;
    }

}

application(stateIndex)