def log_result(result):
    with open('results.txt', 'a', encoding='utf-8') as f:
        f.write(f'\nПобедил {result} ')
