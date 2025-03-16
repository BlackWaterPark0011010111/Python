import threading
import time
from log_parser import LogParser
from emotion_analyze import SentimentAnalyzer

LOG_FILE = "app.log"

def process_logs():
    """Функция для многопоточного анализа логов Function for multi-threaded log analysis"""

    parser = LogParser(LOG_FILE)

    messages = parser.extract_messages()

    analyzer = SentimentAnalyzer()

    mood = analyzer.analyze(messages)

    print(f"Overall system mood: {'😊' if mood > 0 else '😐' if mood == 0 else '😢'}")

if __name__ == "__main__":

    start_time = time.time()

    # Запуск в нескольких потоках Running in multiple threads
    threads = []
    for _ in range(3):
        
        t = threading.Thread(target=process_logs)
        threads.append(t)
        t.start()



    for t in threads:
        t.join()

    print(f"Execution time: {time.time() - start_time:.4f} seconds")