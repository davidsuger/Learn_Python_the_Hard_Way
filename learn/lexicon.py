def scan(sentence):
    result = []
    words = sentence.split()
    direction_words = ['north', 'south', 'east', 'west', 'down', 'up', 'left', 'right', 'back']
    verbs = ['go', 'stop', 'kill', 'eat']
    stop_words = ['the', 'in', 'of', 'from', 'at', 'it']
    nouns = ['door', 'bear', 'princess', 'cabinet']

    for word in words:
        error = 0
        try:
            if direction_words.index(word) >= 0:
                result.append(('direction', word))
        except ValueError as e:
            error += 1
        try:
            if verbs.index(word) >= 0:
                result.append(('verb', word))
        except ValueError as e:
            error += 1
        try:
            if stop_words.index(word) >= 0:
                result.append(('stop', word))
        except ValueError as e:
            error += 1
        try:
            if nouns.index(word) >= 0:
                result.append(('noun', word))
        except ValueError as e:
            error += 1
        try:
            result.append(('number', int(word)))
        except ValueError as e:
            error += 1
        if error == 5:
            result.append(('error', word))
    return result
