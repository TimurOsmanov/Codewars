def generate_hashtag(s):
    row = '#' + s.strip().title().replace(' ', '')
    return False if len(row) > 140 or s == '' else row


print(generate_hashtag(" Hello there thanks for trying my Kata"))