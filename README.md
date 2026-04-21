# 2021-LSSE Emotion-Based Music Selection

A system for automatically selecting music based on the emotional state and activity context of the user.

## Overview

This project is designed to automatically select music according to the user's emotional condition and current activity context.

The main idea is to adapt the music to the user’s state. Depending on the scenario, the selected music can become more relaxing or more energetic. The application considers both the user’s ongoing activity and emotional state in order to support context-aware music selection.

According to the original project description, the relevant activities include:

- sport
- meditation

The emotional state can include values such as:

- focused
- relaxed
- excited
- stressed 

## Main Idea

Every 3–4 seconds, the system receives data from multiple independent sources. The current project description lists the following inputs:

1. **headset**  
   - UUID  
   - EEG data

2. **calendar**  
   - UUID  
   - activity such as sport or meditation

3. **emotional state**  
   - UUID  
   - emotional state such as focused, relaxed, excited, or stressed

4. **playlist**  
   - UUID  
   - current playlist such as pop or ambient

Based on the **headset**, **calendar**, and **playlist** information, the classifier determines the emotional state. Then, another logic module uses that result to determine the playlist to be selected. The original project README states that this playlist-selection logic is not the part analyzed and implemented in detail in this project. 

## Project Goal

The goal of the project is to build a modular system for:

- ingesting heterogeneous user-related signals
- classifying the emotional state of the user
- supporting automatic music adaptation
- integrating multiple subsystems in a larger emotion-aware pipeline

This makes the project relevant to topics such as:

- context-aware systems
- affective computing
- signal-based user state interpretation
- intelligent media adaptation

## Repository Structure

The directory currently contains the following main folders and files:

```text
2021-LSSE-Emotion-based-music-selection-main/
├── PREPARE PHYSIO-BEHAVIOURAL SESSION/ Ingestion_System
├── SimpleSegregation_DevelopmentSystem
├── executionSystem
├── preparation_system
├── testSystem
├── README.md
└── how_to_test.txt
```

This structure suggests that the project is organized into multiple subsystems, including ingestion, preparation, execution, development, and testing components. 

## System Inputs

The system works with several types of data sources:

- physiological data from the headset
- behavioral/activity data from the calendar
- emotional-state information
- playlist context

Because the sources are described as independent systems, the project appears to follow a modular and distributed data-ingestion approach. 

## Functional Workflow

A simplified workflow of the system is:

1. collect the incoming data every few seconds
2. combine the signals using the user UUID
3. classify the emotional state
4. pass the result to a playlist-selection logic module
5. adapt music according to the inferred user state and activity context

## Modules

Based on the directory layout, the project includes multiple modules, such as:

- **Ingestion_System** for collecting or receiving incoming data
- **preparation_system** for preparing or organizing the data
- **executionSystem** for running the main logic
- **SimpleSegregation_DevelopmentSystem** for development-related logic
- **testSystem** for testing and validation 

## Use Case

A typical use case of the system is:

- a user is doing meditation or sport
- EEG and contextual inputs are collected
- the user’s emotional condition is inferred
- music is adapted to better match the situation

For example:

- in meditation, the system may favor more relaxing music
- in sport, it may favor more energetic music

This behavior is consistent with the original project description.
## Notes

This project focuses on the emotional-state classification side of a music adaptation system. The project description explicitly states that the downstream logic that determines the actual playlist is outside the scope of the implemented analysis. 

## How to Test

The repository includes a file named:

- `how_to_test.txt`

which likely contains instructions for running or testing the project. 
## License

This project is licensed under the MIT License.
