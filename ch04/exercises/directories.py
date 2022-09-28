article = "Enkidu awakens from a chilling nightmare. In the dream, the gods were angry with him and Gilgamesh and met to decide their fate. Great Anu, Ishtar’s father and the god of the firmament, decreed that they must punish someone for killing Humbaba and the Bull of Heaven and for felling the tallest cedar tree. Only one of the companions, however, must die. Enlil, Humbaba’s master and the god of earth, wind, and air, said that Enkidu should be the one to die. Shamash, the sun god, defended Enkidu. He said that Enkidu and Gilgamesh were only doing what he told them to do when they went to the Cedar Forest. Enlil became angry that Shamash took their side and accused Shamash of being their comrade, not a god. The dream proves true when Enkidu falls ill. Overcome with self-pity, he curses the cedar gate that he and Gilgamesh brought back from the forbidden forest. He says he would have chopped the gate to pieces if he’d known his fate, and that he’d rather be forgotten forever than doomed to die like this. Gilgamesh is distraught. He tells Enkidu that he has gone before the gods himself to plead his case, but that Enlil was adamant. Gilgamesh promises his friend that he will build him an even greater monument than the cedar gate. He will erect an enormous statue of Enkidu, made entirely of gold." 


substitutions = {
  "nightmare": "spoon" ,
  "angry":"happy" , 
  "Humbaba":"toothpaste" , 
  "forgotten":"coding" , 
  "Enkidu":"ralph" , 
  "gold":"marshmellows" ,
  "the": "sleep" 
}

for key, value in substitutions.items():
  article = article.replace(key, value) 

print(article) 
  
  