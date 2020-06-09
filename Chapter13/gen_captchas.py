from captcha.audio import AudioCaptcha
from captcha.image import ImageCaptcha

#audio = AudioCaptcha(voicedir='/usr/share/festival/voices')
image = ImageCaptcha(fonts=['/usr/share/fonts/truetype/padauk/Padauk-Bold.ttf', '/usr/share/fonts/truetype/ttf-bitstream-vera/Vera.ttf'])

text = '4MmC3'
#data = audio.generate(text)
#audio.write(text, 'out.wav')

data = image.generate(text)
image.write(text, 'captchaExample.png')



