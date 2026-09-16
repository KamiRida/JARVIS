def read_context():
    know = open("src/rag_system/knowledge.txt")
    know = know.read()
    know_read = know.split('#')

    return know_read

print(read_context())

        
