import wikipedia
from text_to_speech import save

tt = wikipedia.summary("Google LLC")

save(tt, "en", file="Hello-World.mp3")

