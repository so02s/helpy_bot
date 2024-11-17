def save_message(note: Note) -> None:
    curr_date = note.date
    curr_time = note.time
    if one_line_note():
        # Replace all line breaks with spaces and make simple time stamp
        note_body = note.text.replace('\n', ' ')
        note_text = check_if_task(check_if_negative(f'[[{curr_date}]] - {note_body}\n'))
    else:
        # Keep line breaks and add a header with a time stamp
        note_body = check_if_task(check_if_negative(note.text))
        note_text = f'#### [[{curr_date}]] {curr_time}\n{note_body}\n\n'
    with open(get_note_name(curr_date), 'a', encoding='UTF-8') as f:
        f.write(note_text)

def date_note(date) -> None:
    
    with open(get_note_name(date), 'w', encoding='UTF-8') as f:
        f.write(f'#### [[{date}]]\n\n')