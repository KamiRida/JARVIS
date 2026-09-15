def read_context():
    know = open("src/rag/knowledge.txt")
    know = know.read()
    know_read = know.split('#')

    return know_read[1]

print(read_context())

        
