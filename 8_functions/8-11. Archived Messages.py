def show_messages(messages):
    for message in messages:
        print(message)


def show_sent_messages(messages):
    sent_messages = []

    while messages:
        sent_message = messages.pop()
        sent_message_txt = f'Sent the message "{sent_message}"'
        sent_messages.append(sent_message_txt)

    for sent_message_txt in sent_messages:
        messages.append(sent_message_txt)

    return messages


messages = ['Hey there!', 'Hello', 'Welcome']
show_messages(messages)

print("\nSent messages")
sent_messages = show_sent_messages(messages[:])
show_messages(sent_messages)


print("\nOriginal messages")
show_messages(messages)
