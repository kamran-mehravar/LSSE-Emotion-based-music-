# 2021-LSSE-Emotion-based-music-selection
This application allows to automatically select a music based on the emotional state of the user. Depending on the activity, the music can be set towards more relaxing or more energetic symphonies. This depends on the activity that is taking place, meditation or sports, and on the emotional state of the subject obtained from the EEG, which can be relaxed, excited, or concentrated. Every 3-4 seconds the following data sources are provided by independent systems: 

 (1) headset => UUID, EEG-data;  

(2) calendar => UUID, activity (sport, meditation);  

(3) emotional state => UUID, emotional state (focused, relaxed, excited, stressed); 

 (4) playlist => UUID, current playlist (pop, ambient). 

 Based on the headset, calendar, and playlist, the classifier will determine the emotional state; from the latter, another logic module determines the playlist (that we will not analyze and implement).
