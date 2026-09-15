JARVIS

I built JARVIS as a way to build the ultimate context about me. JARVIS is a webcam mounted onto 2 servo motors that sees me as I walk around my room, and proactively talks to me based on what I'm doing (or wearing, or how I look that day). 
My responses (if deemed worthy enough by the Qwen reasoning model) are saved to a knowledge based, that JARVIS has access to via RAG. In addition to this, it tracks my hand movements and lets me turn my lights on/off based on my hand movements.

Since this project was to learn, I refrained from using AI to write any code for me. 

Current capabilities include:

YOLO-based person detection
Face and hand tracking
Voice input and speech output
Smart-home control
RAG-based personal memory retrieval

The long-term goal is to combine continuous local perception with persistent memory and higher-level AI reasoning, so JARVIS can understand both what is happening now and what it already knows about me.

Built primarily with Python, YOLO, MediaPipe, OpenSeeFace, Whisper, Sentence Transformers, and local/API-based LLMs.
